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


def time_var(time, pref, t):
    # Handling different time cases with conditional statements
    if time == "danas":
        return pref + " danas"

    elif time in ["utor", "ponedelj", "pet", "četvrt"]:
        # Handling cases for specific days and time prefixes like "od", "do", or "u"
        if pref in ["od", "do"]:
            # Check if time is during a period (based on condition in t)
            if t[2] == "during" and t[3] == "through":
                return time + "ka"
            else:
                return pref + " " + time + "ka"
        elif pref == "u":
            return "u " + time + "ak"
        else:
            return time + "ak"

    elif time == "nedelj":
        # Handling cases for "nedelj" with different prefixes
        if pref in ["od", "do"]:
            return "nedelje"
        elif pref == "u":
            return "u nedelju"
        else:
            return "nedelja"

    elif time in ["subot", "sred"]:
        # Handling cases for "subot" and "sred" with different prefixes
        if pref in ["od", "do"]:
            return time + "e"
        elif pref == "u":
            return "u " + time + "u"
        else:
            return time + "u"

    elif time == "noć":
        # Special case handling for "noć" with specific conditions
        if t[1] == "starting-continuing-until" or pref == "u":
            return "tokom noći"
        else:
            return "noća"

    elif time == "sutra noć":
        # Similar logic for "sutra noć"
        if t[2] == "starting-continuing-until" or pref == "u":
            return "tokom noći"
        else:
            return "sutra noć"

    elif time == "kasnije noć":
        # Special handling based on conditions in t
        if t[2] == "starting":
            return "kasnije tokom noći"
        else:
            return "kasnije noć"

    elif time == "kasnije ovog jutra":
        # Special handling for "kasnije ovog jutra"
        if t[1] == "during":
            return "kasnije tokom ovog jutra"
        else:
            return "kasnije ovog jutra"

    else:
        # Default case if no conditions match
        return time


def check_condition(c):
    # Check condition based on specific cases for "padavine" types
    if c in ["slabe padavine", "padavine", "jake padavine"]:
        return "počinju"
    else:
        return "počev od"


def get_prefix(a, t):
    # Get prefix based on time and condition for different cases
    if a == "sred":
        return " i "

    elif a == "sutra ujutro":
        # Check conditions in t for specific "during" and "and" cases
        if t[1] == "during" and t[2] == "and":
            return " i "
        else:
            return ", "

    else:
        # Default case, check if title and and are present in t
        if t[0] == "title" and t[1] == "and":
            return " i "
        else:
            return ", "


def and_function(stack, a, b):
    return join_with_shared_prefix(
        time_var(a, "u", stack),
        time_var(b, "u", stack),
        get_prefix(b, stack),
    )


def through_function(stack, a, b):
    return join_with_shared_prefix(
        time_var(a, "od", stack),
        time_var(b, "do", stack),
        " do ",
    )


def during_function(stack, a, b):
    """
    This function formats the condition and time based on a specific pattern.
    It uses the `time_var` function to determine the proper time formatting,
    then returns the formatted string based on the context.

    Parameters:
    - stack (list): A list containing context values (used to check the conjunction "and").
    - a (str): The condition (e.g., weather-related condition).
    - b (str): The time (e.g., "danas", "sutra", etc.).

    Returns:
    - str: A formatted string combining the condition and time based on the context.
    """

    # Use time_var function to format the time with the appropriate prefix ("u")
    time = time_var(b, "u", stack)

    # If the second element in the context list is "and", concatenate time and condition
    if stack[1] == "and":
        return f"{time} {a}"
    else:
        # Otherwise, concatenate condition and time
        return f"{a} {time}"


def starting_function(stack, condition, period):
    return condition + " počinje " + time_var(period, "u", stack)


def until_function(stack, condition, period):
    return condition + " do " + time_var(period, "", stack)


def until_starting_again_function(stack, condition, a, b):
    return condition + " " + time_var(a, "do", stack) + " i opet počinje " + b


def starting_continuing_until_function(stack, condition, a, b):
    start_from = time_var(a, "", stack)
    to_end = time_var(b, "u", stack)
    return (
        condition
        + " "
        + check_condition(condition)
        + " "
        + start_from
        + ", nastaviće se "
        + to_end
    )


def temperatures_peaking_function(stack, temp, at):
    return "temperaturom najviše do " + temp + " " + time_var(at, "u", stack)


def temperatures_rising_function(stack, temp, at):
    return "temperaturnim rastom do " + temp + " " + time_var(at, "u", stack)


def temperatures_valleying_function(stack, temp, at):
    return "temperaturom najniže do " + temp + " " + time_var(at, "u", stack)


def temperatures_falling_function(stack, temp, at):
    return "temperaturnim padom do " + temp + " " + time_var(at, "u", stack)


def title_function(stack, s):
    """
    Capitalize the first letter of every word.
    """
    return s[0].upper() + s[1:]


def sentence_function(stack, s):
    """
    Capitalize the first word of the sentence and end with a period.
    """
    s = s[0].upper() + s[1:]
    if not s.endswith("."):
        s += "."
    return s


template = {
    "clear": "vedro",
    "no-precipitation": "nema padavina",
    "mixed-precipitation": "različite padavine",
    "possible-very-light-precipitation": "moguće su veoma slabe padavine",
    "very-light-precipitation": "veoma slabe padavine",
    "possible-light-precipitation": "moguće su slabe padavine",
    "light-precipitation": "slabe padavine",
    "medium-precipitation": "padavine",
    "heavy-precipitation": "jake padavine",
    "possible-very-light-rain": "moguća je veoma sitna kiša",
    "very-light-rain": "veoma sitna kiša",
    "possible-light-rain": "moguća je sitna kiša",
    "light-rain": "sitna kiša",
    "medium-rain": "kiša",
    "heavy-rain": "jaka kiša",
    "possible-very-light-sleet": "moguća je veoma slaba susnežica",
    "very-light-sleet": "veoma slaba susnežica",
    "possible-light-sleet": "moguća je slaba susnežica",
    "light-sleet": "slaba susnežica",
    "medium-sleet": "susnežica",
    "heavy-sleet": "jaka susnežica",
    "possible-very-light-snow": "moguć je veoma sitan sneg",
    "very-light-snow": "veoma sitan sneg",
    "possible-light-snow": "moguć je sitan sneg",
    "light-snow": "sitan sneg",
    "medium-snow": "sneg",
    "heavy-snow": "jak sneg",
    "possible-thunderstorm": "moguća je grmljavina",
    "thunderstorm": "grmljavina",
    "possible-medium-precipitation": "moguće su padavine",
    "possible-heavy-precipitation": "moguće su jake padavine",
    "possible-medium-rain": "moguća je kiša",
    "possible-heavy-rain": "moguća je jaka kiša",
    "possible-medium-sleet": "moguća je susnežica",
    "possible-heavy-sleet": "moguća je jaka slsusnežicaeet",
    "possible-medium-snow": "moguć je sneg",
    "possible-heavy-snow": "moguć je jak sneg",
    "possible-very-light-freezing-rain": "moguća je ledena veoma sitna",
    "very-light-freezing-rain": "ledena veoma sitna",
    "possible-light-freezing-rain": "moguća je sitna ledena kiša",
    "light-freezing-rain": "sitna ledena kiša",
    "possible-medium-freezing-rain": "moguća je ledena kiša",
    "medium-freezing-rain": "ledena kiša",
    "possible-heavy-freezing-rain": "moguća je jaka ledena kiša",
    "heavy-freezing-rain": "jaka ledena kiša",
    "possible-hail": "moguća je tuča",
    "hail": "tuča",
    "light-wind": "vetrovito",
    "medium-wind": "vetrovito",
    "heavy-wind": "opasno vetrovito",
    "low-humidity": "suvo",
    "high-humidity": "vlažno",
    "fog": "maglovito",
    "very-light-clouds": "pretežno vedro",
    "light-clouds": "mestimično oblačno",
    "medium-clouds": "pretežno oblačno",
    "heavy-clouds": "oblačno",
    "today-morning": "ovog jutra",
    "later-today-morning": "kasnije ovog jutra",
    "today-afternoon": "ovog popodneva",
    "later-today-afternoon": "kasnije ovog popodneva",
    "today-evening": "uveče",
    "later-today-evening": "kasno uveče",
    "today-night": "večeras",
    "later-today-night": "kasnije noć",
    "tomorrow-morning": "sutra ujutro",
    "tomorrow-afternoon": "sutra popodne",
    "tomorrow-evening": "sutra uveče",
    "tomorrow-night": "sutra noć",
    "morning": "ujutro",
    "afternoon": "popodne",
    "evening": "uveče",
    "night": "noć",
    "today": "danas",
    "tomorrow": "sutra",
    "monday": "ponedelj",
    "tuesday": "utor",
    "wednesday": "sred",
    "thursday": "četvrt",
    "friday": "pet",
    "saturday": "subot",
    "sunday": "nedelj",
    "next-monday": "ponedelj",  # FIXME
    "next-tuesday": "utor",  # FIXME
    "next-wednesday": "sred",  # FIXME
    "next-thursday": "četvrt",  # FIXME
    "next-friday": "pet",  # FIXME
    "next-saturday": "subot",  # FIXME
    "next-sunday": "nedelj",  # FIXME
    "minutes": "$1 minuta",
    "fahrenheit": "$1\u00b0F",
    "celsius": "$1\u00b0C",
    "inches": "$1 inča",
    "centimeters": "$1cm",
    "less-than": "ispod $1",
    "and": and_function,
    "through": through_function,
    "with": "$1, sa $2",
    "range": "$1\u2013$2",
    "parenthetical": "$1 ($2)",
    "for-hour": "$1 za ovaj sat",
    "starting-in": "$1 počinje za $2",
    "stopping-in": "$1 prestaje za $2",
    "starting-then-stopping-later": "$1 počinje za $2, onda prestaje za $3",
    "stopping-then-starting-later": "$1 prestaje za $2, onda počinje za $3",
    "for-day": "$1 tokom celog dana",
    "starting": starting_function,
    "until": until_function,
    "until-starting-again": until_starting_again_function,
    "starting-continuing-until": starting_continuing_until_function,
    "during": during_function,
    "for-week": "$1 tokom sedmice",
    "over-weekend": "$1 tokom vikenda",
    "temperatures-peaking": temperatures_peaking_function,
    "temperatures-rising": temperatures_rising_function,
    "temperatures-valleying": temperatures_valleying_function,
    "temperatures-falling": temperatures_falling_function,
    "title": title_function,
    "sentence": sentence_function,
    "next-hour-forecast-status": "прогнозе за следећи сат су $1 због $2",
    "unavailable": "недоступно",
    "temporarily-unavailable": "привремено недоступно",
    "partially-unavailable": "делимично недоступно",
    "station-offline": "све оближње радарске станице су ван мреже",
    "station-incomplete": "празнине у покривености са оближњих радарских станица",
}
