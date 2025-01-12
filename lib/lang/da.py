import re


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
    if period.startswith("om natte"):
        return period[3:]
    elif period.startswith("under "):
        return period[6:]
    return period


def grammar(s):
    s = re.sub(r"på ", "om ", s, flags=re.IGNORECASE)
    s = re.sub(
        r"(man|tirs|ons|tors|fre|lør|søn)(dag)", r"\1dagen", s, flags=re.IGNORECASE
    )
    return s


def and_function(stack, a, b):
    return join_with_shared_prefix(a, b, ", og " if "," in a else " og ")


def through_function(stack, a, b):
    return join_with_shared_prefix(a, b, " indtil ")


def until_function(stack, condition, period):
    return condition + " indtil " + strip_prefix(period)


def until_starting_again_function(stack, condition, a, b):
    return condition + " indtil " + strip_prefix(a) + ", kommer igen " + b


def starting_continuing_until_function(stack, condition, a, b):
    return condition + " " + a + ", fortsætter indtil " + strip_prefix(b)


def title_function(stack, s):
    # Apply custom_capitalize to every word
    return s[0].upper() + s[1:]


def sentence_function(stack, s):
    s = s[0].upper() + s[1:]
    if not s.endswith("."):
        s += "."
    return s


def temperatures_peaking_function(stack, a, b):
    return "temperaturer op til " + a + " " + grammar(b)


def temperatures_rising_function(stack, a, b):
    return "temperaturer stigende til " + a + " " + grammar(b)


def temperatures_valleying_function(stack, a, b):
    return "temperaturer der stopper ved " + a + " " + grammar(b)


def temperatures_falling_function(stack, a, b):
    return "temperaturer faldende til " + a + " " + grammar(b)


template = {
    "clear": "klart",
    "no-precipitation": "ingen målbar nedbør",
    "mixed-precipitation": "blandet nedbør",
    "possible-very-light-precipitation": "mulighed for meget let nedbør",
    "very-light-precipitation": "meget let nedbør",
    "possible-light-precipitation": "mulighed for let nedbør",
    "light-precipitation": "let nedbør",
    "medium-precipitation": "nedbør",
    "heavy-precipitation": "kraftig regn",
    "possible-very-light-rain": "mulighed for let støvregn",
    "very-light-rain": "støvregn",
    "possible-light-rain": "mulighed for lette regnbyger",
    "light-rain": "regnbyger",
    "medium-rain": "regn",
    "heavy-rain": "kraftige regnbyger",
    "possible-very-light-sleet": "mulighed for meget let slud",
    "very-light-sleet": "meget let slud",
    "possible-light-sleet": "mulighed for let slud",
    "light-sleet": "let slud",
    "medium-sleet": "slud",
    "heavy-sleet": "kraftig slud",
    "possible-very-light-snow": "mulighed for meget let sne",
    "very-light-snow": "meget let sne",
    "possible-light-snow": "mulighed for let sne",
    "light-snow": "let sne",
    "medium-snow": "sne",
    "heavy-snow": "rigelig med sne",
    "possible-thunderstorm": "tordenvejr kan forekomme",
    "thunderstorm": "tordenvejr",
    "possible-medium-precipitation": "mulighed for nedbør",
    "possible-heavy-precipitation": "mulighed for kraftig nedbør",
    "possible-medium-rain": "mulighed for regn",
    "possible-heavy-rain": "mulighed for kraftige regn",
    "possible-medium-sleet": "mulighed for slud",
    "possible-heavy-sleet": "mulighed for kraftig slud",
    "possible-medium-snow": "mulighed for sne",
    "possible-heavy-snow": "mulighed for rigelig med sne",
    "possible-very-light-freezing-rain": "mulighed for frysende støvregn",
    "very-light-freezing-rain": "frysende støvregn",
    "possible-light-freezing-rain": "mulighed for let frysende regn",
    "light-freezing-rain": "let frysende regn",
    "possible-medium-freezing-rain": "mulighed for frysende regn",
    "medium-freezing-rain": "frysende regn",
    "possible-heavy-freezing-rain": "mulighed for kraftige frysende regn",
    "heavy-freezing-rain": "kraftig frysende regn",
    "possible-hail": "mulighed for hagl",
    "hail": "hagl",
    "light-wind": "let vind",
    "medium-wind": "stærk vind",
    "heavy-wind": "storm",
    "low-humidity": "tørt",
    "high-humidity": "fugtigt",
    "fog": "tåge",
    "very-light-clouds": "for det meste klart",
    "light-clouds": "let skyet",
    "medium-clouds": "skyet",
    "heavy-clouds": "overskyet",
    "today-morning": "på formiddagen",
    "later-today-morning": "senere på formiddagen",
    "today-afternoon": "i eftermiddag",
    "later-today-afternoon": "senere i eftermiddag",
    "today-evening": "i aften",
    "later-today-evening": "senere i aften",
    "today-night": "i nat",
    "later-today-night": "senere i nat",
    "tomorrow-morning": "i morgen tidlig",
    "tomorrow-afternoon": "i morgen eftermiddag",
    "tomorrow-evening": "i morgen aften",
    "tomorrow-night": "i morgen nat",
    "morning": "om morgenen",
    "afternoon": "om eftermiddagen",
    "evening": "om aftenen",
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
    "next-sunday": "næste søndag",
    "next-monday": "næste mandag",
    "next-tuesday": "næste tirsdag",
    "next-wednesday": "næste onsdag",
    "next-thursday": "næste torsdag",
    "next-friday": "næste fredag",
    "next-saturday": "næste lørdag",
    "minutes": "$1 min.",
    "fahrenheit": "$1\u00b0F",
    "celsius": "$1\u00b0C",
    "inches": "$1 tommer",
    "centimeters": "$1 cm",
    "less-than": "under $1",
    "and": and_function,
    "through": through_function,
    "with": "$1, med $2",
    "range": "$1\u2013$2",
    "parenthetical": "$1 ($2)",
    "for-hour": "$1 i løbet af de næste par timer",
    "starting-in": "$1 om $2",
    "stopping-in": "$1 der aftager om $2",
    "starting-then-stopping-later": "$1 om $2, aftager $3 senere",
    "stopping-then-starting-later": "$1 aftager om $2, begynder igen $3 senere",
    "for-day": "$1 i løbet af dagen",
    "starting": "$1 $2",
    "until": until_function,
    "until-starting-again": until_starting_again_function,
    "starting-continuing-until": starting_continuing_until_function,
    "during": "$1 $2",
    "for-week": "$1 i løbet af ugen",
    "over-weekend": "$1 over weekenden",
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
