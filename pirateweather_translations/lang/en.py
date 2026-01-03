import re


def join_with_shared_prefix(a, b, joiner):
    m = a
    i = 0

    # HACK: This replicates the JS logic.
    if m == "today" or m == "tomorrow":
        m = "on " + m

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
    if period.startswith("overnight"):
        return period[4:]
    elif period.startswith("in the "):
        return period[7:]
    return period


def custom_capitalize(s):
    # Do not capitalize certain words:
    if s in ["a", "and", "cm", "in", "of", "with"]:
        return s
    return s[0].upper() + s[1:] if s else s


def and_function(stack, a, b):
    return join_with_shared_prefix(a, b, ", and " if "," in a else " and ")


def through_function(stack, a, b):
    return join_with_shared_prefix(a, b, " through ")


def until_function(stack, condition, period):
    return condition + " until " + strip_prefix(period)


def until_starting_again_function(stack, condition, a, b):
    return (
        condition
        + " until "
        + strip_prefix(a)
        + ", returning "
        + format_period_with_preposition(b)
    )


def starting_continuing_until_function(stack, condition, a, b):
    return condition + " from " + a + " until " + strip_prefix(b)


def title_function(stack, s):
    # Apply custom_capitalize to every word
    return re.sub(r"\w+", lambda m: custom_capitalize(m.group(0)), s)


def sentence_function(stack, s):
    s = custom_capitalize(s)
    if not s.endswith("."):
        s += "."
    return s


def format_period_with_preposition(period):
    # If the period is effectively an adverb, don't add "in the"
    # "later-today-morning" becomes "later this morning" via templates,
    # so we usually don't need "in the" for those either.

    # Simple check: (morning, afternoon, evening), add "in the"
    if period.startswith(("morning", "afternoon", "evening")):
        return "in the " + period

    # Otherwise return the period
    return period


def during_function(stack, condition, period):
    # Logic: "Rain" + "in the morning" OR "Rain" + "overnight"
    return condition + " " + format_period_with_preposition(period)


def starting_function(stack, condition, period):
    # Logic: "Rain starting" + "in the morning" OR "Rain starting" + "overnight"
    return condition + " starting " + format_period_with_preposition(period)


def multiple_sentences_function(stack, a, b):
    a = custom_capitalize(a)
    b = custom_capitalize(b)
    if not a.endswith("."):
        a += "."

    if not b.endswith("."):
        b += "."
    return a + " " + b


template = {
    "clear": "clear",
    "no-precipitation": "no precipitation",
    "mixed-precipitation": "mixed precipitation",
    "very-light-precipitation": "light precipitation",
    "light-precipitation": "light precipitation",
    "medium-precipitation": "precipitation",
    "heavy-precipitation": "heavy precipitation",
    "very-light-rain": "drizzle",
    "light-rain": "light rain",
    "medium-rain": "rain",
    "heavy-rain": "heavy rain",
    "very-light-sleet": "light sleet",
    "light-sleet": "light sleet",
    "medium-sleet": "sleet",
    "heavy-sleet": "heavy sleet",
    "very-light-snow": "flurries",
    "light-snow": "light snow",
    "medium-snow": "snow",
    "heavy-snow": "heavy snow",
    "thunderstorm": "thunderstorms",
    "very-light-freezing-rain": "freezing drizzle",
    "light-freezing-rain": "light freezing rain",
    "medium-freezing-rain": "freezing rain",
    "heavy-freezing-rain": "heavy freezing rain",
    "hail": "hail",
    "light-wind": "breezy",
    "medium-wind": "windy",
    "heavy-wind": "dangerously windy",
    "low-humidity": "dry",
    "high-humidity": "humid",
    "fog": "foggy",
    "smoke": "smoke",
    "haze": "hazy",
    "mist": "misty",
    "very-light-clouds": "mostly clear",
    "light-clouds": "partly cloudy",
    "medium-clouds": "mostly cloudy",
    "heavy-clouds": "overcast",
    "today-morning": "this morning",
    "today-afternoon": "this afternoon",
    "today-evening": "this evening",
    "today-night": "tonight",
    "tomorrow-morning": "tomorrow morning",
    "tomorrow-afternoon": "tomorrow afternoon",
    "tomorrow-evening": "tomorrow evening",
    "tomorrow-night": "tomorrow night",
    "morning": "morning",
    "afternoon": "afternoon",
    "evening": "evening",
    "night": "overnight",
    "today": "today",
    "tomorrow": "tomorrow",
    "sunday": "on Sunday",
    "monday": "on Monday",
    "tuesday": "on Tuesday",
    "wednesday": "on Wednesday",
    "thursday": "on Thursday",
    "friday": "on Friday",
    "saturday": "on Saturday",
    "next-sunday": "next Sunday",
    "next-monday": "next Monday",
    "next-tuesday": "next Tuesday",
    "next-wednesday": "next Wednesday",
    "next-thursday": "next Thursday",
    "next-friday": "next Friday",
    "next-saturday": "next Saturday",
    "minutes": "$1 min",
    "fahrenheit": "$1\u00b0F",
    "celsius": "$1\u00b0C",
    "inches": "$1 in",
    "centimeters": "$1 cm",
    "millimeters": "$1 mm",
    "less-than": "less than $1",
    "and": and_function,
    "through": through_function,
    "with": "$1, with $2",
    "range": "$1\u2013$2",
    "parenthetical": "$1 accumulations of $2 expected",
    "for-hour": "$1 for the hour",
    "starting-in": "$1 starting in $2",
    "stopping-in": "$1 ending in $2",
    "starting-then-stopping-later": "$1 starting in $2, ending $3 later",
    "stopping-then-starting-later": "$1 ending in $2, returning $3 later",
    "for-day": "$1 throughout the day",
    "starting": starting_function,
    "until": until_function,
    "until-starting-again": until_starting_again_function,
    "starting-continuing-until": starting_continuing_until_function,
    "during": during_function,
    "for-week": "$1 throughout the week",
    "over-weekend": "$1 over the weekend",
    "temperatures-peaking": "highs reaching $1 $2",
    "temperatures-rising": "highs climbing to $1 $2",
    "temperatures-valleying": "highs dipping to $1 $2",
    "temperatures-falling": "highs falling to $1 $2",
    "title": title_function,
    "sentence": sentence_function,
    "multiple-sentences": multiple_sentences_function,
    "next-hour-forecast-status": "next hour forecasts are $1 due to $2",
    "unavailable": "unavailable",
    "temporarily-unavailable": "temporarily unavailable",
    "station-offline": "missing model data",
    "chance-of": "chance of $1",
    "risk-of": "risk of $1",
    "at-times": "$1 at times",
    "occasional": "occasional $1",
    "off-and-on": "off and on $1",
    "to": "$1 to $2",
    "generally": "generally $1",
    "increasing": "increasing clouds $1",
    "clearing": "clearing $1",
}
