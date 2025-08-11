import re


def join_with_shared_prefix(a, b, joiner):
    i = 0
    min_len = min(len(a), len(b))

    while i < min_len and ord(a[i]) == ord(b[i]):
        i += 1

    # Move back until we hit a space or start of string
    while i > 0 and (i > len(a) or (i <= len(a) and a[i - 1] != " ")):
        i -= 1

    # Return the joined string
    return a[:i] + a[i:] + joiner + b[i:]


def and_function(stack, a, b):
    return join_with_shared_prefix(a, b, ", et " if "," in a else " et ")


def through_function(stack, a, b):
    return join_with_shared_prefix(a, b, " jusqu’à ")


def starting_in_function(stack, condition, period):
    if condition == "ciel couvert":
        return f"ciel se couvrant dans {period}"
    if condition == "ciel dégagé":
        return f"ciel se dégageant dans {period}"
    return f"{condition} commençant dans {period}"


def starting_then_stopping_later_function(stack, condition, start, end):
    if condition == "ciel couvert":
        return f"ciel se couvrant dans {start}, se terminant {end} plus tard"
    if condition == "ciel dégagé":
        return f"ciel se dégageant dans {start}, se terminant {end} plus tard"
    return f"{condition} commençant dans {start}, se terminant {end} plus tard"


def stopping_then_starting_later_function(stack, a, b, c):
    return f"{a} se terminant dans {b}, et reprenant {c} plus tard"


def starting_function(stack, condition, start):
    if condition == "ciel couvert":
        return f"ciel se couvrant {start}"
    if condition == "ciel dégagé":
        return f"ciel se dégageant {start}"
    return f"{condition} commençant {start}"


def until_function(stack, condition, period):
    # Replace "jusqu’à dans" with "jusque dans"
    res = condition + " jusqu’à " + period
    return res.replace("jusqu’à dans", "jusque dans")


def until_starting_again_function(stack, condition, a, b):
    res = condition + " jusqu’à " + a + ", reprenant " + b
    return res.replace("jusqu’à dans", "jusque dans")


def starting_continuing_until_function(stack, condition, a, b):
    res = condition + " commençant " + a + ", se prolongeant jusqu’à " + b
    return res.replace("jusqu’à dans", "jusque dans")


def title_function(stack, s):
    # Capitalize first letter of every word except "et"
    def repl(m):
        word = m.group(0)
        return word if word == "et" else word[0].upper() + word[1:]

    return re.sub(r"\S+", repl, s)


def sentence_function(stack, s):
    s = s[0].upper() + s[1:] if s else s
    if not s.endswith("."):
        s += "."
    return s


template = {
    "clear": "ciel dégagé",
    "mostly-clear": "en grande partie clair",
    "no-precipitation": "pas de précipitations",
    "mixed-precipitation": "précipitations mixtes",
    "possible-very-light-precipitation": "très faibles précipitations possibles",
    "very-light-precipitation": "très faibles précipitations",
    "possible-light-precipitation": "faibles précipitations possibles",
    "light-precipitation": "faibles précipitations",
    "medium-precipitation": "précipitations",
    "heavy-precipitation": "fortes précipitations",
    "possible-very-light-rain": "bruine possible",
    "very-light-rain": "bruine",
    "possible-light-rain": "pluie faible possible",
    "light-rain": "pluie faible",
    "medium-rain": "pluie",
    "heavy-rain": "pluie forte",
    "possible-very-light-sleet": "très faible neige fondante possible",
    "very-light-sleet": "très faible neige fondante",
    "possible-light-sleet": "faible neige fondante possible",
    "light-sleet": "faible neige fondante",
    "medium-sleet": "neige fondante",
    "heavy-sleet": "forte neige fondante",
    "possible-very-light-snow": "averses de neige possibles",
    "very-light-snow": "averses de neige",
    "possible-light-snow": "neige faible possible",
    "light-snow": "neige faible",
    "medium-snow": "neige",
    "heavy-snow": "neige abondante",
    "possible-thunderstorm": "orages possibles",
    "thunderstorm": "orage",
    "possible-medium-precipitation": "précipitations possible",
    "possible-heavy-precipitation": "fortes précipitations possible",
    "possible-medium-rain": "pluie possible",
    "possible-heavy-rain": "pluie forte possible",
    "possible-medium-sleet": "neige fondante possible",
    "possible-heavy-sleet": "forte neige fondante possible",
    "possible-medium-snow": "neige possible",
    "possible-heavy-snow": "neige abondante possible",
    "possible-very-light-freezing-rain": "bruine verglaçante possible",
    "very-light-freezing-rain": "bruine verglaçante",
    "possible-light-freezing-rain": "pluie légère verglaçante possible",
    "light-freezing-rain": "pluie légère verglaçante",
    "possible-medium-freezing-rain": "pluie verglaçante possible",
    "medium-freezing-rain": "pluie verglaçante",
    "possible-heavy-freezing-rain": "forte pluie verglaçante possible",
    "heavy-freezing-rain": "forte pluie verglaçante",
    "possible-hail": "grêle possible",
    "hail": "grêle",
    "light-wind": "vent faible",
    "medium-wind": "vent moyen",
    "heavy-wind": "vent fort",
    "low-humidity": "temps sec",
    "high-humidity": "temps humide",
    "fog": "brumeux",
    "very-light-clouds": "en grande partie clair",
    "light-clouds": "faibles passages nuageux",
    "medium-clouds": "ciel nuageux",
    "heavy-clouds": "ciel couvert",
    "today-morning": "ce matin",
    "later-today-morning": "dans la matinée",
    "today-afternoon": "cet après-midi",
    "later-today-afternoon": "dans l’après-midi",
    "today-evening": "ce soir",
    "later-today-evening": "dans la soirée",
    "today-night": "cette nuit",
    "later-today-night": "dans la nuit",
    "tomorrow-morning": "demain matin",
    "tomorrow-afternoon": "demain après-midi",
    "tomorrow-evening": "demain soir",
    "tomorrow-night": "demain pendant la nuit",
    "morning": "dans la matinée",
    "afternoon": "dans l’après-midi",
    "evening": "dans la soirée",
    "night": "dans la nuit",
    "today": "aujourd’hui",
    "tomorrow": "demain",
    "sunday": "dimanche",
    "monday": "lundi",
    "tuesday": "mardi",
    "wednesday": "mercredi",
    "thursday": "jeudi",
    "friday": "vendredi",
    "saturday": "samedi",
    "next-sunday": "dimanche prochain",
    "next-monday": "lundi prochain",
    "next-tuesday": "mardi prochain",
    "next-wednesday": "mercredi prochain",
    "next-thursday": "jeudi prochain",
    "next-friday": "vendredi prochain",
    "next-saturday": "samedi prochain",
    "minutes": "$1 min.",
    "fahrenheit": "$1\u00b0F",
    "celsius": "$1\u00b0C",
    "inches": "$1 in.",
    "centimeters": "$1 cm.",
    "less-than": "moins de $1",
    "and": and_function,
    "through": through_function,
    "with": "$1, avec $2",
    "range": "$1\u2013$2",
    "parenthetical": "$1 ($2)",
    "for-hour": "$1 pendant la prochaine heure",
    "starting-in": starting_in_function,
    "stopping-in": "$1 se terminant dans $2",
    "starting-then-stopping-later": starting_then_stopping_later_function,
    "stopping-then-starting-later": stopping_then_starting_later_function,
    "for-day": "$1 toute la journée",
    "starting": starting_function,
    "until": until_function,
    "until-starting-again": until_starting_again_function,
    "starting-continuing-until": starting_continuing_until_function,
    "during": "$1 $2",
    "for-week": "$1 pendant toute la semaine",
    "over-weekend": "$1 pendant tout le week-end",
    "temperatures-peaking": "des températures maximales atteignant $1 $2",
    "temperatures-rising": "des températures maximales montant jusqu’à $1 $2",
    "temperatures-valleying": "des températures maximales atteignant $1 $2",
    "temperatures-falling": "des températures maximales descendant jusqu’à $1 $2",
    "title": title_function,
    "sentence": sentence_function,
    "next-hour-forecast-status": "Les prévisions pour la prochaine heure sont $1 car $2.",
    "unavailable": "indisponibles",
    "temporarily-unavailable": "temporairement indisponibles",
    "partially-unavailable": "partiellement indisponibles",
    "station-offline": "les stations radars voisines sont hors-ligne",
    "station-incomplete": "il y a des lacunes dans la couverture des stations radars voisines",
    "smoke": "fumée",
    "haze": "brume",
    "mist": "brume",
}
