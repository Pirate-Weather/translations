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
    if period.startswith("yfir nóttina"):
        return period[5:]
    elif period.startswith("um "):
        return period[3:]
    return period


def and_function(stack, a, b):
    joiner = " - " if "," in a else " og "
    return join_with_shared_prefix(a, b, joiner)


def through_function(stack, a, b):
    return join_with_shared_prefix(a, b, " þangað til ")


def until_function(stack, condition, period):
    return condition + " þangað til " + strip_prefix(period)


def until_starting_again_function(stack, condition, a, b):
    return condition + " þangað til " + strip_prefix(a) + ", byrjar aftur " + b


def starting_continuing_until_function(stack, condition, a, b):
    return condition + ", byrjar " + a + " og heldur áfram yfir " + strip_prefix(b)


def title_function(stack, s):
    return s[0].upper() + s[1:]


def sentence_function(stack, s):
    s = s[0].upper() + s[1:]
    if not s.endswith("."):
        s += "."
    return s


template = {
    "clear": "heiðskýrt",
    "no-precipitation": "engin úrkoma",
    "mixed-precipitation": "úrkoma með köflum",
    "possible-very-light-precipitation": "möguleiki á lítilsháttar úrkomu",
    "very-light-precipitation": "lítilsháttar úrkoma",
    "possible-light-precipitation": "möguleiki á smávægilegri úrkomu",
    "light-precipitation": "smávægileg úrkoma",
    "medium-precipitation": "úrkoma",
    "heavy-precipitation": "mikil úrkoma",
    "possible-very-light-rain": "líkur á úða",
    "very-light-rain": "úði",
    "possible-light-rain": "líkur á skúrum",
    "light-rain": "skúrir",
    "medium-rain": "rigning",
    "heavy-rain": "mikil rigning",
    "possible-very-light-sleet": "líkur á lítilsháttar slyddu",
    "very-light-sleet": "lítilsháttar slydda",
    "possible-light-sleet": "líkur á smávægilegri slyddu",
    "light-sleet": "smávægileg slydda",
    "medium-sleet": "slydda",
    "heavy-sleet": "mikil slydda",
    "possible-very-light-snow": "líkur á lítilsháttar snjókomu",
    "very-light-snow": "lítilsháttar snjókoma",
    "possible-light-snow": "líkur á smávægilegri snjókomu",
    "light-snow": "smávægileg snjókoma",
    "medium-snow": "snjókoma",
    "heavy-snow": "mikil snjókoma",
    "possible-thunderstorm": "líkur á þrumuveður",
    "thunderstorm": "þrumuveður",
    "possible-medium-precipitation": "möguleiki á úrkoma",
    "possible-heavy-precipitation": "möguleiki á mikil úrkoma",
    "possible-medium-rain": "líkur á rigning",
    "possible-heavy-rain": "líkur á mikil rigning",
    "possible-medium-sleet": "líkur á slydda",
    "possible-heavy-sleet": "líkur á mikil slydda",
    "possible-medium-snow": "líkur á snjókoma",
    "possible-heavy-snow": "líkur á mikil snjókoma",
    "possible-very-light-freezing-rain": "líkur á ískalt súld",
    "very-light-freezing-rain": "ískalt súld",
    "possible-light-freezing-rain": "líkur á smávægileg ískalt rigning",
    "light-freezing-rain": "smávægileg ískalt rigning",
    "possible-medium-freezing-rain": "líkur á ískalt rigning",
    "medium-freezing-rain": "ískalt rigning",
    "possible-heavy-freezing-rain": "líkur á mikil ískalt rigning",
    "heavy-freezing-rain": "mikil ískalt rigning",
    "possible-hail": "líkur á haglél",
    "hail": "haglél",
    "light-wind": "gola",
    "medium-wind": "rok",
    "heavy-wind": "hávaðarok",
    "low-humidity": "lítill raki",
    "high-humidity": "mikill raki",
    "fog": "þoka",
    "very-light-clouds": "að mestu leyti skýrt",
    "light-clouds": "skýjað að hluta til",
    "medium-clouds": "skýjað",
    "heavy-clouds": "alskýjað",
    "today-morning": "þennan morguninn",
    "later-today-morning": "seinna um morguninn",
    "today-afternoon": "þennan eftirmiðsdag",
    "later-today-afternoon": "seinnipart dags",
    "today-evening": "í kvöld",
    "later-today-evening": "seinna í kvöld",
    "today-night": "í nótt",
    "later-today-night": "seinna í nótt",
    "tomorrow-morning": "í fyrramálið",
    "tomorrow-afternoon": "seinnipart morgundags",
    "tomorrow-evening": "annað kvöld",
    "tomorrow-night": "næstu nótt",
    "morning": "um morguninn",
    "afternoon": "í síðdeginu",
    "evening": "um kvöldið",
    "night": "yfir nóttina",
    "today": "í dag",
    "tomorrow": "á morgun",
    "sunday": "á sunnudag",
    "monday": "á mánudag",
    "tuesday": "á þriðjudag",
    "wednesday": "á miðvikudag",
    "thursday": "á fimmtudag",
    "friday": "á föstudag",
    "saturday": "á laugardag",
    "next-sunday": "á sunnudag",  # FIXME
    "next-monday": "á mánudag",  # FIXME
    "next-tuesday": "á þriðjudag",  # FIXME
    "next-wednesday": "á miðvikudag",  # FIXME
    "next-thursday": "á fimmtudag",  # FIXME
    "next-friday": "á föstudag",  # FIXME
    "next-saturday": "á laugardag",  # FIXME
    "minutes": "$1 mín.",
    "fahrenheit": "$1\u00b0F",
    "celsius": "$1\u00b0C",
    "inches": "$1 in.",
    "centimeters": "$1 cm.",
    "less-than": "undir $1",
    "and": and_function,
    "through": through_function,
    "with": "$1, með $2",
    "range": "$1\u2013$2",
    "parenthetical": "$1 ($2)",
    "for-hour": "$1 næsta klukkutímann",
    "starting-in": "$1 sem byrjar eftir $2",
    "stopping-in": "$1, líkur eftir $2",
    "starting-then-stopping-later": "$1 sem byrjar eftir $2, líkur $3 seinna",
    "stopping-then-starting-later": "$1 sem líkur eftir $2, byrjar aftur $3 seinna",
    "for-day": "$1 yfir daginn",
    "starting": "$1, byrjar $2",
    "until": until_function,
    "until-starting-again": until_starting_again_function,
    "starting-continuing-until": starting_continuing_until_function,
    "during": "$1 $2",
    "for-week": "$1 yfir vikuna",
    "over-weekend": "$1 yfir helgina",
    "temperatures-peaking": "hita upp að $1 $2",
    "temperatures-rising": "hita að nálgast $1 $2",
    "temperatures-valleying": "hita niður í $1 $2",
    "temperatures-falling": "hita að falla niður í $1 $2",
    "title": title_function,
    "sentence": sentence_function,
    "next-hour-forecast-status": "spár fyrir næstu klukkustund eru $1 vegna $2",
    "unavailable": "ófáanlegt",
    "temporarily-unavailable": "tímabundið ófáanlegt",
    "partially-unavailable": "að hluta til ófáanlegt",
    "station-offline": "allar ratsjárstöðvar í nágrenninu eru ótengdar",
    "station-incomplete": "eyður í umfjöllun frá ratsjárstöðvum í nágrenninu",
    "smoke": "reykur",
    "haze": "þoka",
    "mist": "mistur",
}
