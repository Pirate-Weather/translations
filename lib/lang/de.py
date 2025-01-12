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


def until_time(time):
    if time == "Abend":
        return "bis abends"
    elif time == "Nacht":
        return "die ganze Nacht"
    else:
        return "bis " + time


def and_function(stack, a, b):
    if "bis" in a or "bis" in b:
        joiner = " sowie "
    elif "," in a:
        joiner = ", und "
    else:
        joiner = " und "
    return join_with_shared_prefix(a, b, joiner)


def through_function(stack, a, b):
    return join_with_shared_prefix(
        a.replace("am ", "von "), b.replace("am ", ""), " bis "
    )


def starting_function(stack, condition, period):
    if stack[1] == "starting":
        return f"{period}{'s' if period in ['Vormittag', 'Nachmittag', 'Abend', 'Nacht'] else ''} {condition}"

    if stack[1] == "and":
        return f"{period} {condition}"

    return f"{condition} {period}"


def until_function(stack, condition, period):
    return condition + " " + until_time(period)


def until_starting_again_function(stack, condition, a, b):
    return (
        f"{condition} bis zum {a}{' und Nacht' if b == 'Nacht' else f' und {b} wieder'}"
    )


def starting_continuing_until_function(stack, condition, a, b):
    if a == "Abend" and b == "Nacht":
        return condition + " abends und nächtlich"

    if a == "Abend":
        a = "abends "
    elif a == "Vormittag":
        a = "vormittags"
    elif a == "Mittag":
        a = "mittags"
    elif a == "Nachmittag":
        a = "nachmittags"
    return condition + " von " + a + " " + until_time(b)


def during_function(stack, condition, time):
    if stack[1] == "and":
        return f"{time} {condition}"

    if stack[1] == "with":
        return f"{condition} {time}"

    if time == "Nacht":
        return f"{condition} in der {time}"

    if time == "heute" or time == "morgen":
        return f"{condition} {time}"

    return f"{condition} am {time}"


def title_function(stack, s):
    # Apply custom_capitalize to every word
    return s[0].upper() + s[1:]


def sentence_function(stack, s):
    s = s[0].upper() + s[1:]
    if not s.endswith("."):
        s += "."
    return s


template = {
    "clear": "Klar",
    "no-precipitation": "kein Niederschlag",
    "mixed-precipitation": "wechselnder Niederschlag",
    "possible-very-light-precipitation": "leichter Niederschlag möglich",
    "very-light-precipitation": "leichter Niederschlag",
    "possible-light-precipitation": "leichter Niederschlag möglich",
    "light-precipitation": "leichter Niederschlag",
    "medium-precipitation": "Niederschlag",
    "heavy-precipitation": "schwerer Niederschlag",
    "possible-very-light-rain": "Nieselregen möglich",
    "very-light-rain": "Nieselregen",
    "possible-light-rain": "leichter Regen möglich",
    "light-rain": "leichter Regen",
    "medium-rain": "Regen",
    "heavy-rain": "Regenschauer",
    "possible-very-light-sleet": "leichter Graupelregen möglich",
    "very-light-sleet": "leichter Graupelregen",
    "possible-light-sleet": "leichter Graupelregen möglich",
    "light-sleet": "leichter Graupelregen",
    "medium-sleet": "Graupelregen",
    "heavy-sleet": "Graupelschauer",
    "possible-very-light-snow": "leichter Schneefall möglich",
    "very-light-snow": "leichter Schneefall",
    "possible-light-snow": "leichter Schneefall möglich",
    "light-snow": "leichter Schneefall",
    "medium-snow": "Schneefall",
    "heavy-snow": "starker Schneefall",
    "possible-thunderstorm": "Gewitter möglich",
    "thunderstorm": "Gewitter",
    "possible-medium-precipitation": "Niederschlag möglich",
    "possible-heavy-precipitation": "schwerer Niederschlag möglich",
    "possible-medium-rain": "Regen möglich",
    "possible-heavy-rain": "Regenschauer möglich",
    "possible-medium-sleet": "Graupelregen möglich",
    "possible-heavy-sleet": "Graupelschauer möglich",
    "possible-medium-snow": "Schneefall möglich",
    "possible-heavy-snow": "starker Schneefall möglich",
    "possible-very-light-freezing-rain": "gefrierender Nieselregen möglich",
    "very-light-freezing-rain": "gefrierender Nieselregen",
    "possible-light-freezing-rain": "leichter gefrierender Regen möglich",
    "light-freezing-rain": "leichter gefrierender Regen",
    "possible-medium-freezing-rain": "gefrierender Regen möglich",
    "medium-freezing-rain": "gefrierender Regen",
    "possible-heavy-freezing-rain": "starker gefrierender Regen möglich",
    "heavy-freezing-rain": "starker gefrierender Regen",
    "possible-hail": "Hagel möglich",
    "hail": "Hagel",
    "light-wind": "leichter Wind",
    "medium-wind": "frische Brise",
    "heavy-wind": "Sturm",
    "low-humidity": "niedrige Luftfeuchtigkeit",
    "high-humidity": "hohe Luftfeuchtigkeit",
    "fog": "Nebel",
    "very-light-clouds": "überwiegend Klar",
    "light-clouds": "leicht bewölkt",
    "medium-clouds": "überwiegend bewölkt",
    "heavy-clouds": "stark bewölkt",
    "today-morning": "heute Vormittag",
    "later-today-morning": "späteren Vormittag",
    "today-afternoon": "heute Nachmittag",
    "later-today-afternoon": "am späteren Nachmittag",
    "today-evening": "heute Abend",
    "later-today-evening": "späteren Abend",
    "today-night": "heute Nacht",
    "later-today-night": "heute in der späteren Nacht",
    "tomorrow-morning": "morgen Vormittag",
    "tomorrow-afternoon": "morgen Nachmittag",
    "tomorrow-evening": "morgen Abend",
    "tomorrow-night": "morgen Nacht",
    "morning": "Vormittag",
    "afternoon": "Nachmittag",
    "evening": "Abend",
    "night": "Nacht",
    "today": "heute",
    "tomorrow": "morgen",
    "sunday": "am Sonntag",
    "monday": "am Montag",
    "tuesday": "am Dienstag",
    "wednesday": "am Mittwoch",
    "thursday": "am Donnerstag",
    "friday": "am Freitag",
    "saturday": "am Samstag",
    "next-sunday": "am nächsten Sonntag",
    "next-monday": "am nächsten Montag",
    "next-tuesday": "am nächsten Dienstag",
    "next-wednesday": "am nächsten Mittwoch",
    "next-thursday": "am nächsten Donnerstag",
    "next-friday": "am nächsten Freitag",
    "next-saturday": "am nächsten Samstag",
    "minutes": "$1 Min.",
    "fahrenheit": "$1\u00b0F",
    "celsius": "$1\u00b0C",
    "inches": "$1 Zoll",
    "centimeters": "$1 cm",
    "less-than": "weniger als $1",
    "and": and_function,
    "through": through_function,
    "with": "$1 mit $2",
    "range": "$1 bis $2",
    "parenthetical": "$1 ($2)",
    "for-hour": "in der kommenden Stunde $1",
    "starting-in": "in $2 $1",
    "stopping-in": "$1, endet in $2",
    "starting-then-stopping-later": "$1 in $2 für $3",
    "stopping-then-starting-later": "$1 endet in $2 und beginnt $3 danach erneut",
    "for-day": "den ganzen Tag lang $1",
    "starting": starting_function,
    "until": until_function,
    "until-starting-again": until_starting_again_function,
    "starting-continuing-until": starting_continuing_until_function,
    "during": during_function,
    "for-week": "die ganze Woche $1",
    "over-weekend": "$1 am Wochenende",
    "temperatures-peaking": "einem Temperaturmaximum von $1 $2",
    "temperatures-rising": "steigender Temperatur von $1 $2",
    "temperatures-valleying": "einem Temperaturminimum von $1 $2",
    "temperatures-falling": "fallender Temperatur von $1 $2",
    "title": title_function,
    "sentence": sentence_function,
    "next-hour-forecast-status": "next hour forecasts are $1 due to $2",
    "unavailable": "unavailable",
    "temporarily-unavailable": "temporarily unavailable",
    "partially-unavailable": "partially unavailable",
    "station-offline": "all nearby radar stations being offline",
    "station-incomplete": "gaps in coverage from nearby radar stations",
}
