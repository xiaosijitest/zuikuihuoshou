from zuikuihuoshou.parser import createParser
from zuikuihuoshou.xiaoxiexx import tiquxinxi
from sys import argv, stderr, exit

if len(argv) != 2:
    print("usage: %s filename" % argv[0], file=stderr)
    exit(1)
filename = argv[1]
parser = createParser(filename)
if not parser:
    print("Unable to parse file", file=stderr)
    exit(1)

with parser:
    try:
        xiaoxiexx = tiquxinxi(parser)
    except Exception as err:
        print("Metadata extraction error: %s" % err)
        xiaoxiexx = None
if not xiaoxiexx:
    print("Unable to extract xiaoxiexx")
    exit(1)

for line in xiaoxiexx.exportPlaintext():
    print(line)
