import re


def join_with_shared_prefix(a, b, joiner):
    m = a
    i = 0

    # HACK: This replicates the JS logic.
    if m == "odaytay" or m == "omorrowtay":
        m = "onway " + m

    # Skip the prefix of b that is shared with a.
    min_len = min(len(m), len(b))
    while i < min_len and ord(m[i]) == ord(b[i]):
        i += 1

    # ...except whitespace! We need that whitespace!
    # Move back until we hit a space or start of string
    while i > 0 and (
        i > len(b) or (i <= len(b) and b[i - 1] != " ")
    ):  # pragma: no cover
        i -= 1

    return a + joiner + b[i:]


def strip_prefix(period):
    if period.startswith("overnightway"):
        return "ightnay" + period[12:]
    elif period.startswith("inway ethay "):
        return period[12:]
    return period


def and_function(stack, a, b):
    return join_with_shared_prefix(a, b, ", andway " if "," in a else " andway ")


def through_function(stack, a, b):
    return join_with_shared_prefix(a, b, " oughthray ")


def until_function(stack, condition, period):
    return condition + " untilway " + strip_prefix(period)


def until_starting_again_function(stack, condition, a, b):
    return condition + " untilway " + strip_prefix(a) + ", artingstay againway " + b


def starting_continuing_until_function(stack, condition, a, b):
    return condition + " artingstay " + a + ", ontinuingcay untilway " + strip_prefix(b)


def title_function(stack, s):
    # Apply custom_capitalize to every word
    return re.sub(r"\b(?:a(?!ndway\b)|[^\Wa])", lambda match: match.group(0).upper(), s)


def sentence_function(stack, s):
    s = s[0].upper() + s[1:]
    if not s.endswith("."):
        s += "."
    return s


template = {
    "clear": "earclay",
    "no-precipitation": "onay ecipitationpray",
    "mixed-precipitation": "ixedmay ecipitationpray",
    "possible-very-light-precipitation": "ossiblepay ightlay ecipitationpray",
    "very-light-precipitation": "ightlay ecipitationpray",
    "possible-light-precipitation": "ossiblepay ightlay ecipitationpray",
    "light-precipitation": "ightlay ecipitationpray",
    "medium-precipitation": "ecipitationpray",
    "heavy-precipitation": "eavyhay ecipitationpray",
    "possible-very-light-rain": "ossiblepay izzledray",
    "very-light-rain": "izzledray",
    "possible-light-rain": "ossiblepay ightlay ainray",
    "light-rain": "ightlay ainray",
    "medium-rain": "ainray",
    "heavy-rain": "eavyhay ainray",
    "possible-very-light-sleet": "ossiblepay ightlay eetslay",
    "very-light-sleet": "ightlay eetslay",
    "possible-light-sleet": "ossiblepay ightlay eetslay",
    "light-sleet": "ightlay eetslay",
    "medium-sleet": "eetslay",
    "heavy-sleet": "eavyhay eetslay",
    "possible-very-light-snow": "ossiblepay urriesflay",
    "very-light-snow": "urriesflay",
    "possible-light-snow": "ossiblepay ightlay owsnay",
    "light-snow": "ightlay owsnay",
    "medium-snow": "owsnay",
    "heavy-snow": "eavyhay owsnay",
    "possible-thunderstorm": "ossiblepay understormsthay",
    "thunderstorm": "understormsthay",
    "possible-medium-precipitation": "ossiblepay ecipitationpray",
    "possible-heavy-precipitation": "ossiblepay eavyhay ecipitationpray",
    "possible-medium-rain": "ossiblepay ainray",
    "possible-heavy-rain": "ossiblepay eavyhay ainray",
    "possible-medium-sleet": "ossiblepay eetslay",
    "possible-heavy-sleet": "ossiblepay eavyhay eetslay",
    "possible-medium-snow": "ossiblepay owsnay",
    "possible-heavy-snow": "ossiblepay eavyhay owsnay",
    "possible-freezing-drizzle": "ossiblepay eezingfray izzledray",
    "freezing-drizzle": "eezingfray izzledray",
    "possible-light-freezing-rain": "ossiblepay ightlay eezingfray ainray",
    "light-freezing-rain": "ightlay eezingfray ainray",
    "possible-freezing-rain": "ossiblepay eezingfray ainray",
    "freezing-rain": "eezingfray ainray",
    "possible-heavy-freezing-rain": "ossiblepay eavyhay eezingfray ainray",
    "heavy-freezing-rain": "eavyhay eezingfray ainray",
    "possible-hail": "ossiblepay ailhay",
    "hail": "ailhay",
    "light-wind": "eezybray",
    "medium-wind": "indyway",
    "heavy-wind": "angerouslyday indyway",
    "low-humidity": "ydray",
    "high-humidity": "umidhay",
    "fog": "oggyfay",
    "very-light-clouds": "ostlymay earclay",
    "light-clouds": "artlypay oudyclay",
    "medium-clouds": "ostlymay oudyclay",
    "heavy-clouds": "overcastway",
    "today-morning": "isthay orningmay",
    "later-today-morning": "aterlay isthay orningmay",
    "today-afternoon": "isthay afternoonway",
    "later-today-afternoon": "aterlay isthay afternoonway",
    "today-evening": "isthay eveningway",
    "later-today-evening": "aterlay isthay eveningway",
    "today-night": "onighttay",
    "later-today-night": "aterlay onighttay",
    "tomorrow-morning": "omorrowtay orningmay",
    "tomorrow-afternoon": "omorrowtay afternoonway",
    "tomorrow-evening": "omorrowtay eveningway",
    "tomorrow-night": "omorrowtay ightnay",
    "morning": "inway ethay orningmay",
    "afternoon": "inway ethay afternoonway",
    "evening": "inway ethay eveningway",
    "night": "overnightway",
    "today": "odaytay",
    "tomorrow": "omorrowtay",
    "sunday": "onway undaysay",
    "monday": "onway ondaymay",
    "tuesday": "onway uesdaytay",
    "wednesday": "onway ednesdayway",
    "thursday": "onway ursdaythay",
    "friday": "onway idayfray",
    "saturday": "onway aturdaysay",
    "next-sunday": "extnay undaysay",
    "next-monday": "extnay ondaymay",
    "next-tuesday": "extnay uesdaytay",
    "next-wednesday": "extnay ednesdayway",
    "next-thursday": "extnay ursdaythay",
    "next-friday": "extnay idayfray",
    "next-saturday": "extnay aturdaysay",
    "minutes": "$1 min.",
    "fahrenheit": "$1\u00b0F",
    "celsius": "$1\u00b0C",
    "inches": "$1 in.",
    "centimeters": "$1 cm.",
    "less-than": "underway $1",
    "and": and_function,
    "through": through_function,
    "with": "$1, ithway $2",
    "range": "$1\u2013$2",
    "parenthetical": "$1 ($2)",
    "for-hour": "$1 orfay ethay hourway",
    "starting-in": "$1 artingstay inway $2",
    "stopping-in": "$1 oppingstay inway $2",
    "starting-then-stopping-later": "$1 artingstay inway $2, oppingstay $3 aterlay",
    "stopping-then-starting-later": "$1 oppingstay inway $2, artingstay againway $3 aterlay",
    "for-day": "$1 oughoutthray ethay ayday",
    "starting": "$1 artingstay $2",
    "until": until_function,
    "until-starting-again": until_starting_again_function,
    "starting-continuing-until": starting_continuing_until_function,
    "during": "$1 $2",
    "for-week": "$1 oughoutthray ethay eekway",
    "over-weekend": "$1 overway ethay eekendway",
    "temperatures-peaking": "emperaturestay eakingpay atway $1 $2",
    "temperatures-rising": "emperaturestay isingray otay $1 $2",
    "temperatures-valleying": "emperaturestay ottomingbay outway atway $1 $2",
    "temperatures-falling": "emperaturestay allingfay otay $1 $2",
    "title": title_function,
    "sentence": sentence_function,
    "next-hour-forecast-status": "extnay hourway orecastsfay areway $1 ueday otay $2.",
    "unavailable": "unavailableway",
    "temporarily-unavailable": "emporarilytay unavailableway",
    "partially-unavailable": "artiallypay unavailableway",
    "station-offline": "allway earbynay adarray tationssay eingbay offlineway",
    "station-incomplete": "apsgay inway overagecay romfay earbynay adarray ationsstay",
}
