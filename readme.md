# Decompiler2

Modified from https://github.com/Ouroboros/Falcom/tree/master/Decompiler2.

Extended Reverie (ED85) to support a new opcode `0xF1` and other changes for [Kiseki-Frida](https://github.com/Drew0912/kiseki-frida) along with helper scena functions.

## Setting up Decompiler2

Instructions are for Windows. May work for other operating systems (not tested) using equivalent instructions not included here but the included `.bat` scripts will not work.

Decompiler2 requires Python 3.10 or newer so if not installed, install [Python](https://www.python.org/). Then, if not already done so, download/clone this repo. 

For this set up, a virtual environment will be used to avoid installing packages globally and avoid setting up environment variables. Open command prompt (cmd) in the Decompiler2 directory (you should see 3 folders in the Decompiler2 directory called Assembler, Common and Falcom) and create a python virtual environment (.venv) by running the following command

`python -m venv .venv`

Now activate the virtual environment by running the following command in the same terminal

`.venv\Scripts\activate.bat`

You should see `(.venv)` to the left of a file path on the current line of the terminal. The `(.venv)` at the start of the line tells you that you have activated the virtual environment for the terminal. It is important that the virtual environment is being used for Decompiler2.

Next, install the required libraries for Decompiler2 by running the following command in the same terminal

`pip install git+https://github.com/Ouroboros/PyLibs`

To use Decompiler2, we need the path to the folder `Decompiler2` to be added to the PYTHONPATH as well as having venv activated. The included `.bat` scripts will handle this.

Decompiler2 is now set up.

## General use

To use Decompiler2, navigate to the following directory.

- Falcom\ED6 = [Trails in the Sky](Decompiler2/Falcom/ED6/)
- Falcom\ED62 = [Trails in the Sky SC](Decompiler2/Falcom/ED62/)
- Falcom\ED83 = [Trails of Cold Steel 3](Decompiler2/Falcom/ED83/)
- Falcom\ED84 = [Trails of Cold Steel 4](Decompiler2/Falcom/ED84/)
- Falcom\ED85 = [Hajimari no Kiseki/Trails into Reverie](Decompiler2/Falcom/ED85/)
- Falcom\ED9 = [Kuro no Kiseki/Trails through Daybreak](Decompiler2/Falcom/ED9/)

Only the above games are supported. Further instructions are in the `readme.md` files in the corresponding directories.

## Instructions by others to set up and use Decompiler2.

The following instructions do set up Decompiler2 in a different way, just use the Decompiler2 folder from this repo instead.

- https://github.com/Ouroboros/Falcom/wiki/Decompiler2-ED8-Usage
- https://github.com/Trails-Research-Group/Doc/blob/main/tutorials/Setting-up-ED8-Decompiler.md

