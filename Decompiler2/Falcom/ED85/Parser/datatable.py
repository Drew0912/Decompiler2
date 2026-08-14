from Falcom.Common import *
from Falcom.ED84.Parser.datatable import *
from Falcom.ED84.Parser.datatable import createDataTable

class MapBgmTableData(TableDataEntry):
    DESCRIPTOR  = (
        ('map',     'M'),
        ('bgmId',   'H'),
        ('word03',  'W'),
        ('word04',  'W'),
    )

class EventTableData(TableDataEntry):
    DESCRIPTOR = (
        ('eventId',         'W'),
        ('eventEntry',      'S'),
        ('word01',          'W'),
        ('word02',          'W'),
        ('desc',            'S'),
        ('jumpEntry',       'S'),
        ('word03',          'W'),
        ('word04',          'W'),
        ('scena',           'S'),
        ('word05',          'W'),
        ('nextEventId',     'W'),
        ('word06',          'W'),
        ('str04',           'S'),
        ('word07',          'W'),
        ('word08',          'W'),
        ('word09',          'W'),
        ('word0A',          'W'),
        ('word0B',          'W'),
        ('word0C',          'W'),
        ('word0D',          'W'),
        ('word0E',          'W'),
    )

class EventGroupData(TableDataEntry):
    DESCRIPTOR  = (
        ('id',      'W'),
        ('name',    'S'),
    )

class ItemTableData(TableDataEntry):
    ENTRY_NAME = 'item'
    DESCRIPTOR = (
        ('itemId',          'W'),
        ('chrId',           'W'),
        ('flags',           'S'),
        ('word04',          'W'),
        ('type',            'W'),
        ('unkByte',         'B'),
        ('subtype',         'B'),
        ('attribute',       'B'),
        ('battleStyle',     'W'),
        ('slash',           'B'),
        ('thrust',          'B'),
        ('pierce',          'B'),
        ('strike',          'B'),
        ('rangeType',       'B'),
        ('range',           'f'),
        ('area',            'C'),
        ('effect1',         'W'),
        ('effect1Param1',   'L'),
        ('effect1Param2',   'L'),
        ('effect1Param3',   'L'),
        ('effect2',         'W'),
        ('effect2Param1',   'L'),
        ('effect2Param2',   'L'),
        ('effect2Param3',   'L'),
        ('effect3',         'W'),
        ('effect3Param1',   'L'),
        ('effect3Param2',   'L'),
        ('effect3Param3',   'L'),
        ('effect4',         'W'),
        ('effect4Param1',   'L'),
        ('effect4Param2',   'L'),
        ('effect4Param3',   'L'),
        ('effect5',         'W'),
        ('effect5Param1',   'L'),
        ('effect5Param2',   'L'),
        ('effect5Param3',   'L'),
        ('str',             'I'),
        ('def_',            'I'),
        ('ats',             'I'),
        ('adf',             'I'),
        ('dex',             'I'),
        ('agl',             'I'),
        ('spd',             'I'),
        ('mov',             'I'),
        ('hp',              'I'),
        ('ep',              'I'),
        ('price',           'I'),
        ('maxAmount',       'H'),
        ('unku16',          'H'),
        ('sort',            'H'),
        ('dlcId',           'W'),
        ('name',            'S'),
        ('description',     'S'),
    )

class ItemTableDataQuartz(TableDataEntry):
    ENTRY_NAME = 'item_q'
    DESCRIPTOR = ItemTableData.DESCRIPTOR + (
        ("word",            "W"),
        ("prio_balanced",   "W"),
        ("prio_phy",        "W"),
        ("prio_mag",        "W"),
        ("prio_spd",        "W"),
        ("artId1",          "W"),
        ("artId2",          "W"),
        ("artId3",          "W"),
        ("artId4",          "W"),
        ("artId5",          "W"),
        ("artId6",          "W"),
    )

class ItemTableDataEquipment(TableDataEntry):
    ENTRY_NAME = 'item_e'
    DESCRIPTOR = ItemTableData.DESCRIPTOR + (
        ("word",            "W"),
        ("prio_balanced",   "W"),
        ("prio_phy",        "W"),
        ("prio_mag",        "W"),
        ("prio_spd",        "W"),
    )

DataTable.DataTableDataTypes.update({
    'MapBgmTableData'       : MapBgmTableData,
    'EventTableData'        : EventTableData,
    'EventGroupData'        : EventGroupData,
    'item'                  : ItemTableData,
    'item_q'                : ItemTableDataQuartz,
    'item_e'                : ItemTableDataEquipment,
})

DataTable.PythonHeader = [
    'from Falcom.ED85.Parser.datatable import *',
    '',
    'entries = [',
]
