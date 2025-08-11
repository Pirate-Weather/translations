# This would be one of your translations, as a Python dictionary
cases = {
    "صاف": ["title", "clear"],
    "احتمال بارش پراکنده": ["title", "possible-very-light-precipitation"],
    "بارش پراکنده": ["title", "very-light-precipitation"],
    "احتمال بارش پراکنده": ["title", "possible-light-precipitation"],
    "بارش پراکنده": ["title", "light-precipitation"],
    "بارش": ["title", "medium-precipitation"],
    "بارش شدید": ["title", "heavy-precipitation"],
    "احتمال رگبار پراکنده": ["title", "possible-very-light-rain"],
    "رگبار پراکنده": ["title", "very-light-rain"],
    "احتمال باران پراکنده": ["title", "possible-light-rain"],
    "باران پراکنده": ["title", "light-rain"],
    "باران": ["title", "medium-rain"],
    "باران شدید": ["title", "heavy-rain"],
    "احتمال تگرگ بسیار پراکنده": ["title", "possible-very-light-sleet"],
    "تگرگ پراکنده": ["title", "very-light-sleet"],
    "احتمال تگرگ پراکنده": ["title", "possible-light-sleet"],
    "تگرگ پراکنده": ["title", "light-sleet"],
    "تگرگ": ["title", "medium-sleet"],
    "تگرگ شدید": ["title", "heavy-sleet"],
    "احتمال برف بسیار پراکنده": ["title", "possible-very-light-snow"],
    "برف بسیار پراکنده": ["title", "very-light-snow"],
    "احتمال برف پراکنده": ["title", "possible-light-snow"],
    "برف پراکنده": ["title", "light-snow"],
    "برف": ["title", "medium-snow"],
    "برف شدید": ["title", "heavy-snow"],
    "باد": ["title", "medium-wind"],
    "باد شدید": ["title", "heavy-wind"],
    "مه": ["title", "fog"],
    "عمدتا روشن": ["title", "very-light-clouds"],
    "آسمان کمی ابری": ["title", "light-clouds"],
    "آسمان کمی تا قسمتی ابری": ["title", "medium-clouds"],
    "آسمان ابری": ["title", "heavy-clouds"],
    "رطوبت پایین و نسیم": ["title", ["and", "low-humidity", "light-wind"]],
    "رگبار پراکنده و باد شدید": ["title", ["and", "very-light-rain", "heavy-wind"]],
    "رطوبت بالا و آسمان کمی ابری": ["title", ["and", "high-humidity", "light-clouds"]],
    "صاف برای این ساعت": ["sentence", ["for-hour", "clear"]],
    "برف بسیار پراکنده در 35 دقیقه آغاز می‌شود": [
        "sentence",
        ["starting-in", "very-light-snow", ["minutes", 35]],
    ],
    "باران پراکنده در 15 دقیقه پایان می‌یابد": [
        "sentence",
        ["stopping-in", "light-rain", ["minutes", 15]],
    ],
    "تگرگ شدید در 20 دقیقه آغاز می‌شود و 30 دقیقه بعد پایان می‌یابد": [
        "sentence",
        [
            "starting-then-stopping-later",
            "heavy-sleet",
            ["minutes", 20],
            ["minutes", 30],
        ],
    ],
    "باران در 25 دقیقه پایان می‌یابد و 8 دقیقه بعد دوباره آغاز می‌شود": [
        "sentence",
        [
            "stopping-then-starting-later",
            "medium-rain",
            ["minutes", 25],
            ["minutes", 8],
        ],
    ],
    "آسمان کمی تا قسمتی ابری در طول روز": ["sentence", ["for-day", "medium-clouds"]],
    "تگرگ بسیار پراکنده در طول صبح آغاز می‌شود": [
        "sentence",
        ["starting", "very-light-sleet", "morning"],
    ],
    "باد تا امشب": ["sentence", ["until", "medium-wind", "today-night"]],
    "بارش شدید تا بعد از ظهر": [
        "sentence",
        ["until", "heavy-precipitation", "afternoon"],
    ],
    "نسیم در طول بعد از ظهر": ["sentence", ["during", "light-wind", "afternoon"]],
    "برف غروب امروز و صبح فردا": [
        "sentence",
        ["during", "medium-snow", ["and", "later-today-evening", "tomorrow-morning"]],
    ],
    "باران شدید تا پیش از ظهر امروز و سپس عصر امروز دوباره شروع می‌شود": [
        "sentence",
        ["until-starting-again", "heavy-rain", "later-today-morning", "today-evening"],
    ],
    "آسمان ابری عصر شروع می‌شود و تا شب ادامه می‌یابد": [
        "sentence",
        ["starting-continuing-until", "heavy-clouds", "evening", "night"],
    ],
    "تگرگ پراکنده بعد از ظهر امروز و مه صبح فردا": [
        "sentence",
        [
            "and",
            ["during", "light-sleet", "later-today-afternoon"],
            ["during", "fog", "tomorrow-morning"],
        ],
    ],
    "باد شدید صبح امروز شروع می‌شود و تا ظهر امروز ادامه می‌یابد و تگرگ صبح فردا": [
        "sentence",
        [
            "and",
            [
                "starting-continuing-until",
                "heavy-wind",
                "today-morning",
                "today-afternoon",
            ],
            ["during", "medium-sleet", "tomorrow-morning"],
        ],
    ],
    "آسمان ابری نیمه شب امشب آغاز می‌شود و برف شدید بعد از ظهر فردا": [
        "sentence",
        [
            "and",
            ["starting", "heavy-clouds", "later-today-night"],
            ["during", "heavy-snow", "tomorrow-afternoon"],
        ],
    ],
    "رطوبت پایین امشب و بارش پراکنده عصر فردا شروع می‌شود و تا فردا شب ادامه می‌یابد": [
        "sentence",
        [
            "and",
            ["during", "low-humidity", "today-night"],
            [
                "starting-continuing-until",
                "light-precipitation",
                "tomorrow-evening",
                "tomorrow-night",
            ],
        ],
    ],
    "برف (5 اینچ) در طول شب": [
        "sentence",
        ["during", ["parenthetical", "medium-snow", ["inches", 5]], "night"],
    ],
    "برف پراکنده (2 سانتیمتر) پیش از ظهر امروز": [
        "sentence",
        [
            "during",
            ["parenthetical", "light-snow", ["centimeters", 2]],
            "later-today-morning",
        ],
    ],
    "برف شدید (8 تا 12 اینچ) در طول روز": [
        "sentence",
        ["for-day", ["parenthetical", "heavy-snow", ["inches", ["range", 8, 12]]]],
    ],
    "برف (کمتر از 1 سانتیمتر) در طول بعد از ظهر": [
        "sentence",
        [
            "during",
            ["parenthetical", "medium-snow", ["less-than", ["centimeters", 1]]],
            "afternoon",
        ],
    ],
    "بدون بارش در طول هفته، به همراه رسیدن حداکثر دما به 85\u00b0F در فردا": [
        "sentence",
        [
            "with",
            ["for-week", "no-precipitation"],
            ["temperatures-peaking", ["fahrenheit", 85], "tomorrow"],
        ],
    ],
    "بارش ترکیبی در آخر هفته، به همراه افزایش دما تا حداکثر 32\u00b0C در پنج‌شنبه": [
        "sentence",
        [
            "with",
            ["over-weekend", "mixed-precipitation"],
            ["temperatures-rising", ["celsius", 32], "thursday"],
        ],
    ],
    "رگبار پراکنده دوشنبه، به همراه رسیدن حداکثر دما به 15\u00b0F در آدینه": [
        "sentence",
        [
            "with",
            ["during", "very-light-rain", "monday"],
            ["temperatures-valleying", ["fahrenheit", 15], "friday"],
        ],
    ],
    "برف پراکنده سه‌شنبه و چهارشنبه آینده، به همراه کاهش حداکثر دما به 0\u00b0C در یک‌شنبه": [
        "sentence",
        [
            "with",
            ["during", "light-snow", ["and", "tuesday", "next-wednesday"]],
            ["temperatures-falling", ["celsius", 0], "sunday"],
        ],
    ],
    "بارش امروز تا شنبه، به همراه رسیدن حداکثر دما به 100\u00b0F در دوشنبه": [
        "sentence",
        [
            "with",
            ["during", "medium-precipitation", ["through", "today", "saturday"]],
            ["temperatures-peaking", ["fahrenheit", 100], "monday"],
        ],
    ],
    "بارش ترکیبی (1 تا 3 اینچ برف) در طول روز": [
        "sentence",
        [
            "for-day",
            ["parenthetical", "mixed-precipitation", ["inches", ["range", 1, 3]]],
        ],
    ],
    "برف شدید (1 تا 3 اینچ)": [
        "title",
        ["parenthetical", "heavy-snow", ["inches", ["range", 1, 3]]],
    ],
    "برف شدید (3 تا 5 سانتیمتر)": [
        "title",
        ["parenthetical", "heavy-snow", ["centimeters", ["range", 3, 5]]],
    ],
    "احتمال آذرخش و تندر": ["title", "possible-thunderstorm"],
    "باران شدید و آذرخش و تندر": ["title", ["and", "heavy-rain", "thunderstorm"]],
    "رگبار پراکنده در کمتر از 1 دقیقه آغاز می‌شود": [
        "sentence",
        ["starting-in", "very-light-rain", ["less-than", ["minutes", 1]]],
    ],
    "دود": ["title", "smoke"],
    "دود در طول روز": ["sentence", ["for-day", "smoke"]],
    "دود در طول صبح": ["sentence", ["during", "smoke", "morning"]],
    "دود تا عصر امروز": ["sentence", ["until", "smoke", "today-evening"]],
    "دود و آسمان کمی ابری": ["title", ["and", "smoke", "light-clouds"]],
    "غبار": ["title", "haze"],
    "غبار در طول روز": ["sentence", ["for-day", "haze"]],
    "غبار در طول بعد از ظهر": ["sentence", ["during", "haze", "afternoon"]],
    "غبار و رطوبت بالا": ["title", ["and", "haze", "high-humidity"]],
    "مه در طول روز": ["sentence", ["for-day", "mist"]],
    "مه در طول شب": ["sentence", ["during", "mist", "night"]],
    "مه و آسمان ابری": ["title", ["and", "mist", "heavy-clouds"]],
    "آذرخش و تندر برای این ساعت": ["sentence", ["for-hour", "thunderstorm"]],
    "تگرگ در 5 دقیقه آغاز می‌شود و 45 دقیقه بعد پایان می‌یابد": [
        "sentence",
        [
            "starting-then-stopping-later",
            "hail",
            ["minutes", 5],
            ["minutes", 45],
        ],
    ],
    "باران یخبندان شدید در 10 دقیقه پایان می‌یابد و 32 دقیقه بعد دوباره آغاز می‌شود": [
        "sentence",
        [
            "stopping-then-starting-later",
            "heavy-freezing-rain",
            ["minutes", 10],
            ["minutes", 32],
        ],
    ],
    "نم نم باران یخ زده در 49 دقیقه آغاز می‌شود": [
        "sentence",
        ["starting-in", "very-light-freezing-rain", ["minutes", 49]],
    ],
}
