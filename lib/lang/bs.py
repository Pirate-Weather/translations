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
    return join_with_shared_prefix(a, b, ", i " if "," in a else " i ")


def through_function(stack, a, b):
    return join_with_shared_prefix(a, b, " do ")


def title_function(stack, s):
    # Apply custom_capitalize to every word
    return s[0].upper() + s[1:]


def sentence_function(stack, s):
    s = s[0].upper() + s[1:]
    if not s.endswith("."):
        s += "."
    return s


template = {
    "clear": "vedro",
    "no-precipitation": "nema padavina",
    "mixed-precipitation": "različite padavine",
    "possible-very-light-precipitation": "moguće su slabe padavine",
    "very-light-precipitation": "slabe padavine",
    "possible-light-precipitation": "moguće su slabe padavine",
    "light-precipitation": "slabe padavine",
    "medium-precipitation": "padavine",
    "heavy-precipitation": "jake padavine",
    "possible-very-light-rain": "moguće je sitna kiša",
    "very-light-rain": "sitna kiša",
    "possible-light-rain": "moguće je sitna kiša",
    "light-rain": "sitna kiša",
    "medium-rain": "kiša",
    "heavy-rain": "jaka kiša",
    "possible-very-light-sleet": "moguće je slaba susnježica",
    "very-light-sleet": "slaba susnježica",
    "possible-light-sleet": "moguće je slaba susnježica",
    "light-sleet": "slaba susnježica",
    "medium-sleet": "susnježica",
    "heavy-sleet": "jaka susnježica",
    "possible-very-light-snow": "moguće je sitan snijeg",
    "very-light-snow": "sitan snijeg",
    "possible-light-snow": "moguće je sitan snijeg",
    "light-snow": "sitan snijeg",
    "medium-snow": "snijeg",
    "heavy-snow": "jak snijeg",
    "possible-thunderstorm": "moguće je grmljavine",
    "thunderstorm": "grmljavine",
    "possible-medium-precipitation": "moguće su padavine",
    "possible-heavy-precipitation": "moguće su jake padavine",
    "possible-medium-rain": "moguće je kiša",
    "possible-heavy-rain": "moguće je jaka kiša",
    "possible-medium-sleet": "moguće je susnježica",
    "possible-heavy-sleet": "moguće je jaka susnježica",
    "possible-medium-snow": "moguće je snijeg",
    "possible-heavy-snow": "moguće je jaka snijeg",
    "possible-freezing-drizzle": "moguće je ledena kiša",
    "freezing-drizzle": "ledena kiša",
    "possible-light-freezing-rain": "moguće je sitan ledena kiša",
    "light-freezing-rain": "sitan ledena kiša",
    "possible-freezing-rain": "moguće je ledena kiša",
    "freezing-rain": "ledena kiša",
    "possible-heavy-freezing-rain": "moguće je jaka ledena kiša",
    "heavy-freezing-rain": "jaka ledena kiša",
    "possible-hail": "moguća grmljavina sa gradom",
    "hail": "grmljavina sa gradom",
    "light-wind": "vjetrovito",
    "medium-wind": "vjetrovito",
    "heavy-wind": "opasno vjetrovito",
    "low-humidity": "suho",
    "high-humidity": "vlažno",
    "fog": "maglovito",
    "very-light-clouds": "pretežno vedro",
    "light-clouds": "djelom oblačno",
    "medium-clouds": "pretežno oblačno",
    "heavy-clouds": "oblačno",
    "today-morning": "ovo jutro",
    "later-today-morning": "kasnije ovog jutra",
    "today-afternoon": "ove podne",
    "later-today-afternoon": "kasnije ove podne",
    "today-evening": "večeras",
    "later-today-evening": "kasnije večeras",
    "today-night": "u noć",
    "later-today-night": "kasnije u noć",
    "tomorrow-morning": "sutra ujutro",
    "tomorrow-afternoon": "sutra popodne",
    "tomorrow-evening": "sutra uveče",
    "tomorrow-night": "sutra u noć",
    "morning": "ujutro",
    "afternoon": "popodne",
    "evening": "uveče",
    "night": "u noć",
    "today": "danas",
    "tomorrow": "sutra",
    "sunday": "u nedjelju",
    "monday": "u ponedjeljak",
    "tuesday": "u utorak",
    "wednesday": "u srijeda",
    "thursday": "u četvrtak",
    "friday": "u petak",
    "saturday": "u subotu",
    "next-sunday": "u nedjelju",  # FIXME
    "next-monday": "u ponedjeljak",  # FIXME
    "next-tuesday": "u utorak",  # FIXME
    "next-wednesday": "u srijeda",  # FIXME
    "next-thursday": "u četvrtak",  # FIXME
    "next-friday": "u petak",  # FIXME
    "next-saturday": "u subotu",  # FIXME
    "minutes": "$1 minuta",
    "fahrenheit": "$1\u00b0F",
    "celsius": "$1\u00b0C",
    "inches": "$1 inča",
    "centimeters": "$1 centimetra",
    "less-than": "ispod $1",
    "and": and_function,
    "through": through_function,
    "with": "$1, sa $2",
    "range": "$1\u2013$2",
    "parenthetical": "$1 ($2)",
    "for-hour": "$1 za ovaj sat",
    "starting-in": "$1 počinje za $2",
    "stopping-in": "$1 prekida za $2",
    "starting-then-stopping-later": "$1 počinje za $2, ondak prekida za $3",
    "stopping-then-starting-later": "$1 prekida za $2, ondak počinje za $3",
    "for-day": "$1 tokom cijelog dana",
    "starting": "$1 počinje $2",
    "until": "$1 do $2",
    "until-starting-again": "$1 do $2, i opet poćinje $3",
    "starting-continuing-until": "$1 poćinje $2, ostaje do $3",
    "during": "$1 $2",
    "for-week": "$1 tokom sedmice",
    "over-weekend": "$1 tokom vikenda",
    "temperatures-peaking": "temperaturom najviše do $1 $2",
    "temperatures-rising": "temperaturom raste do $1 $2",
    "temperatures-valleying": "temperaturom najniže do $1 $2",
    "temperatures-falling": "temperaturom pada do $1 $2",
    "title": title_function,
    "sentence": sentence_function,
    "next-hour-forecast-status": "next hour forecasts are $1 due to $2",
    "unavailable": "unavailable",
    "temporarily-unavailable": "temporarily unavailable",
    "partially-unavailable": "partially unavailable",
    "station-offline": "all nearby radar stations being offline",
    "station-incomplete": "gaps in coverage from nearby radar stations",
}
