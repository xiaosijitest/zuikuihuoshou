# Field classes
from zuikuihuoshou.field.field import Field, FieldError, MissingField, joinPath  # noqa
from zuikuihuoshou.field.bit_field import Bit, Bits, RawBits  # noqa
from zuikuihuoshou.field.byte_field import Bytes, RawBytes  # noqa
from zuikuihuoshou.field.sub_file import SubFile, CompressedField  # noqa
from zuikuihuoshou.field.character import Character  # noqa
from zuikuihuoshou.field.integer import (Int8,  Int16,  Int24,  Int32,  Int64,  # noqa
                                   UInt8, UInt16, UInt24, UInt32, UInt64,
                                   GenericInteger)
from zuikuihuoshou.field.enum import Enum  # noqa
from zuikuihuoshou.field.string_field import (GenericString,  # noqa
                                        String, CString, UnixLine,
                                        PascalString8, PascalString16,
                                        PascalString32)
from zuikuihuoshou.field.padding import (PaddingBits, PaddingBytes,  # noqa
                                   NullBits, NullBytes)

# Functions
from zuikuihuoshou.field.helper import (isString, isInteger,  # noqa
                                  createPaddingField, createNullField,
                                  createRawField, writeIntoFile,
                                  createOrphanField)

# FieldSet classes
from zuikuihuoshou.field.fake_array import FakeArray  # noqa
from zuikuihuoshou.field.basic_field_set import (BasicFieldSet,  # noqa
                                           ParserError, MatchError)
from zuikuihuoshou.field.generic_field_set import GenericFieldSet  # noqa
from zuikuihuoshou.field.seekable_field_set import SeekableFieldSet, RootSeekableFieldSet  # noqa
from zuikuihuoshou.field.field_set import FieldSet  # noqa
from zuikuihuoshou.field.static_field_set import StaticFieldSet  # noqa
from zuikuihuoshou.field.parser import Parser  # noqa
from zuikuihuoshou.field.vector import GenericVector, UserVector  # noqa

# Complex types
from zuikuihuoshou.field.float import Float32, Float64, Float80  # noqa
from zuikuihuoshou.field.timestamp import (  # noqa
    GenericTimestamp,
    TimestampUnix32, TimestampUnix64, TimestampMac32, TimestampUUID60,
    TimestampWin64, TimedeltaMillisWin64,
    DateTimeMSDOS32, TimeDateMSDOS32, TimedeltaWin64)

# Special Field classes
from zuikuihuoshou.field.link import Link, Fragment  # noqa
from zuikuihuoshou.field.fragment import FragmentGroup, CustomFragment  # noqa

available_types = (Bit, Bits, RawBits,
                   Bytes, RawBytes,
                   SubFile,
                   Character,
                   Int8, Int16, Int24, Int32, Int64,
                   UInt8, UInt16, UInt24, UInt32, UInt64,
                   String, CString, UnixLine,
                   PascalString8, PascalString16, PascalString32,
                   Float32, Float64,
                   PaddingBits, PaddingBytes,
                   NullBits, NullBytes,
                   TimestampUnix32, TimestampMac32, TimestampWin64,
                   TimedeltaMillisWin64,
                   DateTimeMSDOS32, TimeDateMSDOS32,
                   #                   GenericInteger, GenericString,
                   )
