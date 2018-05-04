APPNAME="Shimenkan"
getufoinfo('source/masters/ShimenkanMaster-ExtraLight.ufo')
for d in ('Roman', ):
    designspace('source/Shimenkan'+d+'.designspace',
                target="${DS:FILENAME_BASE}.ttf")
