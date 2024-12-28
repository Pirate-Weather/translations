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
    "no rīta": ["rīta", "rītam"],
    "vēlāk no rīta": ["rīta", "rītam"],
    "pēcpusdienā": ["pēcpusdienas", "pēcpusdienai"],
    "vēlāk pēcpusdienā": ["pēcpusdienas", "pēcpusdienai"],
    "vakarā": ["vakara", "vakaram"],
    "vēlāk vakarā": ["vakara", "vakaram"],
    "naktī": ["nakts", "naktij"],
    "vēlāk naktī": ["nakts", "naktij"],
    "rīt no rīta": ["rītdienas rīta", "rītdienas rītam"],
    "rīt pēcpusdienā": ["rītdienas pēcpusdienas", "rītdienas pēcpusdienai"],
    "rītvakar": ["rītvakara", "rītvakaram"],
    "rīt naktī": ["rītdienas nakts", "rītdienas naktij"],
    "šodien": ["šodienas", "šodienai"],
    "rīt": ["rītdienas", "rītdienai"],
    "svētdien": ["svētdienas", "svētdienai"],
    "pirmdien": ["pirmdienas", "pirmdienai"],
    "otrdien": ["otrdienas", "otrdienai"],
    "trešdien": ["trešdienas", "trešdienai"],
    "ceturtdien": ["ceturtdienas", "ceturtdienai"],
    "piektdien": ["piektdienas", "piektdienai"],
    "sestdien": ["sestdienas", "sestdienai"],
    "nākamsvētdien": ["nākamās svētdienas", "nākamai svētdienai"],
    "nākampirmdien": ["nākamās pirmdienas", "nākamai pirmdienai"],
    "nākamotrdien": ["nākamās otrdienas", "nākamai otrdienai"],
    "nākamtrešdien": ["nākamās trešdienas", "nākamai trešdienai"],
    "nākamceturtdien": ["nākamās ceturtdienas", "nākamai ceturtdienai"],
    "nākampiektdien": ["nākamās piektdienas", "nākamai piektdienai"],
    "nākamsestdien": ["nākamās sestdienas", "nākamai sestdienai"],
}


def accusativus(word):
    return grammar[word][0] if word in grammar else word


def dativus(word):
    return grammar[word][1] if word in grammar else word


def and_function(stack, a, b):
    return join_with_shared_prefix(a, b, " un ")


def through_function(stack, a, b):
    return "no " + accusativus(a) + " līdz " + dativus(b)


def starting_function(stack, a, b):
    if a == "daļēji mākoņains" or a == "pārsvarā mākoņains" or a == "apmācies":
        return b + " būs " + a

    return b + " sāksies " + a


def until_function(stack, condition, period):
    return condition + " līdz " + dativus(period)


def until_starting_again_function(stack, condition, a, b):
    return condition + " līdz " + dativus(a) + ", atsāksies " + b


def starting_continuing_until_function(stack, condition, a, b):
    return "no " + accusativus(a) + " līdz " + dativus(b) + " " + condition


def title_function(stack, s):
    return s[0].upper() + s[1:]


def sentence_function(stack, s):
    s = s[0].upper() + s[1:]

    if not s.endswith("."):
        s += "."
    return s


template = {
    "clear": "skaidrs",
    "no-precipitation": "bez nokrišņiem",
    "mixed-precipitation": "jaukti nokrišņi",
    "possible-very-light-precipitation": "iespējami nelieli nokrišņi",
    "very-light-precipitation": "nelieli nokrišņi",
    "possible-light-precipitation": "iespējami nelieli nokrišņi",
    "light-precipitation": "nelieli nokrišņi",
    "medium-precipitation": "nokrišņi",
    "heavy-precipitation": "stipri nokrišņi",
    "possible-very-light-rain": "iespējams smidzinošs lietus",
    "very-light-rain": "smidzinošs lietus",
    "possible-light-rain": "iespējams neliels lietus",
    "light-rain": "neliels lietus",
    "medium-rain": "lietus",
    "heavy-rain": "stiprs lietus",
    "possible-very-light-sleet": "iespējams neliels slapjš sniegs",
    "very-light-sleet": "neliels slapjš sniegs",
    "possible-light-sleet": "iespējams neliels slapjš sniegs",
    "light-sleet": "neliels slapjš sniegs",
    "medium-sleet": "slapjš sniegs",
    "heavy-sleet": "stiprs slapjš sniegs",
    "possible-very-light-snow": "iespējams neliels sniegs",
    "very-light-snow": "neliels sniegs",
    "possible-light-snow": "iespējams neliels sniegs",
    "light-snow": "neliels sniegs",
    "medium-snow": "sniegs",
    "heavy-snow": "stiprs sniegs",
    "possible-thunderstorm": "iespējams negaiss",
    "thunderstorm": "negaiss",
    "possible-medium-precipitation": "possible precipitation",
    "possible-heavy-precipitation": "possible heavy precipitation",
    "possible-medium-rain": "possible rain",
    "possible-heavy-rain": "possible heavy rain",
    "possible-medium-sleet": "possible sleet",
    "possible-heavy-sleet": "possible heavy sleet",
    "possible-medium-snow": "possible snow",
    "possible-heavy-snow": "possible heavy snow",
    "possible-freezing-drizzle": "possible freezing drizzle",
    "freezing-drizzle": "freezing drizzle",
    "possible-light-freezing-rain": "possible light freezing rain",
    "light-freezing-rain": "light freezing rain",
    "possible-freezing-rain": "possible freezing rain",
    "freezing-rain": "freezing rain",
    "possible-heavy-freezing-rain": "possible heavy freezing rain",
    "heavy-freezing-rain": "heavy freezing rain",
    "possible-hail": "possible hail",
    "hail": "hail",
    "light-wind": "lēns vējš",
    "medium-wind": "vējš",
    "heavy-wind": "stiprs vējš",
    "low-humidity": "sauss",
    "high-humidity": "mitrs",
    "fog": "migla",
    "very-light-clouds": "pārsvarā skaidrs",
    "light-clouds": "daļēji mākoņains",
    "medium-clouds": "pārsvarā mākoņains",
    "heavy-clouds": "apmācies",
    "today-morning": "no rīta",
    "later-today-morning": "vēlāk no rīta",
    "today-afternoon": "pēcpusdienā",
    "later-today-afternoon": "vēlāk pēcpusdienā",
    "today-evening": "vakarā",
    "later-today-evening": "vēlāk vakarā",
    "today-night": "naktī",
    "later-today-night": "vēlāk naktī",
    "tomorrow-morning": "rīt no rīta",
    "tomorrow-afternoon": "rīt pēcpusdienā",
    "tomorrow-evening": "rītvakar",
    "tomorrow-night": "rīt naktī",
    "morning": "no rīta",
    "afternoon": "pēcpusdienā",
    "evening": "vakarā",
    "night": "naktī",
    "today": "šodien",
    "tomorrow": "rīt",
    "sunday": "svētdien",
    "monday": "pirmdien",
    "tuesday": "otrdien",
    "wednesday": "trešdien",
    "thursday": "ceturtdien",
    "friday": "piektdien",
    "saturday": "sestdien",
    "next-sunday": "nākamsvētdien",
    "next-monday": "nākampirmdien",
    "next-tuesday": "nākamotrdien",
    "next-wednesday": "nākamtrešdien",
    "next-thursday": "nākamceturtdien",
    "next-friday": "nākampiektdien",
    "next-saturday": "nākamsestdien",
    "minutes": "$1 min.",
    "fahrenheit": "$1\u00b0F",
    "celsius": "$1\u00b0C",
    "inches": "$1 collas",
    "centimeters": "$1 cm.",
    "less-than": "< $1",
    "and": and_function,
    "through": through_function,
    "with": "$1, $2",
    "range": "$1\u2013$2",
    "parenthetical": "$1 ($2)",
    "for-hour": "nākamo stundu $1",
    "starting-in": "$1 sāksies nākamo $2 laikā",
    "stopping-in": "$1 beigsies nākamo $2 laikā",
    "starting-then-stopping-later": "$1 sāksies $2 laikā, beigsies $3 vēlāk",
    "stopping-then-starting-later": "$1 beigsies $2 laikā, atsāksies $3 vēlāk",
    "for-day": "visu dienu $1",
    "starting": starting_function,
    "until": until_function,
    "until-starting-again": until_starting_again_function,
    "starting-continuing-until": starting_continuing_until_function,
    "during": "$2 $1",
    "for-week": "šonedēļ $1",
    "over-weekend": "nedēļas nogalē $1",
    "temperatures-peaking": "ar augstāko temperatūru $1 $2",
    "temperatures-rising": "temperatūrai sasniedzot $1 $2",
    "temperatures-valleying": "ar zemāko temperatūru $1 $2",
    "temperatures-falling": "temperatūrai nokrītoties līdz $1 $2",
    "title": title_function,
    "sentence": sentence_function,
    "next-hour-forecast-status": "tuvākās stundas laikā, laikaziņas ir $1 jo $2",
    "unavailable": "nepieejamas,",
    "temporarily-unavailable": "īslaicīgi nepieejamas,",
    "partially-unavailable": "daļēji nepieejamas,",
    "station-offline": "nav pieejami apgabala staciju radari",
    "station-incomplete": "ir traucējumi starp staciju radariem",
}
