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


SUNDAY = "ראשון"
MONDAY = "שני"
TUESDAY = "שלישי"
WEDNESDAY = "רביעי"
THURSDAY = "חמישי"
FRIDAY = "שישי"
SATURDAY = "שבת"


def proper_at_time_prefix(at):
    if (
        at.startswith(SUNDAY)
        or at.startswith(MONDAY)
        or at.startswith(TUESDAY)
        or at.startswith(WEDNESDAY)
        or at.startswith(THURSDAY)
        or at.startswith(FRIDAY)
        or at.startswith(SATURDAY)
    ):
        return "ב"
    # default, return no prefix
    return ""


def and_function(stack, a, b):
    # Check if a contains a comma
    joiner = ", ו" if "," in a else " ו"

    # Return the result of joining with shared prefix
    return join_with_shared_prefix(a, b, joiner)


def through_function(stack, a, b):
    return join_with_shared_prefix(a, b, " עד ")


def minutes_function(stack, a):
    if a == "1":
        return "דקה"
    else:
        return a + " דקות"


def during_function(stack, a, b):
    return f"{a} {proper_at_time_prefix(b)}{b}"


def centimeters_function(stack, a):
    if a == "1":
        return "סֿ״מ"
    else:
        return a + " סֿ״מ"


def parenthetical_function(stack, a, b):
    # Check if a equals "משקעים מעורבים"
    if a == "משקעים מעורבים":
        return f"{a} ({b} של שלג)"
    else:
        return f"{a} ({b})"


def until_function(stack, condition, period):
    return condition + " עד " + period


def until_starting_again_function(stack, condition, a, b):
    return condition + " עד " + a + ", ויתחדש " + b


def starting_continuing_until_function(stack, condition, a, b):
    # Check if a is "בבוקר", if so replace with "הבוקר"
    if a == "בבוקר":
        a = "הבוקר"

    # Return the formatted string
    return f"{condition} מ{a}, ימשך עד {b}"


def title_function(stack, s):
    return s


def sentence_function(stack, s):
    if not s.endswith("."):
        s += "."
    return s


def temperatures_peaking_function(stack, temp, at):
    return f"חום גבוה יגיע לשיא של {temp} {proper_at_time_prefix(at)}{at}"


def temperatures_rising_function(stack, temp, at):
    return f"חום גבוה יטפס ל-{temp} {proper_at_time_prefix(at)}{at}"


def temperatures_valleying_function(stack, temp, at):
    return f"חום גבוה ירד עד {temp} {proper_at_time_prefix(at)}{at}"


def temperatures_falling_function(stack, temp, at):
    return f"חום גבוה יפול ל-{temp} {proper_at_time_prefix(at)}{at}"


template = {
    "clear": "בהיר",
    "mostly-clear": "בעיקר בהיר",
    "no-precipitation": "ללא משקעים",
    "mixed-precipitation": "משקעים מעורבים",
    "possible-very-light-precipitation": "אפשרות נמוך מאוד למשקעים",
    "very-light-precipitation": "משקעים קלים מאוד",
    "possible-light-precipitation": "אפשרות נמוך למשקעים",
    "light-precipitation": "משקעים קלים",
    "medium-precipitation": "משקעים",
    "heavy-precipitation": "משקעים כבדים",
    "possible-very-light-rain": "אפשרות לטפטוף",
    "very-light-rain": "טפטוף",
    "possible-light-rain": "אפשרות לגשם קל",
    "light-rain": "גשם קל",
    "medium-rain": "גשם",
    "heavy-rain": "גשם כבד",
    "possible-very-light-sleet": "אפשרות לשלג-קרח קל מאוד",
    "very-light-sleet": "שלג-קרח קל",
    "possible-light-sleet": "אפשרות לשלג-קרח קל",
    "light-sleet": "שלג-קרח קל",
    "medium-sleet": "שלג-קרח",
    "heavy-sleet": "שלג-קרח כבד",
    "possible-very-light-snow": "אפשרות לשלג קל מאוד",
    "very-light-snow": "שלג קל מאוד",
    "possible-light-snow": "אפשרות לשלג קל",
    "light-snow": "שלג קל",
    "medium-snow": "שלג",
    "heavy-snow": "שלג כבד",
    "possible-thunderstorm": "אפשרות לסופת ברקים",
    "thunderstorm": "סופת ברקים",
    "possible-medium-precipitation": "משקעים אפשריים",
    "possible-heavy-precipitation": "משקעים כבדים אפשריים",
    "possible-medium-rain": "גשם אפשרי",
    "possible-heavy-rain": "גשם חזק אפשרי",
    "possible-medium-sleet": "גשם אפשרי",
    "possible-heavy-sleet": "גשם כבד אפשרי",
    "possible-medium-snow": "שלג אפשרי",
    "possible-heavy-snow": "שלג כבד אפשרי",
    "possible-very-light-freezing-rain": "טפטוף מקפיא אפשרי",
    "very-light-freezing-rain": "טפטוף מקפיא",
    "possible-light-freezing-rain": "גשם קל וקפוא אפשרי",
    "light-freezing-rain": "גשם קפוא קל",
    "possible-medium-freezing-rain": "גשם קופא אפשרי",
    "medium-freezing-rain": "גשם קפוא",
    "possible-heavy-freezing-rain": "גשם קפוא אפשרי",
    "heavy-freezing-rain": "גשם קפוא חזק",
    "possible-hail": "ברד אפשרי",
    "hail": "ברד",
    "light-wind": "רוח קלה",
    "medium-wind": "רוח",
    "heavy-wind": "רוח חזקה",
    "low-humidity": "יבש",
    "high-humidity": "לחות גבוהה",
    "fog": "ערפל",
    "very-light-clouds": "ברור בעיקר",
    "light-clouds": "עננות חלקית",
    "medium-clouds": "מעונן חלקית",
    "heavy-clouds": "עננות",
    "today-morning": "בבוקר",
    "later-today-morning": "מאוחר יותר בבוקר",
    "today-afternoon": "אחרי הצהרים",
    "later-today-afternoon": "מאוחר יותר אחר הצהרים",
    "today-evening": "הערב",
    "later-today-evening": "מאוחר יותר הערב",
    "today-night": "הלילה",
    "later-today-night": "מאוחר יותר הלילה",
    "tomorrow-morning": "מחר בבוקר",
    "tomorrow-afternoon": "מחר אחרי הצהרים",
    "tomorrow-evening": "מחר בערב",
    "tomorrow-night": "מחר בלילה",
    "morning": "בבוקר",
    "afternoon": "אחר הצהרים",
    "evening": "הערב",
    "night": "הלילה",
    "today": "היום",
    "tomorrow": "מחר",
    "sunday": SUNDAY,
    "monday": MONDAY,
    "tuesday": TUESDAY,
    "wednesday": WEDNESDAY,
    "thursday": THURSDAY,
    "friday": FRIDAY,
    "saturday": SATURDAY,
    "next-sunday": f"{SUNDAY} הבא",
    "next-monday": f"{MONDAY} הבא",
    "next-tuesday": f"{TUESDAY} הבא",
    "next-wednesday": f"{WEDNESDAY} הבא",
    "next-thursday": f"{THURSDAY} הבא",
    "next-friday": f"{FRIDAY} הבא",
    "next-saturday": f"{SATURDAY} הבאה",
    "minutes": minutes_function,
    "fahrenheit": "$1 מעלות פרנהייט",
    "celsius": "$1 מעלות צלסיוס",
    "inches": "$1 אינץ׳",
    "centimeters": centimeters_function,
    "less-than": "פחות מ$1",
    "and": and_function,
    "through": through_function,
    "with": "$1, ו$2",
    "range": "$1\u2013$2",
    "parenthetical": parenthetical_function,
    "for-hour": "$1 לשעה הקרובה",
    "starting-in": "$1 יתחיל בעוד $2",
    "stopping-in": "$1 יפסק בעוד $2",
    "starting-then-stopping-later": "$1 יתחיל בעוד $2, יפסק אחרי $3",
    "stopping-then-starting-later": "$1 יפסק בעוד $2, יתחדש לאחר $3",
    "for-day": "$1 לאורך היום",
    "starting": "$1 מתחיל $2",
    "until": until_function,
    "until-starting-again": until_starting_again_function,
    "starting-continuing-until": starting_continuing_until_function,
    "during": during_function,
    "for-week": "$1 במשך השבוע",
    "over-weekend": "$1 לאורך הסוף שבוע",
    "temperatures-peaking": temperatures_peaking_function,
    "temperatures-rising": temperatures_rising_function,
    "temperatures-valleying": temperatures_valleying_function,
    "temperatures-falling": temperatures_falling_function,
    "title": title_function,
    "sentence": sentence_function,
    "next-hour-forecast-status": "תחזיות לשעה הבאה הן $1 בגלל $2",
    "unavailable": "לא זמין",
    "temporarily-unavailable": "לא זמין באופן זמני",
    "partially-unavailable": "לא זמין באופן חלקי",
    "station-offline": "כל תחנות הרדאר הסמוכות לא מקוונות",
    "station-incomplete": 'פערים בכיסוי מתחנות מכ"ם סמוכות',
    "smoke": "עשן",
    "haze": "אובך",
    "mist": "ערפל",
}
