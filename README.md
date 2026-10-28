# 🎨 Git Heatmap Painter

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.8+"/>
  <img src="https://img.shields.io/badge/Dependencies-Zero-success?style=for-the-badge" alt="Zero Dependencies"/>
  <img src="https://img.shields.io/badge/License-MIT-blue?style=for-the-badge" alt="MIT License"/>
  <img src="https://img.shields.io/badge/PRs-Welcome-brightgreen?style=for-the-badge" alt="PRs Welcome"/>
</p>

> Turn your boring GitHub contribution graph into an 8-bit canvas or boost your daily activity to neon green with a single command! 🚀

---

## ✨ Features

- 👾 **Built-in Pixel Art Presets**: Invaders, Cats, Hearts, Ghosts, and more.
- 🔤 **Custom Text Renderer**: Type any text (`HELLO`, `DEV`, `404`) and it gets converted to a 7-row pixel font automatically.
- 🔥 **Fast Activity Booster (`--today N`)**: Need today to glow bright neon green with 20 commits right now? One flag does it all.
- 🌈 **4-Level Green Heatmap Simulation**: True-to-life GitHub intensity simulation (1 to 12 commits per cell).
- 🖥️ **ANSI Terminal Preview**: See exactly how your canvas looks before writing a single commit.
- ⚡ **Zero External Dependencies**: Uses only standard Python library (`sys`, `subprocess`, `datetime`, `argparse`). Works on Windows, macOS, and Linux out-of-the-box.
- 🛡️ **Safe & Isolated**: Generates commits into a clean target repo without altering your existing repositories.

---

## 📺 Terminal Preview

```text
==============================================================
  Preset: 'invader'
==============================================================
     00        10        20        30        40        50
Sun  ░░░░░░░░░░░░░░░░░░░░░░█░░░░░█░░░░░░░░░░░░░░░░░░░░░░░
Mon  ░░░░░░░░░░░░░░░░░░░░░░░█░░░█░░░░░░░░░░░░░░░░░░░░░░░░
Tue  ░░░░░░░░░░░░░░░░░░░░░░███████░░░░░░░░░░░░░░░░░░░░░░░
Wed  ░░░░░░░░░░░░░░░░░░░░░██░███░██░░░░░░░░░░░░░░░░░░░░░░
Thu  ░░░░░░░░░░░░░░░░░░░░███████████░░░░░░░░░░░░░░░░░░░░░
Fri  ░░░░░░░░░░░░░░░░░░░░█░███████░█░░░░░░░░░░░░░░░░░░░░░
Sat  ░░░░░░░░░░░░░░░░░░░░█░█░░░░░█░█░░░░░░░░░░░░░░░░░░░░░
--------------------------------------------------------------
Active Days: 42 | Estimated Commits: 504
```

---

## 🚀 Quick Start

### 1. Fast Activity Boost for Today (20 commits)

Want your GitHub square today to turn maximum neon green immediately?

```bash
python painter.py --today 20 --repo my-activity-repo
```

Then push to GitHub:
```bash
cd my-activity-repo
git remote add origin https://github.com/<YOUR-USERNAME>/<ANY-EMPTY-REPO>.git
git branch -M main
git push -u origin main --force
```

### 2. Preview Art in Terminal

```bash
# Preview built-in pixel art
python painter.py --art invader --preview
python painter.py --art cat --preview
python painter.py --art heart --preview
python painter.py --art ghost --preview

# Preview custom text
python painter.py --text "HI" --preview
python painter.py --text "DEV" --preview
```

### 3. Paint and Generate Commits

```bash
# Paint on the live rolling 52-week profile window
python painter.py --art invader --paint --repo canvas-repo

# Paint for a specific historical year (e.g. 2025)
python painter.py --art heart --year 2025 --paint --repo canvas-repo
```

### 4. Push to Your GitHub Profile

1. Create a new repository on [GitHub](https://github.com/new) (can be **public** or **private** — make sure *"Include private contributions"* is checked in your profile settings if private).
2. Push your generated canvas:

```bash
cd canvas-repo
git remote add origin https://github.com/<YOUR-USERNAME>/<REPO-NAME>.git
git branch -M main
git push -u origin main --force
```

Refresh your profile page and admire your new pixel art! 🎉

---

## 🎨 Creating Custom Presets

Create a text file in `presets/your_art.txt` with up to 7 lines:
- `.` or ` ` = 0 commits (blank)
- `1` = 1 commit (light green)
- `2` = 3 commits (medium green)
- `3` = 6 commits (dark green)
- `4` or `#` = 12 commits (bright neon green)

Example:
```text
 #   # 
### ###
#######
# # # #
#######
 # # # 
  ###  
```

Run:
```bash
python painter.py --art your_art --preview
```

---

## 🧪 Testing

```bash
python -m unittest discover -s tests
```

---

## 📜 License

MIT License. Free to use, modify, and star! ⭐
