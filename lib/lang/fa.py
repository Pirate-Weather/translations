def strip_prefix(period):
    if period.startswith("در طول "):
        return period[7:]
    return period


def custom_capitalize(s):
    # Do not capitalize certain words:
    if s in ["a", "and", "cm", "in", "of", "with"]:
        return s
    return s[0].upper() + s[1:] if s else s


def and_function(stack, a, b):
    return a + " و " + b


def through_function(stack, a, b):
    return a + " تا " + b


def parenthetical_function(stack, a, b):
    return f"{a} ({b}{' برف)' if a == 'بارش ترکیبی' else ')'}"


def until_function(stack, condition, period):
    return condition + " تا " + strip_prefix(period)


def until_starting_again_function(stack, condition, a, b):
    return (
        condition
        + " تا "
        + strip_prefix(a)
        + " و سپس "
        + strip_prefix(b)
        + " دوباره شروع می‌شود"
    )


def starting_continuing_until_function(stack, condition, a, b):
    return (
        condition
        + " "
        + strip_prefix(a)
        + " شروع می‌شود و تا "
        + strip_prefix(b)
        + " ادامه می‌یابد"
    )


template = {
    "clear": "صاف",
    "no-precipitation": "بدون بارش",
    "mixed-precipitation": "بارش ترکیبی",
    "possible-very-light-precipitation": "احتمال بارش بسیار پراکنده",
    "very-light-precipitation": "بارش بسیار پراکنده",
    "possible-light-precipitation": "احتمال بارش پراکنده",
    "light-precipitation": "بارش پراکنده",
    "medium-precipitation": "بارش",
    "heavy-precipitation": "بارش شدید",
    "possible-very-light-rain": "احتمال رگبار پراکنده",
    "very-light-rain": "رگبار پراکنده",
    "possible-light-rain": "احتمال باران پراکنده",
    "light-rain": "باران پراکنده",
    "medium-rain": "باران",
    "heavy-rain": "باران شدید",
    "possible-very-light-sleet": "احتمال تگرگ بسیار پراکنده",
    "very-light-sleet": "تگرگ بسیار پراکنده",
    "possible-light-sleet": "احتمال تگرگ پراکنده",
    "light-sleet": "تگرگ پراکنده",
    "medium-sleet": "تگرگ",
    "heavy-sleet": "تگرگ شدید",
    "possible-very-light-snow": "احتمال برف بسیار پراکنده",
    "very-light-snow": "برف بسیار پراکنده",
    "possible-light-snow": "احتمال برف پراکنده",
    "light-snow": "برف پراکنده",
    "medium-snow": "برف",
    "heavy-snow": "برف شدید",
    "possible-thunderstorm": "احتمال آذرخش و تندر",
    "thunderstorm": "آذرخش و تندر",
    "possible-medium-precipitation": "بارش احتمالی",
    "possible-heavy-precipitation": "احتمال بارش شدید",
    "possible-medium-rain": "باران احتمالی",
    "possible-heavy-rain": "باران شدید احتمالی",
    "possible-medium-sleet": "بارش احتمالی",
    "possible-heavy-sleet": "بارش باران سنگین احتمالی",
    "possible-medium-snow": "برف احتمالی",
    "possible-heavy-snow": "احتمال برف سنگین",
    "possible-freezing-drizzle": "نم نم باران یخبندان احتمالی",
    "freezing-drizzle": "نم نم باران یخ زده",
    "possible-light-freezing-rain": "باران یخبندان خفیف احتمالی",
    "light-freezing-rain": "باران یخبندان خفیف",
    "possible-freezing-rain": "باران یخبندان احتمالی",
    "freezing-rain": "باران یخ زده",
    "possible-heavy-freezing-rain": "باران یخبندان شدید احتمالی",
    "heavy-freezing-rain": "باران یخبندان شدید",
    "possible-hail": "تگرگ احتمالی",
    "hail": "تگرگ",
    "light-wind": "نسیم",
    "medium-wind": "باد",
    "heavy-wind": "باد شدید",
    "low-humidity": "رطوبت پایین",
    "high-humidity": "رطوبت بالا",
    "fog": "مه",
    "very-light-clouds": "عمدتا روشن",
    "light-clouds": "آسمان کمی ابری",
    "medium-clouds": "آسمان کمی تا قسمتی ابری",
    "heavy-clouds": "آسمان ابری",
    "today-morning": "صبح امروز",
    "later-today-morning": "پیش از ظهر امروز",
    "today-afternoon": "ظهر امروز",
    "later-today-afternoon": "بعد از ظهر امروز",
    "today-evening": "عصر امروز",
    "later-today-evening": "غروب امروز",
    "today-night": "امشب",
    "later-today-night": "نیمه شب امشب",
    "tomorrow-morning": "صبح فردا",
    "tomorrow-afternoon": "بعد از ظهر فردا",
    "tomorrow-evening": "عصر فردا",
    "tomorrow-night": "فردا شب",
    "morning": "در طول صبح",
    "afternoon": "در طول بعد از ظهر",
    "evening": "در طول عصر",
    "night": "در طول شب",
    "today": "امروز",
    "tomorrow": "فردا",
    "sunday": "یک‌شنبه",
    "monday": "دوشنبه",
    "tuesday": "سه‌شنبه",
    "wednesday": "چهارشنبه",
    "thursday": "پنج‌شنبه",
    "friday": "آدینه",
    "saturday": "شنبه",
    "next-sunday": "یک‌شنبه آینده",
    "next-monday": "دوشنبه آینده",
    "next-tuesday": "سه‌شبنه آینده",
    "next-wednesday": "چهارشنبه آینده",
    "next-thursday": "پنج‌شنبه آینده",
    "next-friday": "آدینه آینده",
    "next-saturday": "شنبه آینده",
    "minutes": "$1 دقیقه",
    "fahrenheit": "$1\u00b0F",
    "celsius": "$1\u00b0C",
    "inches": "$1 اینچ",
    "centimeters": "$1 سانتیمتر",
    "less-than": "کمتر از $1",
    "and": and_function,
    "through": through_function,
    "with": "$1، به همراه $2",
    "range": "$1 تا $2",
    "parenthetical": parenthetical_function,
    "for-hour": "$1 برای این ساعت",
    "starting-in": "$1 در $2 آغاز می‌شود",
    "stopping-in": "$1 در $2 پایان می‌یابد",
    "starting-then-stopping-later": "$1 در $2 آغاز می‌شود و $3 بعد پایان می‌یابد",
    "stopping-then-starting-later": "$1 در $2 پایان می‌یابد و $3 بعد دوباره آغاز می‌شود",
    "for-day": "$1 در طول روز",
    "starting": "$1 $2 آغاز می‌شود",
    "until": until_function,
    "until-starting-again": until_starting_again_function,
    "starting-continuing-until": starting_continuing_until_function,
    "during": "$1 $2",
    "for-week": "$1 در طول هفته",
    "over-weekend": "$1 در آخر هفته",
    "temperatures-peaking": "رسیدن حداکثر دما به $1 در $2",
    "temperatures-rising": "افزایش دما تا حداکثر $1 در $2",
    "temperatures-valleying": "رسیدن حداکثر دما به $1 در $2",
    "temperatures-falling": "کاهش حداکثر دما به $1 در $2",
    "title": "$1",
    "sentence": "$1",
    "next-hour-forecast-status": "next hour forecasts are $1 due to $2",
    "unavailable": "unavailable",
    "temporarily-unavailable": "temporarily unavailable",
    "partially-unavailable": "partially unavailable",
    "station-offline": "all nearby radar stations being offline",
    "station-incomplete": "gaps in coverage from nearby radar stations",
}
