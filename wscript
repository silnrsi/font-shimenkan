#!/usr/bin/python2
# encoding: utf-8
# this is a smith configuration file
# http://scripts.sil.org/smith

# set some default output folders
# DOCDIR = ["documentation", "web"]

# set the version control system for srcdist
VCS = 'git'

# set the font name, version, licensing and description
APPNAME="Shimenkan"
DESC_SHORT = "A family of fonts for the Miao (Pollard) script."

# retrieve all the authorship information from one of the master UFOs
getufoinfo('source/masters/ShimenkanMaster-ExtraLight.ufo')
BUILDLABEL="test"

# set up the sile tests (using fontproof)
testCommand('sile', cmd='${SILE} -o "${TGT}" "${SRC[0].abspath()}" -f "${SRC[1]}"', extracmds=['sile'], shapers=0, supports=['.sil'], ext='.pdf')

def langfontname(f, l):
    return f + " " + l

# set up the build parameters from the designspace files
# (the Italic designspace is not included yet)
fontfamily=APPNAME
for dspace in ('Roman', ):
    d = designspace('source/' + fontfamily + dspace + '.designspace',
                target = "${DS:FILENAME_BASE}.ttf",
                opentype = fea("source/${DS:FILENAME_BASE}.fea",
                                master = "source/" + fontfamily + ".feax"),
                pdf = fret(params="-r -oi"),
                name = "${DS:FAMILYNAME}")
    for l in ("sfm", "hmz", "lpo", "hmd"):
        for f in d.fonts:
            font(target = process('langs/' + l + "/" + f.target[:f.target.rindex("-")] + l.title() + f.target[f.target.rindex("-"):],
                            cmd("ttfdeflang -d " + l + " ${DEP} ${TGT}"),
                            name(langfontname(f.name, l))),
                 source = f.target)

