from zuikuihuoshou.parser import createParser
from zuikuihuoshou.editor import createEditor
from zuikuihuoshou.field import writeIntoFile

parser = createParser("file.zip")
with parser:
    editor = createEditor(parser)
    editor["end_central_directory/comment"].value = "new comment"
    writeIntoFile(editor, "file_comment.zip")
