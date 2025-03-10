# This would be one of your translations, as a Python dictionary
cases = {
    "晴れ": ["title", "clear"],
    "弱い降水の可能性あり": ["title", "possible-very-light-precipitation"],
    "弱い降水": ["title", "very-light-precipitation"],
    "弱い降水の可能性あり": ["title", "possible-light-precipitation"],
    "弱い降水": ["title", "light-precipitation"],
    "降水": ["title", "medium-precipitation"],
    "強い降水": ["title", "heavy-precipitation"],
    "霧雨の可能性あり": ["title", "possible-very-light-rain"],
    "霧雨": ["title", "very-light-rain"],
    "小雨の可能性あり": ["title", "possible-light-rain"],
    "小雨": ["title", "light-rain"],
    "雨": ["title", "medium-rain"],
    "大雨": ["title", "heavy-rain"],
    "弱いみぞれの可能性あり": ["title", "possible-very-light-sleet"],
    "弱いみぞれ": ["title", "very-light-sleet"],
    "弱いみぞれの可能性あり": ["title", "possible-light-sleet"],
    "弱いみぞれ": ["title", "light-sleet"],
    "みぞれ": ["title", "medium-sleet"],
    "強いみぞれ": ["title", "heavy-sleet"],
    "にわか雪の可能性あり": ["title", "possible-very-light-snow"],
    "にわか雪": ["title", "very-light-snow"],
    "小雪の可能性あり": ["title", "possible-light-snow"],
    "小雪": ["title", "light-snow"],
    "雪": ["title", "medium-snow"],
    "大雪": ["title", "heavy-snow"],
    "強い風": ["title", "medium-wind"],
    "猛烈な風": ["title", "heavy-wind"],
    "霧": ["title", "fog"],
    "ほぼ晴れ": ["title", "very-light-clouds"],
    "薄曇り": ["title", "light-clouds"],
    "曇り": ["title", "medium-clouds"],
    "曇り": ["title", "heavy-clouds"],
    "乾燥及び弱い風": ["title", ["and", "low-humidity", "light-wind"]],
    "霧雨及び猛烈な風": ["title", ["and", "very-light-rain", "heavy-wind"]],
    "多湿及び薄曇り": ["title", ["and", "high-humidity", "light-clouds"]],
    "一時間晴れ。": ["sentence", ["for-hour", "clear"]],
    "にわか雪が35分に始まる。": [
        "sentence",
        ["starting-in", "very-light-snow", ["minutes", 35]],
    ],
    "小雨が15分に終わる。": [
        "sentence",
        ["stopping-in", "light-rain", ["minutes", 15]],
    ],
    "強いみぞれが20分に始まり、30分後終わる。": [
        "sentence",
        [
            "starting-then-stopping-later",
            "heavy-sleet",
            ["minutes", 20],
            ["minutes", 30],
        ],
    ],
    "雨が25分に終わり、また8分後始まる。": [
        "sentence",
        [
            "stopping-then-starting-later",
            "medium-rain",
            ["minutes", 25],
            ["minutes", 8],
        ],
    ],
    "一日中曇り。": ["sentence", ["for-day", "medium-clouds"]],
    "朝から弱いみぞれが始まる。": [
        "sentence",
        ["starting", "very-light-sleet", "morning"],
    ],
    "今夜まで強い風。": ["sentence", ["until", "medium-wind", "today-night"]],
    "昼過ぎまで強い降水。": ["sentence", ["until", "heavy-precipitation", "afternoon"]],
    "昼過ぎにかけて弱い風。": ["sentence", ["during", "light-wind", "afternoon"]],
    "今日の夜遅く及び明日の朝にかけて雪。": [
        "sentence",
        ["during", "medium-snow", ["and", "later-today-evening", "tomorrow-morning"]],
    ],
    "今日の午前中まで大雨、今日の夜の初め頃からまた始まる。": [
        "sentence",
        ["until-starting-again", "heavy-rain", "later-today-morning", "today-evening"],
    ],
    "曇りが夕方から始まり夜まで続く。": [
        "sentence",
        ["starting-continuing-until", "heavy-clouds", "evening", "night"],
    ],
    "今日の夕方にかけて弱いみぞれ。及び明日の朝にかけて霧。": [
        "sentence",
        [
            "and",
            ["during", "light-sleet", "later-today-afternoon"],
            ["during", "fog", "tomorrow-morning"],
        ],
    ],
    "猛烈な風が今朝から始まり今日の昼過ぎまで続く。及び明日の朝にかけてみぞれ。": [
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
    "今夜遅くから曇りが始まる。及び明日の昼過ぎにかけて大雪。": [
        "sentence",
        [
            "and",
            ["starting", "heavy-clouds", "later-today-night"],
            ["during", "heavy-snow", "tomorrow-afternoon"],
        ],
    ],
    "今夜にかけて乾燥。及び弱い降水が明日の夕方から始まり明日の夜まで続く。": [
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
    "夜にかけて雪 (5インチ)。": [
        "sentence",
        ["during", ["parenthetical", "medium-snow", ["inches", 5]], "night"],
    ],
    "今日の午前中にかけて小雪 (2センチメートル)。": [
        "sentence",
        [
            "during",
            ["parenthetical", "light-snow", ["centimeters", 2]],
            "later-today-morning",
        ],
    ],
    "一日中大雪 (8–12インチ)。": [
        "sentence",
        ["for-day", ["parenthetical", "heavy-snow", ["inches", ["range", 8, 12]]]],
    ],
    "昼過ぎにかけて雪 (1センチメートル未満)。": [
        "sentence",
        [
            "during",
            ["parenthetical", "medium-snow", ["less-than", ["centimeters", 1]]],
            "afternoon",
        ],
    ],
    "一週間中降水なし。明日は最高気温85°F。": [
        "sentence",
        [
            "with",
            ["for-week", "no-precipitation"],
            ["temperatures-peaking", ["fahrenheit", 85], "tomorrow"],
        ],
    ],
    "土、日曜日にみぞれ。気温は32°C、木曜日に上がる。": [
        "sentence",
        [
            "with",
            ["over-weekend", "mixed-precipitation"],
            ["temperatures-rising", ["celsius", 32], "thursday"],
        ],
    ],
    "月曜日にかけて霧雨。金曜日は最低気温15°F。": [
        "sentence",
        [
            "with",
            ["during", "very-light-rain", "monday"],
            ["temperatures-valleying", ["fahrenheit", 15], "friday"],
        ],
    ],
    "火曜日及び次の水曜日にかけて小雪。気温は0°C、日曜日に下がる。": [
        "sentence",
        [
            "with",
            ["during", "light-snow", ["and", "tuesday", "next-wednesday"]],
            ["temperatures-falling", ["celsius", 0], "sunday"],
        ],
    ],
    "今日から土曜日にかけて降水。月曜日は最高気温100°F。": [
        "sentence",
        [
            "with",
            ["during", "medium-precipitation", ["through", "today", "saturday"]],
            ["temperatures-peaking", ["fahrenheit", 100], "monday"],
        ],
    ],
    "一日中みぞれ (1–3インチ)。": [
        "sentence",
        [
            "for-day",
            ["parenthetical", "mixed-precipitation", ["inches", ["range", 1, 3]]],
        ],
    ],
    "大雪 (1–3インチ)": [
        "title",
        ["parenthetical", "heavy-snow", ["inches", ["range", 1, 3]]],
    ],
    "大雪 (3–5センチメートル)": [
        "title",
        ["parenthetical", "heavy-snow", ["centimeters", ["range", 3, 5]]],
    ],
    "激しい雷雨の可能性あり": ["title", "possible-thunderstorm"],
    "大雨及び雷雨": ["title", ["and", "heavy-rain", "thunderstorm"]],
    "霧雨が1分未満に始まる。": [
        "sentence",
        ["starting-in", "very-light-rain", ["less-than", ["minutes", 1]]],
    ],
}
