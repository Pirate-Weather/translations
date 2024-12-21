def join_with_shared_prefix(a, b, joiner):
    m = a
    i = 0

    # HACK: This replicates the JS logic.
    if m == "ma" or m == "holnap":
        m = "a" + m + "i nap"

    # Skip the prefix of b that is shared with a.
    min_len = min(len(m), len(b))
    while i < min_len and ord(m[i]) == ord(b[i]):
        i += 1

    # ...except whitespace! We need that whitespace!
    # Move back until we hit a space or start of string
    while i > 0 and (i > len(b) or (i <= len(b) and b[i - 1] != " ")):
        i -= 1

    return a + " és " + b[i:] + joiner


def and_function(stack, a, b):
    return join_with_shared_prefix(
        a,
        b,
        "",
    )


def through_function(stack, a, b):
    return join_with_shared_prefix(a, b, " között")


def parenthetical_function(stack, a, b):
    # Check if a is "vegyes csapadék", if so append " hó"
    if a == "vegyes csapadék":
        return f"{a} ({b} hó)"
    else:
        return f"{a} ({b})"


def title_function(stack, s):
    return s[0].upper() + s[1:]


def sentence_function(stack, s):
    s = s[0].upper() + s[1:]
    if not s.endswith("."):
        s += "."
    return s


template = {
    "clear": "derült",
    "no-precipitation": "csapadékmentes idő",
    "mixed-precipitation": "vegyes csapadék",
    "possible-very-light-precipitation": "szitáló csapadék lehetséges",
    "very-light-precipitation": "szitáló csapadék",
    "possible-light-precipitation": "gyenge csapadék lehetséges",
    "light-precipitation": "gyenge csapadék",
    "medium-precipitation": "csapadék",
    "heavy-precipitation": "intenzív csapadék",
    "possible-very-light-rain": "gyenge szitálás lehetséges",
    "very-light-rain": "gyenge szitálás",
    "possible-light-rain": "gyenge eső lehetséges",
    "light-rain": "gyenge eső",
    "medium-rain": "eső",
    "heavy-rain": "intenzív eső",
    "possible-very-light-sleet": "ónos szitálás lehetséges",
    "very-light-sleet": "ónos szitálás",
    "possible-light-sleet": "gyenge ónos eső lehetséges",
    "light-sleet": "gyenge ónos eső",
    "medium-sleet": "ónos eső",
    "heavy-sleet": "havas eső",
    "possible-very-light-snow": "hószállingózás lehetséges",
    "very-light-snow": "hószállingózás",
    "possible-light-snow": "gyenge havazás lehetséges",
    "light-snow": "gyenge havazás",
    "medium-snow": "havazás",
    "heavy-snow": "intenzív havazás",
    "possible-thunderstorm": "zivatarok lehetséges",
    "thunderstorm": "zivatarok",
    "possible-medium-precipitation": "csapadék lehetséges",
    "possible-heavy-precipitation": "intenzív csapadék lehetséges",
    "possible-medium-rain": "eső lehetséges",
    "possible-heavy-rain": "intenzív eső lehetséges",
    "possible-medium-sleet": "ónos eső lehetséges",
    "possible-heavy-sleet": "havas ónos eső lehetséges",
    "possible-medium-snow": "havazás lehetséges",
    "possible-heavy-snow": "intenzív havazás lehetséges",
    "possible-freezing-drizzle": "fagyos gyenge szitálás lehetséges",
    "freezing-drizzle": "fagyos gyenge szitálás",
    "possible-light-freezing-rain": "gyenge fagyos eső lehetséges",
    "light-freezing-rain": "gyenge fagyos eső",
    "possible-freezing-rain": "fagyos eső lehetséges",
    "freezing-rain": "fagyos eső",
    "possible-heavy-freezing-rain": "intenzív fagyos eső lehetséges",
    "heavy-freezing-rain": "intenzív fagyos eső",
    "possible-hail": "fagyos lehetséges",
    "hail": "fagyos",
    "light-wind": "enyhe szél",
    "medium-wind": "mérsékelt szél",
    "heavy-wind": "erős szél",
    "low-humidity": "száraz idő",
    "high-humidity": "párás idő",
    "fog": "ködös idő",
    "very-light-clouds": "erős derült",
    "light-clouds": "közepes felhősödés",
    "medium-clouds": "erős felhősödés",
    "heavy-clouds": "borult idő",
    "today-morning": "ma reggel",
    "later-today-morning": "ma késő délelőtt",
    "today-afternoon": "ma délután",
    "later-today-afternoon": "ma késő délután",
    "today-evening": "ma este",
    "later-today-evening": "ma késő este",
    "today-night": "ma éjjel",
    "later-today-night": "ma késő éjjel",
    "tomorrow-morning": "holnap reggel",
    "tomorrow-afternoon": "holnap délután",
    "tomorrow-evening": "holnap este",
    "tomorrow-night": "holnap éjjel",
    "morning": "reggel",
    "afternoon": "délután",
    "evening": "este",
    "night": "éjjel",
    "today": "ma",
    "tomorrow": "holnap",
    "sunday": "vasárnap",
    "monday": "hétfői nap",
    "tuesday": "keddi nap",
    "wednesday": "szerdai nap",
    "thursday": "csütörtöki nap",
    "friday": "pénteki nap",
    "saturday": "szombati nap",
    "next-sunday": "vasárnap",  # FIXME
    "next-monday": "hétfői nap",  # FIXME
    "next-tuesday": "keddi nap",  # FIXME
    "next-wednesday": "szerdai nap",  # FIXME
    "next-thursday": "csütörtöki nap",  # FIXME
    "next-friday": "pénteki nap",  # FIXME
    "next-saturday": "szombati nap",  # FIXME
    "minutes": "$1 perc",
    "fahrenheit": "$1\u00b0F",
    "celsius": "$1\u00b0C",
    "inches": "$1 in.",
    "centimeters": "$1 cm.",
    "less-than": "$1 alatt",
    "and": and_function,
    "through": through_function,
    "with": "$1, $2",
    "range": "$1\u2013$2",
    "parenthetical": parenthetical_function,
    "for-hour": "$1 ebben az órában",
    "starting-in": "$1 $2 múlva",
    "stopping-in": "$1 $2 múlva véget ér",
    "starting-then-stopping-later": "$1 $2 múlva, $3ig",
    "stopping-then-starting-later": "$1 $2 múlva véget ér, de $3 elteltével újra várható",
    "for-day": "$1 egész nap",
    "starting": "$1 lesz $2",
    "until": "$1 $2",
    "until-starting-again": "$1 $2, majd $3 ismét",
    "starting-continuing-until": "$1 kezdődik $2, $3 folytatódik",
    "during": "$1 $2",
    "for-week": "$1 ezen a héten",
    "over-weekend": "$1 a hétvégén",
    "temperatures-peaking": "$1 csúcshőmérséklettel $2",
    "temperatures-rising": "$1-ra emelkedő hőmérséklettel $2",
    "temperatures-valleying": "$1 minimum hőmérséklettel $2",
    "temperatures-falling": "$1-ra eső hőmérséklettel $2",
    "title": title_function,
    "sentence": sentence_function,
    "next-hour-forecast-status": "next hour forecasts are $1 due to $2",
    "unavailable": "unavailable",
    "temporarily-unavailable": "temporarily unavailable",
    "partially-unavailable": "partially unavailable",
    "station-offline": "all nearby radar stations being offline",
    "station-incomplete": "gaps in coverage from nearby radar stations",
}
