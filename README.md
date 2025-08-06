# Lncur

A simple python CLI to easily port Windows cursor packs to Linux! </br>
[![](https://img.shields.io/github/v/release/claymorwan/lncur)](https://GitHub.com/claymorwan/lncur)
## Install

### Pypi
```shell
pip install lncur
```

### Aur
lncur is also available on the AUR with your AUR helper.
```shell
yay -S python-lncur
```
## Usage
### Setup
1. First you need to set up your cursor theme directory, you can refer to the step 5 of the [KDE guide for creating cursor theme](https://develop.kde.org/docs/features/cursor/#creating-a-theme-folder).
It should look like this :
```
Root of your super cool ported theme :D
├── cursors
└── index.theme
```
> You can run `lncur -m` to quickly set up the directory 

2. Put all of your Windows cursor theme files (.ico and/or .ani) in the `cursors` directory.
3. Rename all your file like the following (here using default Windows cursor names, depending on what cursor theme you're porting, the files can be named different, it's fine just rename them):

| Cursor                                                                                                                                   | Windows name             | Linux/Xcursor name |
|------------------------------------------------------------------------------------------------------------------------------------------|--------------------------|--------------------|
| ![Normal_select.png](https://raw.githubusercontent.com/claymorwan/lncur/refs/heads/main/assets/wincur/Normal_select.png)                 | Normal select            | `default`          |
| ![Text_select.png](https://raw.githubusercontent.com/claymorwan/lncur/refs/heads/main/assets/wincur/Text_select.png)                     | Text select              | `text`             |
| ![Busy.png](https://raw.githubusercontent.com/claymorwan/lncur/refs/heads/main/assets/wincur/Busy.gif)                                   | Busy                     | `wait`             |
| ![Precision_select.png](https://raw.githubusercontent.com/claymorwan/lncur/refs/heads/main/assets/wincur/Precision_select.png)           | Precision select         | `crosshair`        |
| ![Alternate_select.png](https://raw.githubusercontent.com/claymorwan/lncur/refs/heads/main/assets/wincur/Alternate_select.png)           | Alternate select         | `up-arrow`         |
| ![Diagonal_resize_1.png](https://raw.githubusercontent.com/claymorwan/lncur/refs/heads/main/assets/wincur/Diagonal_resize_1.png)         | Diagonal resize 1        | `size_fdiag`       |
| ![Diagonal_resize_2.png](https://raw.githubusercontent.com/claymorwan/lncur/refs/heads/main/assets/wincur/Diagonal_resize_2.png)         | Diagonal resize 2        | `size_bdiag`       |
| ![Horizontal_resize.png](https://raw.githubusercontent.com/claymorwan/lncur/refs/heads/main/assets/wincur/Horizontal_resize.png)         | Horizontal resize        | `size_hor`         |
| ![Horizontal_resize.png](https://raw.githubusercontent.com/claymorwan/lncur/refs/heads/main/assets/wincur/Vertical_resize.png)           | Vertical resize          | `size_ver`         |
| ![Move.png](https://raw.githubusercontent.com/claymorwan/lncur/refs/heads/main/assets/wincur/Move.png)                                   | Move                     | `fleur`            |
| ![Unavailable.png](https://raw.githubusercontent.com/claymorwan/lncur/refs/heads/main/assets/wincur/Unavailable.png)                     | Unavailable              | `not-allowed`      |
| ![Link_select.png](https://raw.githubusercontent.com/claymorwan/lncur/refs/heads/main/assets/wincur/Link_select.png)                     | Link select              | `pointer`          |
| ![Working_in_background.gif](https://raw.githubusercontent.com/claymorwan/lncur/refs/heads/main/assets/wincur/Working_in_background.gif) | Working in background    | `progress`         |
| ![Help_select.png](https://raw.githubusercontent.com/claymorwan/lncur/refs/heads/main/assets/wincur/Help_select.png)                     | Help select              | `help`             |
| ![Pen.png](https://raw.githubusercontent.com/claymorwan/lncur/refs/heads/main/assets/wincur/Pen.png)                                     | The pen one idk the name | `pencil`           |
> All of the names are taken from the KDE breeze cursor theme </br>
> Cursors image from [Microsoft](https://learn.microsoft.com/en-us/windows/win32/menurc/about-cursors) </br>
You can remove the pin and person cursors as they're not used.

 4. Convert the files to X cursor files using [win2xcur](https://github.com/quantum5/win2xcur), you can convert them all by going in the `cursors` directory and run
```shell
win2xcur *
```
Now your cursor theme should look like this now:
```
Root of ur super amazing theme :3
├── cursors
│   ├── crosshair
│   ├── default
│   ├── fleur
│   ├── help
│   ├── not-allowed
│   ├── pencil
│   ├── pointer
│   ├── progress
│   ├── size_bdiag
│   ├── size_fdiag
│   ├── size_hor
│   ├── size_ver
│   ├── text
│   ├── up-arrow
│   └── wait
└── index.theme
```
### Running the program
Now you can use lncur to do all the symlinking by running lncur inside the directory where the `cursors` dir and running:
```shell
lncur -l
```

All arguments:
```shell
usage: lncur [-h] [-v] [-l] [-m MAKE]

options:
  -h, --help       show this help message and exit
  -v, --version    Prints version
  -l, --link       Symlinks cursors files
  -m, --make MAKE  Make a cursor theme directory
```

## Dev

1. Install [uv](https://docs.astral.sh/uv/)
2. Run:
```shell
git clone https://github.com/claymorwan/lncur.git
cd lncur
uv venv
source ./.venv/bin/activate
uv sync
```
3. Build package with `uv build`
