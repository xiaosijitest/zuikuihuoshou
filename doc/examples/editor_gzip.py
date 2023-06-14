from zuikuihuoshou.parser import createParser
from zuikuihuoshou.editor import createEditor
from zuikuihuoshou.field import writeIntoFile

parser = createParser("file.gz")
with parser:
    editor = createEditor(parser)
    del editor["filename"]
    editor["has_filename"].value = False
    writeIntoFile(editor, "noname.gz")
