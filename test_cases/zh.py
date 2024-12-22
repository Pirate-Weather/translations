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
    "倾盆大雨": ["title", "heavy-rain"],
    "可能有轻微雨夹雪": ["title", "possible-very-light-sleet"],
    "轻微的雨夹雪": ["title", "very-light-sleet"],
    "可能有轻微雨夹雪": ["title", "possible-light-sleet"],
    "轻微的雨夹雪": ["title", "light-sleet"],
    "雨夹雪": ["title", "medium-sleet"],
    "较强的雨夹雪": ["title", "heavy-sleet"],
    "可能有轻微降雪": ["title", "possible-very-light-snow"],
    "轻微降雪": ["title", "very-light-snow"],
    "可能有小雪": ["title", "possible-light-snow"],
    "小雪": ["title", "light-snow"],
    "降雪": ["title", "medium-snow"],
    "鹅毛大雪": ["title", "heavy-snow"],
    "有风": ["title", "medium-wind"],
    "推人大风": ["title", "heavy-wind"],
    "有雾": ["title", "fog"],
    "大部分時間晴朗": ["title", "very-light-clouds"],
    "局部多云": ["title", "light-clouds"],
    "多云": ["title", "medium-clouds"],
    "多云转阴": ["title", "heavy-clouds"],
    "干燥，微风": ["title", ["and", "low-humidity", "light-wind"]],
    "毛毛雨，推人大风": ["title", ["and", "very-light-rain", "heavy-wind"]],
    "潮湿，局部多云": ["title", ["and", "high-humidity", "light-clouds"]],
    "多云，可能有雷暴": ["title", ["and", "medium-clouds", "possible-thunderstorm"]],
    "多云，雷暴": ["title", ["and", "medium-clouds", "thunderstorm"]],
    "在接下来一个小时内晴朗。": ["sentence", ["for-hour", "clear"]],
    "轻微降雪将于35分钟后开始。": [
        "sentence",
        ["starting-in", "very-light-snow", ["minutes", 35]],
    ],
    "小雨将于15分钟后结束。": [
        "sentence",
        ["stopping-in", "light-rain", ["minutes", 15]],
    ],
    "较强的雨夹雪将于20分钟后开始，并在之后的30分钟结束。": [
        "sentence",
        [
            "starting-then-stopping-later",
            "heavy-sleet",
            ["minutes", 20],
            ["minutes", 30],
        ],
    ],
    "降雨将于25分钟后结束，而在之后的8分钟又将继续。": [
        "sentence",
        [
            "stopping-then-starting-later",
            "medium-rain",
            ["minutes", 25],
            ["minutes", 8],
        ],
    ],
    "多云将持续一整天。": ["sentence", ["for-day", "medium-clouds"]],
    "轻微的雨夹雪开始于早上。": [
        "sentence",
        ["starting", "very-light-sleet", "morning"],
    ],
    "有风将持续至明晚。": ["sentence", ["until", "medium-wind", "today-night"]],
    "大量降水将持续至下午。": [
        "sentence",
        ["until", "heavy-precipitation", "afternoon"],
    ],
    "雷暴将持续至下周一。": ["sentence", ["until", "thunderstorm", "next-monday"]],
    "微风持续至下午。": ["sentence", ["during", "light-wind", "afternoon"]],
    "降雪持续至今天夜里，明天上午。": [
        "sentence",
        ["during", "medium-snow", ["and", "later-today-evening", "tomorrow-morning"]],
    ],
    "倾盆大雨直到今天上午晚些时候，将于今晚再次出现。": [
        "sentence",
        ["until-starting-again", "heavy-rain", "later-today-morning", "today-evening"],
    ],
    "多云转阴开始于晚上，将持续至当晚。": [
        "sentence",
        ["starting-continuing-until", "heavy-clouds", "evening", "night"],
    ],
    "轻微的雨夹雪持续至午后，有雾持续至明天上午。": [
        "sentence",
        [
            "and",
            ["during", "light-sleet", "later-today-afternoon"],
            ["during", "fog", "tomorrow-morning"],
        ],
    ],
    "推人大风开始于今天早上，将持续至今天下午，雨夹雪持续至明天上午。": [
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
    "多云转阴开始于今天夜里。鹅毛大雪持续至明天下午。": [
        "sentence",
        [
            "and",
            ["starting", "heavy-clouds", "later-today-night"],
            ["during", "heavy-snow", "tomorrow-afternoon"],
        ],
    ],
    "干燥持续至明晚，少量降水开始于明晚，将持续至明晚。": [
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
    "降雪(5英寸)持续至当晚。": [
        "sentence",
        ["during", ["parenthetical", "medium-snow", ["inches", 5]], "night"],
    ],
    "小雪(2厘米)持续至今天上午晚些时候。": [
        "sentence",
        [
            "during",
            ["parenthetical", "light-snow", ["centimeters", 2]],
            "later-today-morning",
        ],
    ],
    "鹅毛大雪(8–12英寸)将持续一整天。": [
        "sentence",
        ["for-day", ["parenthetical", "heavy-snow", ["inches", ["range", 8, 12]]]],
    ],
    "降雪(低于1厘米)持续至下午。": [
        "sentence",
        [
            "during",
            ["parenthetical", "medium-snow", ["less-than", ["centimeters", 1]]],
            "afternoon",
        ],
    ],
    "无降水持续一整周，且明天温度剧增到85°F。": [
        "sentence",
        [
            "with",
            ["for-week", "no-precipitation"],
            ["temperatures-peaking", ["fahrenheit", 85], "tomorrow"],
        ],
    ],
    "多云转雨持续一整周，且周四升温到32°C。": [
        "sentence",
        [
            "with",
            ["over-weekend", "mixed-precipitation"],
            ["temperatures-rising", ["celsius", 32], "thursday"],
        ],
    ],
    "毛毛雨持续至周一，且周五温度骤降到15°F。": [
        "sentence",
        [
            "with",
            ["during", "very-light-rain", "monday"],
            ["temperatures-valleying", ["fahrenheit", 15], "friday"],
        ],
    ],
    "小雪持续至周二，周三，且周日温度下降到0°C。": [
        "sentence",
        [
            "with",
            ["during", "light-snow", ["and", "tuesday", "wednesday"]],
            ["temperatures-falling", ["celsius", 0], "sunday"],
        ],
    ],
    "中度降水持续至今天直至周六，且周一温度剧增到100°F。": [
        "sentence",
        [
            "with",
            ["during", "medium-precipitation", ["through", "today", "saturday"]],
            ["temperatures-peaking", ["fahrenheit", 100], "monday"],
        ],
    ],
    "多云转雨(1–3英寸)将持续一整天。": [
        "sentence",
        [
            "for-day",
            ["parenthetical", "mixed-precipitation", ["inches", ["range", 1, 3]]],
        ],
    ],
    "鹅毛大雪(1–3英寸)": [
        "title",
        ["parenthetical", "heavy-snow", ["inches", ["range", 1, 3]]],
    ],
    "鹅毛大雪(3–5厘米)": [
        "title",
        ["parenthetical", "heavy-snow", ["centimeters", ["range", 3, 5]]],
    ],
}
