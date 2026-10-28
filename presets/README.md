# Presets Guide

Place `.txt` files in this directory to create custom heatmap presets.

## Rules:
- Up to 7 lines (each line corresponds to a day of the week, starting with Sunday).
- Use numbers `0` to `4` or symbols:
  - `.` or ` ` = Empty (0 commits)
  - `1` or `░` = Light green (1 commit)
  - `2` or `▒` = Medium green (3 commits)
  - `3` or `▓` = Deep green (6 commits)
  - `4` or `█` or `#` = Maximum bright green (12 commits)
