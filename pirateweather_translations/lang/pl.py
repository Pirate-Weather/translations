def join_with_shared_prefix(a, b, joiner):
    """
    Joins two strings with a shared prefix and an appropriate joiner.

    Args:
        a (str): The first string.
        b (str): The second string.
        joiner (str): The string used to join `a` and `b`.

    Returns:
        str: The combined string with the shared prefix.
    """
    m = a
    n = b
    i = 0

    # Handle special cases for "we wtorek"
    if m == "we wtorek":
        m = "w wtorek"
    if n == "we wtorek":
        n = "w wtorek"

    # Find the shared prefix
    while i < len(m) and i < len(n) and ord(m[i]) == ord(n[i]):
        i += 1

    # Adjust index to avoid breaking words
    while i > 0 and ord(m[i - 1]) != 32:
        i -= 1

    # Handle edge case for "we wtorek"
    if i == 2 and b == "we wtorek":
        i = 3

    return a + joiner + b[i:]


def genitive_form(word):
    """
    Converts a word to its genitive form based on specific cases.

    Args:
        word (str): The word to convert.

    Returns:
        str: The genitive form of the word if it matches a specific case, otherwise returns the input.
    """
    genitive_cases = {
        "jutro": "jutra",
        "w poniedziałek": "poniedziałku",
        "we wtorek": "wtorku",
        "w środę": "środy",
        "w czwartek": "czwartku",
        "w piątek": "piątku",
        "w sobotę": "soboty",
        "w niedzielę": "niedzieli",
        "w przyszły poniedziałek": "przyszłego poniedziałku",
        "w przyszły wtorek": "przyszłego wtorku",
        "w przyszłą środę": "przyszłej środy",
        "w przyszły czwartek": "przyszłego czwartku",
        "w przyszły piątek": "przyszłego piątku",
        "w przyszłą sobotę": "przyszłej soboty",
        "w przyszłą niedzielę": "przyszłej niedzieli",
    }
    return genitive_cases.get(word, word)


def and_function(stack, a, b):
    """
    Joins two strings with a shared prefix.

    Args:
        a (str): The first string.
        b (str): The second string.

    Returns:
        str: The joined string.
    """
    times = [
        "w poniedziałek",
        "we wtorek",
        "w środę",
        "w czwartek",
        "w piątek",
        "w sobotę",
        "w niedzielę",
        "rano",
        "po południu",
        "wieczorem",
        "nocą",
        "przed południem",
        "późnym popołudniem",
        "późnym wieczorem",
        "późno w nocy",
        "dzisiaj",
        "jutro",
        "jutro rano",
        "jutro po południu",
        "jutro wieczorem",
        "w przyszły poniedziałek",
        "w przyszły wtorek",
        "w przyszłą środę",
        "w przyszły czwartek",
        "w przyszły piątek",
        "w przyszłą sobotę",
        "w przyszłą niedzielę",
    ]
    joiner = " i " if "," not in a and a in times and b in times else ", "
    return join_with_shared_prefix(a, b, joiner)


def through_function(stack, a, b):
    return "od " + genitive_form(a) + " do " + genitive_form(b)


def parenthetical_function(stack, a, b):
    """
    Constructs a parenthetical statement.

    Args:
        a (str): The main statement.
        b (str): The additional detail.

    Returns:
        str: The constructed parenthetical statement.
    """
    return a + " (" + b + (" śniegu)" if a == "przelotne opady" else ")")


def until_function(stack, condition, period):
    """
    Constructs a sentence indicating when a condition will stop.

    Args:
        condition (str): The condition being described.
        period (str): The period when the condition will stop.

    Returns:
        str: The constructed sentence.
    """
    lstr = ", ustaną " if "opady" in condition else ", ustanie "
    return condition + lstr + period


def until_starting_again_function(stack, condition, a, b):
    """
    Constructs a sentence indicating when a condition will stop and start again.

    Args:
        condition (str): The condition being described.
        a (str): The period when the condition stops.
        b (str): The period when the condition starts again.

    Returns:
        str: The constructed sentence.
    """
    lstr = ", ustaną " if "opady" in condition else ", ustanie "
    return condition + lstr + a + ", " + b + " ponownie " + condition


def starting_continuing_until_function(stack, condition, a, b):
    """
    Constructs a string describing a condition starting at `a` and continuing until `b`.

    Args:
        condition (str): The condition being described.
        a (str): The starting point.
        b (str): The ending point.

    Returns:
        str: The constructed sentence.
    """
    lstr = ", skończą się" if "opady" in condition else ", skończy się"
    return f"{a} {condition}{lstr} {b}"


def title_function(stack, s):
    """
    Capitalize the first letter of every word is not adequate for this module
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
    "clear": "bezchmurnie",
    "no-precipitation": "brak opadów",
    "mixed-precipitation": "przelotne opady",
    "possible-very-light-precipitation": "możliwe słabe opady",
    "very-light-precipitation": "słabe opady",
    "possible-light-precipitation": "możliwe niewielkie opady",
    "light-precipitation": "niewielkie opady",
    "medium-precipitation": "opady",
    "heavy-precipitation": "silne opady",
    "possible-very-light-rain": "możliwa mżawka",
    "very-light-rain": "mżawka",
    "possible-light-rain": "możliwy niewielki deszcz",
    "light-rain": "niewielki deszcz",
    "medium-rain": "deszcz",
    "heavy-rain": "ulewa",
    "possible-very-light-sleet": "możliwe słabe opady deszczu ze śniegiem",
    "very-light-sleet": "słabe opady deszczu ze śniegiem",
    "possible-light-sleet": "możliwe niewielkie opady deszczu ze śniegiem",
    "light-sleet": "niewielkie opady deszczu ze śniegiem",
    "medium-sleet": "deszcz ze śniegiem",
    "heavy-sleet": "deszcz ze śniegiem",
    "possible-very-light-snow": "możliwy drobny śnieg",
    "very-light-snow": "drobny śnieg",
    "possible-light-snow": "możliwy niewielki śnieg",
    "light-snow": "niewielki śnieg",
    "medium-snow": "śnieg",
    "heavy-snow": "śnieżyca",
    "possible-thunderstorm": "możliwa burza",
    "thunderstorm": "burza",
    "possible-medium-precipitation": "możliwe opady",
    "possible-heavy-precipitation": "możliwe silne opady",
    "possible-medium-rain": "możliwy deszcz",
    "possible-heavy-rain": "możliwa ulewa",
    "possible-medium-sleet": "możliwy deszcz ze śniegiem",
    "possible-heavy-sleet": "możliwy silny deszcz ze śniegiem",
    "possible-medium-snow": "możliwy śnieg",
    "possible-heavy-snow": "możliwy śnieżyca",
    "possible-very-light-freezing-rain": "możliwa marznąca mżawka",
    "very-light-freezing-rain": "marznąca mżawka",
    "possible-light-freezing-rain": "możliwy niewielki marznący deszcz",
    "light-freezing-rain": "niewielki marznący deszcz",
    "possible-medium-freezing-rain": "możliwy marznący deszcz",
    "medium-freezing-rain": "marznący deszcz",
    "possible-heavy-freezing-rain": "możliwy ulewny marznący deszcz",
    "heavy-freezing-rain": "ulewny marznący deszcz",
    "possible-hail": "możliwy grad",
    "hail": "grad",
    "light-wind": "słaby wiatr",
    "medium-wind": "umiarkowany wiatr",
    "heavy-wind": "silny wiatr",
    "low-humidity": "niska wilgotność",
    "high-humidity": "duża wilgotność",
    "fog": "mgła",
    "very-light-clouds": "przeważnie bezchmurnie",
    "light-clouds": "niewielkie zachmurzenie",
    "medium-clouds": "średnie zachmurzenie",
    "heavy-clouds": "duże zachmurzenie",
    "today-morning": "rano",
    "later-today-morning": "przed południem",
    "today-afternoon": "po południu",
    "later-today-afternoon": "późnym popołudniem",
    "today-evening": "wieczorem",
    "later-today-evening": "późnym wieczorem",
    "today-night": "nocą",
    "later-today-night": "późno w nocy",
    "tomorrow-morning": "jutro rano",
    "tomorrow-afternoon": "jutro po południu",
    "tomorrow-evening": "jutro wieczorem",
    "tomorrow-night": "jutro w nocy",
    "morning": "rano",
    "afternoon": "po południu",
    "evening": "wieczorem",
    "night": "nocą",
    "today": "dzisiaj",
    "tomorrow": "jutro",
    "sunday": "w niedzielę",
    "monday": "w poniedziałek",
    "tuesday": "we wtorek",
    "wednesday": "w środę",
    "thursday": "w czwartek",
    "friday": "w piątek",
    "saturday": "w sobotę",
    "next-sunday": "w przyszłą niedzielę",
    "next-monday": "w przyszły poniedziałek",
    "next-tuesday": "w przyszły wtorek",
    "next-wednesday": "w przyszłą środę",
    "next-thursday": "w przyszły czwartek",
    "next-friday": "w przyszły piątek",
    "next-saturday": "w przyszłą sobotę",
    "minutes": "$1 min.",
    "fahrenheit": "$1\u00b0F",
    "celsius": "$1\u00b0C",
    "inches": "$1 in",
    "centimeters": "$1 cm",
    "less-than": "mniej niż $1",
    "and": and_function,
    "through": through_function,
    "with": "$1, $2",
    "range": "$1\u2013$2",
    "parenthetical": parenthetical_function,
    "for-hour": "$1 przez godzinę",
    "starting-in": "$1 za $2",
    "stopping-in": "$1 skończy się za $2",
    "starting-then-stopping-later": "$1 za $2, skończy się po $3",
    "stopping-then-starting-later": "$1 skończy się za $2, ponownie zacznie $3 później",
    "for-day": "$1 w ciągu dnia",
    "starting": "$2 $1",
    "until": until_function,
    "until-starting-again": until_starting_again_function,
    "starting-continuing-until": starting_continuing_until_function,
    "during": "$2 $1",
    "for-week": "$1 w ciągu tygodnia",
    "over-weekend": "$1 w ciągu weekendu",
    "temperatures-peaking": "$2 temperatura wzrośnie do $1",
    "temperatures-rising": "$2 ocieplenie do $1",
    "temperatures-valleying": "$2 temperatura spadnie do $1",
    "temperatures-falling": "$2 ochłodzenie do $1",
    "title": title_function,
    "sentence": sentence_function,
    "next-hour-forecast-status": "prognozy na następną godzinę to $1, z powodu $2",
    "unavailable": "niedostępny",
    "temporarily-unavailable": "tymczasowo niedostępny",
    "partially-unavailable": "częściowo niedostępny",
    "station-offline": "wszystkie pobliskie stacje radarowe są offline",
    "station-incomplete": "luki w zasięgu pobliskich stacji radarowych",
    "smoke": "dym",
    "haze": "zmętnienie",
    "mist": "zamglenie",
}
