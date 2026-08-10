def _init():
    import Common

    if Common.log.name:
        return

    Common.GlobalConfig.DefaultEncoding = 'UTF8'
    Common.log.setLevel(Common.logging.DEBUG)
    Common.log.name = 'ED85'

    if not Common.GlobalConfig.ChrTable:
        try:
            from .Metadata.chrId_table import chrIdTable
            Common.GlobalConfig.ChrTable.update(chrIdTable)
        except ModuleNotFoundError as e:
            print(f"No chrId Metadata found, run gen_tables.py: {e}")

_init()

from .InstructionTable import *
from .Parser import *
