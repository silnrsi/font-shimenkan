#!/usr/bin/python2
# encoding: utf-8
# this is a smith configuration file
# http://scripts.sil.org/smith

# set some default output folders
DOCDIR = ["documentation", "web"]

# set the version control system
VCS = 'git'

# set the font name, version, licensing and description
APPNAME="Shimenkan"
FONTFAMILY=APPNAME
DESC_SHORT = "A family of fonts for the Miao (Pollard) script."

# retrieve all the authorship information from one of the master UFOs
getufoinfo('source/masters/ShimenkanMaster-ExtraLight.ufo')
BUILDLABEL="test"

# set up the sile tests (using fontproof)
testCommand('sile', cmd='${SILE} -o "${TGT}" "${SRC[0].abspath()}" -f "${SRC[1]}"', extracmds=['sile'], shapers=0, supports=['.sil'], ext='.pdf')

# set up the build parameters from the designspace files
# (the Italic designspace is not included yet)
for DESIGNSPACEFILE in ('Roman', ):
    designspace('source/' + FONTFAMILY + DESIGNSPACEFILE + '.designspace',
                target = "${DS:FILENAME_BASE}.ttf",
                opentype = fea("source/${DS:FILENAME_BASE}.fea",
                                master = "source/" + FONTFAMILY + ".feax"),
                pdf = fret(params="-r -oi"))
