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


def custom_capitalize(s):
    # Do not capitalize certain words:
    if s in ["e"]:
        return s
    return s[0].upper() + s[1:] if s else s


def strip_prefix(period):
    if period == "in serata":
        return "sera"
    if period == "in mattinata":
        return "mattina"
    if period.startswith("nella "):
        return period[6:]
    if period.startswith("nel "):
        return period[4:]
    return period


def and_function(stack, a, b):
    if len(b) > 8 and b[:8] == "prossimo":
        joiner = " e il "
    elif len(b) > 8 and b[:8] == "prossima":
        joiner = " e la "
    else:
        joiner = " e "

    if "," in a:
        joiner = "," + joiner

    return join_with_shared_prefix(a, b, joiner)


def through_function(stack, a, b):
    if len(b) > 8 and b[:8] == "prossimo":
        joiner = " fino al "
    elif len(b) > 8 and b[:8] == "prossima":
        joiner = " fino alla "
    else:
        joiner = " fino a "

    return join_with_shared_prefix(a, b, joiner)


def parenthetical_function(stack, a, b):
    return f"{a} ({b}{' di neve)' if a == 'precipitazioni miste' else ')'}"


def starting_function(stack, condition, period):
    return condition + " a partire da " + strip_prefix(period)


def until_function(stack, condition, period):
    return condition + " fino a " + strip_prefix(period)


def until_starting_again_function(stack, condition, a, b):
    return condition + " fino a " + strip_prefix(a) + ", ricominciando da " + b


def starting_continuing_until_function(stack, condition, a, b):
    return (
        condition + " a partire da " + strip_prefix(a) + ", fino a " + strip_prefix(b)
    )


def title_function(stack, s):
    # Capitalize the first letter of every word, except if that word is "e".
    return re.sub(r"\w+", lambda m: custom_capitalize(m.group(0)), s)


def sentence_function(stack, s):
    s = s[0].upper() + s[1:]
    if not s.endswith("."):
        s += "."
    return s


template = {
    "clear": "sereno",
    "no-precipitation": "nessuna precipitazione",
    "mixed-precipitation": "precipitazioni miste",
    "possible-very-light-precipitation": "possibilità di precipitazioni molto leggere",
    "very-light-precipitation": "precipitazioni molto leggere",
    "possible-light-precipitation": "possibilità di precipitazioni leggere",
    "light-precipitation": "precipitazioni leggere",
    "medium-precipitation": "precipitazioni",
    "heavy-precipitation": "forti precipitazioni",
    "possible-very-light-rain": "possibilità di pioggia molto leggera",
    "very-light-rain": "pioggia molto leggera",
    "possible-light-rain": "possibilità di pioggia leggera",
    "light-rain": "pioggia leggera",
    "medium-rain": "pioggia",
    "heavy-rain": "temporali",
    "possible-very-light-sleet": "possibilità di nevischio molto leggero",
    "very-light-sleet": "nevischio molto leggero",
    "possible-light-sleet": "possibilità di nevischio leggero",
    "light-sleet": "nevischio leggero",
    "medium-sleet": "nevischio",
    "heavy-sleet": "forte nevischio",
    "possible-very-light-snow": "possibilità di nevicate molto leggere",
    "very-light-snow": "nevicate molto leggere",
    "possible-light-snow": "possibilità di neve leggera",
    "light-snow": "neve leggera",
    "medium-snow": "nevicate",
    "heavy-snow": "forti nevicate",
    "possible-thunderstorm": "possibili nubifragi",
    "thunderstorm": "nubifragi",
    "possible-medium-precipitation": "possibilità di precipitazioni",
    "possible-heavy-precipitation": "possibilità di forti precipitazioni",
    "possible-medium-rain": "possibilità di pioggia",
    "possible-heavy-rain": "possibilità di temporali",
    "possible-medium-sleet": "possibilità di nevischio",
    "possible-heavy-sleet": "possibilità di forte nevischio",
    "possible-medium-snow": "possibilità di nevicate",
    "possible-heavy-snow": "possibilità di forti nevicate",
    "possible-very-light-freezing-rain": "possibilità di pioggia leggera molto gelata",
    "very-light-freezing-rain": "pioggia leggera molto gelata",
    "possible-light-freezing-rain": "possibilità di pioggia gelata leggera",
    "light-freezing-rain": "freezing pioggia leggera",
    "possible-medium-freezing-rain": "possibilità di pioggia gelata",
    "medium-freezing-rain": "pioggia gelata",
    "possible-heavy-freezing-rain": "possibilità di forte pioggia gelata",
    "heavy-freezing-rain": "forte pioggia gelata",
    "possible-hail": "possibilità di grandine",
    "hail": "grandine",
    "light-wind": "venticello",
    "medium-wind": "vento",
    "heavy-wind": "forte vento",
    "low-humidity": "bassa umidità",
    "high-humidity": "umido",
    "fog": "nebbia",
    "very-light-clouds": "prevalentemente sereno",
    "light-clouds": "poco nuvoloso",
    "medium-clouds": "nubi sparse",
    "heavy-clouds": "nuvoloso",
    "today-morning": "stamattina",
    "later-today-morning": "a mattina inoltrata",
    "today-afternoon": "questo pomeriggio",
    "later-today-afternoon": "a pomeriggio inoltrato",
    "today-evening": "stasera",
    "later-today-evening": "a sera inoltrata",
    "today-night": "stanotte",
    "later-today-night": "notte inoltrata",
    "tomorrow-morning": "domani mattina",
    "tomorrow-afternoon": "domani pomeriggio",
    "tomorrow-evening": "domani sera",
    "tomorrow-night": "domani notte",
    "morning": "in mattinata",
    "afternoon": "nel pomeriggio",
    "evening": "in serata",
    "night": "nella notte",
    "today": "oggi",
    "tomorrow": "domani",
    "sunday": "Domenica",
    "monday": "Lunedì",
    "tuesday": "Martedì",
    "wednesday": "Mercoledì",
    "thursday": "Giovedì",
    "friday": "Venerdì",
    "saturday": "Sabato",
    "next-sunday": "prossima Domenica",
    "next-monday": "prossimo Lunedì",
    "next-tuesday": "prossimo Martedì",
    "next-wednesday": "prossimo Mercoledì",
    "next-thursday": "prossimo Giovedì",
    "next-friday": "prossimo Venerdì",
    "next-saturday": "prossimo Sabato",
    "minutes": "$1 min.",
    "fahrenheit": "$1\u00b0F",
    "celsius": "$1\u00b0C",
    "inches": "$1 in.",
    "centimeters": "$1 cm.",
    "less-than": "meno di $1",
    "and": and_function,
    "through": through_function,
    "with": "$1, con $2",
    "range": "$1\u2013$2",
    "parenthetical": parenthetical_function,
    "for-hour": "$1 per un ora",
    "starting-in": "$1 tra $2",
    "stopping-in": "$1 per $2",
    "starting-then-stopping-later": "$1 a partire tra $2 per $3",
    "stopping-then-starting-later": "$1 per altri $2, per ricominciare $3 più tardi",
    "for-day": "$1 durante il giorno",
    "starting": starting_function,
    "until": until_function,
    "until-starting-again": until_starting_again_function,
    "starting-continuing-until": starting_continuing_until_function,
    "during": "$1 $2",
    "for-week": "$1 durante la settimana",
    "over-weekend": "$1 tutto il week end",
    "temperatures-peaking": "temperatura massima di $1 $2",
    "temperatures-rising": "temperature in aumento fino a $1 $2",
    "temperatures-valleying": "temperatura minima di $1 $2",
    "temperatures-falling": "temperature in diminuzione fino a $1 $2",
    "title": title_function,
    "sentence": sentence_function,
    "next-hour-forecast-status": "le previsioni per la prossima ora sono di $1 a causa di $2",
    "unavailable": "non disponibile",
    "temporarily-unavailable": "temporaneamente non disponibile",
    "partially-unavailable": "parzialmente non disponibile",
    "station-offline": "tutte le stazioni radar vicine sono offline",
    "station-incomplete": "lacune nella copertura delle stazioni radar vicine",
    "smoke": "fumo",
    "haze": "foschia",
    "mist": "nebbia",
}
