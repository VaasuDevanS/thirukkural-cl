
from subprocess import check_output
from bs4 import BeautifulSoup
from pprint import pprint
import sqlite3
import re

if __name__ == "__main__":

    html = lambda link: check_output("curl -s %s" % link,
                                     shell=True).decode("utf-8")

    # http://tamilnation.co/literature/kural/kaviyogi/tks1a.htm
    # https://ilakkiyam.com/thirukural
    Paal, Iyal, Adigaaram = [], [], []

    Paal += [("அறத்துப்பால்",  "Righteousness", "Arathuppal")] * 37
    Paal += [("பொருட்பால்", "Wealth", "Porutpaal")] * 71
    Paal += [("காமத்துப்பால்",  "Love", "Kaamathuppal")] * 25

    Iyal += [("பாயிரவியல்",  "Prologue", "Paayiraviyal")] * 4
    Iyal += [("இல்லறவியல்",  "Domestic Virtue", "Illaraviyal")] * 20
    Iyal += [("துறவறவியல்", "Ascetic Virtue", "Thuravaraviyal")] * 13
    Iyal += [("ஊழியல்",  "Fate", "Oozhiyal")] * 1
    Iyal += [("அரசியல்",  "Royalty", "Arasiyal")] * 25
    Iyal += [("அமைச்சியல்",  "Ministers of State", "Amaichiyal")] * 10
    Iyal += [("அங்கவியல்",  "Politics", "Angaviyal")] * 22
    Iyal += [("ஒழிபியல்",  "Miscellaneous", "Ozhibiyal")] * 13
    Iyal += [("களவியல்",  "The Pre-marital love", "Kalaviyal")] * 7
    Iyal += [("கற்பியல்",  "The Post-marital love", "Karpiyal")] * 18

    link = "http://www.ytamizh.com/thirukuralchapters/"
    soup = BeautifulSoup(html(link), "html.parser")
    t = soup.find_all("tr")[1:]
    for chap in t:
        info = [j.contents[0] for j in chap.find_all("td")][:-1]
        info[1] = [j.contents[0] for j in chap.find_all("a")][0]
        Adigaaram.append(tuple(info))

    Kural = [list(sum(i,())) for i in zip(Paal, Iyal, Adigaaram) for j in range(10)]
    no = 0

    for chap in range(1, 134):

        link = "http://www.ytamizh.com/thirukural/chapter-%s/" % chap
        soup = BeautifulSoup(html(link), "html.parser")
        kurals = soup.find_all("div", attrs={"class": "kural_sub"})
        for kural in kurals:
            for k in kural.find_all('p'):
                K = [re.sub(r"<br/>|\r", "", str(i)) for i in k]
                Kural[no].append("".join(K))
            Kural[no].insert(0, no+1)
            no += 1

    print("started")
    with sqlite3.connect("kural.db") as conn:
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS kural (
                no INTEGER PRIMARY KEY,
                paal_ta TEXT,
                paal_en TEXT,
                paal_te TEXT,
                iyal_ta TEXT,
                iyal_en TEXT,
                iyal_te TEXT,
                adigaaram_no INTEGER,
                adigaaram_ta TEXT,
                adigaaram_en TEXT,
                adigaaram_te TEXT,
                kural_ta TEXT,
                varadarasan TEXT,
                paapaya TEXT,
                kural_en TEXT,
                en_meaning TEXT,
                kural_te TEXT
            )""")

        for rec in Kural:
            cur.execute("""
                INSERT INTO kural values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
                """, rec)

#EOF
