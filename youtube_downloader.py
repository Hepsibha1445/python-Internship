# yt_downloader.py — YouTube Video Downloader
# Requires: pip install pytubefix

import os
from pytubefix import YouTube
from pytubefix.cli import on_progress


def download_video(url: str, output_path: str = "downloads", quality: str = "highest") -> None:
    """
    Download a YouTube video.

    Args:
        url         : Full YouTube video URL
        output_path : Folder to save the file (created if missing)
        quality     : "highest" | "lowest" | "audio"
    """
    try:
        # ── Validate URL ──────────────────────────────────────────────────────
        url = url.strip()
        if not url:
            raise ValueError("URL cannot be empty.")
        if "youtube.com/watch" not in url and "youtu.be/" not in url:
            raise ValueError(
                "Invalid URL. Must be a YouTube link "
                "(e.g. https://www.youtube.com/watch?v=... or https://youtu.be/...)"
            )

        # ── Create destination folder if it doesn't exist ─────────────────────
        os.makedirs(output_path, exist_ok=True)

        # ── Fetch video metadata ───────────────────────────────────────────────
        print("\nFetching video info ...")
        yt = YouTube(url, on_progress_callback=on_progress)

        print(f"  Title   : {yt.title}")
        print(f"  Author  : {yt.author}")
        print(f"  Length  : {yt.length // 60}m {yt.length % 60}s")
        print(f"  Views   : {yt.views:,}")

        # ── Select stream ──────────────────────────────────────────────────────
        quality = quality.strip().lower()
        if quality == "highest":
            stream = yt.streams.get_highest_resolution()
        elif quality == "lowest":
            stream = yt.streams.get_lowest_resolution()
        elif quality == "audio":
            stream = yt.streams.get_audio_only()
        else:
            raise ValueError(
                f"Unknown quality '{quality}'. Choose: highest | lowest | audio"
            )

        if stream is None:
            raise RuntimeError("No matching stream found for this video.")

        res_label = stream.resolution if hasattr(stream, "resolution") else "audio"
        print(f"\nDownloading [{res_label}] → {output_path}/")

        # ── Download ───────────────────────────────────────────────────────────
        stream.download(output_path=output_path)
        print(f"\n✓ Done! File saved to: {os.path.abspath(output_path)}")

    except ValueError as e:
        print(f"\n[INPUT ERROR] {e}")
    except RuntimeError as e:
        print(f"\n[RUNTIME ERROR] {e}")
    except Exception as e:
        print(f"\n[ERROR] {e}")
        print("Tip: Check your internet connection or whether the video is age-restricted / private.")


def main() -> None:
    print("=" * 50)
    print("       YouTube Video Downloader")
    print("=" * 50)

    url = input("\nEnter YouTube URL       : ").strip()

    folder_input = input("Save folder [downloads] : ").strip()
    output_path = folder_input if folder_input else "downloads"

    print("Quality options  →  highest | lowest | audio")
    quality_input = input("Quality [highest]       : ").strip()
    quality = quality_input if quality_input else "highest"

    download_video(url, output_path, quality)


if __name__ == "__main__":
    main()