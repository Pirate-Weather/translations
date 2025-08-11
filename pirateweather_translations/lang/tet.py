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

    return a[:i] + a[i:] + joiner + b[i:]


def strip_prefix(period):
    if period.startswith("iha kalan"):
        return period[4:]
    elif period.startswith("iha "):
        return period[7:]
    return period


def and_function(stack, a, b):
    """
    Joins two strings using a specific joiner based on the presence of a comma in the first string.

    This function checks if the first string contains a comma. If it does, it uses the joiner ", ho ";
    otherwise, it uses " ho ". It then calls the `join_with_shared_prefix` function to join the two strings.

    Parameters:
    - a (str): The first string.
    - b (str): The second string.

    Returns:
    - str: The two strings joined using the appropriate joiner.
    """
    joiner = ", ho " if "," in a else " ho "
    return join_with_shared_prefix(a, b, joiner)


def through_function(stack, a, b):
    return join_with_shared_prefix(a, b, " to ")


def until_function(stack, condition, period):
    return condition + " to " + strip_prefix(period)


def until_starting_again_function(stack, condition, a, b):
    return condition + " to " + strip_prefix(a) + ", hahu fali " + b


def starting_continuing_until_function(stack, condition, a, b):
    return condition + " hahu " + a + ", kontinua to " + strip_prefix(b)


def title_function(stack, s):
    """
    Converts the first letter of each word in the input string to uppercase.

    This function capitalizes the first letter of each word in the input string. It uses regular expressions
    to identify word boundaries (spaces or dashes) and applies the capitalization to the first letter following
    those boundaries.

    Parameters:
    - s (str): The input string whose words' first letters are to be capitalized.

    Returns:
    - str: A new string with the first letter of each word capitalized.
    """
    return re.sub(r"(^|\s|-)\w", lambda match: match.group(0).upper(), s)


def sentence_function(stack, s):
    """
    Capitalize the first word of the sentence and end with a period.
    """
    s = s[0].upper() + s[1:]
    if not s.endswith("."):
        s += "."
    return s


template = {
    "clear": "pas",
    "no-precipitation": "udan la iha",
    "mixed-precipitation": "udan - maran kahur",
    "possible-very-light-precipitation": "karik udan uituan deit",
    "very-light-precipitation": "udan uituan",
    "possible-light-precipitation": "karik udan uituan",
    "light-precipitation": "udan uituan",
    "medium-precipitation": "udan",
    "heavy-precipitation": "udan bo'ot",
    "possible-very-light-rain": "karik udan uituan deit",
    "very-light-rain": "udan uituan deit",
    "possible-light-rain": "karik udan uituan",
    "light-rain": "udan uituan",
    "medium-rain": "udan",
    "heavy-rain": "udan bo'ot",
    "possible-very-light-sleet": "karik udan - salju kahur uituan deit",
    "very-light-sleet": "udan - salju kahur uituan deit",
    "possible-light-sleet": "karik udan - salju kahur uituan",
    "light-sleet": "udan - salju kahur uituan",
    "medium-sleet": "udan - salju kahur",
    "heavy-sleet": "udan - salju kahur bo'ot",
    "possible-very-light-snow": "karik salju uituan deit",
    "very-light-snow": "salju uituan deit",
    "possible-light-snow": "karik salju uituan",
    "light-snow": "salju uituan",
    "medium-snow": "salju",
    "heavy-snow": "salju bo'ot",
    "possible-thunderstorm": "karik rai-tarutu",
    "thunderstorm": "rai-tarutu",
    "possible-medium-precipitation": "karik udan",
    "possible-heavy-precipitation": "karik udan bo'ot",
    "possible-medium-rain": "karik udan",
    "possible-heavy-rain": "karik udan bo'ot",
    "possible-medium-sleet": "karik udan - salju kahur",
    "possible-heavy-sleet": "karik udan - salju kahur bo'ot",
    "possible-medium-snow": "karik salju",
    "possible-heavy-snow": "karik salju bo'ot",
    "possible-very-light-freezing-rain": "karik uituan malirin deit",
    "very-light-freezing-rain": "uituan malirin deit",
    "possible-light-freezing-rain": "karik udan malirin uituan",
    "light-freezing-rain": "udan malirin uituan",
    "possible-medium-freezing-rain": "karik udan malirin",
    "medium-freezing-rain": "udan malirin",
    "possible-heavy-freezing-rain": "karik udan malirin bo'ot",
    "heavy-freezing-rain": "udan malirin bo'ot",
    "possible-hail": "karik saudasaun",
    "hail": "saudasaun",
    "light-wind": "anin ki'ik",
    "medium-wind": "anin",
    "heavy-wind": "anin bo'ot",
    "low-humidity": "maran",
    "high-humidity": "bokon",
    "fog": "abu-abu taka rai",
    "very-light-clouds": "klaru liu",
    "light-clouds": "abu-abu uituan",
    "medium-clouds": "abu-abu",
    "heavy-clouds": "abu-abu taka loron",
    "today-morning": "ohin dader",
    "later-today-morning": "orsida ohin dader",
    "today-afternoon": "ohin lokraik",
    "later-today-afternoon": "orsida lokraik",
    "today-evening": "ohin kalan",
    "later-today-evening": "orsida kalan",
    "today-night": "ohin kalan bo'ot",
    "later-today-night": "orsida kalan bo'ot",
    "tomorrow-morning": "aban dader",
    "tomorrow-afternoon": "aban lokraik",
    "tomorrow-evening": "aban kalan",
    "tomorrow-night": "aban kalan bo'ot",
    "morning": "iha dader",
    "afternoon": "lokraik",
    "evening": "iha kalan",
    "night": "iha kalan bo'ot",
    "today": "ohin",
    "tomorrow": "aban",
    "sunday": "iha Domingu",
    "monday": "iha Segunda",
    "tuesday": "iha Tersa",
    "wednesday": "iha Kuarta",
    "thursday": "iha Kinta",
    "friday": "iha Sexta",
    "saturday": "iha Sabadu",
    "next-sunday": "iha Domingu",  # FIXME
    "next-monday": "iha Segunda",  # FIXME
    "next-tuesday": "iha Tersa",  # FIXME
    "next-wednesday": "iha Kuarta",  # FIXME
    "next-thursday": "iha Kinta",  # FIXME
    "next-friday": "iha Sexta",  # FIXME
    "next-saturday": "iha Sabadu",  # FIXME
    "minutes": "$1 min.",
    "fahrenheit": "$1\u00b0F",
    "celsius": "$1\u00b0C",
    "inches": "$1 in.",
    "centimeters": "$1 cm.",
    "less-than": "$1 mai kraik",
    "and": and_function,
    "through": through_function,
    "with": "$1, ho $2",
    "range": "$1\u2013$2",
    "parenthetical": "$1 ($2)",
    "for-hour": "$1 ba oras ida",
    "starting-in": "$1 hahu iha $2",
    "stopping-in": "$1 para iha $2",
    "starting-then-stopping-later": "$1 hahu iha $2, hein $3 para",
    "stopping-then-starting-later": "$1 para iha $2, hein $3 hahu fali",
    "for-day": "$1 loron tomak",
    "starting": "$1 hahu $2",
    "until": until_function,
    "until-starting-again": until_starting_again_function,
    "starting-continuing-until": starting_continuing_until_function,
    "during": "$1 $2",
    "for-week": "$1 durante semana ida",
    "over-weekend": "$1 durante Sabadu - Domingu",
    "temperatures-peaking": "temperatur la sai liu $1 $2",
    "temperatures-rising": "temperatur sai to $1 $2",
    "temperatures-valleying": "temperatur la tun liu $1 $2",
    "temperatures-falling": "temperatur tun to $1 $2",
    "title": title_function,
    "sentence": sentence_function,
    "next-hour-forecast-status": "previzaun oras tuir mai maka $1 tanba $2",
    "unavailable": "la disponivel",
    "temporarily-unavailable": "temporariamente la disponivel",
    "partially-unavailable": "parsialmente la disponivel",
    "station-offline": "estasaun radar sira ne'ebé besik hotu la iha liña",
    "station-incomplete": "lakuna sira iha kobertura hosi estasaun radar sira ne'ebé besik",
    "smoke": "ahi-suar",
    "haze": "rai-rahun",
    "mist": "kalohan",
}
