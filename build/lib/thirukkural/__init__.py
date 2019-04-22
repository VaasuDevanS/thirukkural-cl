# Wrapper around the SQLite kural db providing rich thirukkural
# Objects for the users

from textwrap import wrap
import pkg_resources
import webbrowser
import argparse
import sqlite3
import random
import sys

__version__   = "1.1"
__developer__ = 'Vaasudevan Srinivasan'

DBFile = pkg_resources.resource_filename('thirukkural', 'kural.db')

class Paal:
    """
    """
    def __init__(self, no):

        # Check the conditions
        assert 0 < no < 4, "Paal should be 1 or 2 or 3"

        self.iyals = []
        self.adigaarams = []
        self.kurals = []
        self.paalNo = no

        with sqlite3.connect(DBFile) as conn:
            cur = conn.cursor()
            cur.execute("""SELECT DISTINCT iyal_no, paal_ta
                           FROM kural
                           WHERE paal_no=%s""" % no)
            for row in cur:
                self.iyals.append(Iyal(row[0]))
                self.paalName = row[1]

        for iyal in self.iyals:
            for adigaaram in iyal.adigaarams:
                for kural in adigaaram.kurals:
                    self.kurals.append(kural)
                self.adigaarams.append(adigaaram)

    def __dir__(self):

        return ["paalNo", "paalName",
                "iyals", "adigaarams", "kurals", "__str__", "__iter"]

    def __repr__(self):

        return "<%s:%s>" % (self.paalNo, self.paalName)

    def __str__(self):

        return "<%s:%s>" % (self.paalNo, self.paalName)

    def __iter__(self):

        for i in self.iyals:
            yield i

    @classmethod
    def show_all_paals(self):

        with sqlite3.connect(DBFile) as conn:
            cur = conn.cursor()
            flds = ["paal_%s" % i for i in ["no", "en", "te", "ta"]]
            cur.execute("""SELECT DISTINCT %s
                           FROM kural""" % (",".join(flds))
                       )
            temp = "{:<3} {:<15} {:<14} {:}"
            print("-" * 45)
            print(temp.format(*["No", "Category", "Paal", "பால்"]))
            print("-" * 45)
            for row in cur.fetchall():
                print(temp.format(*row))
            print("-" * 45)

    def showCL(self):

        print("\nபால்: %s(%s/3)" % (self.paalName, self.paalNo))
        Iyal.show_all_iyals(whr="paal_no=%s"%self.paalNo)


class Iyal:
    """
    """
    def __init__(self, no):

        # Check the conditions
        assert 0 < no < 11, "Iyal should be in between 1-10"

        self.adigaarams = []
        self.iyalNo = no
        self.__iyalInfo = {}

        with sqlite3.connect(DBFile) as conn:
            cur = conn.cursor()
            cur.execute("PRAGMA table_info(kural)")
            keys = [i[1] for i in cur.fetchall()]
            cur.execute("""SELECT DISTINCT adigaaram_no, iyal_ta
                           FROM kural
                           WHERE iyal_no=%s""" % no)
            for row in cur.fetchall():
                self.adigaarams.append(Adigaaram(row[0]))
                self.iyalName = row[1]
            cur.execute("SELECT * FROM kural WHERE iyal_no=%s LIMIT 1"%no)
            for k,val in zip(keys, cur.fetchone()):
                self.__iyalInfo[k] = val

    def __dir__(self):

        return ["iyalNo", "iyalName", "adigaarams", "__str__", "__iter__"]

    def __repr__(self):

        return "<%s:%s>" % (self.iyalNo, self.iyalName)

    def __str__(self):

        return "<%s:%s>" % (self.iyalNo, self.iyalName)

    def __iter__(self):

        for i in self.adigaarams:
            yield i

    @classmethod
    def show_all_iyals(self, whr="1=1"):

        with sqlite3.connect(DBFile) as conn:
            cur = conn.cursor()
            flds = ["iyal_%s" % i for i in ["no", "en", "te", "ta"]]
            cur.execute("""SELECT DISTINCT %s
                           FROM kural
                           WHERE %s
                           """ % (",".join(flds), whr)
                       )
            temp = "{:<3} {:<22} {:<15} {:}"
            print("-" * 53)
            print(temp.format(*["No", "Sub-Category", "Iyal", "இயல்"]))
            print("-" * 53)
            for row in cur.fetchall():
                print(temp.format(*row))
            print("-" * 53)

    def showCL(self):

        print(("\n"
               "பால்: {paal_ta}({paal_no}/3) | "
               "இயல்: {iyal_ta}({iyal_no}/10)"
               ).format(**self.__iyalInfo))
        Adigaaram.show_all_adigaarams(whr="iyal_no=%s"%self.iyalNo)


class Adigaaram:
    """
    """
    def __init__(self, no=None, name=None):

        # Check the conditions
        assert (no,name) != (None, None), "Either no or name must be given"

        if no != None:
            assert 0 < no < 134, "Adigaaram range should be in 1-133"

        if name != None:
            with sqlite3.connect(DBFile) as conn:
                cur = conn.cursor()
                for f in ["adigaaram_ta", "adigaaram_en", "adigaaram_te"]:
                    q = "SELECT adigaaram_no FROM kural WHERE %s LIKE '%s'"
                    cur.execute(q % (f, name))
                    no = cur.fetchall()
                    if len(no) != 0:
                        no = no[0][0]
                        break
                else:
                    raise ValueError("Adigaaram not found")

        self.adigaaramNo = no
        self.kurals = []
        self.__adigaaramInfo = {}

        with sqlite3.connect(DBFile) as conn:
            cur = conn.cursor()
            cur.execute("PRAGMA table_info(kural)")
            keys = [i[1] for i in cur.fetchall()]
            cur.execute("SELECT * FROM kural WHERE adigaaram_no=%s"%no)
            for row in cur.fetchall():
                self.kurals.append(Kural(row[0]))
                self.adigaaramName = row[8]
            for k,val in zip(keys, row):
                self.__adigaaramInfo[k] = val

    def __dir__(self):

        return ["adigaaramNo", "adigaaramName", "kurals", "__str__", "__iter__"]

    def __repr__(self):

        return "<%s:%s>" % (self.adigaaramNo, self.adigaaramName)

    def __str__(self):

        return "<%s:%s>" % (self.adigaaramNo, self.adigaaramName)

    def __iter__(self):

        for k in self.kurals:
            yield k

    @classmethod
    def show_all_adigaarams(self, whr="1=1"):

        with sqlite3.connect(DBFile) as conn:
            cur = conn.cursor()
            flds = ["adigaaram_%s" % i for i in ["no", "en", "te", "ta"]]
            cur.execute("""SELECT DISTINCT %s
                           FROM kural
                           WHERE %s
                           """ % (",".join(flds), whr)
                       )
            temp = "{:<4} {:<40} {:<26} {:}"
            print("--" * 50)
            print(temp.format(*["No", "Chapter", "Adigaaram", "அதிகாரம்"]))
            print("--" * 50)
            for row in cur.fetchall():
                print(temp.format(*row))
            print("--" * 50)

    def showCL(self, lang='ta'):

        if lang == 'ta':
            print(("\n"
                   "பால்: {paal_ta}({paal_no}/3) | "
                   "இயல்: {iyal_ta}({iyal_no}/10) | "
                   "அதிகாரம்: {adigaaram_ta}({adigaaram_no}/133)\n"
                   ).format(**self.__adigaaramInfo))
            for k in self.kurals:
                print("குறள்-%s:"%k.no)
                print(k.kural_ta)
                print()

        elif lang == 'en':
            print(("\n"
                   "Category: {paal_en}({paal_no}/3) | "
                   "Sub-Category: {iyal_en}({iyal_no}/10) | "
                   "Chapter: {adigaaram_en}({adigaaram_no}/133)\n"
                   ).format(**self.__adigaaramInfo))
            for k in self.kurals:
                print("Verse-%s:"%k.no)
                print(k.kural_en)
                print()

        else:
            print("Provided lang not available as of now..!!")


class Kural:
    """
    Fundamental class-type of this module
    """
    def __init__(self, no):

        # Check the conditions
        assert 0 < no < 1331, "Range should be in 1-1330"
        self.kuralNo = no
        self.__kuralInfo = {}

        with sqlite3.connect(DBFile) as conn:
            cur = conn.cursor()
            cur.execute("PRAGMA table_info(kural)")
            self.keys = [i[1] for i in cur.fetchall()]
            cur.execute("SELECT * FROM kural WHERE no=%s"%no)
            for k,val in zip(self.keys, cur.fetchone()):
                setattr(self, k, val)
                self.__kuralInfo[k] = val

    def __dir__(self):

        return self.keys + ['__str__']

    def __repr__(self):

        return "<%s:%s>" % (self.no, self.adigaaram_ta)

    def __str__(self):

        return "<%s:%s>" % (self.no, self.adigaaram_ta)

    def showCL(self, lang='ta'):

        # -ta flag
        if lang == 'ta':
            print(("\n"
                   "பால்: {paal_ta}({paal_no}/3) | "
                   "இயல்: {iyal_ta}({iyal_no}/10) | "
                   "அதிகாரம்: {adigaaram_ta}({adigaaram_no}/133)\n\n"
                   "குறள்-{no}:"
                   "\n{kural_ta}"
                   "\n\n{kural_te}"
                   ).format(**self.__kuralInfo))

            print("\nமு.வ உரை:")
            print(*wrap(self.varadarasan, break_long_words=False), sep='\n')
            print("\nசாலமன் பாப்பையா உரை:")
            print(*wrap(self.paapaya, break_long_words=False), sep='\n')
            print()

        # -en flag
        elif lang == 'en':
            print(("\n"
                   "Category: {paal_en}({paal_no}/3) | "
                   "Sub-Category: {iyal_en}({iyal_no}/10) | "
                   "Chapter: {adigaaram_en}({adigaaram_no}/133)\n\n"
                   "Verse-{no}:"
                   "\n{kural_en}"
                   ).format(**self.__kuralInfo))

            print("\nMeaning:")
            print(*wrap(self.en_meaning.strip(), break_long_words=False),
                  sep='\n')
            print()

        else:
            print("Provided lang not available as of now..!!")


def main():

    Help = {
        'des': "Thirukkural by Thiruvalluvar",
          'a': "display the ten Thirukurals in the specified chapter",
          'k': "display the Thirukural and its meaning",
          'i': "display the Adigaarams in the specified Iyal",
          'p': "display the Iyals in the specified Paal",

          'v': "show version info and exit",
          's': "show thiruvalluvar and exit",

         'sp': "display all paals (category)",
         'si': "display all iyals (sub-category)",
         'sa': "display all adigaarams (chapter)",

         'og': "opens the github page in the browser",
        'opy': "opens the PyPi page in the browser",
        'ope': "opens the download stats page in the browser",
        'dev': "opens the developer homepage",

         'en': "set language as english for -k and -a flag"
    }

    parser = argparse.ArgumentParser(description=Help['des'])
    add_arg = parser.add_argument

    # arguments
    st = "store_true"
    add_arg("-en", action=st, help=Help['en'])

    add_arg("-k", metavar="1-1330", help=Help['k'], type=int)
    add_arg("-a", metavar="1-133", help=Help['a'])
    add_arg("-i", metavar="1-10", help=Help['i'], type=int)
    add_arg("-p", metavar="1-3", help=Help['p'], type=int)

    add_arg("--all-paals", action=st, help=Help['sp'])
    add_arg("--all-iyals", action=st, help=Help['si'])
    add_arg("--all-adigaarams", action=st, help=Help['sa'])

    add_arg("--github", action=st, help=Help['og'])
    add_arg("--pypi", action=st, help=Help['opy'])
    add_arg("--pepy", action=st, help=Help['ope'])
    add_arg("--dev", action=st, help=Help['dev'])
    add_arg("-v", action=st, help=Help['v'])
    add_arg("-s", action=st, help=Help['s'])

    args = parser.parse_args()
    L = "en" if args.en else "ta"

    if args.all_paals:
        Paal.show_all_paals()
        sys.exit()

    if args.all_iyals:
        Iyal.show_all_iyals()
        sys.exit()

    if args.all_adigaarams:
        Adigaaram.show_all_adigaarams()
        sys.exit()

    if args.github:
        webbrowser.open("https://github.com/VaasuDevanS/thirukkural-cl")
        sys.exit()

    if args.pypi:
        webbrowser.open("https://pypi.org/project/thirukkural/")
        sys.exit()

    if args.pepy:
        webbrowser.open("https://pepy.tech/project/thirukkural")
        sys.exit()

    if args.dev:
        webbrowser.open("https://vaasudevans.github.io/")
        sys.exit()

    if args.s:
        print(
        """
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
        """
        )
        sys.exit()

    if args.v:
        print("Version: %s" % __version__)
        sys.exit()

    if len(sys.argv) <= 2:
        Kural(random.randint(1,1330)).showCL(lang=L)

    if args.k:
        Kural(args.k).showCL(lang=L)

    if args.a:
        if args.a.isdigit():
            Adigaaram(int(args.a)).showCL(lang=L)
        else:
            Adigaaram(name=args.a).showCL(lang=L)

    if args.i:
        Iyal(int(args.i)).showCL()

    if args.p:
        Paal(int(args.p)).showCL()

# EOF
