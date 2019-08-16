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
TESTFILES = {"wordlists/lpo-headwords.txt": "lang=lpo",
             "wordlists/sfm_combinations.txt": "lang=x-hbotSFM",
             "wordlists/hmd-wordlist.txt": "lang=x-hbotHMD"}

opts = preprocess_args({'opt' : '--alllangs'})

langinfo = {
    'yna' : 'Shimenkan Zonghe',
    'hmz' : 'Shimenkan MGS',
    'hmd' : 'Sapushan',
    'hmdd' : 'Shimenkan Guifan',
    'sfm' : 'Shimenkan MAS',
    'ygp' : 'Shimenkan GSM',
    'ywqa' : 'Salaowu',
    'lpo' : 'Taogu'
}

# set up the sile tests (using fontproof)
# testCommand('sile', cmd='${SILE} -o "${TGT}" "${SRC[0].abspath()}" -f "${SRC[1]}"', extracmds=['sile'], shapers=0, supports=['.sil'], ext='.pdf')

def langfontname(f, l):
    return f.replace('Shimenkan', langinfo[l])

ftmlTest("tools/ftml-padauk.xsl")

# set up the build parameters from the designspace files
# (the Italic designspace is not included yet)
fontfamily=APPNAME
packages = { x : package(appname = langfontname("Shimenkan", x).replace(" ", ""),
                         version = VERSION,
                         package_files = {})
                 for x in langinfo.keys() }
                       
for dspace in ('Roman', ):
    d = designspace('source/' + fontfamily + dspace + '.designspace',
                target = "${DS:FILENAME_BASE}.ttf",
                opentype = fea("source/${DS:FILENAME_BASE}.fea",
                                buildusingsilfont = True,
                                params = '-m source/${DS:FILENAME_BASE}.map',
                                master = "source/" + fontfamily + ".feax"),
                pdf = fret(params="-r -oi"),
                script = ['DFLT'],
                name = "${DS:FAMILYNAME}")
    for l in langinfo.keys():
        packages[l].package_files['langs/' + l + '/*'] = '/'
        for f in d.fonts:
            (fname, _, ext) = f.target.rpartition("-")
            fname = langfontname(fname, l).replace(" ", "")
            outf = 'langs/' + l + "/" + fname + "-" + ext
            n = font(target = process(outf, cmd("psfdeflang -q -L " + l + " ${DEP} ${TGT}"),
                                            name(langfontname(f.name, l))),
                    opentype = internal(),
                    source = f.target,
                    lang = l,
                    package = packages[l])
            if '--alllangs' not in opts:
                n.no_test = True

