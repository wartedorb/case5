"""Case-study #4 Парсинг web-страниц
Разработчики:
Бикметов Э.Б., Кондрашов М.С., Бычков Кирилл"""
import urllib.request
with open('input.txt') as f_in:
    for line in f_in:
        f = urllib.request.urlopen(line)
        s = f.read()
        text = str(s)
        part_name = text.find("nfl-c-player-header__title")
        name = text[text.find('>',part_name)+1:text.find('</h1',part_name)]
        print(name)
