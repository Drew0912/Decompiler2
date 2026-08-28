# Reverie 

## Usage

Run the `activateED85venv.bat` script in the Decompiler2 directory either in terminal or by double clicking. This will open a terminal in the ED85 directory with venv activated ready to use for Reverie. Similarly, running `activateVenv.bat` in the `Decompiler2\Falcom\ED85` directory will do the same.

To disassemble a script file `.dat`, have the script file in the `Falcom/ED85` folder and run the following command

`scena2py.py *.dat`

where `*.dat` is (path to) the script file. The output will be in the directory with `scena2py.py` named `*.py`. If the above command does not work, try `python scena2py.py *.dat`

To disassemble a table file (.tbl), have the table file in the `Falcom/ED85` folder and run the following command

`tbl2py.py *.tbl`

where `*.tbl` is (path to) the table file. The output will be in the directory with `tbl2py.py` named `*.py`. If the above command does not work, try `python tbl2py.py *.tbl`

To assemble the `*.py` back to either the script file (`*.dat`) or table file (`*.tbl`), run the python file in the terminal, i.e `*.py` or `python *.py` in the same folder that it was created in.

# Supported files

# New features
New instruction `OP_F1` has been added to the game scripts for Reverie Script Extender from [Kiseki-Frida](https://github.com/Drew0912/kiseki-frida). It can be used by the instruction `Call2SE()` and takes in a string.

## Table (text\\) files

- t_bgm.tbl
- t_name.tbl
- t_se.tbl
- t_voice.tbl
- t_magic.tbl
- t_item.tbl
- t_mons.tbl

## Metadata

- chrId
- craftId (May not be perfect due to name and craftId not being unique enough e.g United Assault)
- itemId