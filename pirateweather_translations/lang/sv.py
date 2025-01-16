import re


def join_with_shared_prefix(a, b, joiner):
    """
    Joins two strings (`a` and `b`) using a shared prefix with a specified joiner.

    This function compares the characters of `a` and `b` from the start, finding the longest common prefix
    and then joins them with a specified joiner.

    Parameters:
    - a (str): The first string to join.
    - b (str): The second string to join.
    - joiner (str): The string used to join the two strings.

    Returns:
    - str: The two strings joined together using the common prefix and the joiner.
    """

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


def strip_prefix(period):
    if period.startswith("över natten"):
        return period[5:]
    elif period.startswith("under "):
        return period[6:]
    return period


def grammar(input_str):
    """
    This function modifies a given string by replacing specific patterns:
    - Replaces "på " (case insensitive) with "under ".
    - Replaces specific suffixes followed by "dag" with the correct form (e.g., "ån" becomes "ånden").

    Parameters:
    - input_str (str): The input string to be modified.

    Returns:
    - str: The modified string after applying the replacements.
    """
    # Replace "på " with "under " (case insensitive)
    result = re.sub(r"på ", "under ", input_str, flags=re.IGNORECASE)

    # Replace suffixes (ån, is, ns, rs, re, ör, ön) followed by "dag" with the correct form (e.g., "ån" becomes "ånden")
    result = re.sub(
        r"(ån|is|ns|rs|re|ör|ön)(dag)", r"\1dagen", result, flags=re.IGNORECASE
    )

    return result


def and_function(stack, a, b):
    """
    Joins two strings (`a` and `b`) with a shared prefix, using 'och' as the joiner.

    If the string `a` contains a comma, it uses ' och ' as the joiner. Otherwise, it uses ' och ' (same in this case, but for illustration).

    Parameters:
    - a (str): The first string to join.
    - b (str): The second string to join.

    Returns:
    - str: The two strings joined together with the appropriate joiner.
    """
    # Determine the joiner based on whether a contains a comma
    joiner = " och " if "," in a else " och "

    # Use the join_with_shared_prefix function to join the two strings
    return join_with_shared_prefix(a, b, joiner)


def through_function(stack, a, b):
    return join_with_shared_prefix(a, b, " fram till ")


def until_function(stack, condition, period):
    return condition + " fram till " + strip_prefix(period)


def until_starting_again_function(stack, condition, a, b):
    return condition + " fram till " + strip_prefix(a) + ", som startar igen " + b


def starting_continuing_until_function(stack, condition, a, b):
    return condition + " som startar " + a + ", fortsätter fram till " + strip_prefix(b)


def temperatures_peaking_function(stack, temp, at):
    return "temperaturer upp till " + temp + " " + grammar(at)


def temperatures_rising_function(stack, temp, at):
    return "temperaturer som stiger till " + temp + " " + grammar(at)


def temperatures_valleying_function(stack, temp, at):
    return "temperaturer som stannar på " + temp + " " + grammar(at)


def temperatures_falling_function(stack, temp, at):
    return "temperaturer som sjunker till " + temp + " " + grammar(at)


def title_function(stack, s):
    """
    Capitalize the first letter of every word.
    """
    return s[0].upper() + s[1:]


def sentence_function(stack, s):
    """
    Capitalize the first word of the sentence and end with a period.
    """
    s = s[0].upper() + s[1:]
    if not s.endswith("."):
        s += "."
    return s


template = {
    "clear": "klart",
    "no-precipitation": "ingen mätbar nederbörd",
    "mixed-precipitation": "blandad nederbörd",
    "possible-very-light-precipitation": "möjligtvis mycket lätt nederbörd",
    "very-light-precipitation": "mycket lätt nederbörd",
    "possible-light-precipitation": "möjligtvis lätt nederbörd",
    "light-precipitation": "lätt nederbörd",
    "medium-precipitation": "nederbörd",
    "heavy-precipitation": "kraftigt nederbörd",
    "possible-very-light-rain": "möjligtvis lite duggregn",
    "very-light-rain": "duggregn",
    "possible-light-rain": "möjligtvis lätta regnskurar",
    "light-rain": "regnskurar",
    "medium-rain": "regn",
    "heavy-rain": "skyfall",
    "possible-very-light-sleet": "möjligtvis mycket lätt snöblandat regn",
    "very-light-sleet": "mycket lätt snöblandat regn",
    "possible-light-sleet": "möjligtvis lätt snöblandat regn",
    "light-sleet": "lätt snöblandat regn",
    "medium-sleet": "snöblandat regn",
    "heavy-sleet": "tungt snöblandat regn",
    "possible-very-light-snow": "möjligtvis lätt snöby",
    "very-light-snow": "lätt snöby",
    "possible-light-snow": "möjligtvis lätt snöfall",
    "light-snow": "lätt snöfall",
    "medium-snow": "snöby",
    "heavy-snow": "rikligt med snö",
    "possible-thunderstorm": "risk för åska",
    "thunderstorm": "åska",
    "possible-medium-precipitation": "möjligtvis lätt nederbörd",
    "possible-heavy-precipitation": "möjligtvis lätt kraftigt nederbörd",
    "possible-medium-rain": "möjligtvis regn",
    "possible-heavy-rain": "möjligtvis skyfall",
    "possible-medium-sleet": "möjligtvis snöblandat regn",
    "possible-heavy-sleet": "möjligtvis tungt snöblandat regn",
    "possible-medium-snow": "möjligtvis snöby",
    "possible-heavy-snow": "möjligtvis rikligt med snö",
    "possible-very-light-freezing-rain": "möjligtvis lätta underkylt regnskurar",
    "very-light-freezing-rain": "underkylt regnskurar",
    "possible-light-freezing-rain": "möjligtvis lätta underkylt regn",
    "light-freezing-rain": "lätt underkylt regn",
    "possible-medium-freezing-rain": "möjligtvis underkylt regn",
    "medium-freezing-rain": "underkylt regn",
    "possible-heavy-freezing-rain": "möjligtvis kraftigt underkylt regn",
    "heavy-freezing-rain": "kraftigt underkylt regn",
    "possible-hail": "möjligtvis hagel",
    "hail": "hagel",
    "light-wind": "måttlig vind",
    "medium-wind": "hård vind",
    "heavy-wind": "storm",
    "low-humidity": "torka",
    "high-humidity": "fuktigt",
    "fog": "dimma",
    "very-light-clouds": "mestadels klart",
    "light-clouds": "lätt molnighet",
    "medium-clouds": "molnigt",
    "heavy-clouds": "mulet",
    "today-morning": "under morgonen",
    "later-today-morning": "senare under morgonen",
    "today-afternoon": "på eftermiddagen",
    "later-today-afternoon": "senare under eftermiddagen",
    "today-evening": "under kvällen",
    "later-today-evening": "senare under kvällen",
    "today-night": "ikväll",
    "later-today-night": "senare ikväll",
    "tomorrow-morning": "imorgon bitti",
    "tomorrow-afternoon": "imorgon eftermiddag",
    "tomorrow-evening": "imorgon kväll",
    "tomorrow-night": "imorgon natt",
    "morning": "på morgonen",
    "afternoon": "under eftermiddagen",
    "evening": "under kvällen",
    "night": "över natten",
    "today": "idag",
    "tomorrow": "imorgon",
    "sunday": "på söndag",
    "monday": "på måndag",
    "tuesday": "på tisdag",
    "wednesday": "på onsdag",
    "thursday": "på torsdag",
    "friday": "på fredag",
    "saturday": "på lördag",
    "next-sunday": "nästa söndag",
    "next-monday": "nästa måndag",
    "next-tuesday": "nästa tisdag",
    "next-wednesday": "nästa onsdag",
    "next-thursday": "nästa torsdag",
    "next-friday": "nästa fredag",
    "next-saturday": "nästa lördag",
    "minutes": "$1 min.",
    "fahrenheit": "$1\u00b0F",
    "celsius": "$1\u00b0C",
    "inches": "$1 in.",
    "centimeters": "$1 cm.",
    "less-than": "under $1",
    "and": and_function,
    "through": through_function,
    "with": "$1, med $2",
    "range": "$1\u2013$2",
    "parenthetical": "$1 ($2)",
    "for-hour": "$1 under närmaste timme",
    "starting-in": "$1 som startar om $2",
    "stopping-in": "$1 som avtar om $2",
    "starting-then-stopping-later": "$1 som startar om $2, avtar $3 senare",
    "stopping-then-starting-later": "$1 avtar om $2, startar igen $3 senare",
    "for-day": "$1 under dagen",
    "starting": "$1 som startar $2",
    "until": until_function,
    "until-starting-again": until_starting_again_function,
    "starting-continuing-until": starting_continuing_until_function,
    "during": "$1 $2",
    "for-week": "$1 under veckan",
    "over-weekend": "$1 över helgen",
    "temperatures-peaking": temperatures_peaking_function,
    "temperatures-rising": temperatures_rising_function,
    "temperatures-valleying": temperatures_valleying_function,
    "temperatures-falling": temperatures_falling_function,
    "title": title_function,
    "sentence": sentence_function,
    "next-hour-forecast-status": "next hour forecasts are $1 due to $2",
    "unavailable": "unavailable",
    "temporarily-unavailable": "temporarily unavailable",
    "partially-unavailable": "partially unavailable",
    "station-offline": "all nearby radar stations being offline",
    "station-incomplete": "gaps in coverage from nearby radar stations",
}
