# Dictionnaire mois
calendar = {
    "january": [1, 31, "janvier"],
    "february": [2, 28, "février"],
    "march": [3, 31, "mars"],
    "april": [4, 30, "avril"],
    "may": [5, 31, "mai"],
    "june": [6, 30, "juin"],
    "july": [7, 31, "juillet"],
    "august": [8, 31, "aout"],
    "september": [9, 30, "septembre"],
    "october": [10, 31, "octobre"],
    "november": [11, 30, "novembre"],
    "december": [12, 31, "décembre"],
}


game = True
french = False
find = False
a_month = ""
year = -1
days = 0

separator_fr = f"+{'-' * 45}+"
header_fr = f"| Bienvenue sur l'application nombre de jours |"
separator_en = f"+{'-' * 38}+"
header_en = f"| Welcome on days on month application |"
leave = "For leave write 'exit'"
leave_fr = "Pour quitter tapez 'exit'"
label_input_year = "Please enter a year : "
label_input_year_fr = "Veuillez taper une année : "
label_input_month = "Please enter a month : "
label_input_month_fr = "Veuillez taper un mois : "
translate = "Pour le français tapez 'fr'"
translate_fr = "For english write 'en'"


# noinspection DuplicatedCode
def isb(a_year=0):
    if a_year % 4 == 0 and a_year % 100 != 0 or a_year % 400 == 0:
        return True
    else:
        return False


def to_int(something=""):
    try:
        number = int(something)
    except ValueError:
        print("%s n'est pas un nombre (en chiffre hein !) !!!" % something)
        return -1
    else:
        return number


def in_calendar(month_founding="", afrench=french, is_find=find, thedays=days):
    for good in calendar:
        if month_founding.lower() == good:
            afrench = False
            is_find = True
            if (good == "february") & isb(year):
                thedays = calendar[good][2] + 1
            else:
                thedays = calendar[good][2]
            break
        elif month_founding.lower() == calendar[good][3]:
            afrench = True
            is_find = True
            if (calendar[good][3] == "février") & isb(year):
                thedays = calendar[good][2] + 1
            else:
                thedays = calendar[good][2]
            break
    return afrench, is_find, thedays


# programme
while game:
    if french:
        sep_to_print = separator_fr
        head_to_print = header_fr
        leave_print = leave_fr
        translate_print = translate_fr
        lab_imp_y = label_input_year_fr
    else:
        sep_to_print = separator_en
        head_to_print = header_en
        leave_print = leave
        translate_print = translate
        lab_imp_y = label_input_year
    print(sep_to_print)
    print(head_to_print)
    print(sep_to_print)
    print("")
    print(leave_print)
    print(translate_print)

    a_month = input(lab_imp_y)
    if a_month == "exit":
        game = False
    elif a_month == "en":
        french = False
    elif a_month == "fr":
        french = True
