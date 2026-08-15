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

# t_item.tbl
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

# t_mons.tbl
class StatusTableData(TableDataEntry):
    ENTRY_NAME = 'status'
    DESCRIPTOR = (
        ('algoFile',             'S'),
        ('model',                'S'),
        ('ani',                  'S'),
        ('modelScale',           'f'),
        ('cameraPivotHeight',    'f'),
        ('float1',               'f'),
        ('float2',               'f'),
        ('float3',               'f'),
        ('float4',               'f'),
        ('float5',               'f'),
        ('short6',               'W'),
        ('short7',               'W'),
        ('isFemale',             'B'),
        ('level',                'C'),
        ('hpBase',               'I'),
        ('hpMultipler',          'f'),
        ('epMax',                'H'),
        ('epInit',               'H'),
        ('cpMax',                'H'),
        ('cpInit',               'H'),
        ('str',                  'I'),
        ('strMultipler',         'f'),
        ('def_',                 'I'),
        ('defMultipler',         'f'),
        ('ats',                  'I'),
        ('atsMultipler',         'f'),
        ('adf',                  'I'),
        ('adfMultipler',         'f'),
        ('dex',                  'H'),
        ('dexMultipler',         'f'),
        ('agl',                  'H'),
        ('aglMultipler',         'f'),
        ('evade',                'H'),
        ('spd',                  'H'),
        ('spdMultipler',         'f'),
        ('mov',                  'H'),
        ('movMultipler',         'f'),
        ('exp',                  'H'),
        ('expMultipler',         'f'),
        ('brk',                  'H'),
        ('brkMultipler',         'f'),
        ('efficacyEarth',        'C'),
        ('efficacyWater',        'C'),
        ('efficacyFire',         'C'),
        ('efficacyWind',         'C'),
        ('efficacyTime',         'C'),
        ('efficacySpace',        'C'),
        ('efficacyMirage',       'C'),
        ('efficacyPoison',       'C'),
        ('efficacySeal',         'C'),
        ('efficacyMute',         'C'),
        ('efficacyBlind',        'C'),
        ('efficacySleep',        'C'),
        ('efficacyBurn',         'C'),
        ('efficacyFreeze',       'C'),
        ('efficacyPetrify',      'C'),
        ('efficacyFaint',        'C'),
        ('efficacyConfuse',      'C'),
        ('efficacyCharm',        'C'),
        ('efficacyDeathblow',    'C'),
        ('efficacyNightmare',    'C'),
        ('efficacyATDelay',      'C'),
        ('efficacyVanish',       'C'),
        ('efficacySPDDown',      'C'),
        ('efficacySlash',        'H'),
        ('efficacyThurst',       'H'),
        ('efficacyPierce',       'H'),
        ('efficacyStrike',       'H'),
        ('sepithEarth',          'C'),
        ('sepithWater',          'C'),
        ('sepithFire',           'C'),
        ('sepithWind',           'C'),
        ('sepithTime',           'C'),
        ('sepithSpace',          'C'),
        ('sepithMirage',         'C'),
        ('sepithMass',           'C'),
        ('sepithEarthMultipler', 'f'),
        ('sepithWaterMultipler', 'f'),
        ('sepithFireMultipler',  'f'),
        ('sepithWindMultipler',  'f'),
        ('sepithTimeMultipler',  'f'),
        ('sepithSpaceMultipler', 'f'),
        ('sepithMirageMultipler','f'),
        ('sepithMassMultipler',  'f'),
        ('dropItemId1',          'W'),
        ('dropAmountMin1',       'W'),
        ('dropAmountMax1',       'W'),
        ('dropRate1',            'C'),
        ('dropItemId2',          'W'),
        ('dropAmountMin2',       'W'),
        ('dropAmountMax2',       'W'),
        ('dropRate2',            'C'),
        ('statVarMin',           'f'),
        ('statVarMax',           'f'),
        ('flags',                'S'),
        ('chrId',                'W'),
        ('name',                 'S'),
        ('description',          'S'),
    )

    FLAGS_TABLE = {
        'M':  0x00000001,
        'E':  0x00000002,
        'N':  0x00000004,
        'K':  0x00000008,
        'T':  0x00000010,
        'H':  0x00000020,
        'D':  0x00000040,
        'S':  0x00000080,
        'R':  0x00000200,
        'J':  0x00000400,
        'C':  0x00000800,
        'F':  0x00001000,
        'I':  0x00002000,
        'X':  0x00004000,
        'Z':  0x00008000,
        'V':  0x00010000,
        'W':  0x00020000,
        'O':  0x00040000,
        'G':  0x00080000,
        'U':  0x00100000,
        'A':  0x00200000,
        'Y':  0x00400000,
        'B':  0x00800000,
        'P':  0x01000000,
        'Q':  0x02000000,
        'L':  0x04000000,
    }

class McburnResistTableData(TableDataEntry):
    ENTRY_NAME = 'mcburn_resist'
    DESCRIPTOR = (
        ('enemy',           'S'),
        ('long1',           'L'),
)

class ItemHelpData(TableDataEntry):
    DESCRIPTOR  = (
        ('id',      'W'),
        ('word',    'W'),
        ('desc',    'S'),
        ('word3',   'W'),
        ('word4',   'W'),
        ('word5',   'W'),
        ('word6',   'W'),
        ('byte7',   'B'),
)

# t_magic.tbl
class MagicTableData(TableDataEntry):
    ENTRY_NAME = 'magic'
    DESCRIPTOR = (
        ('id',              'W'), 
        ('chrId',           'W'), 
        ('targetType',      'S'), 
        ('type',            'B'), 
        ('damageType',      'B'), 
        ('attribute',       'B'), 
        ('battleStyle',     'B'), 
        ('rangeType',       'B'), 
        ('range',           'f'),
        ('area',            'C'),
        ('float2',          'f'),
        ('float3',          'f'),
        ('float4',          'f'),

        ('effect1',         'W'),
        ('effect1Param1',   'I'),
        ('effect1Param2',   'I'),
        ('effect1Param3',   'I'),

        ('effect2',         'W'),
        ('effect2Param1',   'I'),
        ('effect2Param2',   'I'),
        ('effect2Param3',   'I'),

        ('effect3',         'W'),
        ('effect3Param1',   'I'),
        ('effect3Param2',   'I'),
        ('effect3Param3',   'I'),

        ('effect4',         'W'),
        ('effect4Param1',   'I'),
        ('effect4Param2',   'I'),
        ('effect4Param3',   'I'),

        ('effect5',         'W'),
        ('effect5Param1',   'I'),
        ('effect5Param2',   'I'),
        ('effect5Param3',   'I'),

        ('ariaAT',          'C'),
        ('at',              'C'),
        ('costType',        'C'),
        ('epcp',            'H'),
        ('unbalanceRate',   'C'),
        ('breakRate',       'H'),
        ('level',           'C'),
        ('byte5',           'B'),
        ('sortId',          'W'),
        ('ani',             'S'),
        ('name',            'S'),
        ('description',     'S'),
    )

class ReplaceCraftData(TableDataEntry):
    ENTRY_NAME = 'replace_ex_craft'
    DESCRIPTOR = (
        ('chrId',           'W'),
        ('originalCraftId', 'W'),
        ('replacedCraftId', 'W'),

        ('word01',          'W'),
        ('scenaFlag',       'W'),
        ('word02',          'W'),
    )

DataTable.DataTableDataTypes.update({
    'MapBgmTableData'       : MapBgmTableData,
    'EventTableData'        : EventTableData,
    'EventGroupData'        : EventGroupData,
    'item'                  : ItemTableData,
    'item_q'                : ItemTableDataQuartz,
    'item_e'                : ItemTableDataEquipment,
    'status'                : StatusTableData,
    'mcburn_resist'         : McburnResistTableData,
    'ItemHelpData'          : ItemHelpData,
    'magic'                 : MagicTableData,
    'replace_ex_craft'      : ReplaceCraftData,
})

DataTable.PythonHeader = [
    'from Falcom.ED85.Parser.datatable import *',
    '',
    'entries = [',
]
