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
    "täna": ["tänasest", None],
    "homme": ["homsest", "homseni"],
    "öösel": ["ööst", "ööni"],
    "õhtu": ["õhtust", "õhtuni"],
    "hommikul": ["hommikust", "hommikuni"],
    "õhtul": ["õhtust", "õhtuni"],
    "pärastlõunal": ["pärastlõunast", "pärastlõunani"],
    "homme hommikul": ["homme hommikust", "homse hommikuni"],
    "hiljem õhtul": ["hilisemast õhtust", "hilisema õhtuni"],
    "hiljem öösel": ["hilisemast ööst", "hilisema ööni"],
    "homme pärastlõunal": ["homsest pärastlõunast", "homse pärastlõunani"],
    "homme õhtul": ["homsest õhtust", "homse õhtuni"],
    "homme öösel": ["homsest ööst", "homse ööni"],
    "pühapäeval": ["pühapäevast", "pühapäevani"],
    "esmaspäeval": ["esmaspäevast", "esmaspäevani"],
    "teisipäeval": ["teisipäevast", "teisipäevani"],
    "kolmapäeval": ["kolmapäevast", "kolmapäevani"],
    "neljapäeval": ["neljapäevast", "neljapäevani"],
    "reedel": ["reedest", "reedeni"],
    "laupäeval": ["laupäevast", "laupäevani"],
    "järgmisel pühapäeval": ["järgmisest pühapäevast", "järgmise pühapäevani"],
    "järgmisel esmaspäeval": ["järgmisest esmaspäevast", "järgmise esmaspäevani"],
    "järgmisel teisipäeval": ["järgmisest teisipäevast", "järgmise teisipäevani"],
    "järgmisel kolmapäeval": ["järgmisest kolmapäevast", "järgmise kolmapäevani"],
    "järgmisel neljapäeval": ["järgmisest neljapäevast", "järgmise neljapäevani"],
    "järgmisel reedel": ["järgmisest reedest", "järgmise reedeni"],
    "järgmisel laupäeval": ["järgmisest laupäevast", "järgmise laupäevani"],
}


def elative(word):
    """Get the elative form of a word."""
    return grammar.get(word, [word])[0]


def illative(word):
    """Get the illative form of a word."""
    return grammar.get(word, [None, word])[1]


def and_function(stack, a, b):
    return join_with_shared_prefix(a, b, " ja ")


def through_function(stack, a, b):
    a = elative(a)
    b = illative(b)
    if a and b:
        return f"{a} kuni {b}"
    elif a or b:
        return f"{a or b} kuni"
    else:
        return ""


def starting_function(stack, condition, period):
    return condition + " alates " + elative(period)


def until_function(stack, condition, period):
    return condition + " kuni " + illative(period)


def until_starting_again_function(stack, condition, a, b):
    return condition + " " + illative(a) + ", ja jälle " + b


def starting_continuing_until_function(stack, condition, a, b):
    return condition + " " + elative(a) + " " + illative(b)


def title_function(stack, s):
    # Apply custom_capitalize to every word
    return s[0].upper() + s[1:]


def sentence_function(stack, s):
    s = s[0].upper() + s[1:]
    if not s.endswith("."):
        s += "."
    return s


template = {
    "clear": "selge",
    "no-precipitation": "kuiv",
    "mixed-precipitation": "erinevad sademed",
    "possible-very-light-precipitation": "nõrga saju võimalus",
    "very-light-precipitation": "nõrk sadu",
    "possible-light-precipitation": "kerge saju võimalus",
    "light-precipitation": "kerge sadu",
    "medium-precipitation": "mõõdukas sadu",
    "heavy-precipitation": "tugev sadu",
    "possible-very-light-rain": "nõrga vihmasaju võimalus",
    "very-light-rain": "nõrk vihmasadu",
    "possible-light-rain": "kerge vihmasaju võimalus",
    "light-rain": "kerge vihmasadu",
    "medium-rain": "mõõdukas vihmasadu",
    "heavy-rain": "tugev vihmasadu",
    "possible-very-light-sleet": "nõrga lörtsisaju võimalus",
    "very-light-sleet": "nõrk lörtsisadu",
    "possible-light-sleet": "kerge lörtsisaju võimalus",
    "light-sleet": "kerge lörtsisadu",
    "medium-sleet": "mõõdukas lörtsisadu",
    "heavy-sleet": "tugev lörtsisadu",
    "possible-very-light-snow": "nõrga lumesaju võimalus",
    "very-light-snow": "nõrk lumesadu",
    "possible-light-snow": "kerge lumesaju võimalus",
    "light-snow": "kerge lumesadu",
    "medium-snow": "mõõdukas lumesadu",
    "heavy-snow": "tugev lumesadu",
    "possible-thunderstorm": "äikesetormi võimalus",
    "thunderstorm": "äikesetorm",
    "possible-medium-precipitation": "mõõdukas sadu võimalus",
    "possible-heavy-precipitation": "tugev sadu võimalus",
    "possible-medium-rain": "mõõdukas vihmasadu võimalus",
    "possible-heavy-rain": "tugev vihmasadu võimalus",
    "possible-medium-sleet": "mõõdukas lörtsisadu võimalus",
    "possible-heavy-sleet": "tugev lörtsisadu võimalus",
    "possible-medium-snow": "mõõdukas lumesadu võimalus",
    "possible-heavy-snow": "tugev lumesadu võimalus",
    "possible-very-light-freezing-rain": "jääkülma nõrk vihmasadu võimalus",
    "very-light-freezing-rain": "jääkülma nõrk vihmasadu",
    "possible-light-freezing-rain": "kerge jääkülma vihmasadu võimalus",
    "light-freezing-rain": "kerge jääkülma vihmasadu",
    "possible-medium-freezing-rain": "jääkülma mõõdukas vihmasadu võimalus",
    "medium-freezing-rain": "freezing mõõdukas vihmasadu",
    "possible-heavy-freezing-rain": "tugev jääkülma vihmasadu võimalus",
    "heavy-freezing-rain": "tugev jääkülma vihmasadu",
    "possible-hail": "rahe võimalus",
    "hail": "rahe",
    "light-wind": "kerge tuul",
    "medium-wind": "mõõdukas tuul",
    "heavy-wind": "tugev tuul",
    "low-humidity": "kuiv",
    "high-humidity": "niiske",
    "fog": "udu",
    "very-light-clouds": "enamasti selge",
    "light-clouds": "vähene pilvisus",
    "medium-clouds": "mõõdukas pilvisus",
    "heavy-clouds": "pilves",
    "today-morning": "hommikul",
    "later-today-morning": "hiljem täna hommikul",
    "today-afternoon": "pärastlõunal",
    "later-today-afternoon": "hiljem pärastlõunal",
    "today-evening": "õhtul",
    "later-today-evening": "hiljem õhtul",
    "today-night": "öösel",
    "later-today-night": "hiljem öösel",
    "tomorrow-morning": "homme hommikul",
    "tomorrow-afternoon": "homme pärastlõunal",
    "tomorrow-evening": "homme õhtul",
    "tomorrow-night": "homme öösel",
    "morning": "hommikul",
    "afternoon": "pärastlõunal",
    "evening": "õhtul",
    "night": "öösel",
    "today": "täna",
    "tomorrow": "homme",
    "sunday": "pühapäeval",
    "monday": "esmaspäeval",
    "tuesday": "teisipäeval",
    "wednesday": "kolmapäeval",
    "thursday": "neljapäeval",
    "friday": "reedel",
    "saturday": "laupäeval",
    "next-sunday": "järgmisel pühapäeval",
    "next-monday": "järgmisel esmaspäeval",
    "next-tuesday": "järgmisel teisipäeval",
    "next-wednesday": "järgmisel kolmapäeval",
    "next-thursday": "järgmisel neljapäeval",
    "next-friday": "järgmisel reedel",
    "next-saturday": "järgmisel laupäeval",
    "minutes": "$1 min.",
    "fahrenheit": "$1\u00b0F",
    "celsius": "$1\u00b0C",
    "inches": "$1 tolli",
    "centimeters": "$1 cm",
    "less-than": "alla $1",
    "and": and_function,
    "through": through_function,
    "with": "$1, $2",
    "range": "$1\u2013$2",
    "parenthetical": "$1 ($2)",
    "for-hour": "$1 järgmised tund aega",
    "starting-in": "$1 oodata $2 pärast",
    "stopping-in": "$1 lõppeb $2 pärast",
    "starting-then-stopping-later": "$1 algab $2 pärast, lõppeb $3 hiljem",
    "stopping-then-starting-later": "$1 lõppeb $2 pärast, algab uuesti $3 hiljem",
    "for-day": "Terve päev on $1",
    "starting": starting_function,
    "until": until_function,
    "until-starting-again": until_starting_again_function,
    "starting-continuing-until": starting_continuing_until_function,
    "during": "$1 $2",
    "for-week": "$1 nädal aega",
    "over-weekend": "$1 nädalavahetusel",
    "temperatures-peaking": "temperatuur tõuseb $2 kuni $1",
    "temperatures-rising": "temperatuur tõuseb $2 kuni $1",
    "temperatures-valleying": "temperatuur langeb $2 kuni $1",
    "temperatures-falling": "temperatuur langeb $2 kuni $1",
    "title": title_function,
    "sentence": sentence_function,
    "next-hour-forecast-status": "järgmise tunni prognoosid on $1 kuni $2",
    "unavailable": "pole saadaval",
    "temporarily-unavailable": "ajutiselt kättesaamatu",
    "partially-unavailable": "osaliselt kättesaamatu",
    "station-offline": "kõik lähedalasuvad radarijaamad on võrguühenduseta",
    "station-incomplete": "lähedalasuvate radarijaamade leviala lüngad",
    "smoke": "suits",
    "haze": "udu",
    "mist": "uduvihm",
}
