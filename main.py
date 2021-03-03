"""Case-study #4 Парсинг web-страниц
Разработчики:
Бикметов Э.Б. = 40, Кондрашов М.С. = 40, Бычков Кирилл Алексеевич = 35"""
import urllib.request
with open('input.txt') as f_in:
    with open('output.txt', 'a+') as f_out:
        for line in f_in:
            f = urllib.request.urlopen(line)
            s = f.read()
            text = str(s)
            part_name = text.find("nfl-c-player-header__title")
            name = text[text.find('>', part_name)+1:text.find('</h1', part_name)]
            COMP_help = text.find('passingCompletions')
            COMP = text[text.find('>', COMP_help)+25:text.find('</th', COMP_help)-22]
            att_help = text.find('passingAttempts')
            ATT = text[text.find('>', att_help)+25:text.find('</th', att_help)-22]
            YDS_help = text.find('passingYards')
            YDS = text[text.find('>', YDS_help)+25:text.find('</th', YDS_help)-22]
            TD_help = text.find('passingTouchdowns')
            TD = text[text.find('>', TD_help)+25:text.find('</th', TD_help)-22]
            INT_help = text.find('passingInterceptions')
            INT = text[text.find('>', INT_help) + 25:text.find('</th', INT_help) - 22]
            PR_help = text.find('passingPasserRating')
            PR = float(text[text.find('>', PR_help) + 25:text.find('</th', PR_help) - 22])
            print('{:<20s}{:<7s}{:<7s}{:<7s}{:<7s}{:<7s}{:<7}'.format(name, COMP, ATT, YDS, TD, INT, PR), file=f_out)
