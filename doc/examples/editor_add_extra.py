from zuikuihuoshou.parser import createParser
from zuikuihuoshou.editor import createEditor
from zuikuihuoshou.field import writeIntoFile
from zuikuihuoshou.editor import EditableInteger, EditableBytes

parser = createParser("file.gz")
with parser:
    editor = createEditor(parser)
    extra = "abcd"
    editor["has_extra"].value = True
    editor.insertAfter("os",
                       EditableInteger(editor, "extra_length", False,
                                       16, len(extra)),
                       EditableBytes(editor, "extra", extra))
    writeIntoFile(editor, "file_extra.gz")
