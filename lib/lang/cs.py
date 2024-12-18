def remove_prefix_and_use_genitive(a):
    genitive_map = {
        "dnes ráno": "dnešního rána",
        "dnes dopoledne": "dnešního dopoledne",
        "dnes odpoledne": "dnešního odpoledne",
        "dnes podvečer": "dnešního podvečera",
        "dnes večer": "dnešního večera",
        "dnes pozdě večer": "dnešního pozdního večera",
        "dnes v noci": "dnešní noci",
        "dnes pozdě v noci": "dnešní pozdní noci",
        "zítra ráno": "zítřejšího rána",
        "zítra odpoledne": "zítřejšího odpoledne",
        "zítra večer": "zítřejšího večera",
        "zítra v noci": "zítřejší noci",
        "ráno": "rána",
        "odpoledne": "odpoledne",
        "večer": "večera",
        "v noci": "noci",
        "v pondělí": "pondelí",
        "v úterý": "uterý",
        "ve středu": "středy",
        "ve čtvrtek": "čtvrtka",
        "v pátek": "pátku",
        "v sobotu": "soboty",
        "v neděli": "neděle",
    }
    return genitive_map.get(a, a)


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
    return join_with_shared_prefix(
        a,
        b,
        " a ",
    )


def through_function(stack, a, b):
    return (
        "od "
        + remove_prefix_and_use_genitive(a)
        + " do "
        + remove_prefix_and_use_genitive(b)
    )


def parenthetical_function(stack, a, b):
    return f"{a} ({b}{' sněhu)' if a == 'smíšené srážky' else ')'}"


def until_function(stack, condition, period):
    return condition + " až do " + remove_prefix_and_use_genitive(period)


def until_starting_again_function(stack, condition, a, b):
    starting = ""
    if condition.endswith("srážky"):
        starting = ", které začnou znovu "
    elif (
        condition.endswith("déšť")
        or condition.endswith("déšť se sněhem")
        or condition.endswith("vítr")
    ):
        starting = ", který začne znovu "
    elif condition.endswith("sněžení") or condition.endswith("mrholení"):
        starting = ", které začne znovu "
    elif condition.endswith("vlhkost"):
        starting = ", která začne znovu "
    elif (
        condition.endswith("zataženo")
        or condition.endswith("mlhavo")
        or condition.endswith("oblačno")
    ):
        starting = "a začne znovu "

    return condition + " až do " + remove_prefix_and_use_genitive(a) + starting + b


def starting_function(stack, a, b):
    return "od " + remove_prefix_and_use_genitive(b) + " " + a


def starting_continuing_until_function(stack, condition, a, b):
    continuing = ""
    if condition.endswith("srážky"):
        continuing = ", které přetrvají až do "
    elif (
        condition.endswith("déšť")
        or condition.endswith("déšť se sněhem")
        or condition.endswith("vítr")
    ):
        continuing = ", který přetrvá až do "
    elif condition.endswith("snežení") or condition.endswith("mrholení"):
        continuing = ", které přetrvá až do "
    elif condition.endswith("vlhkost"):
        continuing = ", která přetrvá až do "
    elif (
        condition.endswith("zataženo")
        or condition.endswith("mlhavo")
        or condition.endswith("oblačno")
    ):
        continuing = " a přetrvá až do "
    return (
        "od "
        + remove_prefix_and_use_genitive(a)
        + " "
        + condition
        + continuing
        + remove_prefix_and_use_genitive(b)
    )


def title_function(stack, s):
    return s[0].upper() + s[1:]


def sentence_function(stack, s):
    s = s[0].upper() + s[1:]
    if not s.endswith("."):
        s += "."
    return s


template = {
    "clear": "jasno",
    "no-precipitation": "bez srážek",
    "mixed-precipitation": "smíšené srážky",
    "possible-very-light-precipitation": "možnost velmi slabých srážek",
    "very-light-precipitation": "velmi slabé srážky",
    "possible-light-precipitation": "možnost slabých srážek",
    "light-precipitation": "slabé srážky",
    "medium-precipitation": "srážky",
    "heavy-precipitation": "silné srážky",
    "possible-very-light-rain": "možnost mrholení",
    "very-light-rain": "mrholení",
    "possible-light-rain": "možnost slabého deště",
    "light-rain": "slabý déšť",
    "medium-rain": "déšť",
    "heavy-rain": "vydatný déšť",
    "possible-very-light-sleet": "možnost slabého deště se sněhem",
    "very-light-sleet": "slabý déšť se sněhem",
    "possible-light-sleet": "možnost slabého deště se sněhem",
    "light-sleet": "slabý déšť se sněhem",
    "medium-sleet": "déšť se sněhem",
    "heavy-sleet": "vydatný déšť se sněhem",
    "possible-very-light-snow": "možnost slabého sněžení",
    "very-light-snow": "slabé sněžení",
    "possible-light-snow": "možnost slabého sněžení",
    "light-snow": "slabé sněžení",
    "medium-snow": "sněžení",
    "heavy-snow": "vydatné sněžení",
    "possible-thunderstorm": "možnost bouřek",
    "thunderstorm": "bouřky",
    "possible-medium-precipitation": "možnost srážky",
    "possible-heavy-precipitation": "možnost silné srážky",
    "possible-medium-rain": "možnost slabého déšť",
    "possible-heavy-rain": "možnost slabého vydatný déšť",
    "possible-medium-sleet": "možnost slabého déšť se sněhem",
    "possible-heavy-sleet": "možnost slabého vydatný déšť se sněhem",
    "possible-medium-snow": "možnost slabého sněžení",
    "possible-heavy-snow": "možnost slabého vydatné sněžení",
    "possible-freezing-drizzle": "možnost slabého mrazivý mrholení",
    "freezing-drizzle": "mrazivý mrholení",
    "possible-light-freezing-rain": "možnost slabého slabý mrazivý déšť",
    "light-freezing-rain": "slabý freezing déšť",
    "possible-freezing-rain": "možnost slabého mrazivý déšť",
    "freezing-rain": "mrazivý déšť",
    "possible-heavy-freezing-rain": "možnost slabého vydatný mrazivý déšť",
    "heavy-freezing-rain": "vydatný mrazivý déšť",
    "possible-hail": "možnost slabého kroupy",
    "hail": "kroupy",
    "light-wind": "slabý vítr",
    "medium-wind": "větrno",
    "heavy-wind": "silný vítr",
    "low-humidity": "nízká vlhkost",
    "high-humidity": "vysoká vlhkost",
    "fog": "mlhavo",
    "very-light-clouds": "převážně jasno",
    "light-clouds": "částečně oblačno",
    "medium-clouds": "převážně oblačno",
    "heavy-clouds": "zataženo",
    "today-morning": "dnes ráno",
    "later-today-morning": "dnes dopoledne",
    "today-afternoon": "dnes odpoledne",
    "later-today-afternoon": "dnes podvečer",
    "today-evening": "dnes večer",
    "later-today-evening": "dnes pozdě večer",
    "today-night": "dnes v noci",
    "later-today-night": "dnes pozdě v noci",
    "tomorrow-morning": "zítra ráno",
    "tomorrow-afternoon": "zítra odpoledne",
    "tomorrow-evening": "zítra večer",
    "tomorrow-night": "zítra v noci",
    "morning": "ráno",
    "afternoon": "odpoledne",
    "evening": "večer",
    "night": "v noci",
    "today": "dnes",
    "tomorrow": "zítra",
    "sunday": "v neděli",
    "monday": "v pondělí",
    "tuesday": "v úterý",
    "wednesday": "ve středu",
    "thursday": "ve čtvrtek",
    "friday": "v pátek",
    "saturday": "v sobotu",
    "next-sunday": "příští neděli",
    "next-monday": "příští pondělí",
    "next-tuesday": "příští úterý",
    "next-wednesday": "příští středu",
    "next-thursday": "příští čtvrtek",
    "next-friday": "příští pátek",
    "next-saturday": "příští sobotu",
    "minutes": "$1 min.",
    "fahrenheit": "$1°F",
    "celsius": "$1°C",
    "inches": "$1 in",
    "centimeters": "$1 cm",
    "less-than": "méně než $1",
    "and": and_function,
    "through": through_function,
    "with": "$1, $2",
    "range": "$1-$2",
    "parenthetical": parenthetical_function,
    "for-hour": "$1 hodinu",
    "starting-in": "$1 za $2",
    "stopping-in": "$1 skončí za $2",
    "starting-then-stopping-later": "$1 za $2, skončí o $3 později",
    "stopping-then-starting-later": "$1 skončí za $2 a začne znovu o $3 později",
    "for-day": "Během dne $1",
    "starting": starting_function,
    "until": until_function,
    "until-starting-again": until_starting_again_function,
    "starting-continuing-until": starting_continuing_until_function,
    "during": "$2 $1",
    "for-week": "$1 během týdne",
    "over-weekend": "$1 přes víkend",
    "temperatures-peaking": "$2 s teplotním maximem $1",
    "temperatures-rising": "$2 s teplotami stoupajícími k $1",
    "temperatures-valleying": "$2 s teplotním minimem $1",
    "temperatures-falling": "$2 s teplotami klesajícími k $1",
    "title": title_function,
    "sentence": sentence_function,
    "next-hour-forecast-status": "next hour forecasts are $1 due to $2",
    "unavailable": "unavailable",
    "temporarily-unavailable": "temporarily unavailable",
    "partially-unavailable": "partially unavailable",
    "station-offline": "all nearby radar stations being offline",
    "station-incomplete": "gaps in coverage from nearby radar stations",
}
