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
    return s[0].upper() + s[1:]


def sentence_function(stack, s):
    s = s[0].upper() + s[1:]
    if not s.endswith("."):
        s += "."
    return s


template = {
    "clear": "vedro",
    "no-precipitation": "nema padalina",
    "mixed-precipitation": "mješavina padalina",
    "possible-very-light-precipitation": "moguće su slabe padaline",
    "very-light-precipitation": "slabe padaline",
    "possible-light-precipitation": "moguće su slabe padaline",
    "light-precipitation": "slabe padaline",
    "medium-precipitation": "padaline",
    "heavy-precipitation": "jake padaline",
    "possible-very-light-rain": "moguća je sitna kiša",
    "very-light-rain": "sitna kiša",
    "possible-light-rain": "moguća je sitna kiša",
    "light-rain": "sitna kiša",
    "medium-rain": "kiša",
    "heavy-rain": "jaka kiša",
    "possible-very-light-sleet": "moguća je slaba susnježica",
    "very-light-sleet": "slaba susnježica",
    "possible-light-sleet": "moguća je slaba susnježica",
    "light-sleet": "slaba susnježica",
    "medium-sleet": "susnježica",
    "heavy-sleet": "jaka susnježica",
    "possible-very-light-snow": "moguć je sitan snijeg",
    "very-light-snow": "sitan snijeg",
    "possible-light-snow": "moguć je sitan snijeg",
    "light-snow": "sitan snijeg",
    "medium-snow": "snijeg",
    "heavy-snow": "jak snijeg",
    "possible-thunderstorm": "moguća grmljavina",
    "thunderstorm": "grmljavina",
    "possible-medium-precipitation": "moguće su padaline",
    "possible-heavy-precipitation": "moguće su jake padaline",
    "possible-medium-rain": "moguća je kiša",
    "possible-heavy-rain": "moguća je jaka kiša",
    "possible-medium-sleet": "possible susnježica",
    "possible-heavy-sleet": "possible jaka susnježica",
    "possible-medium-snow": "moguć je snijeg",
    "possible-heavy-snow": "moguć je jak snijeg",
    "possible-very-light-freezing-rain": "moguća je ledena sitna kiša",
    "very-light-freezing-rain": "ledena sitna kiša",
    "possible-light-freezing-rain": "moguća je ledena sitna kiša",
    "light-freezing-rain": "ledena sitna kiša",
    "possible-medium-freezing-rain": "moguća je ledena kiša",
    "medium-freezing-rain": "ledena kiša",
    "possible-heavy-freezing-rain": "moguća je jaka ledena kiša",
    "heavy-freezing-rain": "jaka ledena kiša",
    "possible-hail": "moguća tuča",
    "hail": "tuča",
    "light-wind": "malo vjetrovito",
    "medium-wind": "vjetrovito",
    "heavy-wind": "jako vjetrovito",
    "low-humidity": "suho",
    "high-humidity": "vlažno",
    "fog": "maglovito",
    "very-light-clouds": "pretežno vedro",
    "light-clouds": "djelomice oblačno",
    "medium-clouds": "pretežno oblačno",
    "heavy-clouds": "oblačno",
    "today-morning": "ovo jutro",
    "later-today-morning": "kasnije ovog jutra",
    "today-afternoon": "poslijepodne",
    "later-today-afternoon": "kasnije poslijepodne",
    "today-evening": "večeras",
    "later-today-evening": "kasnije večeras",
    "today-night": "noćas",
    "later-today-night": "kasnije noćas",
    "tomorrow-morning": "sutra ujutro",
    "tomorrow-afternoon": "sutra popodne",
    "tomorrow-evening": "sutra navečer",
    "tomorrow-night": "sutra u noći",
    "morning": "ujutro",
    "afternoon": "popodne",
    "evening": "navečer",
    "night": "u noći",
    "today": "danas",
    "tomorrow": "sutra",
    "sunday": "u nedjelju",
    "monday": "u ponedjeljak",
    "tuesday": "u utorak",
    "wednesday": "u srijedu",
    "thursday": "u četvrtak",
    "friday": "u petak",
    "saturday": "u subotu",
    "next-sunday": "sljedeću nedjelju",
    "next-monday": "sljedeći ponedjeljak",
    "next-tuesday": "sljedeći utorak",
    "next-wednesday": "sljedeću srijedu",
    "next-thursday": "sljedeći četvrtak",
    "next-friday": "sljedeći petak",
    "next-saturday": "sljedeću subotu",
    "minutes": "$1 minuta",
    "fahrenheit": "$1\u00b0F",
    "celsius": "$1\u00b0C",
    "inches": "$1 inča",
    "centimeters": "$1 centimetra",
    "less-than": "ispod $1",
    "and": and_function,
    "through": through_function,
    "with": "$1, s $2",
    "range": "$1\u2013$2",
    "parenthetical": "$1 ($2)",
    "for-hour": "$1 za sat",
    "starting-in": "$1 počinje za $2",
    "stopping-in": "$1 prestaje za $2",
    "starting-then-stopping-later": "$1 počinje za $2, pa prestaje za $3",
    "stopping-then-starting-later": "$1 prestaje za $2, pa počinje za $3",
    "for-day": "$1 tijekom cijelog dana",
    "starting": "$1 od $2",
    "until": "$1 do $2",
    "until-starting-again": "$1 do $2, i opet počinje $3",
    "starting-continuing-until": "$1 počinje $2, ostaje do $3",
    "during": "$1 $2",
    "for-week": "$1 tijekom tjedna",
    "over-weekend": "$1 tijekom vikenda",
    "temperatures-peaking": "maksimalnom temperaturom do $1 $2",
    "temperatures-rising": "temperaturom u porastu do $1 $2",
    "temperatures-valleying": "najnižom temperaturom do $1 $2",
    "temperatures-falling": "padom temperature do $1 $2",
    "title": title_function,
    "sentence": sentence_function,
    "next-hour-forecast-status": "Prognoze za sljedeći sat su $1 zbog $2",
    "unavailable": "nedostupan",
    "temporarily-unavailable": "privremeno nedostupno",
    "partially-unavailable": "djelomično nedostupno",
    "station-offline": "sve obližnje radarske stanice su izvan mreže",
    "station-incomplete": "praznine u pokrivenosti obližnjih radarskih stanica",
    "smoke": "dim",
    "haze": "sumaglica",
    "mist": "magla",
}
