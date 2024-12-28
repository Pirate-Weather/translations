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

    return a[:i] + a[i:] + joiner + b[i:]


def and_function(stack, a, b):
    return join_with_shared_prefix(a, b, " și " if "," in a else " și ")


def through_function(stack, a, b):
    return join_with_shared_prefix("de " + a, b, " până ")


def parenthetical_function(stack, a, b):
    """
    Formats a string with a parenthetical note, with a special case for 'precipitații mixte'.

    Args:
        a (str): The main string.
        b (str): The parenthetical note.

    Returns:
        str: The formatted string.
    """
    return f"{a} ({b}{' de zăpadă)' if a == 'precipitații mixte' else ')'}"


def minutes_function(stack, time):
    """
    Converts minutes into Romanian text format.

    Args:
        min_value (int): The number of minutes.

    Returns:
        str: The formatted minutes string in Romanian.
    """
    min_value = int(time)

    if min_value < 2:
        return "1 minut"
    if min_value < 20:
        return f"{time} minute"
    return f"{time} de minute"


def title_function(stack, s):
    """
    Capitalizes the first letter of every word in the string, except for specific words or patterns.

    Args:
        string (str): The input string.

    Returns:
        str: The transformed string with appropriate capitalization.
    """

    def capitalize_word(word):
        if word in ["și", "de"] or re.search(r"in\.", word) or re.search(r"cm\.", word):
            return word
        return word[0].upper() + word[1:]

    return re.sub(r"\S+", lambda match: capitalize_word(match.group()), s)


def sentence_function(stack, s):
    s = s[0].upper() + s[1:]
    if not s.endswith("."):
        s += "."
    return s


template = {
    "clear": "senin",
    "no-precipitation": "fără precipitații",
    "mixed-precipitation": "precipitații mixte",
    "possible-very-light-precipitation": "posibile precipitații foarte slabe",
    "very-light-precipitation": "precipitații foarte slabe",
    "possible-light-precipitation": "posibile precipitații slabe",
    "light-precipitation": "precipitații slabe",
    "medium-precipitation": "precipitații",
    "heavy-precipitation": "precipitații abundente",
    "possible-very-light-rain": "posibil burniță",
    "very-light-rain": "burniță",
    "possible-light-rain": "posibil ploaie ușoară",
    "light-rain": "ploaie ușoară",
    "medium-rain": "ploaie",
    "heavy-rain": "ploaie torențială",
    "possible-very-light-sleet": "posibil lapoviță",
    "very-light-sleet": "lapoviță",
    "possible-light-sleet": "posibil lapoviță",
    "light-sleet": "lapoviță",
    "medium-sleet": "lapoviță",
    "heavy-sleet": "lapoviță și ninsoare",
    "possible-very-light-snow": "posibil ninsoare slabă",
    "very-light-snow": "ninsoare slabă",
    "possible-light-snow": "posibil ninsoare slabă",
    "light-snow": "ninsoare slabă",
    "medium-snow": "ninsoare",
    "heavy-snow": "ninsoare puternică",
    "possible-thunderstorm": "posibil furtună",
    "thunderstorm": "furtună",
    "possible-medium-precipitation": "possible precipitation",
    "possible-heavy-precipitation": "possible heavy precipitation",
    "possible-medium-rain": "possible rain",
    "possible-heavy-rain": "possible heavy rain",
    "possible-medium-sleet": "possible sleet",
    "possible-heavy-sleet": "possible heavy sleet",
    "possible-medium-snow": "possible snow",
    "possible-heavy-snow": "possible heavy snow",
    "possible-freezing-drizzle": "possible freezing drizzle",
    "freezing-drizzle": "freezing drizzle",
    "possible-light-freezing-rain": "possible light freezing rain",
    "light-freezing-rain": "light freezing rain",
    "possible-freezing-rain": "possible freezing rain",
    "freezing-rain": "freezing rain",
    "possible-heavy-freezing-rain": "possible heavy freezing rain",
    "heavy-freezing-rain": "heavy freezing rain",
    "possible-hail": "possible hail",
    "hail": "hail",
    "light-wind": "vânt ușor",
    "medium-wind": "bate vântul",
    "heavy-wind": "vânt puternic",
    "low-humidity": "umiditate scăzută",
    "high-humidity": "umiditate ridicată",
    "fog": "ceață",
    "very-light-clouds": "predominant senin",
    "light-clouds": "parțial noros",
    "medium-clouds": "predominant noros",
    "heavy-clouds": "noros",
    "today-morning": "dimineață",
    "later-today-morning": "mai târziu în această dimineață",
    "today-afternoon": "după-amiază",
    "later-today-afternoon": "mai târziu în această după-amiază",
    "today-evening": "diseară",
    "later-today-evening": "mai târziu în această seară",
    "today-night": "la noapte",
    "later-today-night": "la noapte",
    "tomorrow-morning": "mâine dimineață",
    "tomorrow-afternoon": "maine după-amiază",
    "tomorrow-evening": "mâine seară",
    "tomorrow-night": "mâine noapte",
    "morning": "dimineață",
    "afternoon": "după-masă",
    "evening": "seara",
    "night": "la noapte",
    "today": "azi",
    "tomorrow": "mâine",
    "sunday": "duminică",
    "monday": "luni",
    "tuesday": "marți",
    "wednesday": "miercuri",
    "thursday": "joi",
    "friday": "vineri",
    "saturday": "sâmbătă",
    "next-sunday": "duminica viitoare",
    "next-monday": "lunea viitoare",
    "next-tuesday": "marțea viitoare",
    "next-wednesday": "miercurea viitoare",
    "next-thursday": "joia viitoare",
    "next-friday": "vinerea viitoare",
    "next-saturday": "sâmbăta viitoare",
    "minutes": minutes_function,
    "fahrenheit": "$1\u00b0F",
    "celsius": "$1\u00b0C",
    "inches": "$1 in.",
    "centimeters": "$1 cm.",
    "less-than": "mai puțin de $1",
    "and": and_function,
    "through": through_function,
    "with": "$1, cu $2",
    "range": "$1\u2013$2",
    "parenthetical": parenthetical_function,
    "for-hour": "$1 în următoarea oră",
    "starting-in": "$1, în $2",
    "stopping-in": "$1, durează $2",
    "starting-then-stopping-later": "$1 peste $2, durează $3",
    "stopping-then-starting-later": "$1, se oprește în $2, începe din nou $3 mai târziu",
    "for-day": "$1 de-a lungul zilei",
    "starting": "$1, începând de $2",
    "until": "$1 până $2",
    "until-starting-again": "$1 până $2, începe din nou $3",
    "starting-continuing-until": "$1 începând de $2 și până $3",
    "during": "$1 $2",
    "for-week": "$1 pe toată durata săptămânii",
    "over-weekend": "$1 în weekend",
    "temperatures-peaking": "temperaturi ce ating un maxim de $1 $2",
    "temperatures-rising": "temperaturi ce urcă până la $1 $2",
    "temperatures-valleying": "temperaturi ce ating un minim de $1 $2",
    "temperatures-falling": "temperaturi ce coboară până la $1 $2",
    "title": title_function,
    "sentence": sentence_function,
    "next-hour-forecast-status": "next hour forecasts are $1 due to $2",
    "unavailable": "unavailable",
    "temporarily-unavailable": "temporarily unavailable",
    "partially-unavailable": "partially unavailable",
    "station-offline": "all nearby radar stations being offline",
    "station-incomplete": "gaps in coverage from nearby radar stations",
}
