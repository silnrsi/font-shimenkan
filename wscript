APPNAME="Shimenkan"
testCommand('sile', cmd='${SILE} -o "${TGT}" "${SRC[0].abspath()}" -f "${SRC[1]}"', extracmds=['sile'], shapers=0, supports=['.sil'], ext='.pdf')
getufoinfo('source/masters/ShimenkanMaster-ExtraLight.ufo')
for d in ('Roman', ):
    designspace('source/Shimenkan'+d+'.designspace',
                target = "${DS:FILENAME_BASE}.ttf",
                opentype = fea("source/${DS:FILENAME_BASE}.fea",
                                master = "source/shimenkan.feax"),
                pdf = fret(params="-r -oi"))
