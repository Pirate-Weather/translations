def remove_prefix_and_use_genitive(a):
    if a == "dnes ráno":
        return "dnešného rána"
    elif a == "dnes dopoludnia":
        return "dnešného dopoludnia"
    elif a == "dnes popoludní":
        return "dnešného popoludnia"
    elif a == "dnes podvečer":
        return "dnešného podvečera"
    elif a == "dnes večer":
        return "dnešného večera"
    elif a == "dnes neskoro večer":
        return "dnešného neskorého večera"
    elif a == "dnes v noci":
        return "dnešnej noci"
    elif a == "dnes neskoro v noci":
        return "dnešnej neskorej noci"
    elif a == "zajtra ráno":
        return "zajtrajšieho rána"
    elif a == "zajtra popoludní":
        return "zajtrajšieho popoludnia"
    elif a == "zajtra večer":
        return "zajtrajšieho večera"
    elif a == "zajtra v noci":
        return "zajtrajšej noci"
    elif a == "ráno":
        return "rána"
    elif a == "popoludní":
        return "popoludnia"
    elif a == "večer":
        return "večera"
    elif a == "v noci":
        return "noci"
    elif a == "v pondelok":
        return "pondelka"
    elif a == "v utorok":
        return "utorka"
    elif a == "v stredu":
        return "stredy"
    elif a == "vo štvrtok":
        return "štvrtka"
    elif a == "v piatok":
        return "piatka"
    elif a == "v sobotu":
        return "soboty"
    elif a == "v nedeľu":
        return "nedele"
    elif a == "budúci pondelok":
        return "budúceho pondelka"
    elif a == "budúci utorok":
        return "budúceho utorka"
    elif a == "budúca streda":
        return "budúcej stredy"
    elif a == "budúci štvrtok":
        return "budúceho štvrtka"
    elif a == "budúci piatok":
        return "budúceho piatka"
    elif a == "budúca sobota":
        return "budúcej soboty"
    elif a == "budúca nedeľa":
        return "budúcej nedele"
    else:
        return a


def join_with_shared_prefix(a, b, joiner):
    m = a
    i = 0

    # HACK: This replicates the JS logic.
    if m == "today" or m == "tomorrow":
        m = "on " + m

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
    if period.startswith("overnight"):
        return period[4:]
    elif period.startswith("in the "):
        return period[7:]
    return period


def custom_capitalize(s):
    # Do not capitalize certain words:
    if s in ["a", "and", "cm", "in", "of", "with"]:
        return s
    return s[0].upper() + s[1:] if s else s


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
    return f"{a} ({b}{' snehu)' if a == 'zmiešané zrážky' else ')'}"


def starting_function(stack, a, b):
    return "od " + remove_prefix_and_use_genitive(b) + " " + a


def until_function(stack, condition, period):
    return condition + " až do " + remove_prefix_and_use_genitive(period)


def until_starting_again_function(stack, condition, a, b):
    starting = ""

    if condition.endswith("zrážky"):
        starting = ", ktoré začnú znovu "
    elif (
        condition.endswith("dážď")
        or condition.endswith("dážď so snehom")
        or condition.endswith("vietor")
    ):
        starting = ", ktorý začne znovu "
    elif condition.endswith("sneženie") or condition.endswith("mrholenie"):
        starting = ", ktoré začne znovu "
    elif condition.endswith("vlhkosť"):
        starting = ", ktorá začne znovu "
    elif condition.endswith("zamračené") or condition.endswith("hmlisto"):
        starting = "a začne znovu "

    return condition + " až do " + remove_prefix_and_use_genitive(a) + starting + b


def starting_continuing_until_function(stack, condition, a, b):
    continuing = ""

    if condition.endswith("zrážky"):
        continuing = ", ktoré pretrvajú až do "
    elif (
        condition.endswith("dážď")
        or condition.endswith("dážď so snehom")
        or condition.endswith("vietor")
    ):
        continuing = ", ktorý pretrvá až do "
    elif condition.endswith("sneženie") or condition.endswith("mrholenie"):
        continuing = ", ktoré pretrvá až do "
    elif condition.endswith("vlhkosť"):
        continuing = ", ktorá pretrvá až do "
    elif condition.endswith("zamračené") or condition.endswith("hmlisto"):
        continuing = " a pretrvá až do "

    return f"od {remove_prefix_and_use_genitive(a)} {condition}{continuing}{remove_prefix_and_use_genitive(b)}"


def title_function(stack, s):
    """
    Capitalize the first letter of first word.
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
    "clear": "jasno",
    "no-precipitation": "bez zrážok",
    "mixed-precipitation": "zmiešané zrážky",
    "possible-very-light-precipitation": "možnosť veľmi slabých zrážok",
    "very-light-precipitation": "veľmi slabé zrážky",
    "possible-light-precipitation": "možnosť slabých zrážok",
    "light-precipitation": "slabé zrážky",
    "medium-precipitation": "zrážky",
    "heavy-precipitation": "silné zrážky",
    "possible-very-light-rain": "možnosť mrholenia",
    "very-light-rain": "mrholenie",
    "possible-light-rain": "možnosť slabého dažďa",
    "light-rain": "slabý dážď",
    "medium-rain": "dážď",
    "heavy-rain": "vydatný dážď",
    "possible-very-light-sleet": "možnosť slabého dažďa so snehom",
    "very-light-sleet": "slabý dážď so snehom",
    "possible-light-sleet": "možnosť slabého dažďa so snehom",
    "light-sleet": "slabý dážď so snehom",
    "medium-sleet": "dážď so snehom",
    "heavy-sleet": "vydatný dážď so snehom",
    "possible-very-light-snow": "možnosť slabého sneženia",
    "very-light-snow": "slabé sneženie",
    "possible-light-snow": "možnosť slabého sneženia",
    "light-snow": "slabé sneženie",
    "medium-snow": "sneženie",
    "heavy-snow": "vydatné sneženie",
    "possible-thunderstorm": "možnosť búrok",
    "thunderstorm": "búrky",
    "possible-medium-precipitation": "možnosť zrážok",
    "possible-heavy-precipitation": "možnosť silné zrážok",
    "possible-medium-rain": "možnosť slabého dažďa",
    "possible-heavy-rain": "možnosť slabého vydatný dažďa",
    "possible-medium-sleet": "možnosť slabého dažďa so snehom",
    "possible-heavy-sleet": "možnosť slabého vydatný dažďa so snehom",
    "possible-medium-snow": "možnosť slabého sneženia",
    "possible-heavy-snow": "možnosť slabého vydatné sneženia",
    "possible-very-light-freezing-rain": "možnosť mrznúce mrholenie",
    "very-light-freezing-rain": "mrznúce mrholenie",
    "possible-light-freezing-rain": "možnosť slabý mrznúce dažďa",
    "light-freezing-rain": "slabý mrznúce dážď",
    "possible-medium-freezing-rain": "možnosť mrznúce dažďa",
    "medium-freezing-rain": "mrznúce dážď",
    "possible-heavy-freezing-rain": "možnosť vydatný mrznúce dažďa",
    "heavy-freezing-rain": "vydatný mrznúce dážď",
    "possible-hail": "prípadné krupobitie",
    "hail": "krupobitie",
    "light-wind": "slabý vietor",
    "medium-wind": "veterno",
    "heavy-wind": "silný vietor",
    "low-humidity": "nízka vlhkosť",
    "high-humidity": "vysoká vlhkosť",
    "fog": "hmlisto",
    "very-light-clouds": "prevažne jasno",
    "light-clouds": "čiastočne zamračené",
    "medium-clouds": "prevažne zamračené",
    "heavy-clouds": "zamračené",
    "today-morning": "dnes ráno",
    "later-today-morning": "dnes dopoludnia",
    "today-afternoon": "dnes popoludní",
    "later-today-afternoon": "dnes podvečer",
    "today-evening": "dnes večer",
    "later-today-evening": "dnes neskoro večer",
    "today-night": "dnes v noci",
    "later-today-night": "dnes neskoro v noci",
    "tomorrow-morning": "zajtra ráno",
    "tomorrow-afternoon": "zajtra popoludní",
    "tomorrow-evening": "zajtra večer",
    "tomorrow-night": "zajtra v noci",
    "morning": "ráno",
    "afternoon": "popoludní",
    "evening": "večer",
    "night": "v noci",
    "today": "dnes",
    "tomorrow": "zajtra",
    "sunday": "v nedeľu",
    "monday": "v pondelok",
    "tuesday": "v utorok",
    "wednesday": "v stredu",
    "thursday": "vo štvrtok",
    "friday": "v piatok",
    "saturday": "v sobotu",
    "next-sunday": "budúcu nedeľu",
    "next-monday": "budúci pondelok",
    "next-tuesday": "budúci utorok",
    "next-wednesday": "budúcu stredu",
    "next-thursday": "budúci štvrtok",
    "next-friday": "budúci piatok",
    "next-saturday": "budúcu sobotu",
    "minutes": "$1 min.",
    "fahrenheit": "$1°F",
    "celsius": "$1°C",
    "inches": "$1 in",
    "centimeters": "$1 cm",
    "less-than": "menej ako $1",
    "and": and_function,
    "through": through_function,
    "with": "$1, $2",
    "range": "$1-$2",
    "parenthetical": parenthetical_function,
    "for-hour": "$1 hodinu",
    "starting-in": "$1 o $2",
    "stopping-in": "$1 skončí o $2",
    "starting-then-stopping-later": "$1 o $2, skončí o $3 neskôr",
    "stopping-then-starting-later": "$1 skončí o $2 a začne znovu o $3 neskôr",
    "for-day": "Počas dňa $1",
    "starting": starting_function,
    "until": until_function,
    "until-starting-again": until_starting_again_function,
    "starting-continuing-until": starting_continuing_until_function,
    "during": "$2 $1",
    "for-week": "$1 počas týždňa",
    "over-weekend": "$1 cez víkend",
    "temperatures-peaking": "$2 s teplotným maximom $1",
    "temperatures-rising": "$2 s teplotami stúpajúcimi k $1",
    "temperatures-valleying": "$2 s teplotným minimom $1",
    "temperatures-falling": "$2 s teplotami klesajúcimi k $1",
    "title": title_function,
    "sentence": sentence_function,
    "next-hour-forecast-status": "Predpoveď na ďalšiu hodinu je $1, pretože $2.",
    "unavailable": "nedostupná",
    "temporarily-unavailable": "dočasne nedostupná",
    "partially-unavailable": "čiastočne nedostupná",
    "station-offline": "všetky radarové stanice v okolí sú v režime offline",
    "station-incomplete": "vznikli medzery v pokrytí radarovými stanicami v okolí",
}
