# This would be one of your translations, as a Python dictionary
cases = {
    "晴朗": ["title", "clear"],
    "可能有少量降水": ["title", "possible-very-light-precipitation"],
    "少量降水": ["title", "very-light-precipitation"],
    "少量降水": ["title", "possible-light-precipitation"],
    "少量降水": ["title", "light-precipitation"],
    "中度降水": ["title", "medium-precipitation"],
    "大量降水": ["title", "heavy-precipitation"],
    "可能有毛毛雨": ["title", "possible-very-light-rain"],
    "毛毛雨": ["title", "very-light-rain"],
    "可能有小雨": ["title", "possible-light-rain"],
    "小雨": ["title", "light-rain"],
    "降雨": ["title", "medium-rain"],
    "傾盆大雨": ["title", "heavy-rain"],
    "可能有輕微雨夾雪": ["title", "possible-very-light-sleet"],
    "輕微的雨夾雪": ["title", "very-light-sleet"],
    "可能有輕微雨夾雪": ["title", "possible-light-sleet"],
    "輕微的雨夾雪": ["title", "light-sleet"],
    "雨夾雪": ["title", "medium-sleet"],
    "較強的雨夾雪": ["title", "heavy-sleet"],
    "可能有輕微降雪": ["title", "possible-very-light-snow"],
    "輕微降雪": ["title", "very-light-snow"],
    "可能有小雪": ["title", "possible-light-snow"],
    "小雪": ["title", "light-snow"],
    "降雪": ["title", "medium-snow"],
    "鵝毛大雪": ["title", "heavy-snow"],
    "有風": ["title", "medium-wind"],
    "推人大風": ["title", "heavy-wind"],
    "有霧": ["title", "fog"],
    "基本晴朗": ["title", "very-light-clouds"],
    "局部多雲": ["title", "light-clouds"],
    "多雲": ["title", "medium-clouds"],
    "多雲轉陰": ["title", "heavy-clouds"],
    "干燥，微風": ["title", ["and", "low-humidity", "light-wind"]],
    "毛毛雨，推人大風": ["title", ["and", "very-light-rain", "heavy-wind"]],
    "潮濕，局部多雲": ["title", ["and", "high-humidity", "light-clouds"]],
    "多雲，可能有雷暴": ["title", ["and", "medium-clouds", "possible-thunderstorm"]],
    "多雲，雷暴": ["title", ["and", "medium-clouds", "thunderstorm"]],
    "在接下來一個小時內晴朗。": ["sentence", ["for-hour", "clear"]],
    "輕微降雪將於35分鐘後開始。": [
        "sentence",
        ["starting-in", "very-light-snow", ["minutes", 35]],
    ],
    "小雨將於15分鐘後結束。": [
        "sentence",
        ["stopping-in", "light-rain", ["minutes", 15]],
    ],
    "較強的雨夾雪將於20分鐘後開始，並在之後的30分鐘結束。": [
        "sentence",
        [
            "starting-then-stopping-later",
            "heavy-sleet",
            ["minutes", 20],
            ["minutes", 30],
        ],
    ],
    "降雨將於25分鐘後結束，而在之後的8分鐘又將繼續。": [
        "sentence",
        [
            "stopping-then-starting-later",
            "medium-rain",
            ["minutes", 25],
            ["minutes", 8],
        ],
    ],
    "多雲將持續一整天。": ["sentence", ["for-day", "medium-clouds"]],
    "輕微的雨夾雪開始於早上。": [
        "sentence",
        ["starting", "very-light-sleet", "morning"],
    ],
    "有風將持續至明晚。": ["sentence", ["until", "medium-wind", "today-night"]],
    "大量降水將持續至下午。": [
        "sentence",
        ["until", "heavy-precipitation", "afternoon"],
    ],
    "雷暴將持續至下周一。": ["sentence", ["until", "thunderstorm", "next-monday"]],
    "微風持續至下午。": ["sentence", ["during", "light-wind", "afternoon"]],
    "降雪持續至今天夜裡，明天上午。": [
        "sentence",
        ["during", "medium-snow", ["and", "later-today-evening", "tomorrow-morning"]],
    ],
    "傾盆大雨直到今天上午晚些時候，將於今晚再次出現。": [
        "sentence",
        ["until-starting-again", "heavy-rain", "later-today-morning", "today-evening"],
    ],
    "多雲轉陰開始於晚上，將持續至當晚。": [
        "sentence",
        ["starting-continuing-until", "heavy-clouds", "evening", "night"],
    ],
    "輕微的雨夾雪持續至午後，有霧持續至明天上午。": [
        "sentence",
        [
            "and",
            ["during", "light-sleet", "later-today-afternoon"],
            ["during", "fog", "tomorrow-morning"],
        ],
    ],
    "推人大風開始於今天早上，將持續至今天下午，雨夾雪持續至明天上午。": [
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
    "多雲轉陰開始於今天夜裡。鵝毛大雪持續至明天下午。": [
        "sentence",
        [
            "and",
            ["starting", "heavy-clouds", "later-today-night"],
            ["during", "heavy-snow", "tomorrow-afternoon"],
        ],
    ],
    "干燥持續至明晚，少量降水開始於明晚，將持續至明晚。": [
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
    "降雪(5英寸)持續至當晚。": [
        "sentence",
        ["during", ["parenthetical", "medium-snow", ["inches", 5]], "night"],
    ],
    "小雪(2釐米)持續至今天上午晚些時候。": [
        "sentence",
        [
            "during",
            ["parenthetical", "light-snow", ["centimeters", 2]],
            "later-today-morning",
        ],
    ],
    "鵝毛大雪(8–12英寸)將持續一整天。": [
        "sentence",
        ["for-day", ["parenthetical", "heavy-snow", ["inches", ["range", 8, 12]]]],
    ],
    "降雪(低於1釐米)持續至下午。": [
        "sentence",
        [
            "during",
            ["parenthetical", "medium-snow", ["less-than", ["centimeters", 1]]],
            "afternoon",
        ],
    ],
    "無降水持續一整周，且明天溫度劇增到85°F。": [
        "sentence",
        [
            "with",
            ["for-week", "no-precipitation"],
            ["temperatures-peaking", ["fahrenheit", 85], "tomorrow"],
        ],
    ],
    "多雲轉雨持續一整周，且周四升溫到32°C。": [
        "sentence",
        [
            "with",
            ["over-weekend", "mixed-precipitation"],
            ["temperatures-rising", ["celsius", 32], "thursday"],
        ],
    ],
    "毛毛雨持續至周一，且周五溫度驟降到15°F。": [
        "sentence",
        [
            "with",
            ["during", "very-light-rain", "monday"],
            ["temperatures-valleying", ["fahrenheit", 15], "friday"],
        ],
    ],
    "小雪持續至周二，周三，且周日溫度下降到0°C。": [
        "sentence",
        [
            "with",
            ["during", "light-snow", ["and", "tuesday", "wednesday"]],
            ["temperatures-falling", ["celsius", 0], "sunday"],
        ],
    ],
    "中度降水持續至今天直至周六，且周一溫度劇增到100°F。": [
        "sentence",
        [
            "with",
            ["during", "medium-precipitation", ["through", "today", "saturday"]],
            ["temperatures-peaking", ["fahrenheit", 100], "monday"],
        ],
    ],
    "多雲轉雨(1–3英寸)將持續一整天。": [
        "sentence",
        [
            "for-day",
            ["parenthetical", "mixed-precipitation", ["inches", ["range", 1, 3]]],
        ],
    ],
    "鵝毛大雪(1–3英寸)": [
        "title",
        ["parenthetical", "heavy-snow", ["inches", ["range", 1, 3]]],
    ],
    "鵝毛大雪(3–5釐米)": [
        "title",
        ["parenthetical", "heavy-snow", ["centimeters", ["range", 3, 5]]],
    ],
}
