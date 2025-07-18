# This would be one of your translations, as a Python dictionary
cases = {
    "صافِ": ["title", "clear"],
    "إحتمالية هطول أمطار خفيفة": ["title", "possible-very-light-precipitation"],
    "أمطار خفيفة": ["title", "very-light-precipitation"],
    "إحتمالية هطول أمطار خفيفة": ["title", "possible-light-precipitation"],
    "أمطار خفيفة": ["title", "light-precipitation"],
    "أمطار متوسطة": ["title", "medium-precipitation"],
    "أمطار غزيرة": ["title", "heavy-precipitation"],
    "إحتمالية هطول أمطار خفيفة": ["title", "possible-very-light-rain"],
    "أمطار خفيفة": ["title", "very-light-rain"],
    "إحتمالية أمطار خفيفة": ["title", "possible-light-rain"],
    "أمطار خفيفة": ["title", "light-rain"],
    "أمطار متوسطة": ["title", "medium-rain"],
    "أمطار غزيرة": ["title", "heavy-rain"],
    "إحتمالية موجة صقيع خفيفة": ["title", "possible-very-light-sleet"],
    "موجة صقيع خفيفة": ["title", "very-light-sleet"],
    "إحتمالية موجة صقيع خفيفة": ["title", "possible-light-sleet"],
    "موجة صقيع خفيفة": ["title", "light-sleet"],
    "صقيع": ["title", "medium-sleet"],
    "موجة صقيع شديدة": ["title", "heavy-sleet"],
    "احتمالية تساقط ثلوج خفيفة": ["title", "possible-very-light-snow"],
    "ثلوج خفيفة": ["title", "very-light-snow"],
    "احتمالية تساقط ثلوج خفيفة": ["title", "possible-light-snow"],
    "ثلوج خفيفة": ["title", "light-snow"],
    "ثلوج": ["title", "medium-snow"],
    "ثلوج كثيفة": ["title", "heavy-snow"],
    "رياح متوسطة": ["title", "medium-wind"],
    "عواصف": ["title", "heavy-wind"],
    "اجواء غائمة": ["title", "fog"],
    "واضح في الغالب": ["title", "very-light-clouds"],
    "غائم جزئياً": ["title", "light-clouds"],
    "اجواء غائمة": ["title", "medium-clouds"],
    "اجواء غائمة": ["title", "heavy-clouds"],
    "اجواء جافة و رياح خفيفة": ["title", ["and", "low-humidity", "light-wind"]],
    "أمطار خفيفة و عواصف": ["title", ["and", "very-light-rain", "heavy-wind"]],
    "اجواء رطبة و غائم جزئياً": ["title", ["and", "high-humidity", "light-clouds"]],
    "صافِ لهذه الساعة": ["sentence", ["for-hour", "clear"]],
    "رياح خفيفة تبدأ خلال 35 دقيقة": [
        "sentence",
        ["starting-in", "very-light-snow", ["minutes", 35]],
    ],
    "أمطار خفيفة تتوقف خلال 15 دقيقة": [
        "sentence",
        ["stopping-in", "light-rain", ["minutes", 15]],
    ],
    "موجة صقيع شديدة تبدأ خلال 20 دقيقة وتتوقف لاحقاً خلال 30 دقيقة": [
        "sentence",
        [
            "starting-then-stopping-later",
            "heavy-sleet",
            ["minutes", 20],
            ["minutes", 30],
        ],
    ],
    "أمطار متوسطة تتوقف خلال 25 دقيقة وتبدأ لاحقاً خلال 8 دقيقة": [
        "sentence",
        [
            "stopping-then-starting-later",
            "medium-rain",
            ["minutes", 25],
            ["minutes", 8],
        ],
    ],
    "اجواء غائمة خلال اليوم": ["sentence", ["for-day", "medium-clouds"]],
    "موجة صقيع خفيفة تبدأ في الصباح": [
        "sentence",
        ["starting", "very-light-sleet", "morning"],
    ],
    "رياح متوسطة حتى الليلة": ["sentence", ["until", "medium-wind", "today-night"]],
    "أمطار غزيرة حتى بعد الظهيرة": [
        "sentence",
        ["until", "heavy-precipitation", "afternoon"],
    ],
    "رياح خفيفة بعد الظهيرة": ["sentence", ["during", "light-wind", "afternoon"]],
    "ثلوج لاحقاً هذا المساء و الغد صباحاً": [
        "sentence",
        ["during", "medium-snow", ["and", "later-today-evening", "tomorrow-morning"]],
    ],
    "أمطار غزيرة حتى لاحقاً هذا الصباح وتبدأ مجدداً في هذا المساء": [
        "sentence",
        ["until-starting-again", "heavy-rain", "later-today-morning", "today-evening"],
    ],
    "اجواء غائمة تبدأ في المساء وتستمر حتى الليل": [
        "sentence",
        ["starting-continuing-until", "heavy-clouds", "evening", "night"],
    ],
    "موجة صقيع خفيفة لاحقاً بعد الظهر و اجواء غائمة الغد صباحاً": [
        "sentence",
        [
            "and",
            ["during", "light-sleet", "later-today-afternoon"],
            ["during", "fog", "tomorrow-morning"],
        ],
    ],
    "عواصف تبدأ في هذا الصباح وتستمر حتى بعد الظهر و صقيع الغد صباحاً": [
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
    "اجواء غائمة تبدأ لاحقاً الليلة و ثلوج كثيفة غداً بعد الظهر": [
        "sentence",
        [
            "and",
            ["starting", "heavy-clouds", "later-today-night"],
            ["during", "heavy-snow", "tomorrow-afternoon"],
        ],
    ],
    "اجواء جافة الليلة و أمطار خفيفة تبدأ في الغد مساءً وتستمر حتى الغد ليلاً": [
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
    "ثلوج (5 انش) خلال الليل": [
        "sentence",
        ["during", ["parenthetical", "medium-snow", ["inches", 5]], "night"],
    ],
    "ثلوج خفيفة (2 سم) لاحقاً هذا الصباح": [
        "sentence",
        [
            "during",
            ["parenthetical", "light-snow", ["centimeters", 2]],
            "later-today-morning",
        ],
    ],
    "ثلوج كثيفة (8\u201312 انش) خلال اليوم": [
        "sentence",
        ["for-day", ["parenthetical", "heavy-snow", ["inches", ["range", 8, 12]]]],
    ],
    "ثلوج (أقل من 1 سم) بعد الظهيرة": [
        "sentence",
        [
            "during",
            ["parenthetical", "medium-snow", ["less-than", ["centimeters", 1]]],
            "afternoon",
        ],
    ],
    "لا أمطار خلال الأسبوع مع درجات حرارة تبلغ ذروتها عند 85\u00b0F غداً": [
        "sentence",
        [
            "with",
            ["for-week", "no-precipitation"],
            ["temperatures-peaking", ["fahrenheit", 85], "tomorrow"],
        ],
    ],
    "هطول أمطار وثلوج خلال نهاية الأسبوع مع درجات حرارة ترتفع حتى 32\u00b0C يوم الخميس": [
        "sentence",
        [
            "with",
            ["over-weekend", "mixed-precipitation"],
            ["temperatures-rising", ["celsius", 32], "thursday"],
        ],
    ],
    "أمطار خفيفة يوم الإثنين مع انخفاض درجات الحرارة لأدنى مستوى لها عند 15\u00b0F يوم الجمعة": [
        "sentence",
        [
            "with",
            ["during", "very-light-rain", "monday"],
            ["temperatures-valleying", ["fahrenheit", 15], "friday"],
        ],
    ],
    "ثلوج خفيفة يوم الثلاثاء و الأربعاء القادم مع درجات حرارة تنخفض حتى 0\u00b0C يوم الأحد": [
        "sentence",
        [
            "with",
            ["during", "light-snow", ["and", "tuesday", "next-wednesday"]],
            ["temperatures-falling", ["celsius", 0], "sunday"],
        ],
    ],
    "ثلوج خفيفة يومي الثلاثاء و الأربعاء مع درجات حرارة تنخفض حتى 0\u00b0C يوم الأحد": [
        "sentence",
        [
            "with",
            ["during", "light-snow", ["and", "tuesday", "wednesday"]],
            ["temperatures-falling", ["celsius", 0], "sunday"],
        ],
    ],
    "أمطار متوسطة اليوم حتى يوم السبت مع درجات حرارة تبلغ ذروتها عند 100\u00b0F يوم الإثنين": [
        "sentence",
        [
            "with",
            ["during", "medium-precipitation", ["through", "today", "saturday"]],
            ["temperatures-peaking", ["fahrenheit", 100], "monday"],
        ],
    ],
    "عواصف محتملة": ["title", "possible-thunderstorm"],
    "أمطار غزيرة و عواصف": ["title", ["and", "heavy-rain", "thunderstorm"]],
    "هطول أمطار وثلوج (1\u20133 انش من الثلج) خلال اليوم": [
        "sentence",
        [
            "for-day",
            ["parenthetical", "mixed-precipitation", ["inches", ["range", 1, 3]]],
        ],
    ],
    "ثلوج كثيفة (1\u20133 انش)": [
        "title",
        ["parenthetical", "heavy-snow", ["inches", ["range", 1, 3]]],
    ],
    "ثلوج كثيفة (3\u20135 سم)": [
        "title",
        ["parenthetical", "heavy-snow", ["centimeters", ["range", 3, 5]]],
    ],
    "دخان": ["title", "smoke"],
    "دخان خلال اليوم": ["sentence", ["for-day", "smoke"]],
    "دخان في الصباح": ["sentence", ["during", "smoke", "morning"]],
    "دخان حتى هذا المساء": ["sentence", ["until", "smoke", "today-evening"]],
    "دخان و غائم جزئياً": ["title", ["and", "smoke", "light-clouds"]],
    "ضباب": ["title", "haze"],
    "ضباب خلال اليوم": ["sentence", ["for-day", "haze"]],
    "ضباب بعد الظهيرة": ["sentence", ["during", "haze", "afternoon"]],
    "ضباب و اجواء رطبة": ["title", ["and", "haze", "high-humidity"]],
    "شبورة": ["title", "mist"],
    "شبورة خلال اليوم": ["sentence", ["for-day", "mist"]],
    "شبورة خلال الليل": ["sentence", ["during", "mist", "night"]],
    "شبورة و اجواء غائمة": ["title", ["and", "mist", "heavy-clouds"]],
}
