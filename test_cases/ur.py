# This would be one of your translations, as a Python dictionary
cases = {
    "صاف کریں": ["title", "clear"],
    "ممکنہ ورن": ["title", "possible-very-light-precipitation"],
    "ہلکی ورن": ["title", "very-light-precipitation"],
    "ممکنہ ہلکی ورن": ["title", "possible-light-precipitation"],
    "ہلکی ورن": ["title", "light-precipitation"],
    "ورن": ["title", "medium-precipitation"],
    "بھاری ورن": ["title", "heavy-precipitation"],
    "ممکنہ بوندا باندی": ["title", "possible-very-light-rain"],
    "بوندا باندی": ["title", "very-light-rain"],
    "ممکنہ ہلکی بارش": ["title", "possible-light-rain"],
    "ہلکی بارش": ["title", "light-rain"],
    "بارش": ["title", "medium-rain"],
    "بھاری بارش": ["title", "heavy-rain"],
    "ممکنہ اولے والی بارش": ["title", "possible-very-light-sleet"],
    "ہلکی اولے والی بارش": ["title", "very-light-sleet"],
    "ممکنہ ہلکی اولے والی بارش": ["title", "possible-light-sleet"],
    "ہلکی اولے والی بارش": ["title", "light-sleet"],
    "اولے والی بارش": ["title", "medium-sleet"],
    "بھاری اولے والی بارش": ["title", "heavy-sleet"],
    "ممکنہ برف": ["title", "possible-very-light-snow"],
    "برف": ["title", "very-light-snow"],
    "ممکنہ ہلکی برف": ["title", "possible-light-snow"],
    "ہلکی برف": ["title", "light-snow"],
    "برف باری": ["title", "medium-snow"],
    "بھاری برف باری": ["title", "heavy-snow"],
    "طوفانی ہوا": ["title", "medium-wind"],
    "خطرناک ہوائی": ["title", "heavy-wind"],
    "دھندلا": ["title", "fog"],
    "زیادہ تر واضح": ["title", "very-light-clouds"],
    "جزوی طور پر ابر آلود": ["title", "light-clouds"],
    "زیادہ تر ابر آلود": ["title", "medium-clouds"],
    "ابر آلود": ["title", "heavy-clouds"],
    "ہوائی اور روکھا": ["title", ["and", "low-humidity", "light-wind"]],
    "خطرناک ہوائی اور بوندا باندی": ["title", ["and", "very-light-rain", "heavy-wind"]],
    "جزوی طور پر ابر آلود اور نمی": ["title", ["and", "high-humidity", "light-clouds"]],
    "صاف کریں ایک گھنٹے کے لئے": ["sentence", ["for-hour", "clear"]],
    "شروع ہو رہا برف میں منٹ 35": [
        "sentence",
        ["starting-in", "very-light-snow", ["minutes", 35]],
    ],
    "رک رہا ہلکی بارش میں منٹ 15": [
        "sentence",
        ["stopping-in", "light-rain", ["minutes", 15]],
    ],
    "رک رہا ہے منٹ 30 شروع ہو رہا، بعد میں بھاری اولے والی بارش میں منٹ 20": [
        "sentence",
        [
            "starting-then-stopping-later",
            "heavy-sleet",
            ["minutes", 20],
            ["minutes", 30],
        ],
    ],
    "شروع ہو رہا ہے منٹ 8 رک رہا، بعد میں بارش میں منٹ 25": [
        "sentence",
        [
            "stopping-then-starting-later",
            "medium-rain",
            ["minutes", 25],
            ["minutes", 8],
        ],
    ],
    "پورے دن زیادہ تر ابر آلود": ["sentence", ["for-day", "medium-clouds"]],
    "صبح میں ہلکی اولے والی بارش": [
        "sentence",
        ["starting", "very-light-sleet", "morning"],
    ],
    "طوفانی ہوا تک اس رات": ["sentence", ["until", "medium-wind", "today-night"]],
    "بھاری ورن تک دوپہر": ["sentence", ["until", "heavy-precipitation", "afternoon"]],
    "کے دوران دوپہر ہوائی": ["sentence", ["during", "light-wind", "afternoon"]],
    "کے دوران کل صبح اور بعد میں اس شام برف باری": [
        "sentence",
        ["during", "medium-snow", ["and", "later-today-evening", "tomorrow-morning"]],
    ],
    "اس شام دوبارہ شروع کر رہا ہے ،بھاری بارش تک بعد میں آج صبح": [
        "sentence",
        ["until-starting-again", "heavy-rain", "later-today-morning", "today-evening"],
    ],
    "رات بھر جاری رہا ہے جب تک ،ابر آلود تک شام": [
        "sentence",
        ["starting-continuing-until", "heavy-clouds", "evening", "night"],
    ],
    "کے دوران کل صبح دھندلا اور کے دوران بعد میں اس دوپہر ہلکی اولے والی بارش": [
        "sentence",
        [
            "and",
            ["during", "light-sleet", "later-today-afternoon"],
            ["during", "fog", "tomorrow-morning"],
        ],
    ],
    "کے دوران کل صبح اولے والی بارش اور اس دوپہر جاری رہا ہے جب تک ،خطرناک ہوائی تک اس صبح": [
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
    "کے دوران کل دوپہر بھاری برف باری اور بعد میں اس رات میں ابر آلود": [
        "sentence",
        [
            "and",
            ["starting", "heavy-clouds", "later-today-night"],
            ["during", "heavy-snow", "tomorrow-afternoon"],
        ],
    ],
    "کل رات جاری رہا ہے جب تک ،ہلکی ورن تک کل شام اور کے دوران اس رات روکھا": [
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
    "کے دوران رات بھر برف باری (انچ 5)": [
        "sentence",
        ["during", ["parenthetical", "medium-snow", ["inches", 5]], "night"],
    ],
    "کے دوران بعد میں آج صبح ہلکی برف (سینٹی میٹرس 2)": [
        "sentence",
        [
            "during",
            ["parenthetical", "light-snow", ["centimeters", 2]],
            "later-today-morning",
        ],
    ],
    "پورے دن بھاری برف باری (انچ 8–12)": [
        "sentence",
        ["for-day", ["parenthetical", "heavy-snow", ["inches", ["range", 8, 12]]]],
    ],
    "کے دوران دوپہر برف باری (سے کم سینٹی میٹرس 1)": [
        "sentence",
        [
            "during",
            ["parenthetical", "medium-snow", ["less-than", ["centimeters", 1]]],
            "afternoon",
        ],
    ],
    "کے ساتھ ہفتے کے دن پر کل فارن ہائیٹ 85، پورے ہفتے کوئی ورن نہیں": [
        "sentence",
        [
            "with",
            ["for-week", "no-precipitation"],
            ["temperatures-peaking", ["fahrenheit", 85], "tomorrow"],
        ],
    ],
    "کے ساتھ کی طرف تیز درجہ حرارت بڑھ رہا ہے جمعرات کو سیلشن 32، ہفتے کے دن پر مخلوط ورن": [
        "sentence",
        [
            "with",
            ["over-weekend", "mixed-precipitation"],
            ["temperatures-rising", ["celsius", 32], "thursday"],
        ],
    ],
    "کے ساتھ کے نیچے تیز درجہ حرارت بن رہا ہے جمعہ کو فارن ہائیٹ 15، کے دوران پیر کو بوندا باندی": [
        "sentence",
        [
            "with",
            ["during", "very-light-rain", "monday"],
            ["temperatures-valleying", ["fahrenheit", 15], "friday"],
        ],
    ],
    "کے ساتھ کی جانب تیز درجہ حرارت بن رہا ہے اتوار کو سیلشن 0، کے دوران اگلے بدھ اور منگل کو ہلکی برف": [
        "sentence",
        [
            "with",
            ["during", "light-snow", ["and", "tuesday", "next-wednesday"]],
            ["temperatures-falling", ["celsius", 0], "sunday"],
        ],
    ],
    "کے ساتھ ہفتے کے دن پر پیر کو فارن ہائیٹ 100، کے دوران بھر ہفتے کو، آج کے دن ورن": [
        "sentence",
        [
            "with",
            ["during", "medium-precipitation", ["through", "today", "saturday"]],
            ["temperatures-peaking", ["fahrenheit", 100], "monday"],
        ],
    ],
    "پورے دن مخلوط ورن (انچ 1–3)": [
        "sentence",
        [
            "for-day",
            ["parenthetical", "mixed-precipitation", ["inches", ["range", 1, 3]]],
        ],
    ],
    "بھاری برف باری (انچ 1–3)": [
        "title",
        ["parenthetical", "heavy-snow", ["inches", ["range", 1, 3]]],
    ],
    "بھاری برف باری (سینٹی میٹرس 3–5)": [
        "title",
        ["parenthetical", "heavy-snow", ["centimeters", ["range", 3, 5]]],
    ],
    "ممکنہ برق و باراں": ["title", "possible-thunderstorm"],
    "برق و باراں اور بھاری بارش": ["title", ["and", "heavy-rain", "thunderstorm"]],
    "شروع ہو رہا بوندا باندی میں سے کم منٹ 1": [
        "sentence",
        ["starting-in", "very-light-rain", ["less-than", ["minutes", 1]]],
    ],
    "دھواں": ["title", "smoke"],
    "پورے دن دھواں": ["sentence", ["for-day", "smoke"]],
    "کے دوران صبح دھواں": ["sentence", ["during", "smoke", "morning"]],
    "دھواں تک اس شام": ["sentence", ["until", "smoke", "today-evening"]],
    "جزوی طور پر ابر آلود اور دھواں": ["title", ["and", "smoke", "light-clouds"]],
    "دھند": ["title", "haze"],
    "پورے دن دھند": ["sentence", ["for-day", "haze"]],
    "کے دوران دوپہر دھند": ["sentence", ["during", "haze", "afternoon"]],
    "نمی اور دھند": ["title", ["and", "haze", "high-humidity"]],
    "کے دوران رات بھر دھند": ["sentence", ["during", "mist", "night"]],
    "ابر آلود اور دھند": ["title", ["and", "mist", "heavy-clouds"]],
}
