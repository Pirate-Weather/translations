import re


def join_with_shared_prefix(a, b, joiner):
    i = 0
    while i < len(a) and i < len(b) and ord(a[i]) == ord(b[i]):
        i += 1
    while i > 0 and ord(a[i - 1]) != 32:  # Check for space
        i -= 1
    return a + joiner + b[i:]


def time2(time):
    translations = {
        "раніцай": "раніцы",
        "днём": "сярэдзіны дня",
        "вечарам": "вечара",
        "ноччу": "ночы",
        "сёння ранкам": "сённяшняй раніцы",
        "сёння позняй раніцай": "сённяшняй позняй раніцы",
        "сёння днём": "сярэдзіны дня",
        "сёння познім днём": "сённяшняга позняга дня",
        "сёння ўвечары": "сённяшняга вечара",
        "сёння познім вечарам": "сённяшняга позняга вечара",
        "сёння ноччу": "сённяшняй ночы",
        "сёння позняй ноччу": "сённяшняй позняй ночы",
        "заўтра раніцай": "заўтрашняй раніцы",
        "заўтра днём": "заўтрашняга дня",
        "заўтра ўвечары": "заўтрашняга вечара",
        "ўвечары": "вечара",
        "заўтра ноччу": "заўтрашняй ночы",
        "у нядзелю": "нядзелі",
        "у панядзелак": "панядзелка",
        "у аўторак": "аўторка",
        "у сераду": "серады",
        "у чацвер": "чацвярга",
        "у пятніцу": "пятніцы",
        "у суботу": "суботы",
    }
    return translations.get(time, time)


def and_function(stack, a, b):
    joiner = ", і " if "," in a else " і "
    return join_with_shared_prefix(a, b, joiner)


def through_function(stack, a, b):
    return join_with_shared_prefix(a, time2(b), " і да ")


def until_function(stack, condition, period):
    return condition + " да " + time2(period)


def until_starting_again_function(stack, condition, a, b):
    return condition + " да " + time2(a) + ", пачынаючыся зноў " + b


def starting_continuing_until_function(stack, condition, a, b):
    return condition + ", пачынаючыся з " + time2(a) + ", і да " + time2(b)


def title_function(stack, s):
    # Apply custom_capitalize to every word
    return re.sub(
        r"\S+",
        lambda word: word.group(0).capitalize()
        if word.group(0) != "і"
        else word.group(0),
        s,
    )


def sentence_function(stack, s):
    # Replace 'у' with 'ў' after vowels
    s = re.sub(
        r"[аеёіоуыэюя]\sу",
        lambda match: match.group(0)[:-1] + "ў",
        s,
        flags=re.IGNORECASE,
    )
    # Capitalize the first letter
    s = s[0].upper() + s[1:] if s else s
    # Add a period if missing
    if not s.endswith("."):
        s += "."
    return s


def during_function(stack, condition, time):
    return f"{condition} {time}"


template = {
    "clear": "ясна",
    "no-precipitation": "без ападкаў",
    "mixed-precipitation": "змешаныя ападкі",
    "possible-very-light-precipitation": "магчымы нязначныя ападкі",
    "very-light-precipitation": "нязначныя ападкі",
    "possible-light-precipitation": "магчымы невялікія ападкі",
    "light-precipitation": "невялікія ападкі",
    "medium-precipitation": "ападкі",
    "heavy-precipitation": "моцныя ападкі",
    "possible-very-light-rain": "магчымы нязначны дождж",
    "very-light-rain": "нязначны дождж",
    "possible-light-rain": "магчымы невялікі дождж",
    "light-rain": "невялікі дождж",
    "medium-rain": "дождж",
    "heavy-rain": "моцны дождж",
    "possible-very-light-sleet": "магчымы нязначны град",
    "very-light-sleet": "нязначны град",
    "possible-light-sleet": "магчымы невялікі град",
    "light-sleet": "невялікі град",
    "medium-sleet": "град",
    "heavy-sleet": "моцны град",
    "possible-very-light-snow": "магчымы нязначны снег",
    "very-light-snow": "нязначны снег",
    "possible-light-snow": "магчымы невялікі снег",
    "light-snow": "невялікі снег",
    "medium-snow": "снег",
    "heavy-snow": "снегапад",
    "possible-thunderstorm": "магчымы навальніцы",
    "thunderstorm": "навальніцы",
    "possible-medium-precipitation": "магчымы ападкі",
    "possible-heavy-precipitation": "магчымы моцныя ападкі",
    "possible-medium-rain": "магчымы дождж",
    "possible-heavy-rain": "магчымы моцны дождж",
    "possible-medium-sleet": "магчымы град",
    "possible-heavy-sleet": "магчымы моцны град",
    "possible-medium-snow": "магчымы снег",
    "possible-heavy-snow": "магчымы моцны снег",
    "possible-very-light-freezing-rain": "магчымы замарожванне нязначны дождж",
    "very-light-freezing-rain": "замарожванне нязначны дождж",
    "possible-light-freezing-rain": "магчымы невялікі замарожванне дождж",
    "light-freezing-rain": "невялікі замарожванне дождж",
    "possible-medium-freezing-rain": "магчымы замарожванне дождж",
    "medium-freezing-rain": "замарожванне дождж",
    "possible-heavy-freezing-rain": "магчымы моцны замарожванне дождж",
    "heavy-freezing-rain": "моцны замарожванне дождж",
    "possible-hail": "магчымы град",
    "hail": "град",
    "light-wind": "слабы вецер",
    "medium-wind": "вецер",
    "heavy-wind": "моцны вецер",
    "low-humidity": "суха",
    "high-humidity": "вільготна",
    "fog": "туман",
    "very-light-clouds": "моцная ясна",
    "light-clouds": "невялікая воблачнасць",
    "medium-clouds": "воблачна",
    "heavy-clouds": "моцная воблачнасць",
    "today-morning": "сёння ранкам",
    "later-today-morning": "сёння позняй раніцай",
    "today-afternoon": "сёння днём",
    "later-today-afternoon": "сёння познім днём",
    "today-evening": "сёння ўвечары",
    "later-today-evening": "сёння познім вечарам",
    "today-night": "сёння ноччу",
    "later-today-night": "сёння позняй ноччу",
    "tomorrow-morning": "заўтра раніцай",
    "tomorrow-afternoon": "заўтра днём",
    "tomorrow-evening": "заўтра ўвечары",
    "tomorrow-night": "заўтра ноччу",
    "morning": "раніцай",
    "afternoon": "днём",
    "evening": "ўвечары",
    "night": "ноччу",
    "today": "сёння",
    "tomorrow": "заўтра",
    "sunday": "у нядзелю",
    "monday": "у панядзелак",
    "tuesday": "у аўторак",
    "wednesday": "у сераду",
    "thursday": "у чацвер",
    "friday": "у пятніцу",
    "saturday": "у суботу",
    "next-sunday": "у наступную нядзелю",
    "next-monday": "у наступны панядзелак",
    "next-tuesday": "у наступны аўторак",
    "next-wednesday": "у наступную сераду",
    "next-thursday": "у наступны чацвер",
    "next-friday": "у наступную пятніцу",
    "next-saturday": "у наступную суботу",
    "minutes": "$1 хв",
    "fahrenheit": "$1\u00b0F",
    "celsius": "$1\u00b0C",
    "inches": "$1 in.",
    "centimeters": "$1 см.",
    "less-than": "менш за $1",
    "and": and_function,
    "through": through_function,
    "with": "$1, з $2",
    "range": "$1\u2013$2",
    "parenthetical": "$1 ($2)",
    "for-hour": "$1 на працягу наступнай гадзіны",
    "starting-in": "$1 пачынаецца на працягу $2",
    "stopping-in": "$1 заканчваецца на працягу $2",
    "starting-then-stopping-later": "$1 пачынаецца на працягу $2, і заканчваецца праз $3",
    "stopping-then-starting-later": "$1 заканчваецца на працягу $2, і пачынаецца зноў праз $3",
    "for-day": "$1 на працягу ўсяго дня",
    "starting": "$1 пачынаецца $2",
    "until": until_function,
    "until-starting-again": until_starting_again_function,
    "starting-continuing-until": starting_continuing_until_function,
    "during": during_function,
    "for-week": "$1 на працягу ўсяго тыдня",
    "over-weekend": "$1 на працягу ўсіх выходных",
    "temperatures-peaking": "тэмпературай, што ўздымаецца да максімуму $1 $2",
    "temperatures-rising": "тэмпературай, што ўздымаецца да $1 $2",
    "temperatures-valleying": "тэмпературай, якая апускаецца да $1 $2",
    "temperatures-falling": "тэмпературай, якая апускаецца да мінімуму $1 $2",
    "title": title_function,
    "sentence": sentence_function,
    "next-hour-forecast-status": "прагнозы на наступную гадзіну складаюць $1 з-за $2",
    "unavailable": "недаступны",
    "temporarily-unavailable": "часова недаступны",
    "partially-unavailable": "часткова недаступна",
    "station-offline": "усе бліжэйшыя радарныя станцыі адключаныя ад сеткі",
    "station-incomplete": "прабелы ў пакрыцці ад бліжэйшых радарных станцый",
    "smoke": "дым",
    "haze": "імгла",
    "mist": "туман",
}
