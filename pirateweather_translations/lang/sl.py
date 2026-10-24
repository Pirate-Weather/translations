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
    return join_with_shared_prefix(a, b, ", in " if "," in a else " in ")


def list_function(stack, *items):
    # Join each item to the previous one so shared prefixes are only written once,
    # using "and" before the last item.
    result = items[0]
    for i in range(1, len(items)):
        prev = items[i - 1]
        if i == len(items) - 1:
            joined = and_function(stack, prev, items[i])
        else:
            joined = join_with_shared_prefix(prev, items[i], ", ")
        result += joined[len(prev) :]
    return result


def through_function(stack, a, b):
    return join_with_shared_prefix(a, b, " do ")


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
    "clear": "jasno",
    "no-precipitation": "brez padavin",
    "mixed-precipitation": "možne padavine",
    "possible-very-light-precipitation": "možne so rahle padavine",
    "very-light-precipitation": "rahle padavine",
    "possible-light-precipitation": "možne so rahle padavine",
    "light-precipitation": "rahle padavine",
    "medium-precipitation": "padavine",
    "heavy-precipitation": "močne padavine",
    "possible-very-light-rain": "možen je rahel dež",
    "very-light-rain": "rosenje",
    "possible-light-rain": "možen je rahel dež",
    "light-rain": "rahel dež",
    "medium-rain": "dež",
    "heavy-rain": "močan dež",
    "possible-very-light-sleet": "možnost rahlega žleda",
    "very-light-sleet": "rahel žled",
    "possible-light-sleet": "možnost žleda",
    "light-sleet": "rahel žled",
    "medium-sleet": "dež s snegom",
    "heavy-sleet": "žled",
    "possible-very-light-snow": "možno je rahlo sneženje",
    "very-light-snow": "rahlo sneženje",
    "possible-light-snow": "možnost rahlega sneženja",
    "light-snow": "rahlo sneženje",
    "medium-snow": "sneg",
    "heavy-snow": "močno sneženje",
    "possible-thunderstorm": "možen je nevihte z grmenjem",
    "thunderstorm": "nevihte z grmenjem",
    "possible-medium-precipitation": "možne so padavine",
    "possible-heavy-precipitation": "možne so močne padavine",
    "possible-medium-rain": "možen je dež",
    "possible-heavy-rain": "možen je močan dež",
    "possible-medium-sleet": "možnost dež s snegom",
    "possible-heavy-sleet": "možnost žled",
    "possible-medium-snow": "možno je sneg",
    "possible-heavy-snow": "možno je močno sneženje",
    "possible-very-light-freezing-rain": "možen je leden rosenje",
    "very-light-freezing-rain": "leden rosenje",
    "possible-light-freezing-rain": "možen je rahel leden dež",
    "light-freezing-rain": "rahel leden dež",
    "possible-medium-freezing-rain": "možen je leden dež",
    "medium-freezing-rain": "leden dež",
    "possible-heavy-freezing-rain": "možen je močan leden dež",
    "heavy-freezing-rain": "močan leden dež",
    "light-wind": "vetrovno",
    "medium-wind": "vetrovno",
    "heavy-wind": "močni sunki vetra",
    "fog": "megleno",
    "very-light-clouds": "pretežno jasno",
    "light-clouds": "delno oblačno",
    "medium-clouds": "pretežno oblačno",
    "heavy-clouds": "oblačno",
    "today-morning": "danes zjutraj",
    "later-today-morning": "kasneje to jutro",
    "today-afternoon": "danes popoldan",
    "later-today-afternoon": "kasneje popoldan",
    "today-evening": "danes zvečer",
    "later-today-evening": "drevi",
    "today-night": "danes ponoči",
    "later-today-night": "danes čez noč",
    "tomorrow-morning": "jutri zjutraj",
    "tomorrow-afternoon": "jutri popoldne",
    "tomorrow-evening": "jutri zvečer",
    "tomorrow-night": "jutri zvečer",
    "morning": "zjutraj",
    "afternoon": "popoldan",
    "evening": "zvečer",
    "night": "zvečer",
    "today": "danes",
    "tomorrow": "jutri",
    "sunday": "v nedeljo",
    "monday": "v ponedeljek",
    "tuesday": "v torek",
    "wednesday": "v sredo",
    "thursday": "v četrtek",
    "friday": "v petek",
    "saturday": "v soboto",
    "next-sunday": "naslednjo nedeljo",
    "next-monday": "naslednji ponedeljek",
    "next-tuesday": "naslednji torek",
    "next-wednesday": "naslednjo sredo",
    "next-thursday": "naslednji četrtek",
    "next-friday": "naslednji petek",
    "next-saturday": "naslednjo soboto",
    "minutes": "$1 min.",
    "fahrenheit": "$1\u00b0F",
    "celsius": "$1\u00b0C",
    "inches": "$1 in.",
    "centimeters": "$1 cm.",
    "less-than": "manj kot $1",
    "and": and_function,
    "list": list_function,
    "through": through_function,
    "with": "$1, s $2",
    "accompanied-by": "$1, pa tudi $2",
    "range": "$1\u2013$2",
    "parenthetical": "$1 ($2)",
    "for-hour": "$1 za uro",
    "starting-in": "$1 od $2",
    "stopping-in": "$1 do $2",
    "starting-then-stopping-later": "$1 od $2, do $3 kasneje",
    "stopping-then-starting-later": "$1 do $2, začelo bo zopet $3 kasneje",
    "for-day": "$1 čez dan",
    "starting": "$1 od $2",
    "until": "$1 do $2",
    "until-starting-again": "$1 do $2, začelo bo zopet $3",
    "starting-continuing-until": "$1 začel $2, do $3",
    "during": "$1 $2",
    "for-week": "$1 čez teden",
    "over-weekend": "$1 v soboto in nedeljo",
    "temperatures-peaking": "temperaturami do $1 $2",
    "temperatures-rising": "temperaturami do $1 $2",
    "temperatures-valleying": "najnižjimi temperaturami okoli $1 $2",
    "temperatures-falling": "temperaturami do $1 $2",
    "title": title_function,
    "sentence": sentence_function,
    "next-hour-forecast-status": "urne napovedi $1, ker $2",
    "unavailable": "niso na voljo",
    "temporarily-unavailable": "začasno niso na voljo",
    "partially-unavailable": "delno niso na voljo",
    "station-offline": "so vse bližnje radarske postaje brez povezave",
    "station-incomplete": "imajo bližnje radarske postaje pomanjkljivo pokritost",
    "smoke": "dim",
    "haze": "meglica",
    "mist": "megla",
    "millimeters": "$1 mm.",
    "multiple-sentences": "$1 $2",
    "of-expected": "pričakuje se $1 ($2)",
    "for-night": "$1 čez noč",
    "intermittent": "$1 s prekinitvami",
    "occasional": "občasno $1",
    "periods-of": "periodično $1",
    "tapering-off": "$1 postopoma ponehuje",
    "to": "$1 do $2",
    "generally": "pretežno $1",
    "increasing": "naraščanje oblačnosti",
    "clearing": "razjasnitev",
    "becoming": "$1, nato $2",
    "temperatures-steady": "temperaturami okoli $1",
}
