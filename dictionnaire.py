# Dictionnaire mois
calendar = {
    "january": 31,
    "february": 28,
    "march": 31,
    "april": 30,
    "may": 31,
    "june": 30,
    "july": 31,
    "august": 31,
    "september": 30,
    "october": 31,
    "november": 30,
    "december": 31,
}

calendrier = {
    "janvier": 31,
    "février": 28,
    "mars": 31,
    "avril": 30,
    "mai": 31,
    "juin": 30,
    "juillet": 31,
    "aout": 31,
    "septembre": 30,
    "octobre": 31,
    "novembre": 30,
    "décembre": 31,
}

game = True
french = False
find = False
a_month = ""
year = -1
days = 0


# def isb(a_year=0):
#     if a_year % 4 == 0 and a_year % 100 != 0 or a_year % 400 == 0:
#         return True
#     else:
#         return False


def to_int(a_year=""):
    try:
        good_year = int(a_year)
    except ValueError:
        print("%s n'est pas un nombre (en chiffre hein !) !!!" % a_year)
        return -1
    else:
        return good_year


# programme
while game:
    while year < 0:
        year = to_int(input("Please type à year : "))

    if not french:
        a_month = input("Please type a month : ")
    else:
        a_month = input("Veuillez donner un mois : ")

    if a_month == "exit":
        print("Goodbye // Au revoir ")
        game = False
    else:
        for good in calendar:
            if a_month.lower() == good:
                french = False
                find = True
                if (good == "february") & isb(year):
                    days = calendar[good] + 1
                else:
                    days = calendar[good]
                break
        for bon in calendrier:
            if a_month.lower() == bon:
                french = True
                find = True
                if (bon == "février") & isb(year):
                    days = calendrier[bon] + 1
                else:
                    days = calendrier[bon]
                break

    if find:
        if french:
            print("Le mois de %s compte %s jours" % (a_month.capitalize(), days))
        else:
            print("The month of %s count %s days" % (a_month.capitalize(), days))
    else:
        if french:
            print("Désolé le mois de %s n'existe pas " % a_month.capitalize())
        else:
            print("Sorry %s doesn't exist" % a_month.capitalize())
    find = False
    year = -1
