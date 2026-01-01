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


def parenthetical_function(stack, a, b):
    # If a does not end with "flurries" or "snow", we adjust b.
    if not a.endswith("flurries") and not a.endswith("snow"):
        if not a.startswith("mixed"):
            b = "with a chance of " + b
        b += " of snow"
    return a + " (" + b + ")"


def until_function(stack, condition, period):
    return condition + " until " + strip_prefix(period)


def until_starting_again_function(stack, condition, a, b):
    return condition + " until " + strip_prefix(a) + ", returning " + b


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
    if (
        period.startswith("morning")
        or period.startswith("afternoon")
        or period.startswith("evening")
    ):
        return "in the " + period

    # Otherwise return the period
    return period


def during_function(stack, condition, period):
    # Logic: "Rain" + "in the morning" OR "Rain" + "overnight"
    return condition + " " + format_period_with_preposition(period)


def starting_function(stack, condition, period):
    # Logic: "Rain starting" + "in the morning" OR "Rain starting" + "overnight"
    print(period)
    return condition + " starting " + format_period_with_preposition(period)


template = {
    "clear": "clear",
    "no-precipitation": "no precipitation",
    "mixed-precipitation": "mixed precipitation",
    "possible-very-light-precipitation": "possible light precipitation",
    "very-light-precipitation": "light precipitation",
    "possible-light-precipitation": "possible light precipitation",
    "light-precipitation": "light precipitation",
    "medium-precipitation": "precipitation",
    "heavy-precipitation": "heavy precipitation",
    "possible-very-light-rain": "possible drizzle",
    "very-light-rain": "drizzle",
    "possible-light-rain": "possible light rain",
    "light-rain": "light rain",
    "medium-rain": "rain",
    "heavy-rain": "heavy rain",
    "possible-very-light-sleet": "possible light sleet",
    "very-light-sleet": "light sleet",
    "possible-light-sleet": "possible light sleet",
    "light-sleet": "light sleet",
    "medium-sleet": "sleet",
    "heavy-sleet": "heavy sleet",
    "possible-very-light-snow": "possible flurries",
    "very-light-snow": "flurries",
    "possible-light-snow": "possible light snow",
    "light-snow": "light snow",
    "medium-snow": "snow",
    "heavy-snow": "heavy snow",
    "possible-thunderstorm": "possible thunderstorms",
    "thunderstorm": "thunderstorms",
    "possible-medium-precipitation": "possible precipitation",
    "possible-heavy-precipitation": "possible heavy precipitation",
    "possible-medium-rain": "possible rain",
    "possible-heavy-rain": "possible heavy rain",
    "possible-medium-sleet": "possible sleet",
    "possible-heavy-sleet": "possible heavy sleet",
    "possible-medium-snow": "possible snow",
    "possible-heavy-snow": "possible heavy snow",
    "possible-very-light-freezing-rain": "possible freezing drizzle",
    "very-light-freezing-rain": "freezing drizzle",
    "possible-light-freezing-rain": "possible light freezing rain",
    "light-freezing-rain": "light freezing rain",
    "possible-medium-freezing-rain": "possible freezing rain",
    "medium-freezing-rain": "freezing rain",
    "possible-heavy-freezing-rain": "possible heavy freezing rain",
    "heavy-freezing-rain": "heavy freezing rain",
    "possible-hail": "possible hail",
    "hail": "hail",
    "light-wind": "breezy",
    "medium-wind": "windy",
    "heavy-wind": "dangerously windy",
    "low-humidity": "dry",
    "high-humidity": "humid",
    "fog": "foggy",
    "very-light-clouds": "mostly clear",
    "light-clouds": "partly cloudy",
    "medium-clouds": "mostly cloudy",
    "heavy-clouds": "overcast",
    "today-morning": "this morning",
    "later-today-morning": "later this morning",
    "today-afternoon": "this afternoon",
    "later-today-afternoon": "later this afternoon",
    "today-evening": "this evening",
    "later-today-evening": "later this evening",
    "today-night": "tonight",
    "later-today-night": "later tonight",
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
    "less-than": "< $1",
    "and": and_function,
    "through": through_function,
    "with": "$1, with $2",
    "range": "$1\u2013$2",
    "parenthetical": parenthetical_function,
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
    "next-hour-forecast-status": "next hour forecasts are $1 due to $2",
    "unavailable": "unavailable",
    "temporarily-unavailable": "temporarily unavailable",
    "partially-unavailable": "partially unavailable",
    "station-offline": "all nearby radar stations being offline",
    "station-incomplete": "gaps in coverage from nearby radar stations",
    "smoke": "smoke",
    "haze": "hazy",
    "mist": "misty",
}
