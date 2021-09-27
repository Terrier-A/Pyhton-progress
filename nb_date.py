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
the_input = ""
year = -1
days = 0

separator_fr = f"+{'-' * 45}+"
header_fr = f"| Bienvenue sur l'application nombre de jours |"
separator_en = f"+{'-' * 38}+"
header_en = f"| Welcome to days on month application |"
leave = "For leave write 'exit'"
leave_fr = "Pour quitter tapez 'exit'"
label_input_year = "Please enter a year : "
label_input_year_fr = "Veuillez taper une année : "
label_input_month = "Please enter a month : "
label_input_month_fr = "Veuillez taper un mois : "
translate = "Pour le français tapez 'fr'"
translate_fr = "For english write 'en'"
prompt_menu_en = "You want to use it ? You can by write yes or use commands bellow : "
prompt_menu_fr = "Vous voulez l'utiliser ?  Tapez oui ou utilisez les commandes ci-dessus : "


# noinspection DuplicatedCode
def isb(a_year=0):
    if a_year % 4 == 0 and a_year % 100 != 0 or a_year % 400 == 0:
        return True
    else:
        return False


def ask_ok(prompt, retries=4, reminder='exit'):
    while retries > 0:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes', 'oui'):
            return "continue"
        elif ok in ('n', 'no', 'nop', 'nope', 'exit', 'leave', 'quit'):
            return reminder
        elif ok in ('fr', 'fra', 'french'):
            return "fr"
        retries = retries - 1
        if retries < 0:
            return reminder


def to_int(prompt, retry=3):
    number = 0
    while retry > 0:
        try:
            number = int(input(prompt))
        except ValueError:
            print("%s n'est pas un nombre (en chiffre hein !) !!!" % number)
        else:
            return number
        finally:
            retry -= 1
            if retry < 1:
                return


def in_calendar(month_founding="", year_is_bis=0):
    the_days = 0
    is_find = False
    for good in calendar:
        if month_founding.lower() == good:
            is_find = True
            if (good == "february") & isb(year_is_bis):
                the_days = calendar[good][1] + 1
            else:
                the_days = calendar[good][1]
            break
        elif month_founding.lower() == calendar[good][2]:
            is_find = True
            if (calendar[good][2] == "février") & isb(year_is_bis):
                the_days = calendar[good][1] + 1
            else:
                the_days = calendar[good][1]
            break
    if is_find:
        return the_days
    else:
        return -1


# programme
while game:
    if french:
        sep_to_print = separator_fr
        head_to_print = header_fr
        leave_print = leave_fr
        translate_print = translate_fr
        lab_imp_y = label_input_year_fr
        lab_imp_m = label_input_month_fr
        prompt_menu = prompt_menu_fr
    else:
        sep_to_print = separator_en
        head_to_print = header_en
        leave_print = leave
        translate_print = translate
        lab_imp_y = label_input_year
        lab_imp_m = label_input_month
        prompt_menu = prompt_menu_en
    print(sep_to_print)
    print(head_to_print)
    print(sep_to_print)
    print("")
    print(leave_print)
    print(translate_print)
    print("")

    the_input = ask_ok(prompt_menu)

    if the_input == "exit":
        game = False
    elif the_input == "en":
        french = False
    elif the_input == "fr":
        french = True
    elif the_input == "continue":
        year = to_int(lab_imp_y)
    if year == -1:
        continue
    else:
        the_input = input(lab_imp_m)
        days = in_calendar(the_input, year)
        if days > 0:
            print("%s %s" % (days, the_input))
        else:
            print("%s" % the_input)
    year = 0
