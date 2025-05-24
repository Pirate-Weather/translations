import re


def strip_prefix(a):
    return "y nos" if a == "dros nos" else re.sub(r"^(?:yn|ar) ", "", a)


def minutes_function(stack, a):
    return a + (" funud" if a == 1 or a == 2 else " munud")


def less_than_function(stack, a):
    return "llai na" + ("g " if re.match(r"^(1|8|11|16)[\D\b]", a) else " ") + a


def and_function(stack, a, b):
    # don't repeat 'yn y'
    if a[:5] == "yn y " and b[:5] == "yn y ":
        return a + " a’r " + b[5:]

    # don't repeat 'ar'
    if a[:9] == "ar ddydd " and b[:9] == "ar ddydd ":
        b = b[4:]

    # include comma if a list
    result = a + ("," if "," in a else "")

    # ac not a if second phrase starts with vowel
    if re.match(r"^[aeiouyw]", b):
        result += " ac "
    else:
        result += " a "

    # p, t, c -> ph, th, ch mutation
    result += re.sub(r"^([ptc])(?!h)", r"\1h", b)

    return result


def through_function(stack, a, b):
    return "o " + strip_prefix(a) + " hyd at " + strip_prefix(b)


def until_function(stack, condition, period):
    return condition + " hyd at " + strip_prefix(period)  # TR


def until_starting_again_function(stack, condition, a, b):
    return condition + " hyd at " + strip_prefix(a) + ", gan gychwyn eto " + b


def starting_continuing_until_function(stack, condition, a, b):
    return condition + " yn cychwyn " + a + ", gan barhau hyd at " + strip_prefix(b)


def title_function(stack, s):
    # Apply custom_capitalize to every word
    return s[0].upper() + s[1:]


def sentence_function(stack, s):
    s = s[0].upper() + s[1:]
    if not s.endswith("."):
        s += "."
    return s


template = {
    "clear": "clir",
    "no-precipitation": "dim gwlybaniaeth",
    "mixed-precipitation": "gwlybaniaeth cymysg",
    "possible-very-light-precipitation": "gwlybaniaeth ysgafn yn bosib",
    "very-light-precipitation": "gwlybaniaeth ysgafn",
    "possible-light-precipitation": "gwlybaniaeth ysgafn yn bosib",
    "light-precipitation": "gwlybaniaeth ysgafn",
    "medium-precipitation": "gwlybaniaeth",
    "heavy-precipitation": "gwlybaniaeth trwm",
    "possible-very-light-rain": "glaw mân yn bosib",
    "very-light-rain": "glaw mân",
    "possible-light-rain": "glaw ysgafn yn bosib",
    "light-rain": "glaw ysgafn",
    "medium-rain": "glaw",
    "heavy-rain": "glaw trwm",
    "possible-very-light-sleet": "eirlaw ysgafn yn bosib",
    "very-light-sleet": "eirlaw ysgafn",
    "possible-light-sleet": "eirlaw ysgafn yn bosib",
    "light-sleet": "eirlaw ysgafn",
    "medium-sleet": "eirlaw",
    "heavy-sleet": "eirlaw trwm",
    "possible-very-light-snow": "eira ysgafn yn bosib",
    "very-light-snow": "eira ysgafn",
    "possible-light-snow": "eira ysgafn yn bosib",
    "light-snow": "eira ysgafn",
    "medium-snow": "eira",
    "heavy-snow": "eira trwm",
    "possible-thunderstorm": "mellt a tharannau yn bosib",
    "thunderstorm": "mellt a tharannau",
    "possible-medium-precipitation": "gwlybaniaeth yn bosib",
    "possible-heavy-precipitation": "gwlybaniaeth trwm yn bosib",
    "possible-medium-rain": "ysgafn glaw yn bosib",
    "possible-heavy-rain": "glaw trwm yn bosib",
    "possible-medium-sleet": "eirlaw yn bosib",
    "possible-heavy-sleet": "eirlaw trwm yn bosib",
    "possible-medium-snow": "eira yn bosib",
    "possible-heavy-snow": "eira trwm yn bosib",
    "possible-very-light-freezing-rain": "glaw mân rhewllyd yn bosib",
    "very-light-freezing-rain": "glaw mân rhewllyd",
    "possible-light-freezing-rain": "ysgafn glaw rhewllyd yn bosib",
    "light-freezing-rain": "ysgafn glaw rhewllyd",
    "possible-medium-freezing-rain": "glaw rhewllyd yn bosib",
    "medium-freezing-rain": "glaw rhewllyd",
    "possible-heavy-freezing-rain": "glaw rhewllyd trwm yn bosib",
    "heavy-freezing-rain": "glaw rhewllyd trwm",
    "possible-hail": "cenllysg yn bosib",
    "hail": "cenllysg",
    "light-wind": "gwyntoedd ysgafn",
    "medium-wind": "gwyntog",
    "heavy-wind": "gwyntoedd cryfion",
    "low-humidity": "sych",
    "high-humidity": "clòs",
    "fog": "niwlog",
    "very-light-clouds": "clir gan mwyaf",
    "light-clouds": "rhannol gymylog",
    "medium-clouds": "cymylog",
    "heavy-clouds": "cymylau trwchus",
    "today-morning": "y bore yma",
    "later-today-morning": "yn hwyrach bore yma",
    "today-afternoon": "y prynhawn yma",
    "later-today-afternoon": "yn hwyrach prynhawn yma",
    "today-evening": "gyda’r hwyr heno",
    "later-today-evening": "yn hwyrach fin nos heno",
    "today-night": "heno",
    "later-today-night": "yn hwyrach heno",
    "tomorrow-morning": "bore yfory",
    "tomorrow-afternoon": "prynhawn yfory",
    "tomorrow-evening": "fin nos yfory",
    "tomorrow-night": "nos yfory",
    "morning": "yn y bore",
    "afternoon": "yn y prynhawn",
    "evening": "gyda’r hwyr",
    "night": "dros nos",
    "today": "heddiw",
    "tomorrow": "yfory",
    "sunday": "ar ddydd Sul",
    "monday": "ar ddydd Llun",
    "tuesday": "ar ddydd Mawrth",
    "wednesday": "ar ddydd Mercher",
    "thursday": "ar ddydd Iau",
    "friday": "ar ddydd Gwener",
    "saturday": "ar ddydd Sadwrn",
    "next-sunday": "ddydd Sul nesaf",
    "next-monday": "ddydd Llun nesaf",
    "next-tuesday": "ddydd Mawrth nesaf",
    "next-wednesday": "ddydd Mercher nesaf",
    "next-thursday": "ddydd Iau nesaf",
    "next-friday": "ddydd Gwener nesaf",
    "next-saturday": "ddydd Sadwrn nesaf",
    "minutes": minutes_function,
    "fahrenheit": "$1\u00b0F",
    "celsius": "$1\u00b0C",
    "inches": "$1 modfedd",
    "centimeters": "$1cm",
    "less-than": less_than_function,
    "and": and_function,
    "through": through_function,
    "with": "$1, gyda\u2019r $2",
    "range": "$1\u2013$2",
    "parenthetical": "$1 ($2)",
    "for-hour": "$1 am yr awr",
    "starting-in": "$1 yn cychwyn mewn $2",
    "stopping-in": "$1 yn dod i ben mewn $2",
    "starting-then-stopping-later": "$1 yn cychwyn mewn $2, ac yn dod i ben $3 wedyn",
    "stopping-then-starting-later": "$1 yn dod i ben mewn $2, gan gychwyn eto $3 wedyn",
    "for-day": "$1 drwy\u2019r dydd",
    "starting": "$1 yn cychwyn $2",  # o?
    "until": until_function,
    "until-starting-again": until_starting_again_function,
    "starting-continuing-until": starting_continuing_until_function,
    "during": "$1 $2",
    "for-week": "$1 drwy’r wythnos",
    "over-weekend": "$1 dros y penwythnos",
    "temperatures-peaking": "tymheredd ar ei uchaf yn $1 $2",
    "temperatures-rising": "tymheredd yn codi i $1 $2",
    "temperatures-valleying": "tymheredd ar ei isaf yn $1 $2",
    "temperatures-falling": "tymheredd yn gostwng i $1 $2",
    "title": title_function,
    "sentence": sentence_function,
    "next-hour-forecast-status": "Dydi rhagolygon yr awr nesa $1 oherwydd $2",
    "unavailable": "ddim ar gael",
    "temporarily-unavailable": "ddim ar gael ar hyn o bryd",
    "partially-unavailable": "ddim yn gyflawn",
    "station-offline": "diffyg gwybodaeth o orsafoedd radar gerllaw",
    "station-incomplete": "bylchau yn narpariaeth gorsafoedd radar gerllaw",
}
