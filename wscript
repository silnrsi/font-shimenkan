APPNAME="Shimenkan"
getufoinfo('source/masters/ShimenkanMaster-ExtraLight.ufo')
for d in ('Roman', ):
    designspace('source/Shimenkan'+d+'.designspace',
                target = "${DS:FILENAME_BASE}.ttf",
                opentype = fea("source/${DS:FILENAME_BASE}.fea",
                                master = "source/shimenkan.feax"),
                pdf = fret(params="-r -oi"))
