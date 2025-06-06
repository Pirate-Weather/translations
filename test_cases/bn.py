# This would be one of your translations, as a Python dictionary
cases = {
    "পরিষ্কার": ["title", "clear"],
    "সম্ভাবিত হাল্কা বর্ষা": ["title", "possible-very-light-precipitation"],
    "হাল্কা বর্ষা": ["title", "very-light-precipitation"],
    "সম্ভাবিত হাল্কা বর্ষা": ["title", "possible-light-precipitation"],
    "হাল্কা বর্ষা": ["title", "light-precipitation"],
    "বর্ষা": ["title", "medium-precipitation"],
    "ভারী বর্ষা": ["title", "heavy-precipitation"],
    "সম্ভাবিত বৃষ্টি": ["title", "possible-very-light-rain"],
    "বৃষ্টি": ["title", "very-light-rain"],
    "সম্ভাবিত হাল্কা বৃষ্টি": ["title", "possible-light-rain"],
    "হাল্কা বৃষ্টি": ["title", "light-rain"],
    "বৃষ্টি": ["title", "medium-rain"],
    "ভারী বৃষ্টি": ["title", "heavy-rain"],
    "সম্ভাবিত হাল্কা শিলাবৃষ্টি": ["title", "possible-very-light-sleet"],
    "হাল্কা শিলাবৃষ্টি": ["title", "very-light-sleet"],
    "সম্ভাবিত হাল্কা শিলাবৃষ্টি": ["title", "possible-light-sleet"],
    "হাল্কা শিলাবৃষ্টি": ["title", "light-sleet"],
    "শিলাবৃষ্টি": ["title", "medium-sleet"],
    "ভারী শিলাবৃষ্টি": ["title", "heavy-sleet"],
    "সম্ভাবিত প্রবাহ": ["title", "possible-very-light-snow"],
    "প্রবাহ": ["title", "very-light-snow"],
    "সম্ভাবিত হাল্কা তুষারাপাত": ["title", "possible-light-snow"],
    "হাল্কা তুষারাপাত": ["title", "light-snow"],
    "তুষারাপাত": ["title", "medium-snow"],
    "ভারী তুষারাপাত": ["title", "heavy-snow"],
    "ঝড়ো": ["title", "medium-wind"],
    "গম্ভীর রূপে ঝড়ো": ["title", "heavy-wind"],
    "কুয়াশাছন্ন": ["title", "fog"],
    "প্রায় পরিষ্কার": ["title", "very-light-clouds"],
    "হাল্কা মেঘাছন্ন": ["title", "light-clouds"],
    "প্রায় মেঘাছন্ন": ["title", "medium-clouds"],
    "তমসাচ্ছন্ন": ["title", "heavy-clouds"],
    "শুকনো এবং বায়ুময়": ["title", ["and", "low-humidity", "light-wind"]],
    "বৃষ্টি এবং গম্ভীর রূপে ঝড়ো": ["title", ["and", "very-light-rain", "heavy-wind"]],
    "আর্দ্র এবং হাল্কা মেঘাছন্ন": ["title", ["and", "high-humidity", "light-clouds"]],
    "পরিষ্কার ঘন্টার জন্য": ["sentence", ["for-hour", "clear"]],
    "প্রবাহ 35 মিনিট এ শুরু হচ্ছে": [
        "sentence",
        ["starting-in", "very-light-snow", ["minutes", 35]],
    ],
    "হাল্কা বৃষ্টি 15 মিনিট এ বন্দ হচ্ছে": [
        "sentence",
        ["stopping-in", "light-rain", ["minutes", 15]],
    ],
    "ভারী শিলাবৃষ্টি 20 মিনিট এ শুরু হচ্ছে, 30 মিনিট এ পরে বন্দ হচ্ছে": [
        "sentence",
        [
            "starting-then-stopping-later",
            "heavy-sleet",
            ["minutes", 20],
            ["minutes", 30],
        ],
    ],
    "বৃষ্টি 25 মিনিট এ বন্দ হচ্ছে, আবার পরে 8 মিনিট এ শুরু হচ্ছে": [
        "sentence",
        [
            "stopping-then-starting-later",
            "medium-rain",
            ["minutes", 25],
            ["minutes", 8],
        ],
    ],
    "সারাদিন প্রায় মেঘাছন্ন": ["sentence", ["for-day", "medium-clouds"]],
    "হাল্কা শিলাবৃষ্টি সকাল এ শুরু হচ্ছে": [
        "sentence",
        ["starting", "very-light-sleet", "morning"],
    ],
    "ঝড়ো আজ রাতে অব্দি": ["sentence", ["until", "medium-wind", "today-night"]],
    "ভারী বর্ষা দুপুর অব্দি": ["sentence", ["until", "heavy-precipitation", "afternoon"]],
    "বায়ুময় দুপুর এর সময়ে": ["sentence", ["during", "light-wind", "afternoon"]],
    "তুষারাপাত এই বিকেলে একটু পরে এবং কাল সকাল এর সময়ে": [
        "sentence",
        ["during", "medium-snow", ["and", "later-today-evening", "tomorrow-morning"]],
    ],
    "ভারী বৃষ্টি এই সকালে একটু পরে অব্দি, এই বিকেলে আবার শুরু": [
        "sentence",
        ["until-starting-again", "heavy-rain", "later-today-morning", "today-evening"],
    ],
    "তমসাচ্ছন্ন বিকেল অব্দি, রাতারাতি অব্দি চলছে": [
        "sentence",
        ["starting-continuing-until", "heavy-clouds", "evening", "night"],
    ],
    "হাল্কা শিলাবৃষ্টি এই বিকেলে একটু পরে এর সময়ে এবং কুয়াশাছন্ন কাল সকাল এর সময়ে": [
        "sentence",
        [
            "and",
            ["during", "light-sleet", "later-today-afternoon"],
            ["during", "fog", "tomorrow-morning"],
        ],
    ],
    "গম্ভীর রূপে ঝড়ো এই সকালে অব্দি, এই বিকেলে অব্দি চলছে এবং শিলাবৃষ্টি কাল সকাল এর সময়ে": [
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
    "তমসাচ্ছন্ন আজ রাতে একটু পরে এ শুরু হচ্ছে এবং ভারী তুষারাপাত কাল দুপুর এর সময়ে": [
        "sentence",
        [
            "and",
            ["starting", "heavy-clouds", "later-today-night"],
            ["during", "heavy-snow", "tomorrow-afternoon"],
        ],
    ],
    "শুকনো আজ রাতে এর সময়ে এবং হাল্কা বর্ষা কাল বিকেল অব্দি, কাল রাত অব্দি চলছে": [
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
    "তুষারাপাত (5 ইঞ্চি) রাতারাতি এর সময়ে": [
        "sentence",
        ["during", ["parenthetical", "medium-snow", ["inches", 5]], "night"],
    ],
    "হাল্কা তুষারাপাত (2 সেন্টিমিটার) এই সকালে একটু পরে এর সময়ে": [
        "sentence",
        [
            "during",
            ["parenthetical", "light-snow", ["centimeters", 2]],
            "later-today-morning",
        ],
    ],
    "সারাদিন ভারী তুষারাপাত (8\u201312 ইঞ্চি)": [
        "sentence",
        ["for-day", ["parenthetical", "heavy-snow", ["inches", ["range", 8, 12]]]],
    ],
    "তুষারাপাত (1 সেন্টিমিটার এর থেকে কম) দুপুর এর সময়ে": [
        "sentence",
        [
            "during",
            ["parenthetical", "medium-snow", ["less-than", ["centimeters", 1]]],
            "afternoon",
        ],
    ],
    "সারা সপ্তাহে বর্ষার সম্ভাবনা নেই সাথে উচ্চ তাপমান যা 85\u00b0F কাল এ বাড়ছে": [
        "sentence",
        [
            "with",
            ["for-week", "no-precipitation"],
            ["temperatures-peaking", ["fahrenheit", 85], "tomorrow"],
        ],
    ],
    "সপ্তাহান্তে বর্ষার মিশ্রিত সম্ভাবনা সাথে উচ্চ তাপমান যা 32\u00b0C বৃহস্পতিবারে অব্দি বাড়ছে": [
        "sentence",
        [
            "with",
            ["over-weekend", "mixed-precipitation"],
            ["temperatures-rising", ["celsius", 32], "thursday"],
        ],
    ],
    "বৃষ্টি সোমবারে এর সময়ে সাথে উচ্চ তাপমান যা 15\u00b0F শুক্রবারে তে কমে আসছে": [
        "sentence",
        [
            "with",
            ["during", "very-light-rain", "monday"],
            ["temperatures-valleying", ["fahrenheit", 15], "friday"],
        ],
    ],
    "হাল্কা তুষারাপাত মঙ্গলবারে এবং পরের বুধবারে এর সময়ে সাথে উচ্চ তাপমান যা 0\u00b0C রবিবারে অব্দি কমে যাচ্ছে": [
        "sentence",
        [
            "with",
            ["during", "light-snow", ["and", "tuesday", "next-wednesday"]],
            ["temperatures-falling", ["celsius", 0], "sunday"],
        ],
    ],
    "বর্ষা আজ এর মাধ্যমে শনিবারে এর সময়ে সাথে উচ্চ তাপমান যা 100\u00b0F সোমবারে এ বাড়ছে": [
        "sentence",
        [
            "with",
            ["during", "medium-precipitation", ["through", "today", "saturday"]],
            ["temperatures-peaking", ["fahrenheit", 100], "monday"],
        ],
    ],
    "সারাদিন বর্ষার মিশ্রিত সম্ভাবনা (1\u20133 ইঞ্চি)": [
        "sentence",
        [
            "for-day",
            ["parenthetical", "mixed-precipitation", ["inches", ["range", 1, 3]]],
        ],
    ],
    "ভারী তুষারাপাত (1\u20133 ইঞ্চি)": [
        "title",
        ["parenthetical", "heavy-snow", ["inches", ["range", 1, 3]]],
    ],
    "ভারী তুষারাপাত (3\u20135 সেন্টিমিটার)": [
        "title",
        ["parenthetical", "heavy-snow", ["centimeters", ["range", 3, 5]]],
    ],
    "সম্ভাবিত বজ্রঝড়": ["title", "possible-thunderstorm"],
    "ভারী বৃষ্টি এবং বজ্রঝড়": ["title", ["and", "heavy-rain", "thunderstorm"]],
    "বৃষ্টি 1 মিনিট এর থেকে কম এ শুরু হচ্ছে": [
        "sentence",
        ["starting-in", "very-light-rain", ["less-than", ["minutes", 1]]],
    ],
}
