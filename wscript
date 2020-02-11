#!/usr/bin/python3
# -*- coding: utf-8 -*-

APPNAME="Shimenkan"
DESC_SHORT = "A family of fonts for the Miao (Pollard) script."

# retrieve all the authorship information from one of the master UFOs
getufoinfo('source/masters/ShimenkanMaster-ExtraLight.ufo')
# BUILDLABEL="test"

opts = preprocess_args({'opt' : '--alllangs'}, {'opt' : '--allreglangs'})

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
                instanceparams = '-W',
                opentype = fea("source/${DS:FILENAME_BASE}.fea",
                                params = '-m source/${DS:FILENAME_BASE}.map',
                                master = "source/" + fontfamily + ".feax"),
                pdf = fret(params="-r -oi"),
                script = ['DFLT'],
                name = "${DS:FAMILYNAME}")
    for l in langinfo.keys():
        packages[l].package_files['langs/' + l + '/*'] = '/'
        packages[l].package_files['documentation/UsingTheFonts.pdf'] = '/'
        packages[l].package_files['documentation/字体使用说明.pdf'] = '/'
        packages[l].package_files['请先阅读.txt'] = '/'
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
            if '--alllangs' not in opts and \
                        (f.target != "Shimenkan-Regular.ttf" or '--allreglangs' not in opts):
                n.no_test = True

