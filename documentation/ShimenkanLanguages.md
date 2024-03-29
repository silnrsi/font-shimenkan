# Shimenkan Language Behavior Summary

This page summarizes language-specific behaviors organized by language. For a more complete description of behaviors see [Font Behavior in the Shimenkan Fonts](ShimenkanBehavior.md).

Code   | Language                                                               | Font
:------|:-----------------------------------------------------------------------|:----------------
[hmd]  | Large Flowery Miao / Dahua Miao / A-Hmao                               | Sapushan
[hmdd] | alternate for Large Flowery Miao using the Normalised Miao orthography | Shimenkan Guifan
[hmz]  | Sinicized Miao / Waishu Miao / Hmong Shua                              | Shimenkan MGS
[lpo]  | Lipo / Dong Lisu                                                       | Taogu
[sfm]  | Small Flowery Miao / Xiaohua Miao                                      | Shimenkan MAS
[ygp]  | Gepo / Bai Yi                                                          | Shimenkan GSM
[yna]  | Aluo / Gan Yi                                                          | Shimenkan Zonghe
[ywqa] | Wuding-Luquan Yi / Hei Yi / Nasu                                       | Salaowu

## [hmd] Large Flowery Miao / Dahua Miao / A-Hmao

Behavior                    | Setting
:---------------------------|:---------
Open AN (u16F57)            | yes
Pointed EI (u16F7A)         | yes
Left Aspiration NA (u16F10) | no, but available via ss01 for traditional texts
Aspiration (u16F51)         | tucked
V+ @S                       | tucked
V @F no asp                 | tucked
V @F + asp                  | right asp
VV @F no asp                | tucked
VV @F + asp                 | tucked
V locations used            | H S W F

## [hmdd] alternate for Large Flowery Miao using the Normalised Miao orthography

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
V locations used                              | F

\* [hmdd] wants V+ @F to tuck only with u16F07 (not yet supported)

## [hmz] Sinicized Miao / Waishu Miao / Hmong Shua

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
V locations used             | H S W F

## [lpo] Lipo / Dong Lisu

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
V locations used                    | H S F

\* [lpo] wants to _half tuck_ V @F without asp (not yet supported)

## [sfm] Small Flowery Miao / Xiaohua Miao 

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
V locations used            | H S E K F

## [ygp] Gepo / Bai Yi

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
V locations used                           | H S F

## [yna] Aluo / Gan Yi

Behavior            | Setting
:-------------------|:---------
Aspiration (u16F51) | after
V+ @S               | tucked
V @F no asp         | tucked
V @F + asp          | right asp
VV @F no asp        | tucked
VV @F + asp         | tucked
V locations used    | H S F

## [ywqa] Wuding-Luquan Yi / Hei Yi / Nasu

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
V locations used              | H S F
V raised @S (u16F5B, u16F5C)  | yes
