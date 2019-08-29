# Font Behavior in the Shimenkan Fonts

This file documents the behavior built into the Shimenkan fonts. It is not intended as a general linguistic script or writing system description. The purpose is to describe the basic behaviors supported for all writing systems that use the Miao (Pollard) script and those that are specific to individual languages and writing systems.

---

## Definitions

Glyphs are referenced using their glyph names, which in most cases are related to their Unicode values.

### Languages and writing systems
Languages are referenced by their ISO 639-3 codes. The language-specific variants of the fonts are listed:

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

> Add links to Ethnologue pages?

### Elements
Syllables are built from a set of elements according to the following pattern, which reflects the order that the elements are _encoded_ into the Unicode text rather than the order in which they might be written or typed. For more information see [The Unicode Standard version 12.1 chapter 18.10](http://www.unicode.org/versions/Unicode12.1.0/ch18.pdf).

`[N] [C] C [M] [asp] V [V] [V] [tone] `

- **C** = consonant (u16F00..u16F4A)
- **V** = vowel, also called a 'final' (u16F54..u16F87)
- **V+** = one or more vowels in sequence
- **VV** = two-vowel sequence
- **tone** = tone marker, does not have a visual representation but rather indicates vowel position (u16F8F..u16F92)
- **M** = modifier (u16F4F)
- **N** = nasalization (u16F50)
- **asp** = aspiration mark (u16F51)

Other voicing-related characters (u16F52, u16F53) and baseline tone marks (u16F93..u16F9F) are included in the font but not fully supported.

### Alignment-related terms

- _tuck_ = Element is moved to the left to 'tuck' under or inside a consonant or other element
- _kern_ = A contextual adjustment in horizontal position only for certain combinations. _Note that the current font version does not support any kerning according to this strict definition._
- _sidebearing_ = Whitespace to the left or right side of the glyph and included in the glyph width 
- _RHS_ = Right hand side of element, _including the right sidebearing_
- _LHS_ = Left hand side of element, _including the left sidebearing_
- _RHS to RHS_ = Right hand sides of glyphs (including sidebearings) are aligned. _Note that this is not a mathematical alignment of element bounding boxes._

---

## Behaviors
These behaviors often differ between languages. A summary of these for each language is in the [Shimenkan Language Behavior Summary](ShimenkanLanguages.md)

### Simple substitutions

The following language-specific substitutions are supported:

> Add images for each of these

#### Dotted Consonants (all warted consonants) [hmdd]
Variants of all warted consonants with wart replaced by dot. Issue [#20](https://github.com/silnrsi/font-shimenkan/issues/20)
_Glyphs:_ u16F01.dot, etc. for all warted glyphs _except_ the nasals (u16F05, u16F11, u16F15, u16F24) as the dots are already the default for these chars for hmdd

#### Centered YI PA (u16F02) [ygp]
Variant with stem in center. Issue [#2](https://github.com/silnrsi/font-shimenkan/issues/2)
_Glyphs:_ u16F02.ygp

#### Narrow MA NA (u16F04, u16F10) [ygp, ywqa]
Variants that are narrow, matching u16F50. Issue [#4](https://github.com/silnrsi/font-shimenkan/issues/4)
_Glyphs:_ u16F04.narrow, u16F10.narrow

#### Rounded MA NA (u16F04, u16F10) [lpo]
Variant with rounded top and bottom. Issue [#10](https://github.com/silnrsi/font-shimenkan/issues/10)
_Glyphs:_ u16F04.lpo, u16F10.lpo

#### Ahmao nasals (u16F04, u16F10, u16F14, u16F23) [hmdd]
Variants that resemble alternate Ahmao style. Issue [#19](https://github.com/silnrsi/font-shimenkan/issues/19)
_Glyphs:_ 
(unwarted/undotted) u16F04.hmdd, u16F10.hmdd, u16F14.hmdd, u16F23.hmdd
(warted/dotted) u16F05.hmdd, u16F11.hmdd, u16F15.hmdd, u16F24.hmdd
_Note that the warted ones have the dotted version as the default, and no ‘wart’_

#### Alternate NNA NGA (u16F14, u16F23) [ygp]
Variants that are narrow and have a less closed loop. Issue [#5](https://github.com/silnrsi/font-shimenkan/issues/5)
_Glyphs:_ u16F14.ygp, u16F23.ygp

#### Flat sided NNA NGA (u16F14, u16F23) [lpo]
Variants with flat sides and rounded corners. Issue [#14](https://github.com/silnrsi/font-shimenkan/issues/14)
_Glyphs:_ u16F14.flat, u16F23.flat

#### Dotted DZHA (u16F2F) [ywqa]
Variant with wart replaced by dot and dot tucked deep inside letter. Issue [#39](https://github.com/silnrsi/font-shimenkan/issues/39)
_Glyphs:_ u16F2F.ywqa

#### Straight SHA (u16F33) [lpo]
Variant with straight stem and hook. Issue [#12](https://github.com/silnrsi/font-shimenkan/issues/12)
_Glyphs:_ u16F33.lpo

#### Alternate ZHA (u16F35) [ywqa]
Variant with an open (flattened) bottom that points to the right. Issue [#8](https://github.com/silnrsi/font-shimenkan/issues/8)
_Glyphs:_ u16F35.ywqa

#### Centered W OEY AE (u16F5C, u16F60, u16F73) [ygp]
Variants with main arm more centered. Issue [#56](https://github.com/silnrsi/font-shimenkan/issues/56)
_Glyphs:_ u16F5C.ygp, u16F60.ygp, u16F73.ygp.u16F5C.mark.ygp, u16F60.mark.ygp, u16F73.mark.ygp

#### Open AN (u16F57) [hmd, hmdd, hmz, lpo]
Variant with an open (flattened) bottom that points to the right. Issue [#8](https://github.com/silnrsi/font-shimenkan/issues/8)
_Glyphs:_ u16F57.open, u16F57.mark.open

#### Alternate ANG (u16F58) [lpo]
Variant with loop that more clearly doubles back on itself (and is more to the right). Issue [#13](https://github.com/silnrsi/font-shimenkan/issues/13)
_Glyphs:_ u16F58.lpo, u16F58.mark.lpo

#### Flat Top EN ENG (u16F5E, u16F5F) [hmdd]
Variants with flat top to match u16F2C. Issue [#22](https://github.com/silnrsi/font-shimenkan/issues/22)
_Glyphs:_ u16F5E.hmdd, u16F5F.hmdd, u16F5E.mark.hmdd, u16F5F.mark.hmdd
_No .mark versions are technically needed as only F location is used, however the .mark versions are included to simplify the OT code._

#### Pointed EI (u16F7A) [hmd, hmdd, hmz, sfm]
Variant with a zigzag-like design. Issue [#15](https://github.com/silnrsi/font-shimenkan/issues/15)
_Glyphs:_ u16F7A.point, u16F7A.mark.point

#### Triangular Comma (uni3001) [lpo]
Variant of ideographic comma in a triangular shape. Issue [#23](https://github.com/silnrsi/font-shimenkan/issues/23)
_Glyphs:_ uni3001.lpo

### Modifier

The modifier bar (u16F4F) is used only by [yna] to indicate a distinct place of articulation. It directly follows the consonant but is moved to appear before the consonant. It only occurs in combination with u16F0E and u16F10 and is implemented using two ligatures (u16F0E_u16F4F, u16F10_u16F4F).

### Aspiration positioning
The aspiration (u16F51) is placed at shoulder level, directly following the consonant, and has two main horizontal alignment positions:

- _tucked (T)_ - The asp is moved left into consonants that are open on the upper right, but is otherwise placed after [default, hmd, hmz, lpo, ywqa]
- _after (A)_ - The asp is _always_ positioned after the consonant, with no tuck [hmdd, sfm, ygp, yna]

There are exceptions to this: When following certain consonants for certain languages the asp is moved to the _left (L)_ hand side of the consonant: Issue [#27](https://github.com/silnrsi/font-shimenkan/issues/27)

- Left Aspiration MA (u16F04) [hmz, sfm]
- Left Aspiration NA (u16F10) [hmd, hmz, sfm]
- Left Aspiration NGA (u16F23) [hmz]

These are implemented as ligatures:  u16F04_u16F51, u16F10_u16F51, u16F23_u16F51

This table summarizes aspiration positioning:

Consonant    | default | hmd | hmdd | hmz | lpo | sfm | ygp | yna | ywqa
:------------|:-------:|:---:|:----:|:---:|:---:|:---:|:---:|:---:|:---:
Almost all   |    T    |  T  |  A   |  T  |  T  |  A  |  A  |  A  |  T
u16F04 (MA)  |         |     |      |  L  |     |  L  |     |     |   
u16F10 (NA)  |         |  L  |      |  L  |     |  L  |     |     |   
u16F23 (NGA) |         |     |      |  L  |     |     |     |     |   

### Vowel positioning
Vowels in current use are positioned in one of six locations. The default location is _foot_. For other locations, a non-visible tone mark (u16F8F..u16F92) is used after the V+ to indicate the location. For each of those locations, the horizontal position may be adjusted when dots or asps are present, or when there is more than one vowel.

The six locations are:

> Add visual example

- **H** = _head_ - above consonant, usually centered
- **S** = _shoulder_ - upper right of consonant, generally aligned with top of consonant
- **E** = _elbow_ - on right, between _shoulder_ and _waist_
- **W** = _waist_ - center right of consonant, centered
- **K** = _knee_ - on right, between _foot_ and _waist_
- **F** = _foot_ - lower right of consonant, sitting on baseline

The following table summarizes language use of locations, and the tone marks used to indicate them:

Location            | hmd | hmdd | hmz | lpo | sfm | ygp | yna | ywqa
:-------------------|:---:|:----:|:---:|:---:|:---:|:---:|:---:|:---:
head (u16F91)       |  H  |      |  H  |  H  |  H  |  H  |  H  |  H
shoulder (u16F90)   |  S  |      |  S  |  S  |  S  |  S  |  S  |  S
elbow (u16F8F)      |     |      |     |     |  E  |     |     |   
waist (u16F8F)      |  W  |      |  W  |     |     |     |     |   
knee (u16F92)       |     |      |     |     |  K  |     |     |   
foot (no tone mark) |  F  |  F   |  F  |  F  |  F  |  F  |  F  |  F

The _elbow_ and _waist_ locations share a tone mark (u16F8F). There is also historically a _floor_ location, centered below the consonant, and indicated by u16F92, but it is no longer used by any languages. That tone mark is re-used by [sfm] to indicate the _knee_ location.

#### Head vowels (u16F91) [hmd, hmz, lpo, sfm, ygp, yna, ywqa] 

Vowels (single or multiple) located at _head_ appear visually centered above the consonant except when the vowel has a descender that collides with the consonant or aspiration, specifically u16F63 and u16F64. In those cases the vowel(s) are moved to the right just enough to avoid collisions. 

#### Shoulder vowels (u16F90) [hmd, hmz, lpo, sfm, ygp, yna, ywqa]

Vowels located at _shoulder_ are vertically positioned so that most of them align with the tops of the consonants and asp. They have two possible horizontal positions:

- _tucked (T)_ - V+ are moved left inside consonants that are open on the upper right side, otherwise follow after the consonant [default, hmd, hmz, lpo, yna, ywqa]
- _after (A)_ - V+ always follow after the consonant, with no horizontal adjustment [hmdd, sfm, ygp]

Vowels that directly follow an aspiration are positioned after the aspiration a constant amount, even if that requires it to tuck a similar amount as the aspiration. 

This table summarizes positioning @S:

Context | default | hmd | hmdd | hmz | lpo | sfm | ygp | yna | ywqa
:-------|:-------:|:---:|:----:|:---:|:---:|:---:|:---:|:---:|:---:
V+ @S   |    T    |  T  |  A   |  T  |  T  |  A  |  A  |  T  |  T

Note that this is identical to the preferences for  _V@F no asp_ below.

#### Elbow vowels (u16F8F) [sfm]

Vowels located at _elbow_ are always positioned _after_ the consonant and possible aspiration.

#### Waist vowels (u16F8F) [hmd, hmz]

Vowels located at _waist_ are always _tucked_.

#### Knee vowels (u16F92) [sfm]

Vowels located at _knee_ are always positioned _after_ the consonant and possible aspiration.

#### Foot vowels [hmd, hmdd, hmz, lpo, sfm, ygp, yna, ywqa]

Vowels located at _foot_ generally sit on the baseline, and have five possible horizontal alignments:

- _tucked (T)_ - V+ are moved left inside consonants that are open on the lower right side, and aligned under the asp for others (as with _under asp_)
- _under asp (U)_ - the LHS of V+ aligns under the LHS of asp
- _under dot (D)_ - the LHS of V+ aligns under the LHS of dot
- _right asp (R)_ - the RHS of V aligns under the RHS of asp when possible given the design of the consonant, otherwise is like _under asp_
- _after (A)_ - V+ always follows after all other elements, and only small adjustments are made to offset visual illusions

Exceptions (not yet supported):
- [lpo] wants to _half tuck_ V @F without asp, but it will not be implemented until a later version. 
- [hmdd] wants V+ @F to tuck only with u16F07

Following [hmdd-only] dotted consonant variants, vowels (V and VV) align _under dot (D)_. The aspiration does not occur after dotted consonants.

This table summarizes positioning @F:

Context      | default | hmd | hmdd | hmz | lpo | sfm | ygp | yna | ywqa
:------------|:-------:|:---:|:----:|:---:|:---:|:---:|:---:|:---:|:---:
V @F no asp  |    T    |  T  |  A*  |  T  | T*  |  A  |  A  |  T  |  T
V @F + asp   |    U    |  R  |  U   |  U  |  U  |  A  |  A  |  R  |  U
VV @F no asp |    T    |  T  |  A*  |  T  | T*  |  A  |  A  |  T  |  T
VV @F + asp  |    U    |  T  |  U   |  U  |  U  |  A  |  A  |  T  |  U
V+ @F dotted |         |     |  D   |     |     |     |     |     |   

\* see _Exceptions_ above
