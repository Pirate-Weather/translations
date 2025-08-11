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
    return join_with_shared_prefix(a, b, ", y " if "," in a else " y ")


def through_function(stack, a, b):
    return join_with_shared_prefix(a, b, " hasta ")


def title_function(stack, s):
    """
    Convert a string to title case, skipping the word 'y'.
    """

    def capitalize_word(word):
        return word if word == "y" else word[0].upper() + word[1:]

    return re.sub(r"\S+", lambda match: capitalize_word(match.group(0)), s)


def sentence_function(stack, s):
    s = s[0].upper() + s[1:]
    if not s.endswith("."):
        s += "."
    return s


template = {
    "clear": "despejado",
    "mostly-clear": "mayormente despejado",
    "no-precipitation": "sin precipitaciones",
    "mixed-precipitation": "precipitación mixta",
    "possible-very-light-precipitation": "posibles lluvias ligeras",
    "very-light-precipitation": "lluvias ligeras",
    "possible-light-precipitation": "posibles lluvias ligeras",
    "light-precipitation": "precipitación ligera",
    "medium-precipitation": "precipitación",
    "heavy-precipitation": "fuerte precipitación",
    "possible-very-light-rain": "posible llovizna",
    "very-light-rain": "llovizna",
    "possible-light-rain": "posible lluvia ligera",
    "light-rain": "lluvia ligera",
    "medium-rain": "lluvia",
    "heavy-rain": "fuertes lluvias",
    "possible-very-light-sleet": "posible aguanieve ligera",
    "very-light-sleet": "aguanieve ligera",
    "possible-light-sleet": "posible aguanieve ligera",
    "light-sleet": "aguanieve ligera",
    "medium-sleet": "aguanieve",
    "heavy-sleet": "fuertes aguanieves",
    "possible-very-light-snow": "posible nevada ligera",
    "very-light-snow": "nevadas ligeras",
    "possible-light-snow": "posible nevada ligera",
    "light-snow": "nevadas ligeras",
    "medium-snow": "nevadas",
    "heavy-snow": "fuertes nevadas",
    "possible-thunderstorm": "tormentas posibles",
    "thunderstorm": "tormenta",
    "possible-medium-precipitation": "posibles precipitation",
    "possible-heavy-precipitation": "posibles fuertes precipitation",
    "possible-medium-rain": "posible lluvia",
    "possible-heavy-rain": "posible heavy lluvia",
    "possible-medium-sleet": "posible aguanieve",
    "possible-heavy-sleet": "posible fuertes aguanieve",
    "possible-medium-snow": "posible nevadas",
    "possible-heavy-snow": "posible fuertes nevadas",
    "possible-very-light-freezing-rain": "posible llovizna helada",
    "very-light-freezing-rain": "llovizna helada",
    "possible-light-freezing-rain": "posible nevadas lluvia helada",
    "light-freezing-rain": "nevadas lluvia helada",
    "possible-medium-freezing-rain": "posible lluvia helada",
    "medium-freezing-rain": "lluvia helada",
    "possible-heavy-freezing-rain": "posible fuertes lluvia helada",
    "heavy-freezing-rain": "fuertes lluvia helada",
    "possible-hail": "posible granizo",
    "hail": "granizo",
    "light-wind": "vientos suaves",
    "medium-wind": "ventoso",
    "heavy-wind": "peligrosamente ventoso",
    "low-humidity": "seco",
    "high-humidity": "húmedo",
    "fog": "niebla",
    "very-light-clouds": "mayormente despejado",
    "light-clouds": "parcialmente nublado",
    "medium-clouds": "mayormente nublado",
    "heavy-clouds": "nublado",
    "today-morning": "esta mañana",
    "later-today-morning": "después esta mañana",
    "today-afternoon": "esta tarde",
    "later-today-afternoon": "después esta tarde",
    "today-evening": "esta noche",
    "later-today-evening": "después esta noche",
    "today-night": "esta noche",
    "later-today-night": "después esta noche",
    "tomorrow-morning": "mañana por la mañana",
    "tomorrow-afternoon": "mañana por la tarde",
    "tomorrow-evening": "mañana por la noche",
    "tomorrow-night": "mañana por la noche",
    "morning": "por la mañana",
    "afternoon": "por la tarde",
    "evening": "por la noche",
    "night": "por la noche",
    "today": "hoy",
    "tomorrow": "mañana",
    "sunday": "el Domingo",
    "monday": "el Lunes",
    "tuesday": "el Martes",
    "wednesday": "el Miércoles",
    "thursday": "el Jueves",
    "friday": "el Viernes",
    "saturday": "el Sábado",
    "next-sunday": "el próximo Domingo",
    "next-monday": "el próximo Lunes",
    "next-tuesday": "el próximo Martes",
    "next-wednesday": "el próximo Miércoles",
    "next-thursday": "el próximo Jueves",
    "next-friday": "el próximo Viernes",
    "next-saturday": "el próximo Sábado",
    "minutes": "$1 min.",
    "fahrenheit": "$1\u00b0F",
    "celsius": "$1\u00b0C",
    "inches": "$1 in.",
    "centimeters": "$1 cm.",
    "less-than": "bajo $1",
    "and": and_function,
    "through": through_function,
    "with": "$1, con $2",
    "range": "$1\u2013$2",
    "parenthetical": "$1 ($2)",
    "for-hour": "$1 por la hora",
    "starting-in": "$1 comenzando en $2",
    "stopping-in": "$1 parando en $2",
    "starting-then-stopping-later": "$1 comenzando en $2, después parando en $3",
    "stopping-then-starting-later": "$1 parando en $2, comenzando de nuevo $3 después",
    "for-day": "$1 durante el día",
    "starting": "$1 comenzando $2",
    "until": "$1 hasta $2",
    "until-starting-again": "$1 hasta $2, comenzando otra vez $3",
    "starting-continuing-until": "$1 comenzando $2, continuando hasta $3",
    "during": "$1 $2",
    "for-week": "$1 durante la semana",
    "over-weekend": "$1 sobre el fin de semana",
    "temperatures-peaking": "temperaturas alcanzando un máximo de $1 $2",
    "temperatures-rising": "temperaturas llegando a $1 $2",
    "temperatures-valleying": "temperaturas alcanzando un mínimo de $1 $2",
    "temperatures-falling": "temperaturas cayendo a $1 $2",
    "title": title_function,
    "sentence": sentence_function,
    "next-hour-forecast-status": "los pronósticos para la próxima hora son $1 debido a $2",
    "unavailable": "no disponible",
    "temporarily-unavailable": "temporalmente no disponible",
    "partially-unavailable": "parcialmente no disponible",
    "station-offline": "todas las estaciones de radar cercanas están fuera de línea",
    "station-incomplete": "lagunas en la cobertura de las estaciones de radar cercanas",
    "smoke": "humo",
    "haze": "calima",
    "mist": "bruma",
}
