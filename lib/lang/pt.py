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
    return join_with_shared_prefix(a, b, ", e " if "," in a else " e ")


def through_function(stack, a, b):
    return join_with_shared_prefix(a, b, " durante ")


def title_function(stack, s):
    """
    Capitalizes the first letter of every word in the string, except for the word 'e'.

    Args:
        s (str): The input string.

    Returns:
        str: The transformed string with appropriate capitalization.
    """

    def capitalize_word(word):
        return word if word == "e" else word[0].upper() + word[1:]

    return re.sub(r"\S+", lambda match: capitalize_word(match.group()), s)


def sentence_function(stack, s):
    s = s[0].upper() + s[1:]
    if not s.endswith("."):
        s += "."
    return s


template = {
    "clear": "limpo",
    "no-precipitation": "sem aguaceiros",
    "mixed-precipitation": "aguaceiros variados",
    "possible-very-light-precipitation": "possíveis aguaceiros muito fracos",
    "very-light-precipitation": "aguaceiros muito fracos",
    "possible-light-precipitation": "possíveis aguaceiros fracos",
    "light-precipitation": "aguaceiros fracos",
    "medium-precipitation": "aguaceiros",
    "heavy-precipitation": "aguaceiros fortes",
    "possible-very-light-rain": "possíveis chuviscos",
    "very-light-rain": "chuviscos",
    "possible-light-rain": "possível chuva fraca",
    "light-rain": "chuva fraca",
    "medium-rain": "chuva",
    "heavy-rain": "chuva forte",
    "possible-very-light-sleet": "possível granizo muito fraco",
    "very-light-sleet": "granizo muito fraco",
    "possible-light-sleet": "possível granizo fraco",
    "light-sleet": "granizo fraco",
    "medium-sleet": "granizo",
    "heavy-sleet": "granizo forte",
    "possible-very-light-snow": "possível neve muito fraca",
    "very-light-snow": "neve muito fraca",
    "possible-light-snow": "possível neve fraca",
    "light-snow": "neve fraca",
    "medium-snow": "neve",
    "heavy-snow": "neve forte",
    "possible-thunderstorm": "tempestades possíveis",
    "thunderstorm": "tempestade",
    "possible-medium-precipitation": "possíveis aguaceiros",
    "possible-heavy-precipitation": "possíveis aguaceiros fortes",
    "possible-medium-rain": "possível chuva",
    "possible-heavy-rain": "possível chuva forte",
    "possible-medium-sleet": "possível granizo",
    "possible-heavy-sleet": "possível granizo forte",
    "possible-medium-snow": "possível neve",
    "possible-heavy-snow": "possível neve forte",
    "possible-very-light-freezing-rain": "possíveis chuvisco congelante",
    "very-light-freezing-rain": "chuvisco congelante",
    "possible-light-freezing-rain": "possíveis chuva fraca e congelante",
    "light-freezing-rain": "chuva fraca e congelante",
    "possible-medium-freezing-rain": "possível chuva congelante",
    "medium-freezing-rain": "chuva congelante",
    "possible-heavy-freezing-rain": "possível chuva forte e gelada",
    "heavy-freezing-rain": "chuva forte e gelada",
    "possible-hail": "possíveis granizo",
    "hail": "saraiva",
    "light-wind": "vento fraco",
    "medium-wind": "vento",
    "heavy-wind": "vento forte",
    "low-humidity": "seco",
    "high-humidity": "úmido",
    "fog": "nevoeiro",
    "very-light-clouds": "principalmente claro",
    "light-clouds": "ligeiramente nublado",
    "medium-clouds": "nublado",
    "heavy-clouds": "muito nublado",
    "today-morning": "hoje de manhã",
    "later-today-morning": "manhã de hoje",
    "today-afternoon": "hoje à tarde",
    "later-today-afternoon": "tarde de hoje",
    "today-evening": "hoje à noite",
    "later-today-evening": "noite de hoje",
    "today-night": "hoje de madrugada",
    "later-today-night": "de madrugada",
    "tomorrow-morning": "amanhã de manhã",
    "tomorrow-afternoon": "amanhã à tarde",
    "tomorrow-evening": "amanhã à noite",
    "tomorrow-night": "amanhã de madrugada",
    "morning": "manhã",
    "afternoon": "tarde",
    "evening": "noite",
    "night": "madrugada",
    "today": "hoje",
    "tomorrow": "amanhã",
    "sunday": "domingo",
    "monday": "segunda-feira",
    "tuesday": "terça-feira",
    "wednesday": "quarta-feira",
    "thursday": "quinta-feira",
    "friday": "sexta-feira",
    "saturday": "sábado",
    "next-sunday": "próximo domingo",
    "next-monday": "próxima segunda-feira",
    "next-tuesday": "próxima terça-feira",
    "next-wednesday": "próxima quarta-feira",
    "next-thursday": "próxima quinta-feira",
    "next-friday": "próxima sexta-feira",
    "next-saturday": "próximo sábado",
    "minutes": "$1 min",
    "fahrenheit": "$1\u00b0F",
    "celsius": "$1\u00b0C",
    "inches": "$1 in.",
    "centimeters": "$1 cm.",
    "less-than": "menos de $1",
    "and": and_function,
    "through": through_function,
    "with": "$1, com $2",
    "range": "$1\u2013$2",
    "parenthetical": "$1 ($2)",
    "for-hour": "$1 na próxima hora",
    "starting-in": "$1 dentro de $2",
    "stopping-in": "$1 termina daqui a $2",
    "starting-then-stopping-later": "$1 dentro de $2, termina $3 mais tarde",
    "stopping-then-starting-later": "$1 termina dentro de $2, recomeça $3 mais tarde",
    "for-day": "$1 durante todo o dia",
    "starting": "$1 começa durante a $2",
    "until": "$1 até $2",
    "until-starting-again": "$1 até $2, recomeça $3",
    "starting-continuing-until": "$1 começa esta $2, continua até à $3",
    "during": "$1 durante $2",
    "for-week": "$1 durante toda a semana",
    "over-weekend": "$1 durante todo o fim de semana",
    "temperatures-peaking": "as temperaturas a chegar a um máximo de $1 $2",
    "temperatures-rising": "as temperaturas a subir aos $1 $2",
    "temperatures-valleying": "as temperaturas a descer até $1 $2",
    "temperatures-falling": "as temperaturas a descer até um minimo de $1 $2",
    "title": title_function,
    "sentence": sentence_function,
    "next-hour-forecast-status": "next hour forecasts are $1 due to $2",
    "unavailable": "unavailable",
    "temporarily-unavailable": "temporarily unavailable",
    "partially-unavailable": "partially unavailable",
    "station-offline": "all nearby radar stations being offline",
    "station-incomplete": "gaps in coverage from nearby radar stations",
}
