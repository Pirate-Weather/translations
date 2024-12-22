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


def time2(time):
    """
    Converts a time-related phrase into its corresponding Russian genitive form.

    Args:
        time (str): The input time phrase.

    Returns:
        str: The transformed time phrase in genitive form.
    """
    mapping = {
        "утром": "утра",
        "днем": "середины дня",
        "вечером": "вечера",
        "ночью": "ночи",
        "сегодня утром": "сегодняшнего утра",
        "сегодня поздним утром": "сегодняшнего позднего утра",
        "сегодня днем": "середины дня",
        "сегодня поздним днем": "сегодняшнего позднего дня",
        "сегодня вечером": "сегодняшнего вечера",
        "сегодня поздним вечером": "сегодняшнего позднего вечера",
        "сегодня ночью": "сегодняшней ночи",
        "сегодня поздней ночью": "сегодняшней поздней ночи",
        "завтра утром": "завтрашнего утра",
        "завтра днем": "завтрашнего дня",
        "завтра вечером": "завтрашнего вечера",
        "завтра ночью": "завтрашней ночи",
        "в воскресенье": "воскресенья",
        "в понедельник": "понедельника",
        "во вторник": "вторника",
        "в среду": "среды",
        "в четверг": "четверга",
        "в пятницу": "пятницы",
        "в субботу": "субботы",
    }
    return mapping.get(time, time)


def and_function(stack, a, b):
    return join_with_shared_prefix(a, b, ", и " if "," in a else " и ")


def through_function(stack, a, b):
    return join_with_shared_prefix(a, time2(b), " и до ")


def until_function(stack, condition, period):
    return condition + " до " + time2(period)


def until_starting_again_function(stack, condition, a, b):
    timeUntil = time2(a)
    return condition + " до " + timeUntil + ", начинаясь снова " + b


def starting_continuing_until_function(stack, condition, a, b):
    timeFrom = time2(a)
    timeTo = time2(b)
    return condition + ", начинаясь с " + timeFrom + ", и до " + timeTo


def during_function(stack, condition, time):
    return condition + " " + time


def title_function(stack, s):
    """
    Capitalizes the first letter of every word in the string, except for и.

    Args:
        string (str): The input string.

    Returns:
        str: The transformed string with appropriate capitalization.
    """

    def capitalize_word(word):
        if word == "и":
            return word
        return word[0].upper() + word[1:]

    return re.sub(r"\S+", lambda match: capitalize_word(match.group()), s)


def sentence_function(stack, s):
    s = s[0].upper() + s[1:]
    if not s.endswith("."):
        s += "."
    return s


template = {
    "clear": "ясно",
    "no-precipitation": "без осадков",
    "mixed-precipitation": "смешанные осадки",
    "possible-very-light-precipitation": "возможны незначительные осадки",
    "very-light-precipitation": "незначительные осадки",
    "possible-light-precipitation": "возможны небольшие осадки",
    "light-precipitation": "небольшие осадки",
    "medium-precipitation": "осадки",
    "heavy-precipitation": "сильные осадки",
    "possible-very-light-rain": "возможен незначительный дождь",
    "very-light-rain": "незначительный дождь",
    "possible-light-rain": "возможен небольшой дождь",
    "light-rain": "небольшой дождь",
    "medium-rain": "дождь",
    "heavy-rain": "сильный дождь",
    "possible-very-light-sleet": "возможен незначительный град",
    "very-light-sleet": "незначительный град",
    "possible-light-sleet": "возможен небольшой град",
    "light-sleet": "небольшой град",
    "medium-sleet": "град",
    "heavy-sleet": "сильный град",
    "possible-very-light-snow": "возможен незначительный снег",
    "very-light-snow": "незначительный снег",
    "possible-light-snow": "возможен небольшой снег",
    "light-snow": "небольшой снег",
    "medium-snow": "снег",
    "heavy-snow": "снегопад",
    "possible-thunderstorm": "возможны грозы",
    "thunderstorm": "грозы",
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
    "light-wind": "слабый ветер",
    "medium-wind": "ветер",
    "heavy-wind": "сильный ветер",
    "low-humidity": "сухо",
    "high-humidity": "влажно",
    "fog": "туман",
    "very-light-clouds": "почти ясно",
    "light-clouds": "небольшая облачность",
    "medium-clouds": "облачно",
    "heavy-clouds": "сильная облачность",
    "today-morning": "сегодня утром",
    "later-today-morning": "сегодня поздним утром",
    "today-afternoon": "сегодня днем",
    "later-today-afternoon": "сегодня поздним днем",
    "today-evening": "сегодня вечером",
    "later-today-evening": "сегодня поздним вечером",
    "today-night": "сегодня ночью",
    "later-today-night": "сегодня поздней ночью",
    "tomorrow-morning": "завтра утром",
    "tomorrow-afternoon": "завтра днем",
    "tomorrow-evening": "завтра вечером",
    "tomorrow-night": "завтра ночью",
    "morning": "утром",
    "afternoon": "днем",
    "evening": "вечером",
    "night": "ночью",
    "today": "сегодня",
    "tomorrow": "завтра",
    "sunday": "в воскресенье",
    "monday": "в понедельник",
    "tuesday": "во вторник",
    "wednesday": "в среду",
    "thursday": "в четверг",
    "friday": "в пятницу",
    "saturday": "в субботу",
    "next-sunday": "в следующее воскресенье",
    "next-monday": "в следующий понедельник",
    "next-tuesday": "в следующий вторник",
    "next-wednesday": "в следующую среду",
    "next-thursday": "в следующий четверг",
    "next-friday": "в следующую пятницу",
    "next-saturday": "в следующую субботу",
    "minutes": "$1 мин",
    "fahrenheit": "$1\u00b0F",
    "celsius": "$1\u00b0C",
    "inches": "$1 in.",
    "centimeters": "$1 см.",
    "less-than": "меньше $1",
    "and": and_function,
    "through": through_function,
    "with": "$1, с $2",
    "range": "$1\u2013$2",
    "parenthetical": "$1 ($2)",
    "for-hour": "$1 в течение следующего часа",
    "starting-in": "$1 начинается в течение $2",
    "stopping-in": "$1 заканчивается в течение $2",
    "starting-then-stopping-later": "$1 начинается в течение $2, и заканчивается через $3",
    "stopping-then-starting-later": "$1 заканчивается в течение $2, и начинается снова через $3",
    "for-day": "$1 в течение всего дня",
    "starting": "$1 начинается $2",
    "until": until_function,
    "until-starting-again": until_starting_again_function,
    "starting-continuing-until": starting_continuing_until_function,
    "during": during_function,
    "for-week": "$1 в течение всей недели",
    "over-weekend": "$1 в течение всех выходных",
    "temperatures-peaking": "температурой, поднимающейся до максимума $1 $2",
    "temperatures-rising": "температурой, поднимающейся до $1 $2",
    "temperatures-valleying": "температурой, опускающейся до $1 $2",
    "temperatures-falling": "температурой, опускающейся до минимума $1 $2",
    "title": title_function,
    "sentence": sentence_function,
    "unavailable": "unavailable",
    "temporarily-unavailable": "temporarily unavailable",
    "partially-unavailable": "partially unavailable",
    "station-offline": "all nearby radar stations being offline",
    "station-incomplete": "gaps in coverage from nearby radar stations",
}
