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


def and_function(stack, a, b):
    return join_with_shared_prefix(a, b, ", и " if "," in a else " и ")


def time2(time):
    if time == "в неделя":
        return "неделя"
    elif time == "в понеделник":
        return "понеделник"
    elif time == "във вторник":
        return "вторник"
    elif time == "в сряда":
        return "сряда"
    elif time == "в четвъртък":
        return "четвъртък"
    elif time == "в петък":
        return "петък"
    elif time == "в събота":
        return "събота"
    else:
        return time


def through_function(stack, a, b):
    return "от " + a + " до " + time2(b)


def until_function(stack, condition, period):
    return condition + " " + period


def until_starting_again_function(stack, condition, a, b):
    return condition + " до " + a + ", започва отново " + b


def starting_continuing_until_function(stack, condition, a, b):
    return condition + ", започва от " + a + ", до " + b


def title_function(stack, s):
    def capitalize_word(word):
        return word if word == "и" else word[0].upper() + word[1:]

    return re.sub(r"\S+", lambda match: capitalize_word(match.group()), s)


def sentence_function(stack, s):
    # Capitalize the first character
    s = s[0].upper() + s[1:] if s else s

    # Add a period if there isn't already one
    if not s.endswith("."):
        s += "."
    return s


template = {
    "clear": "ясно",
    "no-precipitation": "без превалявания",
    "mixed-precipitation": "смесени превалявания",
    "possible-very-light-precipitation": "възможни незначителни превалявания",
    "very-light-precipitation": "незначителни превалявания",
    "possible-light-precipitation": "възможни леки превалявания",
    "light-precipitation": "леки превалявания",
    "medium-precipitation": "превалявания",
    "heavy-precipitation": "силни превалявания",
    "possible-very-light-rain": "възможен ръмеж",
    "very-light-rain": "ръмеж",
    "possible-light-rain": "възможен слаб дъжд",
    "light-rain": "слаб дъжд",
    "medium-rain": "дъжд",
    "heavy-rain": "силен дъжд",
    "possible-very-light-sleet": "възможна много слаба градушка",
    "very-light-sleet": "много слаба градушка",
    "possible-light-sleet": "възможна слаба градушка",
    "light-sleet": "слаба градушка",
    "medium-sleet": "градушка",
    "heavy-sleet": "силна градушка",
    "possible-very-light-snow": "възможен много слаб сняг",
    "very-light-snow": "много слаб сняг",
    "possible-light-snow": "възможен слаб сняг",
    "light-snow": "слаб сняг",
    "medium-snow": "снеговалеж",
    "heavy-snow": "силен снеговалеж",
    "possible-thunderstorm": "възможна гръмотевична буря",
    "thunderstorm": "гръмотевична буря",
    "possible-medium-precipitation": "възможна превалявания",
    "possible-heavy-precipitation": "възможна силен превалявания",
    "possible-medium-rain": "възможна дъжд",
    "possible-heavy-rain": "възможна силен дъжд",
    "possible-medium-sleet": "възможна градушка",
    "possible-heavy-sleet": "възможна силна градушка",
    "possible-medium-snow": "възможна снеговалеж",
    "possible-heavy-snow": "възможна силен снеговалеж",
    "possible-very-light-freezing-rain": "възможна замразяване ръмеж",
    "very-light-freezing-rain": "замразяване ръмеж",
    "possible-light-freezing-rain": "възможна слаб замразяване дъжд",
    "light-freezing-rain": "слаб замразяване дъжд",
    "possible-medium-freezing-rain": "възможна замразяване дъжд",
    "medium-freezing-rain": "замразяване дъжд",
    "possible-heavy-freezing-rain": "възможна силен замразяване дъжд",
    "heavy-freezing-rain": "силен замразяване дъжд",
    "possible-hail": "възможна градушка",
    "hail": "градушка",
    "light-wind": "слаб вятър",
    "medium-wind": "умерен вятър",
    "heavy-wind": "силен вятър",
    "low-humidity": "сухо",
    "high-humidity": "влажно",
    "fog": "мъгла",
    "very-light-clouds": "предимно ясно",
    "light-clouds": "незначителна облачност",
    "medium-clouds": "облачно",
    "heavy-clouds": "гъста облачност",
    "today-morning": "тази сутрин",
    "later-today-morning": "по-късно тази сутрин",
    "today-afternoon": "днес следобед",
    "later-today-afternoon": "по-късно днес следобед",
    "today-evening": "вечерта",
    "later-today-evening": "по-късно вечерта",
    "today-night": "през нощта",
    "later-today-night": "по-късно през нощта",
    "tomorrow-morning": "утре сутринта",
    "tomorrow-afternoon": "утре следобед",
    "tomorrow-evening": "утре вечерта",
    "tomorrow-night": "утре през нощта",
    "morning": "сутринта",
    "afternoon": "следобед",
    "evening": "вечерта",
    "night": "през нощта",
    "today": "днес",
    "tomorrow": "утре",
    "sunday": "в неделя",
    "monday": "в понеделник",
    "tuesday": "във вторник",
    "wednesday": "в сряда",
    "thursday": "в четвъртък",
    "friday": "в петък",
    "saturday": "в събота",
    "next-sunday": "следващата неделя",
    "next-monday": "следващия понеделник",
    "next-tuesday": "следващия вторник",
    "next-wednesday": "следващата сряда",
    "next-thursday": "следващия четвъртък",
    "next-friday": "следващия петък",
    "next-saturday": "следващата събота",
    "minutes": "$1 мин",
    "fahrenheit": "$1\u00b0F",
    "celsius": "$1\u00b0C",
    "inches": "$1 in.",
    "centimeters": "$1 см.",
    "less-than": "по-малко $1",
    "and": and_function,
    "through": through_function,
    "with": "$1, с $2",
    "range": "$1\u2013$2",
    "parenthetical": "$1 ($2)",
    "for-hour": "$1 през следващия час",
    "starting-in": "$1 започва след $2",
    "stopping-in": "$1 приключва до $2",
    "starting-then-stopping-later": "$1 започва след $2, и приключва до $3 по-късно",
    "stopping-then-starting-later": "$1 приключва до $2, и започва отново след $3",
    "for-day": "$1 през целия ден",
    "starting": "$1 започва $2",
    "until": until_function,
    "until-starting-again": until_starting_again_function,
    "starting-continuing-until": starting_continuing_until_function,
    "during": "$1 $2",
    "for-week": "$1 през седмицата",
    "over-weekend": "$1 през уикенда",
    "temperatures-peaking": "максимални температури, достигащи $1 $2",
    "temperatures-rising": "максимални температури, покачващи се до $1 $2",
    "temperatures-valleying": "максимални температури, падащи до $1 $2",
    "temperatures-falling": "максимални температури, падащи до минимум $1 $2",
    "title": title_function,
    "sentence": sentence_function,
    "next-hour-forecast-status": "Прогнозата за идния час $1 поради $2.",
    "unavailable": "не е налична",
    "temporarily-unavailable": "временно не е на разположение",
    "partially-unavailable": "е частична",
    "station-offline": "това че всички близки станции не са на линия",
    "station-incomplete": "пропуски в покритието от близки станции",
}
