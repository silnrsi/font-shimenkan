#!/usr/bin/env python
'''Adds anchors to Miao fonts based on a csv spec (glyphname, anchorset). Based on psfaddanchors.
Deletes all anchors in listed glyphs and adds those appropriate for the names anchorset.'''
__url__ = 'http://github.com/silnrsi/font-shimenkan'
__copyright__ = 'Copyright (c) 2018 SIL International (http://www.sil.org)'
__license__ = 'Released under the MIT License (http://opensource.org/licenses/MIT)'
__author__ = 'Victor Gaultney'

from silfont.core import execute

argspec = [
    ('ifont', {'help': 'Input font file'}, {'type': 'infont'}),
    ('ofont', {'help': 'Output font file', 'nargs': '?'}, {'type': 'outfont'}),
    ('-i', '--input', {'help': 'Input anchors spec in csv'}, {'type': 'incsv'}),
    ('-l','--log',{'help': 'Log file'}, {'type': 'outfile', 'def': 'addedanchors.log'})]

# set height levels
ancparas = {
    'Extra Light': { 'W': 335, 'D': 646, '_S': 170, '_W': 110, '_L': 265 },
    'Black': {'W': 330, 'D': 578, '_S': 200, '_W': 138, '_L': 321 }
}

hlevel = 700
slevel = 660
llevel = -45
hmarklevel = -40

def doit(args) :
    font = args.ifont
    listinput = args.input
    logger = args.logger

    style = font.fontinfo.getval('styleName')

    for line in listinput:
        glyphname = line[0]
        anchorset = line[1]  # could be con, vow, mark

        glyph = font.deflayer[glyphname]
        adv = int(glyph['advance'].width)

        while len(glyph['anchor'])>0:
            glyph.remove('anchor', 0)

        if anchorset == "con":
            glyph.add('anchor', {'name': 'H', 'x': ( adv/2 ), 'y': hlevel})
            glyph.add('anchor', {'name': 'S', 'x': adv, 'y': slevel})
            glyph.add('anchor', {'name': 'W', 'x': adv, 'y': ancparas[style]['W']})
            glyph.add('anchor', {'name': 'E', 'x': adv, 'y': (ancparas[style]['W'] + ((slevel-ancparas[style]['W'])/3))})
            glyph.add('anchor', {'name': 'K', 'x': adv, 'y': (ancparas[style]['W'] - ((slevel-ancparas[style]['W'])/3))})
            glyph.add('anchor', {'name': 'F', 'x': adv, 'y': 0})
            glyph.add('anchor', {'name': 'D', 'x': adv, 'y': ancparas[style]['D']})
            glyph.add('anchor', {'name': 'L', 'x': ( adv/2 ), 'y': llevel})

        if anchorset == "vow":   # vowels used as bases
            glyph.add('anchor', {'name': 'SB', 'x': 0, 'y': ancparas[style]['_S']})
            glyph.add('anchor', {'name': 'WB', 'x': 0, 'y': ancparas[style]['_W']})
            glyph.add('anchor', {'name': 'FB', 'x': 0, 'y': 0})
            glyph.add('anchor', {'name': 'S', 'x': adv, 'y': ancparas[style]['_S']})
            glyph.add('anchor', {'name': 'W', 'x': adv, 'y': ancparas[style]['_W']})
            glyph.add('anchor', {'name': 'F', 'x': adv, 'y': 0})

        if anchorset == "mark":   # vowels used as marks
            glyph.add('anchor', {'name': '_H', 'x': ( adv/2 ), 'y': hmarklevel})
            glyph.add('anchor', {'name': '_HL', 'x': 0, 'y': hmarklevel})
            glyph.add('anchor', {'name': '_HR', 'x': adv, 'y': hmarklevel})
            glyph.add('anchor', {'name': '_L', 'x': ( adv/2 ), 'y': ancparas[style]['_L']})
            glyph.add('anchor', {'name': '_LL', 'x': 0, 'y': ancparas[style]['_L']})
            glyph.add('anchor', {'name': '_LR', 'x': adv, 'y': ancparas[style]['_L']})

    return font


def cmd() : execute("UFO",doit,argspec)
if __name__ == "__main__": cmd()

