# This would be one of your translations, as a Python dictionary
cases = {
    "맑음": ["title", "clear"],
    "아주 약한 강수 가능성": ["title", "possible-very-light-precipitation"],
    "아주 약한 강수": ["title", "very-light-precipitation"],
    "약한 강수 가능성": ["title", "possible-light-precipitation"],
    "약한 강수": ["title", "light-precipitation"],
    "강수": ["title", "medium-precipitation"],
    "강한 강수": ["title", "heavy-precipitation"],
    "이슬비 가능성": ["title", "possible-very-light-rain"],
    "이슬비": ["title", "very-light-rain"],
    "가랑비 가능성": ["title", "possible-light-rain"],
    "약한 비": ["title", "light-rain"],
    "비": ["title", "medium-rain"],
    "강한 비": ["title", "heavy-rain"],
    "약한 진눈깨비 가능성": ["title", "possible-very-light-sleet"],
    "약한 진눈깨비": ["title", "very-light-sleet"],
    "약한 진눈깨비 가능성": ["title", "possible-light-sleet"],
    "약한 진눈깨비": ["title", "light-sleet"],
    "진눈깨비": ["title", "medium-sleet"],
    "강한 진눈깨비": ["title", "heavy-sleet"],
    "흩뿌리는 눈 가능성": ["title", "possible-very-light-snow"],
    "아주 약한 눈": ["title", "very-light-snow"],
    "약한 눈 가능성": ["title", "possible-light-snow"],
    "약한 눈": ["title", "light-snow"],
    "눈": ["title", "medium-snow"],
    "강한 눈": ["title", "heavy-snow"],
    "바람": ["title", "medium-wind"],
    "강한 바람": ["title", "heavy-wind"],
    "안개": ["title", "fog"],
    "대체로 맑음": ["title", "very-light-clouds"],
    "약간 흐림": ["title", "light-clouds"],
    "흐림": ["title", "medium-clouds"],
    "흐림": ["title", "heavy-clouds"],
    "건조, 약한 바람": ["title", ["and", "low-humidity", "light-wind"]],
    "이슬비, 강한 바람": ["title", ["and", "very-light-rain", "heavy-wind"]],
    "습함, 약간 흐림": ["title", ["and", "high-humidity", "light-clouds"]],
    "한 시간 맑음": ["sentence", ["for-hour", "clear"]],
    "35분 후 아주 약한 눈 시작": [
        "sentence",
        ["starting-in", "very-light-snow", ["minutes", 35]],
    ],
    "15분 후 약한 비 멈춤": [
        "sentence",
        ["stopping-in", "light-rain", ["minutes", 15]],
    ],
    "20분 후 강한 진눈깨비 시작, 30분 후 멈춤": [
        "sentence",
        [
            "starting-then-stopping-later",
            "heavy-sleet",
            ["minutes", 20],
            ["minutes", 30],
        ],
    ],
    "25분 후 비 멈춤, 8분 후 다시 시작": [
        "sentence",
        [
            "stopping-then-starting-later",
            "medium-rain",
            ["minutes", 25],
            ["minutes", 8],
        ],
    ],
    "온종일 흐림": ["sentence", ["for-day", "medium-clouds"]],
    "아침에 아주 약한 진눈깨비 시작": [
        "sentence",
        ["starting", "very-light-sleet", "morning"],
    ],
    "오늘 밤까지 바람": ["sentence", ["until", "medium-wind", "today-night"]],
    "오후까지 강한 강수": ["sentence", ["until", "heavy-precipitation", "afternoon"]],
    "오후동안 약한 바람": ["sentence", ["during", "light-wind", "afternoon"]],
    "오늘 저녁, 내일 아침동안 눈": [
        "sentence",
        ["during", "medium-snow", ["and", "later-today-evening", "tomorrow-morning"]],
    ],
    "오늘 오전까지 강한 비, 오늘 저녁 다시 시작": [
        "sentence",
        ["until-starting-again", "heavy-rain", "later-today-morning", "today-evening"],
    ],
    "저녁 흐림 시작, 밤까지 이어짐": [
        "sentence",
        ["starting-continuing-until", "heavy-clouds", "evening", "night"],
    ],
    "오늘 오후동안 약한 진눈깨비, 내일 아침동안 안개": [
        "sentence",
        [
            "and",
            ["during", "light-sleet", "later-today-afternoon"],
            ["during", "fog", "tomorrow-morning"],
        ],
    ],
    "오늘 아침 강한 바람 시작, 오늘 오후까지 이어짐, 내일 아침동안 진눈깨비": [
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
    "오늘 밤에 흐림 시작, 내일 오후동안 강한 눈": [
        "sentence",
        [
            "and",
            ["starting", "heavy-clouds", "later-today-night"],
            ["during", "heavy-snow", "tomorrow-afternoon"],
        ],
    ],
    "오늘 밤동안 건조, 내일 저녁 약한 강수 시작, 내일 밤까지 이어짐": [
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
    "밤동안 눈(5인치)": [
        "sentence",
        ["during", ["parenthetical", "medium-snow", ["inches", 5]], "night"],
    ],
    "오늘 오전동안 약한 눈(2cm)": [
        "sentence",
        [
            "during",
            ["parenthetical", "light-snow", ["centimeters", 2]],
            "later-today-morning",
        ],
    ],
    "온종일 강한 눈(8–12인치)": [
        "sentence",
        ["for-day", ["parenthetical", "heavy-snow", ["inches", ["range", 8, 12]]]],
    ],
    "오후동안 눈(< 1cm)": [
        "sentence",
        [
            "during",
            ["parenthetical", "medium-snow", ["less-than", ["centimeters", 1]]],
            "afternoon",
        ],
    ],
    "일주일 내내 강수 없음, 내일 최고기온 85°F": [
        "sentence",
        [
            "with",
            ["for-week", "no-precipitation"],
            ["temperatures-peaking", ["fahrenheit", 85], "tomorrow"],
        ],
    ],
    "주말 내내 진눈깨비, 목요일 32°C까지 상승": [
        "sentence",
        [
            "with",
            ["over-weekend", "mixed-precipitation"],
            ["temperatures-rising", ["celsius", 32], "thursday"],
        ],
    ],
    "월요일동안 이슬비, 금요일 최저기온 15°F": [
        "sentence",
        [
            "with",
            ["during", "very-light-rain", "monday"],
            ["temperatures-valleying", ["fahrenheit", 15], "friday"],
        ],
    ],
    "화요일, 다음주 수요일동안 약한 눈, 일요일 0°C까지 하강": [
        "sentence",
        [
            "with",
            ["during", "light-snow", ["and", "tuesday", "next-wednesday"]],
            ["temperatures-falling", ["celsius", 0], "sunday"],
        ],
    ],
    "오늘부터 토요일동안 강수, 월요일 최고기온 100°F": [
        "sentence",
        [
            "with",
            ["during", "medium-precipitation", ["through", "today", "saturday"]],
            ["temperatures-peaking", ["fahrenheit", 100], "monday"],
        ],
    ],
    "온종일 진눈깨비(1–3인치)": [
        "sentence",
        [
            "for-day",
            ["parenthetical", "mixed-precipitation", ["inches", ["range", 1, 3]]],
        ],
    ],
    "강한 눈(1–3인치)": [
        "title",
        ["parenthetical", "heavy-snow", ["inches", ["range", 1, 3]]],
    ],
    "강한 눈(3–5cm)": [
        "title",
        ["parenthetical", "heavy-snow", ["centimeters", ["range", 3, 5]]],
    ],
    "뇌우 가능성": ["title", "possible-thunderstorm"],
    "강한 비, 뇌우": ["title", ["and", "heavy-rain", "thunderstorm"]],
    "< 1분 후 이슬비 시작": [
        "sentence",
        ["starting-in", "very-light-rain", ["less-than", ["minutes", 1]]],
    ],
}
