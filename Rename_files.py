"""
File Renaming Automation Script
================================
Renames all files in a folder to a pattern like: file_1.txt, file_2.txt
Uses the `os` module for file system access.
"""

import os


def rename_files(folder_path, base_name="file", start_number=1):
    """
    Renames all files in a folder to: base_name_1.ext, base_name_2.ext ...

    Parameters:
        folder_path (str) : Path to the target folder
        base_name   (str) : Prefix for renamed files (default: 'file')
        start_number(int) : Starting counter (default: 1)
    """

    # --- Step 1: Validate folder path ---
    if not os.path.exists(folder_path):
        print(f"[ERROR] Folder not found: {folder_path}")
        return

    if not os.path.isdir(folder_path):
        print(f"[ERROR] Path is not a folder: {folder_path}")
        return

    # --- Step 2: Get all files (skip sub-folders) ---
    all_entries = os.listdir(folder_path)
    files_only  = [
        entry for entry in all_entries
        if os.path.isfile(os.path.join(folder_path, entry))
    ]

    if not files_only:
        print("[INFO] No files found in the folder.")
        return

    print(f"\n Found {len(files_only)} file(s) in: {folder_path}")
    print("-" * 50)

    # --- Step 3: Rename each file ---
    counter = start_number

    for old_name in sorted(files_only):           # sorted → predictable order
        extension = os.path.splitext(old_name)[1] # e.g.  ".txt", ".jpg"
        new_name  = f"{base_name}_{counter}{extension}"

        old_path  = os.path.join(folder_path, old_name)
        new_path  = os.path.join(folder_path, new_name)

        # Avoid overwriting an already-renamed file
        if old_name == new_name:
            print(f"  [SKIP]    {old_name}  (already has target name)")
            counter += 1
            continue

        os.rename(old_path, new_path)
        print(f"  [RENAMED] {old_name:30s}  →  {new_name}")
        counter += 1

    print("-" * 50)
    print(f" Done! {counter - start_number} file(s) renamed.\n")


# ──────────────────────────────────────────────
# DEMO: creates a test folder, adds dummy files,
#       then renames them so you can see it work
# ──────────────────────────────────────────────
def demo():
    import tempfile

    # Create a temporary folder with sample files
    demo_folder = tempfile.mkdtemp(prefix="rename_demo_")
    sample_files = [
        "report_final.pdf",
        "photo_vacation.jpg",
        "notes_may.txt",
        "data_export.csv",
        "summary.docx",
    ]

    print("\n[DEMO] Creating sample files...")
    for fname in sample_files:
        with open(os.path.join(demo_folder, fname), "w") as f:
            f.write("demo content")
        print(f"  Created: {fname}")

    print(f"\n[DEMO] Folder: {demo_folder}")

    # Run the renamer
    rename_files(folder_path=demo_folder, base_name="file", start_number=1)

    # Show final result
    print("[DEMO] Files after renaming:")
    for name in sorted(os.listdir(demo_folder)):
        print(f"  {name}")

    print(f"\n[DEMO] Folder location: {demo_folder}")


# ──────────────────────────────────────────────
# HOW TO USE ON YOUR OWN FOLDER
# ──────────────────────────────────────────────
# Change the path below to your folder, then run:
#   python rename_files.py
#
# Examples:
#   rename_files(r"C:\Users\YourName\Downloads\photos")
#   rename_files("/home/user/my_folder", base_name="img", start_number=1)
# ──────────────────────────────────────────────

if __name__ == "__main__":
    demo()   # ← runs demo by default

    # Uncomment the line below to rename YOUR folder:
    # rename_files(r"PASTE_YOUR_FOLDER_PATH_HERE")