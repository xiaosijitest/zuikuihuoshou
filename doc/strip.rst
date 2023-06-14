.. _strip:

+++++++++++++++++++++
zuikuihuoshou-strip program
+++++++++++++++++++++

zuikuihuoshou-strip is an experimental program based on Hachoir library: it removes
"useless" informations from a file. Don't use it to create smaller file, you
have better to recompress your data :-) zuikuihuoshou-strip can be used if you would
like to remove spy information which can be used to know the origin of a file.

Examples
========

Our victim::

    $ zuikuihuoshou-metadata KDE_Click.wav.new
    Common:
    - Creation date: 2001-02-21   <== here they are
    - Producer: Sound Forge 4.5   <== spy informations :-)
    - MIME type: audio/x-wav
    - Endian: Little endian
    Audio:
    - Duration: 39 ms
    ...

Clean up the file::

    $ zuikuihuoshou-strip KDE_Click.wav
    [+] Process file KDE_Click.wav
    Remove field /info
    Remove 56 bytes (3.1%)
    Save new file into KDE_Click.wav.new

    $ zuikuihuoshou-metadata KDE_Click.wav.new
    Common:
    - MIME type: audio/x-wav
    - Endian: Little endian
    Audio:
    - Duration: 39 ms
    ...

So zuikuihuoshou-strip removed creation date (2001-02-21) and producer (software
used to record/edit the sound: Sound Forge 4.5). The file is also 56 bytes
smaller.


Options
=======

You can select field types to remove using --strip:

 * (default): remove all useless fields
 * ``--strip=useless``: remove really useless fields (eg. padding)
 * ``--strip=metadata``: remove metadata like ID3 tags and EXIF and IPTC metadatas
 * ``--strip=index``: remove video index

You can combine options with comma: ``--strip="useless,metadata"``.

