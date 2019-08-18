# Shimenkan Language Behavior Summary

This page summarizes language-specific behaviors organized by language. For a more complete description of behaviors see [Font Behavior in the Shimenkan Fonts](ShimenkanBehavior.md).

Code   | Language                            | Font
:------|:------------------------------------|:----------------
[hmd]  | Large Flowery Miao                  | Sapushan
[hmdd] | alternate for Large Flowery Miao    | Shimenkan Guifan
[hmz]  | Sinicized Miao                      | Shimenkan MGS
[lpo]  | Lipo                                | Taogu
[sfm]  | Small Flowery Miao                  | Shimenkan MAS
[ygp]  | Gepo / Bai Yi                       | Shimenkan GSM
[yna]  | Aluo / Gan Yi / Laka / Niluo / Yala | Shimenkan Zonghe
[ywqa] | Wuding-Luquan Yi / Black Yi         | Salaowu

## [hmd]

Behavior                    | Setting
:---------------------------|:---------
Open AN (u16F57)            | yes
Pointed EI (u16F7A)         | yes
Left Aspiration NA (u16F10) | yes
Aspiration (u16F51)         | tucked
V+ @S                       | tucked
V @F no asp                 | tucked
V @F + asp                  | right asp
VV @F no asp                | tucked
VV @F + asp                 | tucked

## [hmdd]

Behavior                                      | Setting
:---------------------------------------------|:---------
Dotted Consonants (all warted consonants)     | yes
Ahmao nasals (u16F04, u16F10, u16F14, u16F23) | yes
Open AN (u16F57)                              | yes
Flat Top EN ENG (u16F5E, u16F5F)              | yes
Pointed EI (u16F7A)                           | yes
Aspiration (u16F51)                           | after
V+ @S                                         | after
V @F no asp                                   | after*
V @F + asp                                    | under asp
VV @F no asp                                  | after*
VV @F + asp                                   | under asp

\* [hmdd] wants V+ @F to tuck only with u16F07 (not yet supported)

## [hmz]

Behavior                     | Setting
:----------------------------|:---------
Left Aspiration MA (u16F04)  | yes
Left Aspiration NA (u16F10)  | yes
Left Aspiration NGA (u16F23) | yes
Open AN (u16F57)             | yes
Pointed EI (u16F7A)          | yes
Aspiration (u16F51)          | tucked
V+ @S                        | tucked
V @F no asp                  | tucked
V @F + asp                   | under asp
VV @F no asp                 | tucked
VV @F + asp                  | under asp

## [lpo]

Behavior                            | Setting
:-----------------------------------|:---------
Rounded MA NA (u16F04, u16F10)      | yes
Flat sided NNA NGA (u16F14, u16F23) | yes
Straight SHA (u16F33)               | yes
Open AN (u16F57)                    | yes
Alternate ANG (u16F58)              | yes
Triangular Comma (uni3001)          | yes
Aspiration (u16F51)                 | tucked
V+ @S                               | tucked
V @F no asp                         | tucked*
V @F + asp                          | under asp
VV @F no asp                        | tucked*
VV @F + asp                         | under asp

\* [lpo] wants to _half tuck_ V @F without asp (not yet supported)

## [sfm]

Behavior                    | Setting
:---------------------------|:-------
Left Aspiration MA (u16F04) | yes
Left Aspiration NA (u16F10) | yes
Pointed EI (u16F7A)         | yes
Aspiration (u16F51)         | after
V+ @S                       | after
V @F no asp                 | after
V @F + asp                  | after
VV @F no asp                | after
VV @F + asp                 | after

## [ygp]

Behavior                                   | Setting
:------------------------------------------|:-------
Centered YI PA (u16F02)                    | yes
Narrow MA NA (u16F04, u16F10)              | yes
Alternate NNA NGA (u16F14, u16F23)         | yes
Centered W OEY AE (u16F5C, u16F60, u16F73) | yes
Aspiration (u16F51)                        | after
V+ @S                                      | after
V @F no asp                                | after
V @F + asp                                 | after
VV @F no asp                               | after
VV @F + asp                                | after

## [yna]

Behavior            | Setting
:-------------------|:---------
Aspiration (u16F51) | after
V+ @S               | tucked
V @F no asp         | tucked
V @F + asp          | right asp
VV @F no asp        | tucked
VV @F + asp         | tucked

## [ywqa]

Behavior                      | Setting
:-----------------------------|:---------
Narrow MA NA (u16F04, u16F10) | yes
Dotted DZHA (u16F2F)          | yes
Alternate ZHA (u16F35)        | yes
Aspiration (u16F51)           | tucked
V+ @S                         | tucked
V @F no asp                   | tucked
V @F + asp                    | under asp
VV @F no asp                  | tucked
VV @F + asp                   | under asp
