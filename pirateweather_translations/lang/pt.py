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
    "clear": "céu limpo",
    "no-precipitation": "sem precipitação",
    "mixed-precipitation": "aguaceiros mistos",
    "possible-very-light-precipitation": "possibilidade de aguaceiros muito fracos",
    "very-light-precipitation": "aguaceiros muito fracos",
    "possible-light-precipitation": "possibilidade de aguaceiros fracos",
    "light-precipitation": "aguaceiros fracos",
    "medium-precipitation": "aguaceiros",
    "heavy-precipitation": "aguaceiros fortes",
    "possible-very-light-rain": "possibilidade de chuviscos",
    "very-light-rain": "chuviscos",
    "possible-light-rain": "possibilidade de chuva fraca",
    "light-rain": "chuva fraca",
    "medium-rain": "chuva",
    "heavy-rain": "chuva forte",
    "possible-very-light-sleet": "possibilidade de chuva congelada (chuva e neve) muito fraca",
    "very-light-sleet": "chuva congelada (chuva e neve) muito fraca",
    "possible-light-sleet": "possibilidade de chuva congelada (chuva e neve) fraca",
    "light-sleet": "chuva congelada (chuva e neve) fraca",
    "medium-sleet": "chuva congelada (chuva e neve)",
    "heavy-sleet": "chuva congelada (chuva e neve) forte",
    "possible-very-light-snow": "possibilidade de neve muito fraca",
    "very-light-snow": "neve muito fraca",
    "possible-light-snow": "possibilidade de neve fraca",
    "light-snow": "neve fraca",
    "medium-snow": "neve",
    "heavy-snow": "neve forte",
    "possible-thunderstorm": "possibilidade de trovoada",
    "thunderstorm": "trovoada",
    "possible-medium-precipitation": "possibilidade de aguaceiros",
    "possible-heavy-precipitation": "possibilidade de aguaceiros fortes",
    "possible-medium-rain": "possibilidade de chuva",
    "possible-heavy-rain": "possibilidade de chuva forte",
    "possible-medium-sleet": "possibilidade de chuva congelada (chuva e neve)",
    "possible-heavy-sleet": "possibilidade de chuva congelada (chuva e neve) forte",
    "possible-medium-snow": "possibilidade de neve",
    "possible-heavy-snow": "possibilidade de neve forte",
    "possible-very-light-freezing-rain": "possibilidade de chuvisco congelante",
    "very-light-freezing-rain": "chuvisco congelante",
    "possible-light-freezing-rain": "possibilidade de chuva congelante fraca",
    "light-freezing-rain": "chuva congelante fraca",
    "possible-medium-freezing-rain": "possibilidade de chuva congelante",
    "medium-freezing-rain": "chuva congelante",
    "possible-heavy-freezing-rain": "possibilidade de chuva congelante forte",
    "heavy-freezing-rain": "chuva congelante forte",
    "possible-hail": "possibilidade de granizo",
    "hail": "granizo",
    "light-wind": "vento fraco",
    "medium-wind": "vento moderado",
    "heavy-wind": "vento forte",
    "low-humidity": "tempo seco",
    "high-humidity": "tempo [h]úmido",
    "fog": "nevoeiro",
    "very-light-clouds": "céu quase limpo",
    "light-clouds": "céu pouco nublado",
    "medium-clouds": "céu nublado",
    "heavy-clouds": "céu encoberto",
    "today-morning": "hoje de manhã",
    "later-today-morning": "hoje ao final da manhã",
    "today-afternoon": "hoje à tarde",
    "later-today-afternoon": "hoje ao final da tarde",
    "today-evening": "hoje à noite",
    "later-today-evening": "hoje ao final da noite",
    "today-night": "amanhã de madrugada",
    "later-today-night": "ao final da madrugada",
    "tomorrow-morning": "amanhã de manhã",
    "tomorrow-afternoon": "amanhã à tarde",
    "tomorrow-evening": "amanhã à noite",
    "tomorrow-night": "amanhã ao final da noite",
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
    "fahrenheit": "$1 °F",
    "celsius": "$1 °C",
    "inches": "$1 pol",
    "centimeters": "$1 cm",
    "less-than": "menos de $1",
    "and": and_function,
    "through": through_function,
    "with": "$1, com $2",
    "range": "$1–$2",
    "parenthetical": "$1 ($2)",
    "for-hour": "$1 na próxima hora",
    "starting-in": "$1 começando em $2",
    "stopping-in": "$1 terminando em $2",
    "starting-then-stopping-later": "$1 começando de $2, terminando ao fim da $3",
    "stopping-then-starting-later": "$1 terminando em $2 e recomeçando em $3",
    "for-day": "$1 até ao fim do dia",
    "starting": "$1 começando de $2",
    "until": "$1 até à $2",
    "until-starting-again": "$1 até à $2, recomeçando de $3",
    "starting-continuing-until": "$1 começando de $2, continuando até de $3",
    "during": "$1 durante $2",
    "for-week": "$1 durante a semana",
    "over-weekend": "$1 durante o fim de semana",
    "temperatures-peaking": "temperatura máxima de $1, $2",
    "temperatures-rising": "subida de temperatura até aos $1, até $2",
    "temperatures-valleying": "descida de temperatura até aos $1, até $2",
    "temperatures-falling": "temperatura mínima de $1, $2",
    "title": title_function,
    "sentence": sentence_function,
    "next-hour-forecast-status": "previsão para a próxima hora $1: $2",
    "unavailable": "indisponível",
    "temporarily-unavailable": "temporariamente indisponível",
    "partially-unavailable": "parcialmente indisponível",
    "station-offline": "dados indisponíveis",
    "station-incomplete": "dados incompletos",
    "smoke": "fumo",
    "haze": "névoa seca",
    "mist": "neblina",
}
