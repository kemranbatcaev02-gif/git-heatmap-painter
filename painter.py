#!/usr/bin/env python3
"""
Git Heatmap Painter
A zero-dependency tool to paint pixel art or generate target commit activity
on your GitHub contribution graph.
"""

import argparse
import datetime
import os
import subprocess
import sys
from pathlib import Path

# Ensure UTF-8 output on Windows consoles
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
if hasattr(sys.stderr, "reconfigure"):
    try:
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

# Built-in 7-row bitmap font for standard ASCII characters
FONT_7X5 = {
    'A': [
        " ### ",
        "#   #",
        "#   #",
        "#####",
        "#   #",
        "#   #",
        "#   #",
    ],
    'B': [
        "#### ",
        "#   #",
        "#   #",
        "#### ",
        "#   #",
        "#   #",
        "#### ",
    ],
    'C': [
        " ####",
        "#    ",
        "#    ",
        "#    ",
        "#    ",
        "#    ",
        " ####",
    ],
    'D': [
        "#### ",
        "#   #",
        "#   #",
        "#   #",
        "#   #",
        "#   #",
        "#### ",
    ],
    'E': [
        "#####",
        "#    ",
        "#    ",
        "#### ",
        "#    ",
        "#    ",
        "#####",
    ],
    'F': [
        "#####",
        "#    ",
        "#    ",
        "#### ",
        "#    ",
        "#    ",
        "#    ",
    ],
    'G': [
        " ####",
        "#    ",
        "#    ",
        "# ###",
        "#   #",
        "#   #",
        " ### ",
    ],
    'H': [
        "#   #",
        "#   #",
        "#   #",
        "#####",
        "#   #",
        "#   #",
        "#   #",
    ],
    'I': [
        "###",
        " # ",
        " # ",
        " # ",
        " # ",
        " # ",
        "###",
    ],
    'J': [
        "  ###",
        "   # ",
        "   # ",
        "   # ",
        "#  # ",
        "#  # ",
        " ##  ",
    ],
    'K': [
        "#   #",
        "#  # ",
        "# #  ",
        "##   ",
        "# #  ",
        "#  # ",
        "#   #",
    ],
    'L': [
        "#    ",
        "#    ",
        "#    ",
        "#    ",
        "#    ",
        "#    ",
        "#####",
    ],
    'M': [
        "#   #",
        "## ##",
        "# # #",
        "#   #",
        "#   #",
        "#   #",
        "#   #",
    ],
    'N': [
        "#   #",
        "##  #",
        "# # #",
        "#  ##",
        "#   #",
        "#   #",
        "#   #",
    ],
    'O': [
        " ### ",
        "#   #",
        "#   #",
        "#   #",
        "#   #",
        "#   #",
        " ### ",
    ],
    'P': [
        "#### ",
        "#   #",
        "#   #",
        "#### ",
        "#    ",
        "#    ",
        "#    ",
    ],
    'Q': [
        " ### ",
        "#   #",
        "#   #",
        "#   #",
        "# # #",
        "#  ##",
        " ####",
    ],
    'R': [
        "#### ",
        "#   #",
        "#   #",
        "#### ",
        "# #  ",
        "#  # ",
        "#   #",
    ],
    'S': [
        " ####",
        "#    ",
        "#    ",
        " ### ",
        "    #",
        "    #",
        "#### ",
    ],
    'T': [
        "#####",
        "  #  ",
        "  #  ",
        "  #  ",
        "  #  ",
        "  #  ",
        "  #  ",
    ],
    'U': [
        "#   #",
        "#   #",
        "#   #",
        "#   #",
        "#   #",
        "#   #",
        " ### ",
    ],
    'V': [
        "#   #",
        "#   #",
        "#   #",
        "#   #",
        " # # ",
        " # # ",
        "  #  ",
    ],
    'W': [
        "#   #",
        "#   #",
        "#   #",
        "# # #",
        "# # #",
        "## ##",
        "#   #",
    ],
    'X': [
        "#   #",
        "#   #",
        " # # ",
        "  #  ",
        " # # ",
        "#   #",
        "#   #",
    ],
    'Y': [
        "#   #",
        "#   #",
        " # # ",
        "  #  ",
        "  #  ",
        "  #  ",
        "  #  ",
    ],
    'Z': [
        "#####",
        "    #",
        "   # ",
        "  #  ",
        " #   ",
        "#    ",
        "#####",
    ],
    ' ': [
        "  ",
        "  ",
        "  ",
        "  ",
        "  ",
        "  ",
        "  ",
    ],
    '!': [
        "#",
        "#",
        "#",
        "#",
        "#",
        " ",
        "#",
    ],
    '0': [
        " ### ",
        "#  ##",
        "# # #",
        "# # #",
        "# # #",
        "##  #",
        " ### ",
    ],
    '1': [
        " ## ",
        "# # ",
        "  # ",
        "  # ",
        "  # ",
        "  # ",
        "#####",
    ],
    '2': [
        " ### ",
        "#   #",
        "    #",
        "  ## ",
        " #   ",
        "#    ",
        "#####",
    ],
    '3': [
        "#### ",
        "    #",
        "   # ",
        " ### ",
        "    #",
        "    #",
        "#### ",
    ],
    '4': [
        "#  # ",
        "#  # ",
        "#  # ",
        "#####",
        "   # ",
        "   # ",
        "   # ",
    ],
    '5': [
        "#####",
        "#    ",
        "#### ",
        "    #",
        "    #",
        "#   #",
        " ### ",
    ],
    '6': [
        " ### ",
        "#    ",
        "#### ",
        "#   #",
        "#   #",
        "#   #",
        " ### ",
    ],
    '7': [
        "#####",
        "    #",
        "   # ",
        "  #  ",
        " #   ",
        "#    ",
        "#    ",
    ],
    '8': [
        " ### ",
        "#   #",
        "#   #",
        " ### ",
        "#   #",
        "#   #",
        " ### ",
    ],
    '9': [
        " ### ",
        "#   #",
        "#   #",
        " ####",
        "    #",
        "    #",
        " ### ",
    ],
    '+': [
        "     ",
        "  #  ",
        "  #  ",
        "#####",
        "  #  ",
        "  #  ",
        "     ",
    ],
    '-': [
        "     ",
        "     ",
        "     ",
        "#####",
        "     ",
        "     ",
        "     ",
    ],
}

# GitHub contribution intensity levels:
# 0 = none, 1 = 1-2 commits, 2 = 3-5 commits, 3 = 6-9 commits, 4 = 10+ commits
INTENSITY_COMMIT_MAP = {
    0: 0,
    1: 1,
    2: 3,
    3: 6,
    4: 12,
}

# ANSI color codes for GitHub Heatmap preview
ANSI_COLORS = {
    0: "\033[90m░\033[0m",   # Dark gray / empty
    1: "\033[32m▒\033[0m",   # Light green
    2: "\033[92m▓\033[0m",   # Medium bright green
    3: "\033[32;1m█\033[0m", # Deep green
    4: "\033[92;1m█\033[0m", # Maximum bright neon green
}


def render_text_to_matrix(text: str) -> list[list[int]]:
    """Convert a text string into a 7-row integer matrix."""
    text = text.upper()
    matrix = [[] for _ in range(7)]
    for char in text:
        char_grid = FONT_7X5.get(char, FONT_7X5.get(' ', ["   "] * 7))
        for row in range(7):
            row_str = char_grid[row]
            for ch in row_str:
                matrix[row].append(4 if ch != ' ' else 0)
            # Add 1 column letter spacing
            matrix[row].append(0)
    return matrix


def load_preset(name_or_path: str, presets_dir: Path) -> list[list[int]]:
    """Load pixel art preset from a file or preset name."""
    target_path = Path(name_or_path)
    if not target_path.exists():
        target_path = presets_dir / f"{name_or_path}.txt"
    if not target_path.exists():
        raise FileNotFoundError(f"Preset '{name_or_path}' not found at {target_path}")

    lines = target_path.read_text(encoding="utf-8").splitlines()
    if len(lines) > 7:
        lines = lines[:7]
    while len(lines) < 7:
        lines.append("")

    max_len = max((len(l) for l in lines), default=0)
    matrix = []
    for line in lines:
        row = []
        padded = line.ljust(max_len)
        for ch in padded:
            if ch in (' ', '.'):
                row.append(0)
            elif ch in ('1', '░'):
                row.append(1)
            elif ch in ('2', '▒'):
                row.append(2)
            elif ch in ('3', '▓'):
                row.append(3)
            elif ch in ('#', '4', '█', '@', '*'):
                row.append(4)
            else:
                row.append(2)
        matrix.append(row)
    return matrix


def place_on_canvas(matrix: list[list[int]], offset_col: int = 0, repeat: bool = False) -> list[list[int]]:
    """Place the matrix on a 7-row by 52-column GitHub canvas."""
    canvas = [[0] * 52 for _ in range(7)]
    art_cols = len(matrix[0]) if matrix and matrix[0] else 0

    if art_cols == 0:
        return canvas

    if repeat:
        for c in range(52):
            source_c = (c - offset_col) % art_cols
            for r in range(7):
                canvas[r][c] = matrix[r][source_c]
    else:
        for r in range(7):
            for c in range(art_cols):
                target_col = offset_col + c
                if 0 <= target_col < 52:
                    canvas[r][target_col] = matrix[r][c]
    return canvas


def print_canvas_preview(canvas: list[list[int]], title: str = "GitHub Contribution Preview"):
    """Render the 7x52 canvas nicely in terminal using ANSI colors."""
    day_labels = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    print("\n" + "=" * 62)
    print(f"  {title}")
    print("=" * 62)
    print("     " + "".join(f"{w:02d}" if w % 5 == 0 else "  " for w in range(0, 52, 2)))
    for r in range(7):
        row_str = "".join(ANSI_COLORS.get(canvas[r][c], "░") for c in range(52))
        print(f"{day_labels[r]}  {row_str}")
    print("-" * 62)
    total_active_days = sum(1 for r in range(7) for c in range(52) if canvas[r][c] > 0)
    total_commits = sum(INTENSITY_COMMIT_MAP.get(canvas[r][c], 0) for r in range(7) for c in range(52))
    print(f"Active Days: {total_active_days} | Estimated Commits: {total_commits}")
    print("Legend: " + " ".join(f"L{lvl}:{ANSI_COLORS[lvl]}" for lvl in range(5)))
    print("=" * 62 + "\n")


def get_dates_for_canvas(year: int) -> list[list[datetime.date]]:
    """
    Compute actual calendar dates corresponding to a 7x52 grid.
    GitHub graphs start with Sunday as Row 0, ending with Saturday as Row 6.
    """
    jan1 = datetime.date(year, 1, 1)
    # Python weekday(): Monday is 0, Sunday is 6.
    # We want Sunday as 0, Monday as 1, ..., Saturday as 6.
    jan1_day_of_week = (jan1.weekday() + 1) % 7
    first_sunday = jan1 - datetime.timedelta(days=jan1_day_of_week)

    grid_dates = []
    for r in range(7):
        row_dates = []
        for c in range(52):
            date_val = first_sunday + datetime.timedelta(weeks=c, days=r)
            row_dates.append(date_val)
        grid_dates.append(row_dates)
    return grid_dates


def get_dates_for_rolling_year() -> list[list[datetime.date]]:
    """Compute dates for the last 52 weeks leading up to today."""
    today = datetime.date.today()
    # Find current week's Saturday
    today_dow = (today.weekday() + 1) % 7
    cur_saturday = today + datetime.timedelta(days=(6 - today_dow))
    start_sunday = cur_saturday - datetime.timedelta(weeks=51, days=6)

    grid_dates = []
    for r in range(7):
        row_dates = []
        for c in range(52):
            date_val = start_sunday + datetime.timedelta(weeks=c, days=r)
            row_dates.append(date_val)
        grid_dates.append(row_dates)
    return grid_dates


def execute_commits(commit_tasks: list[tuple[datetime.date, int]], repo_path: Path):
    """Generate git commits on specified dates in the target repository."""
    repo_path = repo_path.resolve()
    os.makedirs(repo_path, exist_ok=True)
    orig_cwd = os.getcwd()
    os.chdir(repo_path)

    try:
        git_dir = repo_path / ".git"
        if not git_dir.exists():
            print(f"📦 Initializing isolated git repository in: {repo_path}")
            subprocess.run(["git", "init"], check=True)
            subprocess.run(["git", "checkout", "-b", "main"], capture_output=True)

        data_file = repo_path / "activity.txt"
        total_created = 0
        total_days = len(commit_tasks)

        print(f"🚀 Generating commits across {total_days} scheduled days...")

        for idx, (dt, count) in enumerate(commit_tasks, 1):
            date_str = dt.strftime("%Y-%m-%dT12:00:00")
            env = os.environ.copy()
            env["GIT_AUTHOR_DATE"] = date_str
            env["GIT_COMMITTER_DATE"] = date_str

            for c_idx in range(count):
                with open(data_file, "a", encoding="utf-8") as f:
                    f.write(f"Commit at {date_str} #{c_idx + 1}\n")

                subprocess.run(["git", "add", "activity.txt"], check=True, stdout=subprocess.DEVNULL)
                commit_msg = f"chore: heatmap commit {dt.isoformat()} ({c_idx + 1}/{count})"
                subprocess.run(
                    ["git", "commit", "-m", commit_msg],
                    env=env,
                    check=True,
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL
                )
                total_created += 1

            if idx % 10 == 0 or idx == total_days:
                print(f"  Progress: {idx}/{total_days} days processed ({total_created} commits created)")

        print(f"\n🎉 Successfully created {total_created} commits in {repo_path}!")
        print("💡 Next step to show on your GitHub profile:")
        print(f"   cd \"{repo_path}\"")
        print("   git remote add origin https://github.com/<YOUR-USERNAME>/<YOUR-REPO-NAME>.git")
        print("   git push -u origin main --force")
    finally:
        os.chdir(orig_cwd)


def make_today_commits(count: int, repo_path: Path):
    """Quick booster: creates N commits for TODAY so the current day glows bright green."""
    today = datetime.date.today()
    tasks = [(today, count)]
    print(f"🔥 Fast-Boost: Generating {count} commits for today ({today})...")
    execute_commits(tasks, repo_path)


def list_presets(presets_dir: Path):
    """List available presets."""
    print("\n🎨 Available Presets:")
    if not presets_dir.exists():
        print("  (Presets directory not found)")
        return
    for p in sorted(presets_dir.glob("*.txt")):
        print(f"  • {p.stem}")
    print()


def main():
    parser = argparse.ArgumentParser(description="Git Heatmap Painter - Draw pixel art & boost activity on GitHub")
    parser.add_argument("--art", type=str, help="Name of art preset (e.g. invader, cat, heart, ghost, hi)")
    parser.add_argument("--text", type=str, help="Render custom text onto the graph (e.g. 'HI', 'DEV')")
    parser.add_argument("--today", type=int, help="Instantly create N commits for TODAY (e.g. --today 20)")
    parser.add_argument("--year", type=int, help="Target specific year (default: rolling last 52 weeks)")
    parser.add_argument("--col", type=int, default=None, help="Horizontal column offset (0-51). Default: centered")
    parser.add_argument("--repeat", action="store_true", help="Repeat art across all 52 weeks")
    parser.add_argument("--preview", action="store_true", help="Only preview in terminal, do not commit")
    parser.add_argument("--paint", action="store_true", help="Actually generate git commits")
    parser.add_argument("--repo", type=str, default="heatmap-canvas-repo", help="Target git repository folder")
    parser.add_argument("--list", action="store_true", help="List available art presets")

    args = parser.parse_args()
    script_dir = Path(__file__).resolve().parent
    presets_dir = script_dir / "presets"

    if args.list:
        list_presets(presets_dir)
        return

    # Quick TODAY boost mode
    if args.today is not None:
        target_repo = Path(args.repo).resolve()
        make_today_commits(args.today, target_repo)
        return

    if not args.art and not args.text:
        parser.print_help()
        list_presets(presets_dir)
        return

    # Prepare matrix
    if args.text:
        matrix = render_text_to_matrix(args.text)
        art_title = f"Text: '{args.text}'"
    else:
        matrix = load_preset(args.art, presets_dir)
        art_title = f"Preset: '{args.art}'"

    art_width = len(matrix[0]) if matrix and matrix[0] else 0
    if args.col is None:
        # Auto-center
        offset_col = max(0, (52 - art_width) // 2)
    else:
        offset_col = args.col

    canvas = place_on_canvas(matrix, offset_col=offset_col, repeat=args.repeat)
    print_canvas_preview(canvas, title=art_title)

    if args.year:
        grid_dates = get_dates_for_canvas(args.year)
        mode_str = f"Year {args.year}"
    else:
        grid_dates = get_dates_for_rolling_year()
        mode_str = "Rolling 52 Weeks (Live Profile View)"

    print(f"Target Mode: {mode_str}")

    if not args.paint:
        print("ℹ️  Running in preview mode. To generate commits, pass '--paint'.")
        print(f"👉 Example: python painter.py {'--art ' + args.art if args.art else '--text \"' + args.text + '\"'} --paint")
        return

    # Build tasks
    tasks = []
    for r in range(7):
        for c in range(52):
            intensity = canvas[r][c]
            commits_cnt = INTENSITY_COMMIT_MAP.get(intensity, 0)
            if commits_cnt > 0:
                tasks.append((grid_dates[r][c], commits_cnt))

    target_repo = Path(args.repo).resolve()
    execute_commits(tasks, target_repo)


if __name__ == "__main__":
    main()
