Thirukkural
============
A python3 wrapper around the thirukkural

Created by Vaasudevan Srinivasan <vaasuceg.96@gmail.com>

Github Url: https://github.com/VaasuDevanS/thirukkural-cl

Installation
============
```console
$ pip3 install thirukkural
```

Command Line Usage
==================
```console
$ thirukkural -h
usage: thirukkural [-h] [-en] [-k 1-1330] [-a 1-133] [-i 1-10] [-p 1-3]
                   [--all-paals] [--all-iyals] [--all-adigaarams] [--github]
                   [--pypi] [--pepy] [--dev] [-v] [-s]

Thirukkural by Thiruvalluvar

optional arguments:
  -h, --help        show this help message and exit
  -en               set language as english for -k and -a flag
  -k 1-1330         display the Thirukural and its meaning
  -a 1-133          display the ten thirukurals in the specified chapter
  -i 1-10           display the adigaarams in the specified Iyal
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
Display a random thirukkural and exit
```console
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
