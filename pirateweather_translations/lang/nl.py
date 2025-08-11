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

    return a[:i] + a[i:] + joiner + b[i:]


def today_variants(stack, a, b):
    """
    Returns 'a' if 'starting-continuing-until' is in the scope; otherwise, returns 'b'.
    """
    return a if "starting-continuing-until" in stack else b


def weekdays(stack, day):
    """
    Returns a string based on whether 'through' is in the scope.
    Prepends "op " to the day unless 'through' is in the scope.
    """
    return ("" if "through" in stack else "op ") + day


def today_morning_function(stack):
    return today_variants(stack, "de ochtend", "vanochtend")


def today_afternoon_function(stack):
    return today_variants(stack, "de middag", "vanmiddag")


def today_evening_function(stack):
    return today_variants(stack, "de avond", "vanavond")


def today_night_function(stack):
    return today_variants(stack, "de nacht", "vannacht")


def monday_function(stack):
    return weekdays(stack, "maandag")


def tuesday_function(stack):
    return weekdays(stack, "dinsdag")


def wednesday_function(stack):
    return weekdays(stack, "woensdag")


def thursday_function(stack):
    return weekdays(stack, "donderdag")


def friday_function(stack):
    return weekdays(stack, "vrijdag")


def saturday_function(stack):
    return weekdays(stack, "zaterdag")


def and_function(stack, a, b):
    return join_with_shared_prefix(a, b, ", en " if "," in a else " en ")


def through_function(stack, a, b):
    return join_with_shared_prefix(a, b, " tot en met ")


def starting_function(stack, condition, period):
    """
    Constructs a string based on the second element of the `stack` list.
    """
    if stack[1] == "starting":
        return "vanaf " + period + " " + condition

    if stack[1] == "and":
        return period + " " + condition

    return condition + " " + period


def during_function(stack, condition, period):
    """
    Constructs a string based on the second element of the `stack` list.
    """
    if stack[1] == "and":
        return period + " " + condition

    if stack[1] == "with":
        return condition + " " + period

    return condition + " gedurende " + period


def title_function(stack, s):
    return s[0].upper() + s[1:]


def sentence_function(stack, s):
    s = s[0].upper() + s[1:]
    if not s.endswith("."):
        s += "."
    return s


template = {
    "clear": "helder",
    "no-precipitation": "geen neerslag",
    "mixed-precipitation": "wisselende neerslag",
    "possible-very-light-precipitation": "mogelijk lichte neerslag",
    "very-light-precipitation": "lichte neerslag",
    "possible-light-precipitation": "mogelijk lichte neerslag",
    "light-precipitation": "lichte neerslag",
    "medium-precipitation": "neerslag",
    "heavy-precipitation": "zware neerslag",
    "possible-very-light-rain": "mogelijk lichte motregen",
    "very-light-rain": "motregen",
    "possible-light-rain": "mogelijk lichte regen",
    "light-rain": "lichte regen",
    "medium-rain": "regen",
    "heavy-rain": "zware regenbuien",
    "possible-very-light-sleet": "mogelijk lichte ijzelvorming",
    "very-light-sleet": "lichte ijzelvorming",
    "possible-light-sleet": "mogelijk lichte ijzel",
    "light-sleet": "lichte ijzel",
    "medium-sleet": "ijzel",
    "heavy-sleet": "zware ijzel",
    "possible-very-light-snow": "mogelijk lichte sneeuwval",
    "very-light-snow": "lichte sneeuwval",
    "possible-light-snow": "mogelijk sneeuwval",
    "light-snow": "sneeuwval",
    "medium-snow": "sneeuw",
    "heavy-snow": "zware sneeuwbuien",
    "possible-thunderstorm": "mogelijk onweer",
    "thunderstorm": "onweer",
    "possible-medium-precipitation": "mogelijk neerslag",
    "possible-heavy-precipitation": "mogelijk zware neerslag",
    "possible-medium-rain": "mogelijk regen",
    "possible-heavy-rain": "mogelijk zware regenbuien",
    "possible-medium-sleet": "mogelijk ijzel",
    "possible-heavy-sleet": "mogelijk zware ijzel",
    "possible-medium-snow": "mogelijk sneeuw",
    "possible-heavy-snow": "mogelijk zware sneeuwbuien",
    "possible-very-light-freezing-rain": "mogelijk ijskoude motregen",
    "very-light-freezing-rain": "ijskoude motregen",
    "possible-light-freezing-rain": "mogelijk lichte ijskoude regen",
    "light-freezing-rain": "lichte ijskoude regen",
    "possible-medium-freezing-rain": "mogelijk ijskoude regen",
    "medium-freezing-rain": "ijskoude regen",
    "possible-heavy-freezing-rain": "mogelijk ijskoude regenbuien",
    "heavy-freezing-rain": "ijskoude regenbuien",
    "possible-hail": "mogelijk hagel",
    "hail": "hagel",
    "light-wind": "lichte wind",
    "medium-wind": "veel wind",
    "heavy-wind": "zware windstoten",
    "low-humidity": "lage luchtvochtigheid",
    "high-humidity": "hoge luchtvochtigheid",
    "fog": "mist",
    "very-light-clouds": "overwegend helder",
    "light-clouds": "licht bewolkt",
    "medium-clouds": "overwegend bewolkt",
    "heavy-clouds": "zwaar bewolkt",
    "today-morning": today_morning_function,
    "later-today-morning": "later vanochtend",
    "today-afternoon": today_afternoon_function,
    "later-today-afternoon": "later vanmiddag",
    "today-evening": today_evening_function,
    "later-today-evening": "later vanavond",
    "today-night": today_night_function,
    "later-today-night": "later vannacht",
    "tomorrow-morning": "morgenochtend",
    "tomorrow-afternoon": "morgenmiddag",
    "tomorrow-evening": "morgenavond",
    "tomorrow-night": "morgennacht",
    "morning": "de ochtend",
    "afternoon": "de middag",
    "evening": "de avond",
    "night": "de nacht",
    "today": "vandaag",
    "tomorrow": "morgen",
    "sunday": "op zondag",
    "monday": monday_function,
    "tuesday": tuesday_function,
    "wednesday": wednesday_function,
    "thursday": thursday_function,
    "friday": friday_function,
    "saturday": saturday_function,
    "next-sunday": "volgende zondag",
    "next-monday": "volgende maandag",
    "next-tuesday": "volgende dinsdag",
    "next-wednesday": "volgende woensdag",
    "next-thursday": "volgende donderdag",
    "next-friday": "volgende vrijdag",
    "next-saturday": "volgende zaterdag",
    "minutes": "$1 minuten",
    "fahrenheit": "$1\u00b0F",
    "celsius": "$1\u00b0C",
    "inches": "$1 inch",
    "centimeters": "$1 cm",
    "less-than": "minder dan $1",
    "and": and_function,
    "through": through_function,
    "with": "$1 met $2",
    "range": "$1 tot $2",
    "parenthetical": "$1 ($2)",
    "for-hour": "het komende uur $1",
    "starting-in": "over $2 $1",
    "stopping-in": "$1, stopt over $2",
    "starting-then-stopping-later": "$1 begint over $2 en stopt weer $3 later",
    "stopping-then-starting-later": "$1 stopt over $2 maar begint $3 later opnieuw",
    "for-day": "$1 gedurende de dag",
    "starting": starting_function,
    "until": "$1 tot $2",
    "until-starting-again": "$1 tot $2 en $3 weer opnieuw",
    "starting-continuing-until": "$1 vanaf $2, houdt aan tot $3",
    "during": during_function,
    "for-week": "de hele week $1",
    "over-weekend": "$1 dit weekend",
    "temperatures-peaking": "een maximum temperatuur van $1 $2",
    "temperatures-rising": "temperaturen stijgend tot $1 $2",
    "temperatures-valleying": "een minimum temperatuur van $1 $2",
    "temperatures-falling": "temperaturen dalend tot $1 $2",
    "title": title_function,
    "sentence": sentence_function,
    "next-hour-forecast-status": "de eerstvolgende voorspelling is $1 omdat $2",
    "unavailable": "niet beschikbaar",
    "temporarily-unavailable": "tijdelijk niet beschikbaar",
    "partially-unavailable": "gedeeltelijk niet beschikbaar",
    "station-offline": "alle radar stations in de buurt offline zijn",
    "station-incomplete": "de dekking van radar stations in de buurt niet volledig is",
    "smoke": "rook",
    "haze": "nevel",
    "mist": "mist",
}
