# This would be one of your translations, as a Python dictionary
cases = {
    "quang mây": ["title", "clear"],
    "có thể có mưa nhỏ": ["title", "possible-very-light-precipitation"],
    "mưa nhỏ": ["title", "very-light-precipitation"],
    "có thể có mưa nhỏ": ["title", "possible-light-precipitation"],
    "mưa phùn": ["title", "light-precipitation"],
    "lượng mưa trung bình": ["title", "medium-precipitation"],
    "mưa to": ["title", "heavy-precipitation"],
    "có thể có mưa phùn": ["title", "possible-very-light-rain"],
    "mưa phùn": ["title", "very-light-rain"],
    "có thể có mưa nhỏ": ["title", "possible-light-rain"],
    "mưa nhỏ": ["title", "light-rain"],
    "mưa vừa": ["title", "medium-rain"],
    "mưa to": ["title", "heavy-rain"],
    "có thể có mưa tuyết nhỏ": ["title", "possible-very-light-sleet"],
    "mưa tuyết nhỏ": ["title", "very-light-sleet"],
    "có thể có mưa tuyết nhỏ": ["title", "possible-light-sleet"],
    "mưa tuyết nhỏ": ["title", "light-sleet"],
    "mưa tuyết vừa": ["title", "medium-sleet"],
    "mưa tuyết to": ["title", "heavy-sleet"],
    "có thể có tuyết rơi nhỏ": ["title", "possible-very-light-snow"],
    "tuyết rơi rất nhỏ": ["title", "very-light-snow"],
    "có thể có tuyết rơi nhỏ": ["title", "possible-light-snow"],
    "tuyết rơi nhỏ": ["title", "light-snow"],
    "tuyết rơi": ["title", "medium-snow"],
    "tuyết rơi nhiều": ["title", "heavy-snow"],
    "có gió": ["title", "medium-wind"],
    "gió to": ["title", "heavy-wind"],
    "có sương mù": ["title", "fog"],
    "có quang mây": ["title", "very-light-clouds"],
    "ít mây": ["title", "light-clouds"],
    "có mây": ["title", "medium-clouds"],
    "trời âm u": ["title", "heavy-clouds"],
    "trời hanh khô và gió nhẹ": ["title", ["and", "low-humidity", "light-wind"]],
    "mưa phùn và gió to": ["title", ["and", "very-light-rain", "heavy-wind"]],
    "độ ẩm cao và ít mây": ["title", ["and", "high-humidity", "light-clouds"]],
    "Quang mây trong một giờ.": ["sentence", ["for-hour", "clear"]],
    "Tuyết rơi rất nhỏ bắt đầu sau 35 phút.": [
        "sentence",
        ["starting-in", "very-light-snow", ["minutes", 35]],
    ],
    "Mưa nhỏ dừng sau 15 phút.": [
        "sentence",
        ["stopping-in", "light-rain", ["minutes", 15]],
    ],
    "Mưa tuyết to bắt đầu sau 20 phút, dừng lại 30 phút sau.": [
        "sentence",
        [
            "starting-then-stopping-later",
            "heavy-sleet",
            ["minutes", 20],
            ["minutes", 30],
        ],
    ],
    "Mưa vừa dừng sau 25 phút, tiếp tục 8 phút sau.": [
        "sentence",
        [
            "stopping-then-starting-later",
            "medium-rain",
            ["minutes", 25],
            ["minutes", 8],
        ],
    ],
    "Có mây suốt cả ngày.": ["sentence", ["for-day", "medium-clouds"]],
    "Mưa tuyết nhỏ bắt đầu lúc buổi sáng.": [
        "sentence",
        ["starting", "very-light-sleet", "morning"],
    ],
    "Có gió cho đến đêm nay.": ["sentence", ["until", "medium-wind", "today-night"]],
    "Lượng mưa lớn cho đến buổi chiều.": [
        "sentence",
        ["until", "heavy-precipitation", "afternoon"],
    ],
    "Gió nhẹ vào buổi chiều.": ["sentence", ["during", "light-wind", "afternoon"]],
    "Tuyết rơi vào tối hôm nay và sáng mai.": [
        "sentence",
        ["during", "medium-snow", ["and", "later-today-evening", "tomorrow-morning"]],
    ],
    "Mưa to cho đến cuối buổi sáng, bắt đầu lại chiều tối nay.": [
        "sentence",
        ["until-starting-again", "heavy-rain", "later-today-morning", "today-evening"],
    ],
    "Trời âm u bắt đầu lúc buổi tối, tiếp tục tới đêm.": [
        "sentence",
        ["starting-continuing-until", "heavy-clouds", "evening", "night"],
    ],
    "Mưa tuyết nhỏ vào chiều hôm nay và có sương mù vào sáng mai.": [
        "sentence",
        [
            "and",
            ["during", "light-sleet", "later-today-afternoon"],
            ["during", "fog", "tomorrow-morning"],
        ],
    ],
    "Gió to bắt đầu lúc sáng nay, tiếp tục tới trưa nay, và mưa tuyết vừa vào sáng mai.": [
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
    "Trời âm u bắt đầu lúc nửa đêm và tuyết rơi nhiều vào trưa mai.": [
        "sentence",
        [
            "and",
            ["starting", "heavy-clouds", "later-today-night"],
            ["during", "heavy-snow", "tomorrow-afternoon"],
        ],
    ],
    "Trời hanh khô vào đêm nay và lượng mưa nhỏ bắt đầu lúc chiều tối mai, tiếp tục tới tối mai.": [
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
    "Tuyết rơi (5 in) vào đêm.": [
        "sentence",
        ["during", ["parenthetical", "medium-snow", ["inches", 5]], "night"],
    ],
    "Tuyết rơi nhỏ (2 cm) vào cuối buổi sáng.": [
        "sentence",
        [
            "during",
            ["parenthetical", "light-snow", ["centimeters", 2]],
            "later-today-morning",
        ],
    ],
    "Tuyết rơi nhiều (8–12 in) suốt cả ngày.": [
        "sentence",
        ["for-day", ["parenthetical", "heavy-snow", ["inches", ["range", 8, 12]]]],
    ],
    "Tuyết rơi (dưới 1 cm) vào buổi chiều.": [
        "sentence",
        [
            "during",
            ["parenthetical", "medium-snow", ["less-than", ["centimeters", 1]]],
            "afternoon",
        ],
    ],
    "Không mưa cả tuần, với nhiệt độ đỉnh điểm 85\u00b0F vào ngày mai.": [
        "sentence",
        [
            "with",
            ["for-week", "no-precipitation"],
            ["temperatures-peaking", ["fahrenheit", 85], "tomorrow"],
        ],
    ],
    "Mưa rải rác suốt cuốt tuần, với nhiệt độ tăng tới 32°C vào thứ năm.": [
        "sentence",
        [
            "with",
            ["over-weekend", "mixed-precipitation"],
            ["temperatures-rising", ["celsius", 32], "thursday"],
        ],
    ],
    "Mưa phùn vào thứ hai, với nhiệt độ thấp nhất 15°F vào thứ sáu.": [
        "sentence",
        [
            "with",
            ["during", "very-light-rain", "monday"],
            ["temperatures-valleying", ["fahrenheit", 15], "friday"],
        ],
    ],
    "Tuyết rơi nhỏ vào thứ ba và tư tuần sau, với nhiệt độ giảm tới 0°C vào chủ nhật.": [
        "sentence",
        [
            "with",
            ["during", "light-snow", ["and", "tuesday", "next-wednesday"]],
            ["temperatures-falling", ["celsius", 0], "sunday"],
        ],
    ],
    "Lượng mưa trung bình vào hôm nay cho tới thứ bảy, với nhiệt độ đỉnh điểm 100°F vào thứ hai.": [
        "sentence",
        [
            "with",
            ["during", "medium-precipitation", ["through", "today", "saturday"]],
            ["temperatures-peaking", ["fahrenheit", 100], "monday"],
        ],
    ],
    "Mưa rải rác (1–3 in tuyết) suốt cả ngày.": [
        "sentence",
        [
            "for-day",
            ["parenthetical", "mixed-precipitation", ["inches", ["range", 1, 3]]],
        ],
    ],
    "tuyết rơi nhiều (1\u20133 in)": [
        "title",
        ["parenthetical", "heavy-snow", ["inches", ["range", 1, 3]]],
    ],
    "tuyết rơi nhiều (3\u20135 cm)": [
        "title",
        ["parenthetical", "heavy-snow", ["centimeters", ["range", 3, 5]]],
    ],
    "có thể có dông": ["title", "possible-thunderstorm"],
    "mưa to và có dông": ["title", ["and", "heavy-rain", "thunderstorm"]],
    "khói": ["title", "smoke"],
    "Khói suốt cả ngày.": ["sentence", ["for-day", "smoke"]],
    "Khói vào buổi sáng.": ["sentence", ["during", "smoke", "morning"]],
    "Khói cho đến chiều tối nay.": ["sentence", ["until", "smoke", "today-evening"]],
    "khói và ít mây": ["title", ["and", "smoke", "light-clouds"]],
    "sương mù": ["title", "haze"],
    "Sương mù suốt cả ngày.": ["sentence", ["for-day", "haze"]],
    "Sương mù vào buổi chiều.": ["sentence", ["during", "haze", "afternoon"]],
    "sương mù và độ ẩm cao": ["title", ["and", "haze", "high-humidity"]],
    "Sương mù vào đêm.": ["sentence", ["during", "mist", "night"]],
    "sương mù và trời âm u": ["title", ["and", "mist", "heavy-clouds"]],
}
