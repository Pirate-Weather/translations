import re


def make_plural(a):
    """
    Add "j" to words ending in "o" (nouns) or "a" (adjective agreement, but not "la").
    """
    words = a.split(" ")
    pluralized_words = [
        w + "j" if w.endswith("o") or (w.endswith("a") and w != "la") else w
        for w in words
    ]
    return " ".join(pluralized_words)


def make_accusative(a):
    """
    Add "n" to words ending in "o" (nouns), "a" (adjective agreement, but not "la"),
    or "j" (plural).
    """
    words = a.split(" ")
    accusative_words = [
        w + "n"
        if w.endswith("j") or w.endswith("o") or (w.endswith("a") and w != "la")
        else w
        for w in words
    ]
    return " ".join(accusative_words)


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


def minutes_function(stack, a):
    if a == "1":
        return a + " minuto"
    return a + make_plural(" minuto")


def and_function(stack, a, b):
    return join_with_shared_prefix(a, b, ", kaj " if "," in a else " kaj ")


def title_function(stack, s):
    """
    Convert a string to title case, but skip certain words and words containing a period.
    """

    def capitalize_word(word):
        # Skip words with a period or specific words in the exception list
        exceptions = {"dum", "ĝis", "je", "kaj", "la", "malpli", "ol", "pli", "por"}
        if "." in word or word in exceptions:
            return word
        return word[0].upper() + word[1:]

    # Use a regex to find words and apply capitalization selectively
    return re.sub(r"\S+", lambda match: capitalize_word(match.group(0)), s)


def sentence_function(stack, s):
    s = s[0].upper() + s[1:]
    if not s.endswith("."):
        s += "."
    return s


def temperatures_peaking_function(stack, a, b):
    return "la temperaturo atingos sian maksimon je " + a + " " + make_accusative(b)


def temperatures_rising_function(stack, a, b):
    return "la temperaturo plialtiĝos ĝis " + a + " " + make_accusative(b)


def temperatures_valleying_function(stack, a, b):
    return "la temperaturo atingos sian minimumon je " + a + " " + make_accusative(b)


def temperatures_falling_function(stack, a, b):
    return "la temperaturo malplialtiĝos ĝis " + a + " " + make_accusative(b)


template = {
    "clear": "klara ĉielo",
    "no-precipitation": "neniu precipitaĵo",
    "mixed-precipitation": "miksita precipitaĵo",
    "possible-very-light-precipitation": "malforta precipitaĵo eblas",
    "very-light-precipitation": "malforta precipitaĵo",
    "possible-light-precipitation": "malforta precipitaĵo eblas",
    "light-precipitation": "malforta precipitaĵo",
    "medium-precipitation": "precipitaĵo",
    "heavy-precipitation": "forta precipitaĵo",
    "possible-very-light-rain": "drizlo eblas",
    "very-light-rain": "drizlo",
    "possible-light-rain": "malforta pluvo eblas",
    "light-rain": "malforta pluvo",
    "medium-rain": "pluvo",
    "heavy-rain": "forta pluvo",
    "possible-very-light-sleet": "malforta glaciumo eblas",
    "very-light-sleet": "malforta glaciumo",
    "possible-light-sleet": "malforta glaciumo eblas",
    "light-sleet": "malforta glaciumo",
    "medium-sleet": "glaciumo",
    "heavy-sleet": "forta glaciumo",
    "possible-very-light-snow": "malforta neĝo eblas",
    "very-light-snow": "malforta neĝo",
    "possible-light-snow": "malforta neĝo eblas",
    "light-snow": "malforta neĝo",
    "medium-snow": "neĝo",
    "heavy-snow": "forta neĝo",
    "possible-thunderstorm": "fulmotondroj eblas",
    "thunderstorm": "fulmotondroj",
    "possible-medium-precipitation": "precipitaĵo eblas",
    "possible-heavy-precipitation": "forta precipitaĵo eblas",
    "possible-medium-rain": "pluvo eblas",
    "possible-heavy-rain": "forta pluvo eblas",
    "possible-medium-sleet": "glaciumo eblas",
    "possible-heavy-sleet": "forta glaciumo eblas",
    "possible-medium-snow": "neĝo eblas",
    "possible-heavy-snow": "forta neĝo eblas",
    "possible-very-light-freezing-rain": "frosta drizlo eblas",
    "very-light-freezing-rain": "frosta drizlo",
    "possible-light-freezing-rain": "malforta frosta pluvo eblas",
    "light-freezing-rain": "malforta frosta pluvo",
    "possible-medium-freezing-rain": "frosta pluvo eblas",
    "medium-freezing-rain": "frosta pluvo",
    "possible-heavy-freezing-rain": "forta frosta pluvo eblas",
    "heavy-freezing-rain": "forta frosta pluvo",
    "possible-hail": "hajlo eblas",
    "hail": "hajlo",
    "light-wind": "malforta vento",
    "medium-wind": "vento",
    "heavy-wind": "forta vento",
    "low-humidity": "seka humideco",
    "high-humidity": "alta humideco",
    "fog": "nebulo",
    "very-light-clouds": "plejparte klara",
    "light-clouds": "malmultaj nuboj",
    "medium-clouds": "nuboj",
    "heavy-clouds": "multaj nuboj",
    "today-morning": "la mateno",
    "later-today-morning": "la malfrua mateno",
    "today-afternoon": "la tagmezo",
    "later-today-afternoon": "la malfrua tagmezo",
    "today-evening": "la vespero",
    "later-today-evening": "la malfrua vespero",
    "today-night": "la nokto",
    "later-today-night": "la malfrua nokto",
    "tomorrow-morning": "morgaŭ mateno",
    "tomorrow-afternoon": "morgaŭ tagmezo",
    "tomorrow-evening": "morgaŭ vespero",
    "tomorrow-night": "morgaŭ nokto",
    "morning": "la mateno",
    "afternoon": "la tagmezo",
    "evening": "la vespero",
    "night": "la nokto",
    "today": "hodiaŭ",
    "tomorrow": "morgaŭ",
    "sunday": "dimanĉo",
    "monday": "lundo",
    "tuesday": "mardo",
    "wednesday": "mekredo",
    "thursday": "ĵaŭdo",
    "friday": "vendredo",
    "saturday": "sabato",
    "next-sunday": "la venonta dimanĉo",
    "next-monday": "la venonta lundo",
    "next-tuesday": "la venonta mardo",
    "next-wednesday": "la venonta mekredo",
    "next-thursday": "la venonta ĵaŭdo",
    "next-friday": "la venonta vendredo",
    "next-saturday": "la venonta dimanĉo",
    "minutes": minutes_function,
    "fahrenheit": "$1\u00b0F",
    "celsius": "$1\u00b0C",
    "inches": "$1 in.",
    "centimeters": "$1 cm.",
    "less-than": "malpli ol $1",
    "and": and_function,
    "through": "$1 ĝis $2",
    "with": "$1, kaj $2",
    "range": "$1\u2013$2",
    "parenthetical": "$1 ($2)",
    "for-hour": "$1 por unu horo",
    "starting-in": "$1 komenciĝos post $2",
    "stopping-in": "$1 ĉesiĝos post $2",
    "starting-then-stopping-later": "$1 komenciĝos post $2 kaj ĉesiĝos $3 poste",
    "stopping-then-starting-later": "$1 ĉesiĝos post $2 kaj rekomenciĝos $3 poste",
    "for-day": "$1 dum la tago",
    "starting": "$1 komenciĝos je $2",
    "until": "$1 ĝis $2",
    "until-starting-again": "$1 ĝis $2, rekomenciĝos je $3",
    "starting-continuing-until": "$1 komenciĝos je $2, daŭros ĝis $3",
    "during": "$1 dum $2",
    "for-week": "$1 dum la semajno",
    "over-weekend": "$1 dum la semajnfino",
    "temperatures-peaking": temperatures_peaking_function,
    "temperatures-rising": temperatures_rising_function,
    "temperatures-valleying": temperatures_valleying_function,
    "temperatures-falling": temperatures_falling_function,
    "title": title_function,
    "sentence": sentence_function,
    "next-hour-forecast-status": "next hour forecasts are $1 due to $2",
    "unavailable": "unavailable",
    "temporarily-unavailable": "temporarily unavailable",
    "partially-unavailable": "partially unavailable",
    "station-offline": "all nearby radar stations being offline",
    "station-incomplete": "gaps in coverage from nearby radar stations",
}
