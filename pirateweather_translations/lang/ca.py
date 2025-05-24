import re


def join_with_shared_prefix(a, b, joiner):
    m = a
    i = 0

    # Skip the prefix of b that is shared with a.
    min_len = min(len(m), len(b))
    while i < min_len and ord(m[i]) == ord(b[i]):
        i += 1

    # ...except whitespace! We need that whitespace!
    # Move back until we hit a space or start of string
    while i > 0 and (i > len(b) or (i <= len(b) and b[i - 1] != " ")):
        i -= 1

    return a + joiner + b[i:]


def and_function(stack, a, b):
    return join_with_shared_prefix(a, b, ", i " if "," in a else " i ")


def through_function(stack, a, b):
    return join_with_shared_prefix(a, b, " fins a ")


def title_function(stack, s):
    def capitalize_word(word):
        return word if word == "i" else word[0].upper() + word[1:]

    return re.sub(r"\S+", lambda match: capitalize_word(match.group(0)), s)


def sentence_function(stack, s):
    s = s[0].upper() + s[1:]
    if not s.endswith("."):
        s += "."
    return s


template = {
    "clear": "clar",
    "no-precipitation": "sense precipitacions",
    "mixed-precipitation": "precipitacions mixtes",
    "possible-very-light-precipitation": "possibles pluges lleugeres",
    "very-light-precipitation": "pluges lleugeres",
    "possible-light-precipitation": "possibles pluges lleugeres",
    "light-precipitation": "precipitacions lleugeres",
    "medium-precipitation": "precipitació",
    "heavy-precipitation": "fortes precipitacions",
    "possible-very-light-rain": "possible plugim",
    "very-light-rain": "plugim",
    "possible-light-rain": "possible plugim",
    "light-rain": "pluja lleugera",
    "medium-rain": "pluja",
    "heavy-rain": "pluges fortes",
    "possible-very-light-sleet": "possible aiguaneu",
    "very-light-sleet": "aiguaneu",
    "possible-light-sleet": "possible aiguaneu",
    "light-sleet": "aiguaneu",
    "medium-sleet": "aiguaneu",
    "heavy-sleet": "fortes aiguaneu",
    "possible-very-light-snow": "possible nevada lleugera",
    "very-light-snow": "lleugeres nevades",
    "possible-light-snow": "possible nevada lleugera",
    "light-snow": "lleugeres nevades",
    "medium-snow": "nevades",
    "heavy-snow": "fortes nevades",
    "possible-thunderstorm": "possibles tempestes",
    "thunderstorm": "tempesta",
    "possible-medium-precipitation": "possible precipitacions",
    "possible-heavy-precipitation": "possible fortes precipitacions",
    "possible-medium-rain": "possible pluja",
    "possible-heavy-rain": "possible pluja pluja",
    "possible-medium-sleet": "possible aiguaneu",
    "possible-heavy-sleet": "possible fortes aiguaneu",
    "possible-medium-snow": "possible nevades",
    "possible-heavy-snow": "possible fortes nevades",
    "possible-very-light-freezing-rain": "possible plugim glacial",
    "very-light-freezing-rain": "plugim glacial",
    "possible-light-freezing-rain": "possible freezing pluja lleugera",
    "light-freezing-rain": "pluja gelada lleugera",
    "possible-medium-freezing-rain": "possible pluja gelada",
    "medium-freezing-rain": "pluja gelada",
    "possible-heavy-freezing-rain": "possible pluja gelada fortes",
    "heavy-freezing-rain": "pluja gelada fortes",
    "possible-hail": "possible calamarsa",
    "hail": "calamarsa",
    "light-wind": "vents fluixos",
    "medium-wind": "ventós",
    "heavy-wind": "perillosament ventós",
    "low-humidity": "sec",
    "high-humidity": "humit",
    "fog": "ennuvolat",
    "very-light-clouds": "majoritariament clar",
    "light-clouds": "parcialment ennuvolat",
    "medium-clouds": "majoritariament ennuvolat",
    "heavy-clouds": "ennuvolat",
    "today-morning": "aquest matí",
    "later-today-morning": "durant el matí",
    "today-afternoon": "aquesta tarda",
    "later-today-afternoon": "durant la tarda",
    "today-evening": "aquest vespre",
    "later-today-evening": "durant el vespre",
    "today-night": "aquesta nit",
    "later-today-night": "durant la nit",
    "tomorrow-morning": "demà al matí",
    "tomorrow-afternoon": "demà a la tarda",
    "tomorrow-evening": "demà al vespre",
    "tomorrow-night": "demà a la nit",
    "morning": "al matí",
    "afternoon": "a la tarda",
    "evening": "al vespre",
    "night": "a la nit",
    "today": "avui",
    "tomorrow": "demà",
    "sunday": "el diumenge",
    "monday": "el dilluns",
    "tuesday": "el dimarts",
    "wednesday": "el dimecres",
    "thursday": "el dijous",
    "friday": "el divendres",
    "saturday": "el dissabte",
    "next-sunday": "el pròxim diumenge",
    "next-monday": "el pròxim dilluns",
    "next-tuesday": "el pròxim dimarts",
    "next-wednesday": "el pròxim dimecres",
    "next-thursday": "el pròxim dijous",
    "next-friday": "el pròxim divendres",
    "next-saturday": "el pròxim dissabte",
    "minutes": "$1 min.",
    "fahrenheit": "$1\u00b0F",
    "celsius": "$1\u00b0C",
    "inches": "$1 in.",
    "centimeters": "$1 cm.",
    "less-than": "menys de $1",
    "and": and_function,
    "through": through_function,
    "with": "$1, amb $2",
    "range": "$1\u2013$2",
    "parenthetical": "$1 ($2)",
    "for-hour": "$1 cada hora",
    "starting-in": "$1 començant $2",
    "stopping-in": "$1 parant a $2",
    "starting-then-stopping-later": "$1 començant d'aquí $2, després parant al cap $3",
    "stopping-then-starting-later": "$1 parant d'aquí $2, tornant a començar al cap $3",
    "for-day": "$1 durant el dia",
    "starting": "$1 començant $2",
    "until": "$1 $2",
    "until-starting-again": "$1 $2, començant $3",
    "starting-continuing-until": "$1 començant $2, continuant $3",
    "during": "$1 $2",
    "for-week": "$1 durant la setmana",
    "over-weekend": "$1 cap al cap de setmana",
    "temperatures-peaking": "temperatures aconseguint un màxim de $1 $2",
    "temperatures-rising": "temperatures arribant a $1 $2",
    "temperatures-valleying": "temperatures aconseguint un mínim de $1 $2",
    "temperatures-falling": "temperatures per sota a $1 $2",
    "title": title_function,
    "sentence": sentence_function,
    "next-hour-forecast-status": "Les previsions per a la propera hora són $1 a causa de $2",
    "unavailable": "no disponible",
    "temporarily-unavailable": "temporalment no disponible",
    "partially-unavailable": "temporalment no disponible",
    "station-offline": "totes les estacions de radar properes estan desconnectades",
    "station-incomplete": "buits en la cobertura de les estacions de radar properes",
}
