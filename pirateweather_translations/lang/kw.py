import re


def in_the(period):
    if period in ["myttin", "dohajydh", "gorthugher", "nos"]:
        return " y'n " + period
    if period in ["an dohajydh ma", "an nos ma"]:
        return " y'n " + period[3:]
    if period[0] in "123456789":
        return " yn " + period
    return " " + period


def until_the(period):
    if period in ["myttin", "dohajydh", "gorthugher", "nos"]:
        return " bys y'n " + period
    if period in ["an dohajydh ma", "an nos ma"]:
        return " bys y'n " + period[3:]
    return " bys yn " + period


def and_function(stack, a, b):
    andy = ", ha" if "," in a else " ha"

    if b[0] in "aeiou":
        andy += "g"

    return a + andy + " " + b


def through_function(stack, a, b):
    return a + until_the(b)


def parenthetical_function(stack, a, b):
    if a == "kodhans kemyskys":
        return f"{a} ({b} a ergh)"
    return f"{a} ({b})"


def starting_function(stack, condition, period):
    return condition + " ow talleth" + in_the(period)


def starting_in_function(stack, condition, period):
    return condition + " ow talleth" + in_the(period)


def stopping_function(stack, condition, period):
    return condition + " ow hedhi" + in_the(period)


def starting_then_stopping_later_function(stack, condition, period1, period2):
    return (
        condition
        + " ow talleth"
        + in_the(period1)
        + ", ow hedhi "
        + period2
        + " diwettha"
    )


def stopping_then_starting_later_function(stack, condition, period1, period2):
    return (
        condition
        + " ow hedhi"
        + in_the(period1)
        + ", ow tastalleth "
        + period2
        + " diwettha"
    )


def until_function(stack, condition, period):
    return condition + until_the(period)


def until_starting_again_function(stack, condition, a, b):
    return condition + until_the(a) + ", ow tastalleth" + in_the(b)


def starting_continuing_until_function(stack, condition, a, b):
    return condition + " ow talleth" + in_the(a) + ", ow pesya" + until_the(b)


def during_function(stack, condition, period):
    return condition + in_the(period)


def title_function(stack, s):
    def replace_function(letter):
        return letter.upper()

    # Use regex to match the pattern and apply the replacement function
    return re.sub(
        r"\b(?:a(?!nd\b)|c(?!m\.)|i(?!n\.)|[^\Waci])",
        lambda m: replace_function(m.group(0)),
        s,
    )


def sentence_function(stack, s):
    s = s[0].upper() + s[1:]
    if not s.endswith("."):
        s += "."
    return s


template = {
    "clear": "kler",
    "mostly-clear": "yn myns klir",
    "no-precipitation": "kodhans vyth",
    "mixed-precipitation": "kodhans kemyskys",
    "possible-very-light-precipitation": "kodhans skav possybyl",
    "very-light-precipitation": "kodhans pur skav",
    "possible-light-precipitation": "kodhans skav possybyl",
    "light-precipitation": "kodhans skav",
    "medium-precipitation": "kodhans",
    "heavy-precipitation": "kodhans poos",
    "possible-very-light-rain": "glaw skav possybyl",
    "very-light-rain": "glaw pur skav",
    "possible-light-rain": "glaw skav possybyl",
    "light-rain": "glaw skav",
    "medium-rain": "glaw",
    "heavy-rain": "glaw poos",
    "possible-very-light-sleet": "erghlaw skav possybyl",
    "very-light-sleet": "erghlaw pur skav",
    "possible-light-sleet": "erghlaw skav possybyl",
    "light-sleet": "erghlaw skav",
    "medium-sleet": "erghlaw",
    "heavy-sleet": "erghlaw poos",
    "possible-very-light-snow": "ergh skav possybyl",
    "very-light-snow": "ergh pur skav",
    "possible-light-snow": "ergh skav possybyl",
    "light-snow": "ergh skav",
    "medium-snow": "ergh",
    "heavy-snow": "ergh poos",
    "possible-thunderstorm": "tewedhow-taran possybyl",
    "thunderstorm": "tewedhow-taran",
    "possible-medium-precipitation": "kodhans possybyl",
    "possible-heavy-precipitation": "kodhans poos possybyl",
    "possible-medium-rain": "glaw possybyl",
    "possible-heavy-rain": "glaw poos possybyl",
    "possible-medium-sleet": "erghlaw possybyl",
    "possible-heavy-sleet": "erghlaw poos possybyl",
    "possible-medium-snow": "ergh possybyl",
    "possible-heavy-snow": "ergh poos possybyl",
    "possible-very-light-freezing-rain": "glaw rewl pur skav possybyl",
    "very-light-freezing-rain": "glaw rewl pur skav",
    "possible-light-freezing-rain": "glaw rewl skav possybyl",
    "light-freezing-rain": "glaw rewl skav",
    "possible-medium-freezing-rain": "glaw rewl possybyl",
    "medium-freezing-rain": "glaw rewl",
    "possible-heavy-freezing-rain": "glaw rewl poos possybyl",
    "heavy-freezing-rain": "glaw rewl poos",
    "possible-hail": "storm hael possybyl",
    "hail": "storm hael",
    "light-wind": "nebes gwynsek",
    "medium-wind": "gwynsek",
    "heavy-wind": "gwynsek bys yn peryl",
    "low-humidity": "sygh",
    "high-humidity": "glyb",
    "fog": "niwlek",
    "very-light-clouds": "soprattuttu chjaru",
    "light-clouds": "nebes komolek",
    "medium-clouds": "komolek",
    "heavy-clouds": "komolek poos",
    "today-morning": "hedhyw vyttin",
    "later-today-morning": "diwettha hedhyw vyttin",
    "today-afternoon": "an dohajydh ma",
    "later-today-afternoon": "diwettha an dohajydh ma",
    "today-evening": "haneth",
    "later-today-evening": "diwettha haneth",
    "today-night": "an nos ma",
    "later-today-night": "diwettha haneth",
    "tomorrow-morning": "ternos vyttin",
    "tomorrow-afternoon": "dohajydhweyth a-vorow",
    "tomorrow-evening": "gorthugherweyth a-vorow",
    "tomorrow-night": "nosweyth a-vorow",
    "morning": "myttin",
    "afternoon": "dohajydh",
    "evening": "gorthugher",
    "night": "nos",
    "today": "hedhyw",
    "tomorrow": "a-vorow",
    "sunday": "dy' Sul",
    "monday": "dy' Lun",
    "tuesday": "dy' Meurth",
    "wednesday": "dy' Mergher",
    "thursday": "dy' Yow",
    "friday": "dy' Gwener",
    "saturday": "dy' Sadorn",
    "next-sunday": "dy' Sul a dheu",
    "next-monday": "dy' Lun a dheu",
    "next-tuesday": "dy' Meurth a dheu",
    "next-wednesday": "dy' Mergher a dheu",
    "next-thursday": "dy' Yow a dheu",
    "next-friday": "dy' Gwener a dheu",
    "next-saturday": "dy' Sadorn a dheu",
    "minutes": "$1 myn.",
    "fahrenheit": "$1\u00b0F",
    "celsius": "$1\u00b0C",
    "inches": "$1 mv.",
    "centimeters": "$1 cm.",
    "less-than": "le ages $1",
    "and": and_function,
    "through": through_function,
    "with": "$1, gans $2",
    "range": "$1\u2013$2",
    "parenthetical": parenthetical_function,
    "for-hour": "$1 rag an our",
    "starting-in": starting_in_function,
    "stopping-in": stopping_function,
    "starting-then-stopping-later": starting_then_stopping_later_function,
    "stopping-then-starting-later": stopping_then_starting_later_function,
    "for-day": "$1 dres oll an jydh",
    "starting": starting_function,
    "until": until_function,
    "until-starting-again": until_starting_again_function,
    "starting-continuing-until": starting_continuing_until_function,
    "during": during_function,
    "for-week": "$1 dres oll an seythun",
    "over-weekend": "$1 dres an bennseythun",
    "temperatures-peaking": "ughella tempredhow a $1 $2",
    "temperatures-rising": "tempredhow ow kressya dhe $1 $2",
    "temperatures-valleying": "tempredhow ow hedhi kodha dhe $1 $2",
    "temperatures-falling": "tempredhow ow kodha dhe $1 $2",
    "title": title_function,
    "sentence": sentence_function,
    "next-hour-forecast-status": "Darganow herwydh an our yw $1 drefen bos $2.",
    "unavailable": "ankavadow",
    "temporarily-unavailable": "ankavadow dres pols",
    "partially-unavailable": "ankavadow yn rann",
    "station-offline": "pub gorsav radar y'n ranndir dhywarlinen",
    "station-incomplete": "aswaow y'n gorherans dhyworth gorsavow radar y'n ranndir",
    "smoke": "mog",
    "haze": "kemygi",
    "mist": "niwl",
}
