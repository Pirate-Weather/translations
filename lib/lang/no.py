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


def strip_prefix(period):
    if period.startswith("över natten "):
        return period[12:]
    elif period.startswith("under "):
        return period[:6]
    return period


def and_function(stack, a, b):
    """
    Combines two strings with a shared prefix and an appropriate joiner.
    """
    joiner = " og " if "," not in a else " og "
    return join_with_shared_prefix(a, b, joiner)


def through_function(stack, a, b):
    return join_with_shared_prefix(a, b, " fram til ")


def until_function(stack, condition, period):
    return condition + " fram til " + strip_prefix(period)


def until_starting_again_function(stack, condition, a, b):
    return condition + " fram til " + strip_prefix(a) + ", som starter igjen " + b


def starting_continuing_until_function(stack, condition, a, b):
    return condition + " som starter " + a + ", fortsetter fram til " + strip_prefix(b)


def title_function(stack, s):
    """
    Capitalize the sentence (but not each word).
    """
    return s[0].upper() + s[1:]


def sentence_function(stack, s):
    """
    Add a period if there isn't already one.
    """
    s = s[0].upper() + s[1:]
    if not s.endswith("."):
        s += "."
    return s


template = {
    "clear": "klart",
    "no-precipitation": "ingen målbar nedbør",
    "mixed-precipitation": "blandet nedbør",
    "possible-very-light-precipitation": "sjanse for veldig lett nedbør",
    "very-light-precipitation": "veldig lett nedbør",
    "possible-light-precipitation": "sjanse for lett nedbør",
    "light-precipitation": "lett nedbør",
    "medium-precipitation": "nedbør",
    "heavy-precipitation": "kraftig regn",
    "possible-very-light-rain": "sjanse for lett duskregn",
    "very-light-rain": "duskregn",
    "possible-light-rain": "sjanse for lette regnbyger",
    "light-rain": "regnbyger",
    "medium-rain": "regn",
    "heavy-rain": "kraftige regnbyger",
    "possible-very-light-sleet": "sjanse for veldig lett sludd",
    "very-light-sleet": "veldig lett sludd",
    "possible-light-sleet": "sjanse for lett sludd",
    "light-sleet": "lett sludd",
    "medium-sleet": "sludd",
    "heavy-sleet": "kraftig sludd",
    "possible-very-light-snow": "sjanse for vedlig lett snø",
    "very-light-snow": "veldig lett snø",
    "possible-light-snow": "sjanse for lett snø",
    "light-snow": "lett snø",
    "medium-snow": "snø",
    "heavy-snow": "rikelig med snø",
    "possible-thunderstorm": "tordenvær kan forekomme",
    "thunderstorm": "tordenvær",
    "possible-medium-precipitation": "sjanse for nedbør",
    "possible-heavy-precipitation": "sjanse for kraftig regn",
    "possible-medium-rain": "sjanse for regn",
    "possible-heavy-rain": "sjanse for kraftige regnbyger",
    "possible-medium-sleet": "sjanse for sludd",
    "possible-heavy-sleet": "sjanse for kraftig sludd",
    "possible-medium-snow": "sjanse for snø",
    "possible-heavy-snow": "sjanse for rikelig med snø",
    "possible-very-light-freezing-rain": "sjanse for underkjølt duskregn",
    "very-light-freezing-rain": "underkjølt duskregn",
    "possible-light-freezing-rain": "sjanse for lett underkjølt regn",
    "light-freezing-rain": "lett underkjølt regn",
    "possible-medium-freezing-rain": "sjanse for underkjølt regn",
    "medium-freezing-rain": "underkjølt regn",
    "possible-heavy-freezing-rain": "sjanse for kraftig underkjølt regn",
    "heavy-freezing-rain": "kraftig underkjølt regn",
    "possible-hail": "sjanse for hagl",
    "hail": "hagl",
    "light-wind": "lett vind",
    "medium-wind": "sterk vind",
    "heavy-wind": "storm",
    "low-humidity": "tørke",
    "high-humidity": "fuktig",
    "fog": "tåke",
    "very-light-clouds": "stort sett klart",
    "light-clouds": "lettskyet",
    "medium-clouds": "skyet",
    "heavy-clouds": "overskyet",
    "today-morning": "i løpet av formiddagen",
    "later-today-morning": "senere på morgenen",
    "today-afternoon": "på ettermiddagen",
    "later-today-afternoon": "senere på ettermiddagen",
    "today-evening": "i løpet av kvelden",
    "later-today-evening": "senere på kvelden",
    "today-night": "i kveld",
    "later-today-night": "senere i kveld",
    "tomorrow-morning": "i morgen tidlig",
    "tomorrow-afternoon": "i morgen ettermiddag",
    "tomorrow-evening": "i morgen kveld",
    "tomorrow-night": "i morgen natt",
    "morning": "om morgenen",
    "afternoon": "på ettermiddagen",
    "evening": "om kvelden",
    "night": "om natten",
    "today": "i dag",
    "tomorrow": "i morgen",
    "sunday": "på søndag",
    "monday": "på mandag",
    "tuesday": "på tirsdag",
    "wednesday": "på onsdag",
    "thursday": "på torsdag",
    "friday": "på fredag",
    "saturday": "på lørdag",
    "next-sunday": "neste søndag",
    "next-monday": "neste mandag",
    "next-tuesday": "neste tirsdag",
    "next-wednesday": "neste onsdag",
    "next-thursday": "neste torsdag",
    "next-friday": "neste fredag",
    "next-saturday": "neste lørdag",
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
    "for-hour": "$1 i løpet av de neste timene",
    "starting-in": "$1 som starter om $2",
    "stopping-in": "$1 som avtar om $2",
    "starting-then-stopping-later": "$1 som starter om $2, avtar $3 senere",
    "stopping-then-starting-later": "$1 avtar om $2, starter igjen $3 senere",
    "for-day": "$1 i løpet av dagen",
    "starting": "$1 som starter $2",
    "until": until_function,
    "until-starting-again": until_starting_again_function,
    "starting-continuing-until": starting_continuing_until_function,
    "during": "$1 $2",
    "for-week": "$1 i løpet av uken",
    "over-weekend": "$1 over helgen",
    "temperatures-peaking": "temperaturer opptil $1 $2",
    "temperatures-rising": "temperaturer som stiger til $1 $2",
    "temperatures-valleying": "temperaturer som stopper på $1 $2",
    "temperatures-falling": "temperaturer som synker til $1 $2",
    "title": title_function,
    "sentence": sentence_function,
    "next-hour-forecast-status": "Værvarsel for neste time er $1 på grunn av $2.",
    "unavailable": "ikke tilgjengelig",
    "temporarily-unavailable": "midertidlig ikke tilgjengelig",
    "partially-unavailable": "delvis ikke tilgjengelig",
    "station-offline": "ingen kontakt med radarstasjoner i nærheten",
    "station-incomplete": "hull i dekningen fra radarstasjoner i nærheten",
}
