import re


def join_with_shared_prefix(a, b, joiner):
    """
    Joins two strings (`a` and `b`) using a shared prefix with a specified joiner.

    This function compares the characters of `a` and `b` from the start, finding the longest common prefix
    and then joins them with a specified joiner.

    Parameters:
    - a (str): The first string to join.
    - b (str): The second string to join.
    - joiner (str): The string used to join the two strings.

    Returns:
    - str: The two strings joined together using the common prefix and the joiner.
    """
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


def time2(time):
    """
    Converts a given time-related string to its corresponding genitive form in Ukrainian.

    This function takes a string `time` representing a specific time or date phrase
    and returns its corresponding genitive form. It handles various time phrases like
    "вранці" (in the morning), "вдень" (in the afternoon), and specific phrases like
    "сьогодні вранці" (this morning) by mapping them to their genitive forms.

    Parameters:
    - time (str): A string representing a time-related phrase in Ukrainian.

    Returns:
    - str: The genitive form of the input time string, or the input string itself if no match is found.
    """
    if time == "вранці":
        return "ранку"
    elif time == "вдень":
        return "середини дня"
    elif time == "ввечері":
        return "вечору"
    elif time == "вночі":
        return "ночі"
    elif time == "сьогодні вранці":
        return "сьогоднішнього ранку"
    elif time == "сьогодні пізно вранці":
        return "сьогоднішнього пізнього ранку"
    elif time == "сьогодні вдень":
        return "середини дня"
    elif time == "сьогодні пізно вдень":
        return "сьогоднішнього пізнього дня"
    elif time == "сьогодні ввечері":
        return "сьогоднішнього вечору"
    elif time == "сьогодні пізно ввечері":
        return "сьогоднішнього пізнього вечору"
    elif time == "сьогодні вночі":
        return "сьогоднішньої ночі"
    elif time == "сьогодні пізно вночі":
        return "сьогоднішньої пізньої ночі"
    elif time == "завтра вранці":
        return "завтрашнього ранку"
    elif time == "завтра вдень":
        return "завтрашнього дня"
    elif time == "завтра ввечері":
        return "завтрашнього вечору"
    elif time == "завтра вночі":
        return "завтрашньої ночі"
    elif time == "у неділю":
        return "неділі"
    elif time == "в понеділок":
        return "понеділка"
    elif time == "у вівторок":
        return "вівторка"
    elif time == "в середу":
        return "середи"
    elif time == "в четвер":
        return "четверга"
    elif time == "в п'ятницю":
        return "п'ятниці"
    elif time == "в суботу":
        return "суботи"
    else:
        return time


def and_function(stack, a, b):
    return join_with_shared_prefix(a, b, ", і " if "," in a else " і ")


def through_function(stack, a, b):
    return join_with_shared_prefix(a, time2(b), " і до ")


def during_function(stack, a, b):
    return a + " " + b


def until_function(stack, condition, period):
    return condition + " до " + time2(period)


def until_starting_again_function(stack, condition, a, b):
    timeUntil = time2(a)
    return condition + " до " + timeUntil + ", починаючись знову " + b


def starting_continuing_until_function(stack, condition, a, b):
    timeFrom = time2(a)
    timeTo = time2(b)
    return condition + ", починаючись з " + timeFrom + ", і до " + timeTo


def title_function(stack, s):
    """
    Capitalizes the first letter of every word in the string, except for і.

    Args:
        string (str): The input string.

    Returns:
        str: The transformed string with appropriate capitalization.
    """

    def capitalize_word(word):
        if word == "і":
            return word
        return word[0].upper() + word[1:]

    return re.sub(r"\S+", lambda match: capitalize_word(match.group()), s)


def sentence_function(stack, s):
    """
    Capitalize the first word of the sentence and end with a period.
    """
    s = s[0].upper() + s[1:]
    if not s.endswith("."):
        s += "."
    return s


template = {
    "clear": "ясно",
    "no-precipitation": "без опадів",
    "mixed-precipitation": "змішані опади",
    "possible-very-light-precipitation": "можливі незначні опади",
    "very-light-precipitation": "незначні опади",
    "possible-light-precipitation": "можливі невеликі опади",
    "light-precipitation": "невеликі опади",
    "medium-precipitation": "опади",
    "heavy-precipitation": "сильні опади",
    "possible-very-light-rain": "можливий незначний дощ",
    "very-light-rain": "незначний дощ",
    "possible-light-rain": "можливий невеликий дощ",
    "light-rain": "невеликий дощ",
    "medium-rain": "дощ",
    "heavy-rain": "сильний дощ",
    "possible-very-light-sleet": "можливий незначний град",
    "very-light-sleet": "незначний град",
    "possible-light-sleet": "можливий невеликий град",
    "light-sleet": "невеликий град",
    "medium-sleet": "град",
    "heavy-sleet": "сильний град",
    "possible-very-light-snow": "можливий незначний сніг",
    "very-light-snow": "незначний сніг",
    "possible-light-snow": "можливий невеликий сніг",
    "light-snow": "невеликий сніг",
    "medium-snow": "сніг",
    "heavy-snow": "снігопад",
    "possible-thunderstorm": "можливі грози",
    "thunderstorm": "грози",
    "possible-medium-precipitation": "можливі опади",
    "possible-heavy-precipitation": "можливі сильні опади",
    "possible-medium-rain": "можливий дощ",
    "possible-heavy-rain": "можливий сильний дощ",
    "possible-medium-sleet": "можливий град",
    "possible-heavy-sleet": "можливий сильний град",
    "possible-medium-snow": "можливий сніг",
    "possible-heavy-snow": "можливий снігопад",
    "possible-very-light-freezing-rain": "можливий крижаний дощ",
    "very-light-freezing-rain": "крижаний дощ",
    "possible-light-freezing-rain": "можливий невеликий крижаний дощ",
    "light-freezing-rain": "невеликий крижаний дощ",
    "possible-medium-freezing-rain": "можливий крижаний дощ",
    "medium-freezing-rain": "крижаний дощ",
    "possible-heavy-freezing-rain": "можливий сильний крижаний дощ",
    "heavy-freezing-rain": "сильний крижаний дощ",
    "possible-hail": "можливий град",
    "hail": "град",
    "light-wind": "слабкий вітер",
    "medium-wind": "вітер",
    "heavy-wind": "сильний вітер",
    "low-humidity": "сухо",
    "high-humidity": "волого",
    "fog": "туман",
    "very-light-clouds": "переважно ясно",
    "light-clouds": "невелика хмарність",
    "medium-clouds": "хмарно",
    "heavy-clouds": "сильна хмарність",
    "today-morning": "сьогодні вранці",
    "later-today-morning": "сьогодні пізно вранці",
    "today-afternoon": "сьогодні вдень",
    "later-today-afternoon": "сьогодні пізно вдень",
    "today-evening": "сьогодні ввечері",
    "later-today-evening": "сьогодні пізно ввечері",
    "today-night": "сьогодні вночі",
    "later-today-night": "сьогодні пізно вночі",
    "tomorrow-morning": "завтра вранці",
    "tomorrow-afternoon": "завтра вдень",
    "tomorrow-evening": "завтра ввечері",
    "tomorrow-night": "завтра вночі",
    "morning": "вранці",
    "afternoon": "вдень",
    "evening": "ввечері",
    "night": "вночі",
    "today": "сьогодні",
    "tomorrow": "завтра",
    "sunday": "в неділю",
    "monday": "в понеділок",
    "tuesday": "у вівторок",
    "wednesday": "в середу",
    "thursday": "в четвер",
    "friday": "в п'ятницю",
    "saturday": "в суботу",
    "next-sunday": "в неділю",
    "next-monday": "наступного понеділка",
    "next-tuesday": "наступного вівторка",
    "next-wednesday": "наступної середи",
    "next-thursday": "наступного четверга",
    "next-friday": "наступної п'ятниці",
    "next-saturday": "наступної суботи",
    "minutes": "$1 хв.",
    "fahrenheit": "$1\u00b0F",
    "celsius": "$1\u00b0C",
    "inches": "$1 in.",
    "centimeters": "$1 см.",
    "less-than": "менше $1",
    "and": and_function,
    "through": through_function,
    "with": "$1, з $2",
    "range": "$1\u2013$2",
    "parenthetical": "$1 ($2)",
    "for-hour": "$1 протягом наступної години",
    "starting-in": "$1 починається за $2",
    "stopping-in": "$1 закінчується за $2",
    "starting-then-stopping-later": "$1 починається за $2, і закінчується за $3",
    "stopping-then-starting-later": "$1 закінчується за $2, і починається знову за $3",
    "for-day": "$1 протягом всього дня",
    "starting": "$1 починається $2",
    "until": until_function,
    "until-starting-again": until_starting_again_function,
    "starting-continuing-until": starting_continuing_until_function,
    "during": during_function,
    "for-week": "$1 протягом всього тижня",
    "over-weekend": "$1 протягом всіх вихідних",
    "temperatures-peaking": "температурою, що піднімається до максимуму $1 $2",
    "temperatures-rising": "температурою, що піднімається до $1 $2",
    "temperatures-valleying": "температурою, що знижується до $1 $2",
    "temperatures-falling": "температурою, що знижується до мінімуму $1 $2",
    "title": title_function,
    "sentence": sentence_function,
    "next-hour-forecast-status": "прогнози на наступну годину становлять $1 через $2",
    "unavailable": "недоступний",
    "temporarily-unavailable": "тимчасово недоступний",
    "partially-unavailable": "частково недоступний",
    "station-offline": "усі найближчі радіолокаційні станції відключені",
    "station-incomplete": "прогалини в покритті від найближчих радіолокаційних станцій",
    "smoke": "дим",
    "haze": "імла",
    "mist": "туман",
}
