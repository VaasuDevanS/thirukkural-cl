Thirukkural
============
A python3 module / command-line tool for Thirukkural  
Created by Vaasudevan Srinivasan <vaasuceg.96@gmail.com>  
Github Url: https://github.com/VaasuDevanS/thirukkural-cl  
Version: 1.0

Installation
============
```console
$ pip3 install thirukkural
```

Example commands
================
```console
$ thirukkural			  		| $ thirukkural -en			
$ thirukkural -k 100	  		| $ thirukkural -k 100 -en
$ thirukkural -a 10		  		| $ thirukkural -a 10 -en
$ thirukkural -a ilvaazhkkai	| $ thirukkural -a 'domestic life'
$ thirukkural -a இல்வாழ்க்கை     | $ thirukkural -i 5		  		
$ thirukkural -p 1				| $ thirukkural --all-paals 		
$ thirukkural --all-iyals		| $ thirukkural --all-adigaarams
```

```console
$ thirukkural --github  # opens the github page
$ thirukkural --pypi    # opens the PyPi page
$ thirukkural --pepy    # opens the stats page
$ thirukkural --dev     # opens the developer home page
```


Command Line Usage
==================
```
$ thirukkural -h
usage: thirukkural [-h] [-en] [-k 1-1330] [-a 1-133] [-i 1-10] [-p 1-3]
                   [--all-paals] [--all-iyals] [--all-adigaarams] [--github]
                   [--pypi] [--pepy] [--dev] [-v] [-s]

Thirukkural by Thiruvalluvar

optional arguments:
  -h, --help        show this help message and exit
  -en               set language as english for -k and -a flag
  -k 1-1330         display the Thirukural and its meaning
  -a 1-133          display the ten Thirukurals in the specified chapter
  -i 1-10           display the Adigaarams in the specified Iyal
  -p 1-3            display the Iyals in the specified Paal
  --all-paals       display all paals (category)
  --all-iyals       display all iyals (sub-category)
  --all-adigaarams  display all adigaarams (chapter)
  --github          opens the github page in the browser
  --pypi            opens the PyPi page in the browser
  --pepy            opens the download stats page in the browser
  --dev             opens the developer homepage
  -v                show version info and exit
  -s                show thiruvalluvar and exit
```

Display a random Thirukkural
-------------------------------------
```
$ thirukkural

பால்: பொருட்பால்(2/3) | இயல்: ஒழிபியல்(8/10) | அதிகாரம்: பண்புடைமை(100/133)

குறள்-994:
நயனொடு நன்றி புரிந்த பயனுடையார்
பண்புபா ராட்டும் உலகு.

nayanotu nandri purindha payanudaiyaar
paNpupaa raattum ulagu

மு.வ உரை:
நீதியையும் நன்மையையும் விரும்பிப் பிறர்க்குப் பயன்பட வாழும் பெரியோரின்
நல்லப் பண்பை உலகத்தார் போற்றிக் கொண்டாடுவர்.

சாலமன் பாப்பையா உரை:
நீதியையும் அறத்தையும் விரும்பிப் பிறர்க்கும் பயன்படுபவரின் பண்பினை
உலகத்தவர் சிறப்பித்துப் பேசுவர்.

```
```
$ thirukkural -en

Category: Wealth(2/3) | Sub-Category: Miscellaneous(8/10) | Chapter: Courtesy(100/133)

Verse-994:
Of men of fruitful life, who kindly benefits dispense,
The world unites to praise the 'noble excellence'.

Meaning:
The world applauds the character of those whose usefulness results
from their equity and charity.
```

Show Kural for given kural number
---------------------------------
```
$ thirukkural -k 335

பால்: அறத்துப்பால்(1/3) | இயல்: துறவறவியல்(3/10) | அதிகாரம்: நிலையாமை(34/133)

குறள்-335:
நாச்செற்று விக்குள்மேல் வாராமுன் நல்வினை
மேற்சென்று செய்யப் படும்.

naachchetru vikkuLmael vaaraamun nalvinai
maeRsendru seyyap padum

மு.வ உரை:
நாவை அடக்கி விக்கல் மேலெழுவதற்கு முன்னே (இறப்பு நெருங்குவதற்கு முன்)
நல்ல அறச்செயலை விரைந்து செய்யத்தக்கதாகும்.

சாலமன் பாப்பையா உரை:
நாவை அடைத்து விக்கல் வருவதற்கு முன், நல்ல செயல்களை விரைந்து செய்ய
வேண்டும்.

```

```
$ thirukkural -k 335 -en

Category: Righteousness(1/3) | Sub-Category: Ascetic Virtue(3/10) | Chapter: Instability(34/133)

Verse-335:
Before the tongue lie powerless, 'mid the gasp of gurgling breath,
Arouse thyself, and do good deeds beyond the power of death.

Meaning:
Let virtuous deeds be done quickly, before the biccup comes making the
tongue silent.

```

Show Kurals in the given adigaaram
----------------------------------
```
$ thirukkural -a 40

பால்: பொருட்பால்(2/3) | இயல்: அரசியல்(5/10) | அதிகாரம்: கல்வி(40/133)

குறள்-391:
கற்க கசடறக் கற்பவை கற்றபின்
நிற்க அதற்குத் தக.

குறள்-392:
எண்ணென்ப ஏனை எழுத்தென்ப இவ்விரண்டும்
கண்ணென்ப வாழும் உயிர்க்கு..

குறள்-393:
கண்ணுடையர் என்பவர் கற்றோர் முகத்திரண்டு
புண்ணுடையர் கல்லா தவர்.

குறள்-394:
உவப்பத் தலைக்கூடி உள்ளப் பிரிதல்
அனைத்தே புலவர் தொழில்.

குறள்-395:
உடையார்முன் இல்லார்போல் ஏக்கற்றுங் கற்றார்
கடையரே கல்லா தவர்.

குறள்-396:
தொட்டனைத் தூறும் மணற்கேணி மாந்தர்க்குக்
கற்றனைத் தூறும் அறிவு.

குறள்-397:
யாதானும் நாடாமால் ஊராமால் என்னொருவன்
சாந்துணையுங் கல்லாத வாறு.

குறள்-398:
ஒருமைக்கண் தான்கற்ற கல்வி ஒருவற்கு
எழுமையும் ஏமாப் புடைத்து.

குறள்-399:
தாமின் புறுவது உலகின் புறக்கண்டு
காமுறுவர் கற்றறிந் தார்.

குறள்-400:
கேடில் விழுச்செல்வம் கல்வி யொருவற்கு
மாடல்ல மற்றை யவை.

```

```
$ thirukkural -a 40 -en

Category: Wealth(2/3) | Sub-Category: Royalty(5/10) | Chapter: Learning(40/133)

Verse-391:
So learn that you may full and faultless learning gain,
Then in obedience meet to lessons learnt remain.

Verse-392:
The twain that lore of numbers and of letters give
Are eyes, the wise declare, to all on earth that live.

Verse-393:
Men who learning gain have eyes, men say;
Blockheads' faces pairs of sores display.

Verse-394:
You meet with joy, with pleasant thought you part;
Such is the learned scholar's wonderous art!.

Verse-395:
With soul submiss they stand, as paupers front a rich man's face;
Yet learned men are first; th'unlearned stand in lowest place.

Verse-396:
In sandy soil, when deep you delve, you reach the springs below;
The more you learn, the freer streams of wisdom flow.

Verse-397:
The learned make each land their own, in every city find a home;
Who, till they die; learn nought, along what weary ways they roam!.

Verse-398:
The man who store of learning gains,
In one, through seven worlds, bliss attains.

Verse-399:
Their joy is joy of all the world, they see; thus more
The learners learn to love their cherished lore.

Verse-400:
Learning is excellence of wealth that none destroy;
To man nought else affords reality of joy.

```
Any of the following commands will also work (for adigaaram alone) (optionally -en flag could be passed)
```
$ thirukkural -a ilvaazhkkai
$ thirukkural -a 'domestic life'
$ thirukkural -a இல்வாழ்க்கை
```


Show Adigaarams in the given Iyal
----------------------------------
```
$ thirukkural -i 2
----------------------------------------------------------------------------------------------------
No   Chapter                                  Adigaaram                  அதிகாரம்
----------------------------------------------------------------------------------------------------
5    Domestic Life                            Ilvaazhkkai                இல்வாழ்க்கை
6    The Worth of a Wife                      Vaazhkkaith Thunainalam    வாழ்க்கைத் துணைநலம்
7    The Wealth of Children                   Pudhalvaraip Perudhal      மக்கட்பேறு / புதல்வரைப் பெறுதல்
8    The Possession of Love                   Anpudaimai                 அன்புடைமை
9    Hospitality                              Virundhompal               விருந்தோம்பல்
10   The Utterance of Pleasant Words          Iniyavaikooral             இனியவைகூறல்
11   Gratitude                                Seynnandri Aridhal         செய்ந்நன்றி அறிதல்
12   Impartiality                             Natuvu Nilaimai            நடுவு நிலைமை
13   The Possession of Self-restraint         Adakkamudaimai             அடக்கமுடைமை
14   The Possession of Decorum                Ozhukkamudaimai            ஒழுக்கமுடைம
15   Not coveting another's Wife              Piranil Vizhaiyaamai       பிறனில் விழையாமை
16   The Possession of Patience, Forbearance  Poraiyudaimai              பொறையுடைமை
17   Not Envying                              Azhukkaaraamai             அழுக்காறாமை
18   Not Coveting                             Veqkaamai                  வெஃகாமை
19   Not Backbiting                           Purangooraamai             புறங்கூறாமை
20   Against Vain Speaking                    Payanila Sollaamai         பயனில சொல்லாமை
21   Dread of Evil Deeds                      Theevinaiyachcham          தீவினையச்சம்
22   Duty to Society                          Oppuravaridhal             ஒப்புரவறிதல்
23   Giving                                   Eekai                      ஈகை
24   Renown                                   Pukazh                     புகழ்
----------------------------------------------------------------------------------------------------
```

Show Iyals in the given Paal
----------------------------
```
$ thirukkural -p 1

பால்: அறத்துப்பால்(1/3)
-----------------------------------------------------
No  Sub-Category           Iyal            இயல்
-----------------------------------------------------
1   Prologue               Paayiraviyal    பாயிரவியல்
2   Domestic Virtue        Illaraviyal     இல்லறவியல்
3   Ascetic Virtue         Thuravaraviyal  துறவறவியல்
-----------------------------------------------------
```

Show all Paals
--------------
```
$ thirukkural --all-paals
---------------------------------------------
No  Category        Paal           பால்
---------------------------------------------
1   Righteousness   Arathuppal     அறத்துப்பால்
2   Wealth          Porutpaal      பொருட்பால்
3   Love            Kaamathuppal   காமத்துப்பால்
---------------------------------------------
```

Show all Iyals
--------------
```
$ thirukkural --all-iyals
-----------------------------------------------------
No  Sub-Category           Iyal            இயல்
-----------------------------------------------------
1   Prologue               Paayiraviyal    பாயிரவியல்
2   Domestic Virtue        Illaraviyal     இல்லறவியல்
3   Ascetic Virtue         Thuravaraviyal  துறவறவியல்
4   Fate                   Oozhiyal        ஊழியல்
5   Royalty                Arasiyal        அரசியல்
6   Ministers of State     Amaichiyal      அமைச்சியல்
7   Politics               Angaviyal       அங்கவியல்
8   Miscellaneous          Ozhibiyal       ஒழிபியல்
9   The Pre-marital love   Kalaviyal       களவியல்
10  The Post-marital love  Karpiyal        கற்பியல்
-----------------------------------------------------
```

Show all Adigaarams
-------------------
```
$ thirukkural --all-adigaarams
----------------------------------------------------------------------------------------------------
No   Chapter                                  Adigaaram                  அதிகாரம்
----------------------------------------------------------------------------------------------------
1    The Praise of God                        Katavul Vaazhththu         கடவுள் வாழ்த்து
2    The Blessing of Rain                     Vaansirappu                வான்சிறப்பு
3    The Greatness of Ascetics                Neeththaar Perumai         நீத்தார் பெருமை
4    Assertion of the Strength of Virtue      Aran Valiyuruththal        அறன் வலியுறுத்தல்
5    Domestic Life                            Ilvaazhkkai                இல்வாழ்க்கை
6    The Worth of a Wife                      Vaazhkkaith Thunainalam    வாழ்க்கைத் துணைநலம்
7    The Wealth of Children                   Pudhalvaraip Perudhal      மக்கட்பேறு / புதல்வரைப் பெறுதல்
8    The Possession of Love                   Anpudaimai                 அன்புடைமை
9    Hospitality                              Virundhompal               விருந்தோம்பல்
10   The Utterance of Pleasant Words          Iniyavaikooral             இனியவைகூறல்
11   Gratitude                                Seynnandri Aridhal         செய்ந்நன்றி அறிதல்
12   Impartiality                             Natuvu Nilaimai            நடுவு நிலைமை
13   The Possession of Self-restraint         Adakkamudaimai             அடக்கமுடைமை
14   The Possession of Decorum                Ozhukkamudaimai            ஒழுக்கமுடைம
15   Not coveting another's Wife              Piranil Vizhaiyaamai       பிறனில் விழையாமை
16   The Possession of Patience, Forbearance  Poraiyudaimai              பொறையுடைமை
17   Not Envying                              Azhukkaaraamai             அழுக்காறாமை
18   Not Coveting                             Veqkaamai                  வெஃகாமை
19   Not Backbiting                           Purangooraamai             புறங்கூறாமை
20   Against Vain Speaking                    Payanila Sollaamai         பயனில சொல்லாமை
21   Dread of Evil Deeds                      Theevinaiyachcham          தீவினையச்சம்
22   Duty to Society                          Oppuravaridhal             ஒப்புரவறிதல்
23   Giving                                   Eekai                      ஈகை
24   Renown                                   Pukazh                     புகழ்
25   Compassion                               Aruludaimai                அருளுடைமை
26   Abstinence from Flesh                    Pulaanmaruththal           புலான்மறுத்தல்
27   Penance                                  Thavam                     தவம்
28   Imposture                                Koodaavozhukkam            கூடாவொழுக்கம்
29   The Absence of Fraud                     Kallaamai                  கள்ளாமை
30   Veracity                                 Vaaimai                    வாய்மை
31   Restraining Anger                        Vekulaamai                 வெகுளாமை
32   Not doing Evil                           Innaaseyyaamai             இன்னாசெய்யாமை
33   Not killing                              Kollaamai                  கொல்லாமை
34   Instability                              Nilaiyaamai                நிலையாமை
35   Renunciation                             Thuravu                    துறவு
36   Truth-Conciousness                       Meyyunardhal               மெய்யுணர்தல்
37   Curbing of Desire                        Avaavaruththal             அவாவறுத்தல்
38   Fate                                     Oozh                       ஊழ்
39   The Greatness of a King                  Iraimaatchi                இறைமாட்சி
40   Learning                                 Kalvi                      கல்வி
41   Ignorance                                Kallaamai                  கல்லாமை
42   Hearing                                  Kaelvi                     கேள்வி
43   The Possession of Knowledge              Arivudaimai                அறிவுடைமை
44   The Correction of Faults                 Kutrangatidhal             குற்றங்கடிதல்
45   Seeking the Aid of Great Men             Periyaaraith Thunaikkotal  பெரியாரைத் துணைக்கோடல்
46   Avoiding mean Associations               Sitrinanjeraamai           சிற்றினஞ்சேராமை
47   Acting after due Consideration           Therindhuseyalvakai        தெரிந்துசெயல்வகை
48   The Knowledge of Power                   Valiyaridhal               வலியறிதல்
49   Knowing the fitting Time                 Kaalamaridhal              காலமறிதல்
50   Knowing the Place                        Idanaridhal                இடனறிதல்
51   Selection and Confidence                 Therindhudhelidhal         தெரிந்துதெளிதல்
52   Selection and Employment                 Therindhuvinaiyaatal       தெரிந்துவினையாடல்
53   Cherishing Kinsmen                       Sutrandhazhaal             சுற்றந்தழால்
54   Unforgetfulness                          Pochchaavaamai             பொச்சாவாமை
55   The Right Sceptre                        Sengonmai                  செங்கோன்மை
56   The Cruel Sceptre                        Kotungonmai                கொடுங்கோன்மை
57   Absence of Terrorism                     Veruvandhaseyyaamai        வெருவந்தசெய்யாமை
58   Benignity                                Kannottam                  கண்ணோட்டம்
59   Detectives                               Otraadal                   ஒற்றாடல்
60   Energy                                   Ookkamudaimai              ஊக்கமுடைமை
61   Unsluggishness                           Matiyinmai                 மடியின்மை
62   Manly Effort                             Aalvinaiyudaimai           ஆள்வினையுடைமை
63   Hopefulness in Trouble                   Idukkan Azhiyaamai         இடுக்கணழியாமை
64   The Office of Minister of state          Amaichchu                  அமைச்சு
65   Power of Speech                          Solvanmai                  சொல்வன்மை
66   Purity in Action                         Vinaiththooimai            வினைத்தூய்மை
67   Power in Action                          Vinaiththitpam             வினைத்திட்பம்
68   Modes of Action                          Vinaiseyalvakai            வினைசெயல்வகை
69   The Envoy                                Thoodhu                    தூது
70   Conduct in the Presence of the King      Mannaraich Cherndhozhudhal மன்னரைச் சேர்ந்தொழுதல்
71   The Knowledge of Indications             Kuripparidhal              குறிப்பறிதல்
72   The Knowledge of the Council Chamber     Avaiyaridhal               அவையறிதல்
73   Not to dread the Council                 Avaiyanjaamai              அவையஞ்சாமை
74   The Land                                 Naadu                      நாடு 
75   The Fortification                        Aran                       அரண்
76   Way of Accumulating Wealth               Porulseyalvakai            பொருள்செயல்வகை
77   The Excellence of an Army                Padaimaatchi               படைமாட்சி
78   Military Spirit                          Pataichcherukku            படைச்செருக்கு
79   Friendship                               Natpu                      நட்பு 
80   Investigation in forming Friendships     Natpaaraaidhal             நட்பாராய்தல்
81   Familiarity                              Pazhaimai                  பழைமை
82   Evil Friendship                          Thee Natpu                 தீ நட்பு
83   Unreal Friendship                        Kootaanatpu                கூடாநட்பு
84   Folly                                    Paedhaimai                 பேதைமை
85   Ignorance                                Pullarivaanmai             புல்லறிவாண்மை
86   Hostility                                Ikal                       இகல்
87   The Might of Hatred                      Pakaimaatchi               பகைமாட்சி
88   Knowing the Quality of Hate              Pakaiththirandheridhal     பகைத்திறந்தெரிதல்
89   Enmity within                            Utpakai                    உட்பகை
90   Not Offending the Great                  Periyaaraip Pizhaiyaamai   பெரியாரைப் பிழையாமை
91   Being led by Women                       Penvazhichcheral           பெண்வழிச்சேறல்
92   Wanton Women                             Varaivinmakalir            வரைவின்மகளிர்
93   Not Drinking Palm-Wine                   Kallunnaamai               கள்ளுண்ணாமை
94   Gambling                                 Soodhu                     சூது
95   Medicine                                 Marundhu                   மருந்து
96   Nobility                                 Kutimai                    குடிமை
97   Honour                                   Maanam                     மானம்
98   Greatness                                Perumai                    பெருமை
99   Perfectness                              Saandraanmai               சான்றாண்மை
100  Courtesy                                 Panpudaimai                பண்புடைமை
101  Wealth without Benefaction               Nandriyilselvam            நன்றியில்செல்வம்
102  Shame                                    Naanudaimai                நாணுடைமை
103  The Way of Maintaining the Family        Kutiseyalvakai             குடிசெயல்வகை
104  Farming                                  Uzhavu                     உழவு
105  Poverty                                  Nalkuravu                  நல்குரவு
106  Mendicancy                               Iravu                      இரவு
107  The Dread of Mendicancy                  Iravachcham                இரவச்சம்
108  Baseness                                 Kayamai                    கயமை
109  The Pre-marital love                     Thakaiyananguruththal      தகையணங்குறுத்தல்
110  Recognition of the Signs                 Kuripparidhal              குறிப்பறிதல்
111  Rejoicing in the Embrace                 Punarchchimakizhdhal       புணர்ச்சிமகிழ்தல்
112  The Praise of her Beauty                 Nalampunaindhuraiththal    நலம்புனைந்துரைத்தல்
113  Declaration of Love's special Excellence Kaadharsirappuraiththal    காதற்சிறப்புரைத்தல்
114  The Abandonment of Reserve               Naanuththuravuraiththal    நாணுத்துறவுரைத்தல்
115  The Announcement of the Rumour           Alararivuruththal          அலரறிவுறுத்தல்
116  Separation unendurable                   Pirivaatraamai             பிரிவாற்றாமை
117  Complainings                             Patarmelindhirangal        படர்மெலிந்திரங்கல்
118  Eyes consumed with Grief                 Kanvidhuppazhidhal         கண்விதுப்பழிதல்
119  The Pallid Hue                           Pasapparuparuvaral         பசப்புறுபருவரல்
120  The Solitary Anguish                     Thanippatarmikudhi         தனிப்படர்மிகுதி
121  Sad Memories                             Ninaindhavarpulampal       நினைந்தவர்புலம்பல்
122  The Visions of the Night                 Kanavunilaiyuraiththal     கனவுநிலையுரைத்தல்
123  Lamentations at Eventide                 Pozhudhukantirangal        பொழுதுகண்டிரங்கல்
124  Wasting Away                             Uruppunalanazhidhal        உறுப்புநலனழிதல்
125  Soliloquy                                Nenjotukilaththal          நெஞ்சொடுகிளத்தல்
126  Reserve Overcome                         Niraiyazhidhal             நிறையழிதல்
127  Mutual Desire                            Avarvayinvidhumpal         அவர்வயின்விதும்பல்
128  The Reading of the Signs                 Kuripparivuruththal        குறிப்பறிவுறுத்தல்
129  Desire for Reunion                       Punarchchividhumpal        புணர்ச்சிவிதும்பல்
130  Expostulation with Oneself               Nenjotupulaththal          நெஞ்சொடுபுலத்தல்
131  Pouting                                  Pulavi                     புலவி
132  Feigned Anger                            Pulavi Nunukkam            புலவி நுணுக்கம்
133  The Pleasures of Temporary Variance      Oodaluvakai                ஊடலுவகை
----------------------------------------------------------------------------------------------------
```

Show Thiruvalluvar
------------------
```console
$ thirukkural -s

        yyssssssssssssssssssssyyyyyhhhyyyysooooooooooooooooooooooooooooooooooo
        yssssssssssssssssydmdhhhhhhhdmddhhyyysoooooooooooooooooooooooooooooooo
        sssssssssssssssymNmmddhhhdmhsssssyyyyyysssoooooooooooooooooooooooooooo
        ssssssssssssssyNNNmdhddmmhsooosyhhhhhhhhhdhsoooooooooooooooooooooooooo
        ssssssssssssssmNNmmmmNNNmmmmdhhyyssssyyyyyyyysooooooooooooo+++++oooooo
        sssssssssssooyNNNmNmdNNNNNmdhyyhhhyyyhhhhhyyyyyoooooooooooo++++++ooooo
        sssssssssoooosNNmmmmNNNNNmdddmmmmmddddhsshhhhhysooooooooooo+++++++oooo
        ssssssssssoooohNNNNNNNNNmmNmmhhhdddhhdyyyyysyysoosoooooooooo++++++++oo
        ssssssssoooooooydNNNNNNNNmmddhhddddddddddhhhddddhhsooooooooo++++++++++
        ssssssssooooooooosydNNNNmddmdhyssssssooo+++++oosysoooooooo++++++++++++
        sssssoooooooooooooohNNNNmhhdhsooo+++///:::::----:+oooooo++++++++++++++
        sssoooooooooooooooodNNNNmdmdysso+++////::::-:---:/+oooo+++++++++++++++
        sssoooooooooooooooomNNNmddddhysoo++/////::::::--:/+o+o++++++++++++++++
        sssoooooooooooooooomNNmmmmddhyssoossssyddho:::/shhho++++++++++++++++++
        ssssooooooooooooooodNNmmdmmdhyso+/::+++osyy+/+ys++so++++++++++++++++++
        ssssooooooooooooooodysshmddhyso+/+shhsdmhhys+shyhdhs++++++++++++++++++
        sssssoooooooooooooohyyhydmdyyso+///+sosysooo//s+syyo++++++++++++++++++
        ssssssooooooooooooohyydddmhyyso+/:---:::::+o/-+:::/o++++++++++++++++++
        sssssoooooooooooooohhyhyhdhyyys+/:-------:+o+./:--:+++++++++++++++++++
        sssssoooooooooooooodNhhdhdhyyyso+/::::::/syys+o/:-:+++++++++++++++++++
        sssssoooooooooooooodNNdyhdyyyysso+////++:::ohds/://+++++++++++++++++++
        sssssssoooooooooooyNNNdddmdysyyyssooso/:/shyssyd+/+++++++++++++++++++o
        sssssssoooooooooooyNNmsydmdyssyyyysso+/sdddhhhdmy:/o+++++++++++++++++o
        ysssssssoooooooooymNNhsyddhyssssssoo+ohddhyyssshhs/+oo+++++++++++++ooo
        yssssssssoooooooymmdysshmmdhyssssssyhddhyysssoshddo+so++++++++++++oo++
        ysssssssssooossyhyyssssyddhhyssyyyyhhhhhhhhhyyhhdhs+o/--//+++++++oo+++
        yyyssssssssssoossssssssyddyyysyyyyyyhysydhdhhhyyhyoooo-.-..///++++++++
        yysssoooooooo+++++oossssyhhhysyyyhhysssyysssoooshysss/`...`.:.--/+++++
        yssoo+++++++++++ooosssssshhyyhhyhhhyhhysssooosyhyyyso/.`.-..:/./../+++
        so++//:::::///////++oosssyhddhyyssssyysyyhysyyyssoo++:.``...-/-:+-::-/
        o+//:::::::::::::::::///+oyhdhyysoso++o+oso++/+osoo+:-.``...-.:.o./+..
        +/::::::://////::::::::///+shdddhhysooooso++++ooso/:.-```...-.-.o-+o..
        //::::://////////::::::///+osyhyyyhhhhyhysoooooo+:-...```.`.-.:.o:+-..
        /::::///+++oo+///:::::::://++osyhdddmdmddhyyss+:---...```.`..`:.o/-...
        /:::///++osso+//:::::::::///++oossydddmdhyo+/:.`.-.`..````````-.o-....

```






