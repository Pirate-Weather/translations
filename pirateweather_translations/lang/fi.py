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


grammar = {
    "tänään": [None, None],
    "huomenna": ["huomisesta", "huomiseen asti"],
    "yöllä": ["yöstä", "yöhön asti"],
    "ilta": ["illasta", "iltaan asti"],
    "aamulla": ["aamusta", "aamuun asti"],
    "illalla": ["illasta", "iltaan asti"],
    "iltapäivällä": ["iltapäivästä", "iltapäivään asti"],
    "huomisaamu": ["huomisaamusta", "huomisaamuun asti"],
    "myöhemmin illalla": ["myöhemmästä illasta alkaen", "myöhempään iltaan asti"],
    "myöhemmin yöllä": ["myöhemmästä yöstä alkaen", "myöhempään yöhön asti"],
    "huomenna iltapäivällä": ["huomisesta iltapäivästä", "huomiseen iltapäivään asti"],
    "huomenna illalla": ["huomisesta illasta", "huomiseen iltaan asti"],
    "huomenna yöllä": ["huomisesta yöstä", "huomiseen yöhön asti"],
    "maanantaina": ["maanantaista", "maanantaihin"],
    "tiistaina": ["tiistaista", "tiistaihin"],
    "keskiviikkona": ["keskiviikosta", "keskiviikkoon"],
    "torstaina": ["torstaista", "torstaihin"],
    "perjantaina": ["perjantaista", "perjantaihin"],
    "lauantaina": ["lauantaista", "lauantaihin"],
    "sunnuntaina": ["sunnuntaista", "sunnuntaihin"],
}


def elative(word):
    """Return the elative form of a word if it exists in the grammar."""
    return grammar[word][0] if word in grammar else word


def illative(word):
    """Return the illative form of a word if it exists in the grammar."""
    return grammar[word][1] if word in grammar else word


def and_function(stack, a, b):
    return join_with_shared_prefix(a, b, " ja ")


def through_function(stack, a, b):
    a = elative(a)
    b = illative(b)
    if a and b:
        return f"{a} asti {b}"
    elif a or b:
        return f"{a or b} asti"
    else:
        return "asti"


def starting_function(stack, condition, period):
    return condition + " " + elative(period)


def until_function(stack, condition, period):
    return condition + " " + illative(period)


def until_starting_again_function(stack, condition, a, b):
    return condition + " " + illative(a) + ", ja jälleen " + b


def starting_continuing_until_function(stack, condition, a, b):
    return condition + " " + elative(a) + " " + illative(b)


def title_function(stack, s):
    return s[0].upper() + s[1:]


def sentence_function(stack, s):
    s = s[0].upper() + s[1:]
    if not s.endswith("."):
        s += "."
    return s


template = {
    "clear": "selkeää",
    "no-precipitation": "poutaa",
    "mixed-precipitation": "räntäsadetta",
    "possible-very-light-precipitation": "heikon sateen mahdollisuus",
    "very-light-precipitation": "heikkoa sadetta",
    "possible-light-precipitation": "sadekuurojen mahdollisuus",
    "light-precipitation": "sadekuuroja",
    "medium-precipitation": "sadetta",
    "heavy-precipitation": "rankkasadetta",
    "possible-very-light-rain": "heikon sateen mahdollisuus",
    "very-light-rain": "heikkoa sadetta",
    "possible-light-rain": "sadekuurojen mahdollisuus",
    "light-rain": "sadekuuroja",
    "medium-rain": "sadetta",
    "heavy-rain": "rankkasadetta",
    "possible-very-light-sleet": "heikon räntäsateen mahdollisuus",
    "very-light-sleet": "heikkoa räntäsadetta",
    "possible-light-sleet": "räntäkuurojen mahdollisuus",
    "light-sleet": "räntäkuuroja",
    "medium-sleet": "räntäsadetta",
    "heavy-sleet": "voimakasta räntäsadetta",
    "possible-very-light-snow": "heikon lumisateen mahdollisuus",
    "very-light-snow": "heikkoa lumisadetta",
    "possible-light-snow": "lumikuurojen mahdollisuus",
    "light-snow": "lumikuuroja",
    "medium-snow": "lumisadetta",
    "heavy-snow": "rankkaa lumisadetta",
    "possible-thunderstorm": "ukkosmyrskyjä mahdollisuus",
    "thunderstorm": "ukkosmyrskyjä",
    "possible-medium-precipitation": "sadetta mahdollisuus",
    "possible-heavy-precipitation": "rankkasadetta mahdollisuus",
    "possible-medium-rain": "sadetta mahdollisuus",
    "possible-heavy-rain": "rankkasadetta mahdollisuus",
    "possible-medium-sleet": "räntäsadetta mahdollisuus",
    "possible-heavy-sleet": "voimakasta räntäsadetta mahdollisuus",
    "possible-medium-snow": "lumisadetta mahdollisuus",
    "possible-heavy-snow": "rankkaa lumisadetta mahdollisuus",
    "possible-very-light-freezing-rain": "jäätävää tihkusadetta mahdollisuus",
    "very-light-freezing-rain": "jäätävää tihkusadetta",
    "possible-light-freezing-rain": "kevyttä jäätävää sadetta mahdollisuus",
    "light-freezing-rain": "kevyttä jäätävää sadetta",
    "possible-medium-freezing-rain": "jäätävää sadetta mahdollisuus",
    "medium-freezing-rain": "jäätävää sadetta",
    "possible-heavy-freezing-rain": "rankkaa jäätävää sadetta mahdollisuus",
    "heavy-freezing-rain": "rankkaa jäätävää sadetta",
    "possible-hail": "rakeita mahdollisuus",
    "hail": "rakeita",
    "light-wind": "heikkoa tuulta",
    "medium-wind": "tuulista",
    "heavy-wind": "myrskyisää",
    "low-humidity": "kuivaa",
    "high-humidity": "kosteaa",
    "fog": "sumua",
    "very-light-clouds": "enimmäkseen selkeää",
    "light-clouds": "puolipilvistä",
    "medium-clouds": "enimmäkseen pilvistä",
    "heavy-clouds": "pilvistä",
    "today-morning": "aamulla",
    "later-today-morning": "myöhemmin aamulla",
    "today-afternoon": "iltapäivällä",
    "later-today-afternoon": "myöhemmin iltapäivällä",
    "today-evening": "illalla",
    "later-today-evening": "myöhemmin illalla",
    "today-night": "yöllä",
    "later-today-night": "myöhemmin yöllä",
    "tomorrow-morning": "huomisaamuna",
    "tomorrow-afternoon": "huomenna iltapäivällä",
    "tomorrow-evening": "huomenna illalla",
    "tomorrow-night": "huomenna yöllä",
    "morning": "aamulla",
    "afternoon": "iltapäivällä",
    "evening": "illalla",
    "night": "yöllä",
    "today": "tänään",
    "tomorrow": "huomenna",
    "sunday": "sunnuntaina",
    "monday": "maanantaina",
    "tuesday": "tiistaina",
    "wednesday": "keskiviikkona",
    "thursday": "torstaina",
    "friday": "perjantaina",
    "saturday": "lauantaina",
    "next-sunday": "sunnuntaina",  # FIXME
    "next-monday": "maanantaina",  # FIXME
    "next-tuesday": "tiistaina",  # FIXME
    "next-wednesday": "keskiviikkona",  # FIXME
    "next-thursday": "torstaina",  # FIXME
    "next-friday": "perjantaina",  # FIXME
    "next-saturday": "lauantaina",  # FIXME
    "minutes": "$1 min.",
    "fahrenheit": "$1\u00b0F",
    "celsius": "$1\u00b0C",
    "inches": "$1 tuumaa",
    "centimeters": "$1 cm",
    "less-than": "alle $1",
    "and": and_function,
    "through": through_function,
    "with": "$1, $2",
    "range": "$1\u2013$2",
    "parenthetical": "$1 ($2)",
    "for-hour": "$1 seuraavan tunnin ajan",
    "starting-in": "$1 odotettavissa $2 kuluessa",
    "stopping-in": "$1 vielä $2",
    "starting-then-stopping-later": "$1 $2 kuluessa, päättyen $3 myöhemmin",
    "stopping-then-starting-later": "$1 vielä $2, alkaen uudestaan $3 myöhemmin",
    "for-day": "$1 päivän aikana",
    "starting": starting_function,
    "until": until_function,
    "until-starting-again": until_starting_again_function,
    "starting-continuing-until": starting_continuing_until_function,
    "during": "$1 $2",
    "for-week": "$1 viikon ajan",
    "over-weekend": "$1 viikonloppuna",
    "temperatures-peaking": "lämpötilan noustessa lukemaan $1 $2",
    "temperatures-rising": "lämpötilan noustessa lukemaan $1 $2",
    "temperatures-valleying": "lämpötilan käydessä lukemassa $1 $2",
    "temperatures-falling": "lämpötilan laskiessa lukemaan $1 $2",
    "title": title_function,
    "sentence": sentence_function,
    "next-hour-forecast-status": "seuraavan tunnin ennusteet ovat $1 johtuen $2",
    "unavailable": "ei saatavilla",
    "temporarily-unavailable": "tilapäisesti poissa käytöstä",
    "partially-unavailable": "osittain saatavilla",
    "station-offline": "kaikki lähellä olevat tutka-asemat ovat offline-tilassa",
    "station-incomplete": "lähialueiden tutka-asemien kattavuusvaje",
    "smoke": "savu",
    "haze": "huntu",
    "mist": "sumu",
}
