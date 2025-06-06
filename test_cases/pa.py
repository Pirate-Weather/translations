# This would be one of your translations, as a Python dictionary
cases = {
    "ਸਾਫ਼": ["title", "clear"],
    "ਸੰਭਾਵਿਤ ਹਲਕਾ ਮੀਂਹ": ["title", "possible-very-light-precipitation"],
    "ਹਲਕਾ ਮੀਂਹ": ["title", "very-light-precipitation"],
    "ਸੰਭਾਵਿਤ ਹਲਕਾ ਮੀਂਹ": ["title", "possible-light-precipitation"],
    "ਹਲਕਾ ਮੀਂਹ": ["title", "light-precipitation"],
    "ਮੀਂਹ": ["title", "medium-precipitation"],
    "ਭਾਰੀ ਮੀਂਹ": ["title", "heavy-precipitation"],
    "ਸੰਭਾਵੀ ਕਿਣ-ਮਿਣ": ["title", "possible-very-light-rain"],
    "ਕਿਣ-ਮਿਣ": ["title", "very-light-rain"],
    "ਸੰਭਾਵੀ ਹਲਕਾ ਮੀਂਹ": ["title", "possible-light-rain"],
    "ਹਲਕਾ ਮੀਂਹ": ["title", "light-rain"],
    "ਮੀਂਹ": ["title", "medium-rain"],
    "ਭਾਰੀ ਮੀਂਹ": ["title", "heavy-rain"],
    "ਸੰਭਾਵੀ ਔਲੇਯਾਂ ਨਾਲ ਮੀਂਹ": ["title", "possible-very-light-sleet"],
    "ਹਲਕੇ ਔਲੇਯਾਂ ਨਾਲ ਮੀਂਹ": ["title", "very-light-sleet"],
    "ਸੰਭਾਵੀ ਔਲੇਯਾਂ ਨਾਲ ਮੀਂਹ": ["title", "possible-light-sleet"],
    "ਹਲਕੇ ਔਲੇਯਾਂ ਨਾਲ ਮੀਂਹ": ["title", "light-sleet"],
    "ਔਲੇਯਾਂ ਨਾਲ ਮੀਂਹ": ["title", "medium-sleet"],
    "ਭਾਰੀ ਔਲੇਯਾਂ ਨਾਲ ਮੀਂਹ": ["title", "heavy-sleet"],
    "ਸਭਾਵੀ ਬਰਫਬਾਰੀ": ["title", "possible-very-light-snow"],
    "ਬਰਫਬਾਰੀ": ["title", "very-light-snow"],
    "ਸੰਭਾਵੀ ਹਲਕੀ ਬਰਫ਼": ["title", "possible-light-snow"],
    "ਹਲਕੀ ਬਰਫ਼": ["title", "light-snow"],
    "ਬਰਫ਼": ["title", "medium-snow"],
    "ਭਾਰੀ ਬਰਫ": ["title", "heavy-snow"],
    "ਤੇਜ ਹਵਾ": ["title", "medium-wind"],
    "ਖਤਰਨਾਕ ਤੇਜ ਹਵਾ": ["title", "heavy-wind"],
    "ਧੁੰਧ": ["title", "fog"],
    "ਜਿਆਦਾਤਰ ਸਾਫ": ["title", "very-light-clouds"],
    "ਕੁਝ ਹੱਦ ਤਕ ਬੱਦਲ ਹੋਣਾ": ["title", "light-clouds"],
    "ਜ੍ਯਾਦਾ ਬੱਦਲ ਹੋਣਾ": ["title", "medium-clouds"],
    "ਘਣੇ ਬੱਦਲ": ["title", "heavy-clouds"],
    "ਸੁਖਾ ਹੋਰ ਤੁਫਾਨੀ": ["title", ["and", "low-humidity", "light-wind"]],
    "ਕਿਣ-ਮਿਣ ਹੋਰ ਖਤਰਨਾਕ ਤੇਜ ਹਵਾ": ["title", ["and", "very-light-rain", "heavy-wind"]],
    "ਨਮੀ ਹੋਰ ਕੁਝ ਹੱਦ ਤਕ ਬੱਦਲ ਹੋਣਾ": ["title", ["and", "high-humidity", "light-clouds"]],
    "ਘੰਟੇ ਲਈ ਸਾਫ਼": ["sentence", ["for-hour", "clear"]],
    "ਬਰਫਬਾਰੀ ਘਟ ਤੋਂ ਘਟ 35 ਵਿਚ ਸ਼ੁਰੂ ਹੋ ਰਿਹਾ ਹੈ": [
        "sentence",
        ["starting-in", "very-light-snow", ["minutes", 35]],
    ],
    "ਹਲਕਾ ਮੀਂਹ ਘਟ ਤੋਂ ਘਟ 15 ਵਿੱਚ ਰੁਕ ਰਿਹਾ ਹੈ": [
        "sentence",
        ["stopping-in", "light-rain", ["minutes", 15]],
    ],
    "ਭਾਰੀ ਔਲੇਯਾਂ ਨਾਲ ਮੀਂਹ ਘਟ ਤੋਂ ਘਟ 20 ਵਿਚ ਸ਼ੁਰੂ ਹੋ ਰਿਹਾ ਹੈ, ਬਾਅਦ ਵਿਚ ਘਟ ਤੋਂ ਘਟ 30 ਵਿਚ ਬੰਦ ਹੋ ਰਿਹਾ ਹੈ": [
        "sentence",
        [
            "starting-then-stopping-later",
            "heavy-sleet",
            ["minutes", 20],
            ["minutes", 30],
        ],
    ],
    "ਮੀਂਹ ਘਟ ਤੋਂ ਘਟ 25 ਵਿੱਚ ਰੁਕ ਰਿਹਾ ਹੈ, ਘਟ ਤੋਂ ਘਟ 8 ਤੋਂ ਬਾਦ ਸ਼ੁਰੂ ਹੋਏਗਾ": [
        "sentence",
        [
            "stopping-then-starting-later",
            "medium-rain",
            ["minutes", 25],
            ["minutes", 8],
        ],
    ],
    "ਜ੍ਯਾਦਾ ਬੱਦਲ ਹੋਣਾ ਪੂਰਾ ਦਿਨ": ["sentence", ["for-day", "medium-clouds"]],
    "ਹਲਕੇ ਔਲੇਯਾਂ ਨਾਲ ਮੀਂਹ ਸਵੇਰ ਤੋਂ ਸ਼ੁਰੂ": [
        "sentence",
        ["starting", "very-light-sleet", "morning"],
    ],
    "ਤੇਜ ਹਵਾ ਅੱਜ ਰਾਤ ਤਕ": ["sentence", ["until", "medium-wind", "today-night"]],
    "ਭਾਰੀ ਮੀਂਹ ਦੋਪਹਰ ਤਕ": ["sentence", ["until", "heavy-precipitation", "afternoon"]],
    "ਤੁਫਾਨੀ ਦੋਪਹਰ ਦੇ ਦੌਰਾਨ": ["sentence", ["during", "light-wind", "afternoon"]],
    "ਬਰਫ਼ ਅੱਜ ਸ਼ਾਮ ਤੋ ਬਾਅਦ ਹੋਰ ਕਲ ਸਵੇਰੇ ਦੇ ਦੌਰਾਨ": [
        "sentence",
        ["during", "medium-snow", ["and", "later-today-evening", "tomorrow-morning"]],
    ],
    "ਭਾਰੀ ਮੀਂਹ ਅੱਜ ਸਵੇਰੇ ਤੋਂ ਬਾਅਦ ਤਕ, ਅੱਜ ਸ਼ਾਮ ਫੇਰ ਸ਼ੁਰੂ ਹੋ ਰਿਹਾ ਹੈ": [
        "sentence",
        ["until-starting-again", "heavy-rain", "later-today-morning", "today-evening"],
    ],
    "ਘਣੇ ਬੱਦਲ ਸ਼ਾਮ ਤਕ, ਰਾਤ ਭਰ ਤਕ ਚਲ ਰਿਹਾ ਹੈ": [
        "sentence",
        ["starting-continuing-until", "heavy-clouds", "evening", "night"],
    ],
    "ਹਲਕੇ ਔਲੇਯਾਂ ਨਾਲ ਮੀਂਹ ਅੱਜ ਦੋਪਹਰ ਤੋਂ ਬਾਅਦ ਦੇ ਦੌਰਾਨ ਹੋਰ ਧੁੰਧ ਕਲ ਸਵੇਰੇ ਦੇ ਦੌਰਾਨ": [
        "sentence",
        [
            "and",
            ["during", "light-sleet", "later-today-afternoon"],
            ["during", "fog", "tomorrow-morning"],
        ],
    ],
    "ਖਤਰਨਾਕ ਤੇਜ ਹਵਾ ਅੱਜ ਸਵੇਰੇ ਤਕ, ਅੱਜ ਦੋਪਹਰ ਤਕ ਚਲ ਰਿਹਾ ਹੈ ਹੋਰ ਔਲੇਯਾਂ ਨਾਲ ਮੀਂਹ ਕਲ ਸਵੇਰੇ ਦੇ ਦੌਰਾਨ": [
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
    "ਘਣੇ ਬੱਦਲ ਅੱਜ ਰਾਤ ਤੋਂ ਬਾਅਦ ਤੋਂ ਸ਼ੁਰੂ ਹੋਰ ਭਾਰੀ ਬਰਫ ਕਲ ਦੋਪਹਰ ਦੇ ਦੌਰਾਨ": [
        "sentence",
        [
            "and",
            ["starting", "heavy-clouds", "later-today-night"],
            ["during", "heavy-snow", "tomorrow-afternoon"],
        ],
    ],
    "ਸੁਖਾ ਅੱਜ ਰਾਤ ਦੇ ਦੌਰਾਨ ਹੋਰ ਹਲਕਾ ਮੀਂਹ ਕਲ ਸ਼ਾਮ ਤਕ, ਕਲ ਰਾਤ ਤਕ ਚਲ ਰਿਹਾ ਹੈ": [
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
    "ਬਰਫ਼ (5 ਇੰਚ) ਰਾਤ ਭਰ ਦੇ ਦੌਰਾਨ": [
        "sentence",
        ["during", ["parenthetical", "medium-snow", ["inches", 5]], "night"],
    ],
    "ਹਲਕੀ ਬਰਫ਼ (2 ਸੇੰਟੀਮੀਟਰ) ਅੱਜ ਸਵੇਰੇ ਤੋਂ ਬਾਅਦ ਦੇ ਦੌਰਾਨ": [
        "sentence",
        [
            "during",
            ["parenthetical", "light-snow", ["centimeters", 2]],
            "later-today-morning",
        ],
    ],
    "ਭਾਰੀ ਬਰਫ (8\u201312 ਇੰਚ) ਪੂਰਾ ਦਿਨ": [
        "sentence",
        ["for-day", ["parenthetical", "heavy-snow", ["inches", ["range", 8, 12]]]],
    ],
    "ਬਰਫ਼ (1 ਸੇੰਟੀਮੀਟਰ ਤੋਂ ਘੱਟ) ਦੋਪਹਰ ਦੇ ਦੌਰਾਨ": [
        "sentence",
        [
            "during",
            ["parenthetical", "medium-snow", ["less-than", ["centimeters", 1]]],
            "afternoon",
        ],
    ],
    "ਮੀਂਹ ਨਹੀਂ ਹੈ ਪੂਰੇ ਹਫਤੇ ਵਿੱਚ ਨਾਲ ਉੱਚ ਤਾਪਮਾਨ 85\u00b0F ਕਲ ਤੇ ਪਹੁੰਚਦੇ ਹਨ": [
        "sentence",
        [
            "with",
            ["for-week", "no-precipitation"],
            ["temperatures-peaking", ["fahrenheit", 85], "tomorrow"],
        ],
    ],
    "ਮਿਕਸ-ਮੀਂਹ ਸ਼ਨੀਵਾਰ ਵਿਚ ਨਾਲ ਉੱਚ ਤਾਪਮਾਨ 32\u00b0C ਵੀਰਵਾਰ ਨੂੰ ਤਕ ਵਧਦੇ ਹਨ": [
        "sentence",
        [
            "with",
            ["over-weekend", "mixed-precipitation"],
            ["temperatures-rising", ["celsius", 32], "thursday"],
        ],
    ],
    "ਕਿਣ-ਮਿਣ ਸੋਮਵਾਰ ਨੂੰ ਦੇ ਦੌਰਾਨ ਨਾਲ ਉੱਚ ਤਾਪਮਾਨ 15\u00b0F ਸ਼ੁਕਰਵਾਰ ਨੂੰ ਤੋਂ ਥੱਲੇ ਆਰਿਹਾ ਹੈ": [
        "sentence",
        [
            "with",
            ["during", "very-light-rain", "monday"],
            ["temperatures-valleying", ["fahrenheit", 15], "friday"],
        ],
    ],
    "ਹਲਕੀ ਬਰਫ਼ ਮੰਗਲਵਾਰ ਨੂੰ ਹੋਰ ਅਗਲੇ ਬੁਧਵਾਰ ਦੇ ਦੌਰਾਨ ਨਾਲ ਉੱਚ ਤਾਪਮਾਨ 0\u00b0C ਇਤਵਾਰ ਨੂੰ ਤੇ ਆਰਿਹਾ ਹੈ": [
        "sentence",
        [
            "with",
            ["during", "light-snow", ["and", "tuesday", "next-wednesday"]],
            ["temperatures-falling", ["celsius", 0], "sunday"],
        ],
    ],
    "ਮੀਂਹ ਆਜ ਦੇ ਜ਼ਰੀਏ ਸ਼ਨੀਵਾਰ ਨੂੰ ਦੇ ਦੌਰਾਨ ਨਾਲ ਉੱਚ ਤਾਪਮਾਨ 100\u00b0F ਸੋਮਵਾਰ ਨੂੰ ਤੇ ਪਹੁੰਚਦੇ ਹਨ": [
        "sentence",
        [
            "with",
            ["during", "medium-precipitation", ["through", "today", "saturday"]],
            ["temperatures-peaking", ["fahrenheit", 100], "monday"],
        ],
    ],
    "ਮਿਕਸ-ਮੀਂਹ (1\u20133 ਇੰਚ) ਪੂਰਾ ਦਿਨ": [
        "sentence",
        [
            "for-day",
            ["parenthetical", "mixed-precipitation", ["inches", ["range", 1, 3]]],
        ],
    ],
    "ਭਾਰੀ ਬਰਫ (1\u20133 ਇੰਚ)": [
        "title",
        ["parenthetical", "heavy-snow", ["inches", ["range", 1, 3]]],
    ],
    "ਭਾਰੀ ਬਰਫ (3\u20135 ਸੇੰਟੀਮੀਟਰ)": [
        "title",
        ["parenthetical", "heavy-snow", ["centimeters", ["range", 3, 5]]],
    ],
    "ਸੰਭਾਵਿਤ ਤੂਫ਼ਾਨ": ["title", "possible-thunderstorm"],
    "ਭਾਰੀ ਮੀਂਹ ਹੋਰ ਤੂਫ਼ਾਨ": ["title", ["and", "heavy-rain", "thunderstorm"]],
    "ਕਿਣ-ਮਿਣ ਘਟ ਤੋਂ ਘਟ 1 ਤੋਂ ਘੱਟ ਵਿਚ ਸ਼ੁਰੂ ਹੋ ਰਿਹਾ ਹੈ": [
        "sentence",
        ["starting-in", "very-light-rain", ["less-than", ["minutes", 1]]],
    ],
}
