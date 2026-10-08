#!/usr/bin/env python3
"""Fetch a YouTube video's metadata and transcript into raw/videos/<slug>.md.

    python3 tools/fetch_youtube.py https://www.youtube.com/watch?v=VIDEO_ID
    python3 tools/fetch_youtube.py URL --lang nl          # Dutch captions
    python3 tools/fetch_youtube.py URL -o raw/videos/my-name.md

Needs yt-dlp (pip install -r requirements.txt). The video itself is never downloaded:
only its metadata and its captions. Human-made captions are preferred over automatic ones.
"""
import argparse
import html
import json
import re
import subprocess
import sys
import tempfile
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def slugify(text, max_words=10):
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    words = re.findall(r"[a-z0-9]+", text.lower())
    return "-".join(words[:max_words]) or "video"


def yaml_str(value):
    return json.dumps("" if value is None else str(value), ensure_ascii=False)


def yaml_block(value):
    lines = (value or "").strip().splitlines() or [""]
    return "|\n" + "\n".join("  " + line for line in lines)


def run_ytdlp(url, lang, workdir):
    cmd = [
        sys.executable, "-m", "yt_dlp",
        "--skip-download", "--write-info-json",
        "--write-subs", "--write-auto-subs",
        "--sub-langs", f"{lang},{lang}-orig,{lang}.*",
        "--sub-format", "vtt",
        "--no-warnings", "--quiet",
        "-o", str(Path(workdir) / "%(id)s.%(ext)s"),
        url,
    ]
    try:
        subprocess.run(cmd, check=True)
    except FileNotFoundError:
        sys.exit("yt-dlp is not installed. Run: pip install -r requirements.txt")
    except subprocess.CalledProcessError as err:
        sys.exit(f"yt-dlp failed (exit {err.returncode}). Is the URL right, and is the video public?")


def parse_vtt(path):
    """Return [(seconds, text)] with the rolling duplicates of auto-captions removed."""
    cues, start, lines = [], None, []
    stamp = re.compile(r"^(\d+):(\d\d):(\d\d)\.\d+\s+-->")
    for raw in path.read_text(encoding="utf-8").splitlines() + [""]:
        m = stamp.match(raw)
        if m:
            start = int(m.group(1)) * 3600 + int(m.group(2)) * 60 + int(m.group(3))
            lines = []
        elif raw.strip() == "" and start is not None:
            cues.append((start, lines))
            start = None
        elif start is not None:
            lines.append(raw)
    # Auto-captions show each line twice (once arriving, once scrolling up), so a line
    # equal to one of the last two kept is a repeat.
    out, recent = [], []
    for seconds, cue_lines in cues:
        for line in cue_lines:
            text = html.unescape(re.sub(r"<[^>]+>", "", line)).strip()
            if not text or text in recent:
                continue
            out.append((seconds, text))
            recent = (recent + [text])[-2:]
    return out


def paragraphs(segments, every=60):
    """Group segments into paragraphs of about `every` seconds, each with a timestamp."""
    blocks, current, block_start = [], [], None
    for seconds, text in segments:
        if block_start is None:
            block_start = seconds
        if seconds - block_start >= every and current:
            blocks.append((block_start, " ".join(current)))
            current, block_start = [], seconds
        current.append(text)
    if current:
        blocks.append((block_start, " ".join(current)))
    return blocks


def mmss(seconds):
    h, rest = divmod(int(seconds), 3600)
    m, s = divmod(rest, 60)
    return f"{h}:{m:02d}:{s:02d}" if h else f"{m}:{s:02d}"


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("url")
    parser.add_argument("--lang", default="en", help="caption language code (default: en)")
    parser.add_argument("-o", "--output", help="output path (default: raw/videos/<slug>.md)")
    args = parser.parse_args()

    with tempfile.TemporaryDirectory() as workdir:
        run_ytdlp(args.url, args.lang, workdir)
        infos = list(Path(workdir).glob("*.info.json"))
        if not infos:
            sys.exit("No metadata came back. Check the URL.")
        info = json.loads(infos[0].read_text(encoding="utf-8"))
        vid = info["id"]
        manual = info.get("subtitles") or {}
        candidates = sorted(Path(workdir).glob(f"{vid}.*.vtt"))
        # Prefer a human-made track, then the original-language auto track.
        def rank(p):
            code = p.name[len(vid) + 1:-4]
            return (code not in manual, not code.endswith("-orig"), code)
        candidates.sort(key=rank)
        if not candidates:
            sys.exit(f"The video has no '{args.lang}' captions. Try --lang with another code.")
        track = candidates[0]
        code = track.name[len(vid) + 1:-4]
        kind = "manual" if code in manual else "asr"
        blocks = paragraphs(parse_vtt(track))

    title = info.get("title") or vid
    upload = info.get("upload_date") or ""
    published = f"{upload[:4]}-{upload[4:6]}-{upload[6:]}" if len(upload) == 8 else ""
    out = Path(args.output) if args.output else ROOT / "raw" / "videos" / f"{slugify(title)}.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    if out.exists():
        sys.exit(f"{out} already exists. Raw files are never overwritten by accident; remove it first if you mean to replace it.")

    front = [
        "---",
        f"title: {yaml_str(title)}",
        f"video_id: {yaml_str(vid)}",
        f"url: {yaml_str(info.get('webpage_url') or args.url)}",
        f"channel: {yaml_str(info.get('channel') or info.get('uploader'))}",
        f"channel_url: {yaml_str(info.get('channel_url'))}",
        f"date_published: {published}",
        f"duration: {yaml_str(info.get('duration_string'))}",
        f"length_seconds: {int(info.get('duration') or 0)}",
        f"caption_language: {yaml_str(code)}",
        f"caption_kind: {kind}   # manual = made by a person; asr = automatic speech recognition",
        f"description: {yaml_block(info.get('description'))}",
        "---",
        "",
        f"# {title}",
        "",
    ]
    if kind == "asr":
        front += ["*Automatic captions: names, numbers and technical terms may be misheard.*", ""]
    body = [f"**[{mmss(start)}]** {text}\n" for start, text in blocks]
    out.write_text("\n".join(front) + "\n" + "\n".join(body), encoding="utf-8")
    words = sum(len(t.split()) for _, t in blocks)
    print(f"Wrote {out.relative_to(ROOT) if out.is_relative_to(ROOT) else out}  ({info.get('duration_string')}, {words} words, {kind} captions)")


if __name__ == "__main__":
    main()
