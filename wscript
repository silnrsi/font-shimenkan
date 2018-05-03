out = 'results'
APPNAME="Shimenkan"
getufoinfo('source/masters/ShimenkanMaster-ExtraLight.ufo')
for d in ('Roman', ):
    designspace('source/Shimenkan'+d+'.designspace',
                # params="-c",
                target=str_replace('${NAME}.ttf', ' ', '-'))
