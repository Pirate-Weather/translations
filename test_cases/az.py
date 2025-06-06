# This would be one of your translations, as a Python dictionary
cases = {
    "Buludsuz": ["title", "clear"],
    "Yüngül Yağış Ehtimalı": ["title", "possible-very-light-precipitation"],
    "Yüngül Yağış": ["title", "very-light-precipitation"],
    "Yüngül Yağış Ehtimalı": ["title", "possible-light-precipitation"],
    "Yüngül Yağış": ["title", "light-precipitation"],
    "Yağış": ["title", "medium-precipitation"],
    "Güclü Yağış": ["title", "heavy-precipitation"],
    "Çiskin Yağış Ehtimalı": ["title", "possible-very-light-rain"],
    "Çiskin": ["title", "very-light-rain"],
    "Yüngül Yağış Ehtimalı": ["title", "possible-light-rain"],
    "Yüngül Yağış": ["title", "light-rain"],
    "Yağış": ["title", "medium-rain"],
    "Güclü Yağış": ["title", "heavy-rain"],
    "Yüngül Sulu Qar Ehtimalı": ["title", "possible-very-light-sleet"],
    "Yüngül Sulu Qar": ["title", "very-light-sleet"],
    "Yüngül Sulu Qar Ehtimalı": ["title", "possible-light-sleet"],
    "Yüngül Sulu Qar": ["title", "light-sleet"],
    "Sulu Qar": ["title", "medium-sleet"],
    "Güclü Sulu Qar": ["title", "heavy-sleet"],
    "Sulu Qar Ehtimalı": ["title", "possible-very-light-snow"],
    "Sulu Qar": ["title", "very-light-snow"],
    "Yüngül Qar Ehtimalı": ["title", "possible-light-snow"],
    "Yüngül Qar": ["title", "light-snow"],
    "Qar": ["title", "medium-snow"],
    "Güclü Qar": ["title", "heavy-snow"],
    "Külək": ["title", "medium-wind"],
    "Güclü Külək": ["title", "heavy-wind"],
    "Dumanlı": ["title", "fog"],
    "Əsasən Buludsuz": ["title", "very-light-clouds"],
    "Qismən Buludlu": ["title", "light-clouds"],
    "Əsasən Buludlu": ["title", "medium-clouds"],
    "Tutqun Hava": ["title", "heavy-clouds"],
    "Rütubətsiz və Sərin": ["title", ["and", "low-humidity", "light-wind"]],
    "Çiskin və Güclü Külək": ["title", ["and", "very-light-rain", "heavy-wind"]],
    "Rütubətli və Qismən Buludlu": ["title", ["and", "high-humidity", "light-clouds"]],
    "1 saat boyunca buludsuz olacaq.": ["sentence", ["for-hour", "clear"]],
    "35 dəq. sonra sulu qar başlayacaq.": [
        "sentence",
        ["starting-in", "very-light-snow", ["minutes", 35]],
    ],
    "Yüngül yağış 15 dəq. sonra dayanacaq.": [
        "sentence",
        ["stopping-in", "light-rain", ["minutes", 15]],
    ],
    "Güclü sulu qar 20 dəq. sonra başlayacaq, 30 dəq. davam edib dayanacaq.": [
        "sentence",
        [
            "starting-then-stopping-later",
            "heavy-sleet",
            ["minutes", 20],
            ["minutes", 30],
        ],
    ],
    "Yağış 25 dəq. sonra dayanacaq, 8 dəq. sonra yenidən başlayacaq.": [
        "sentence",
        [
            "stopping-then-starting-later",
            "medium-rain",
            ["minutes", 25],
            ["minutes", 8],
        ],
    ],
    "Gün boyu əsasən buludlu olacaq.": ["sentence", ["for-day", "medium-clouds"]],
    "Səhər yüngül sulu qar başlayacaq.": [
        "sentence",
        ["starting", "very-light-sleet", "morning"],
    ],
    "Külək bu gün gecə dayanacaq.": [
        "sentence",
        ["until", "medium-wind", "today-night"],
    ],
    "Güclü yağış günortadan sonra dayanacaq.": [
        "sentence",
        ["until", "heavy-precipitation", "afternoon"],
    ],
    "Günortadan sonra sərin olacaq.": [
        "sentence",
        ["during", "light-wind", "afternoon"],
    ],
    "Bu gün axşam və sabah səhər qar olacaq.": [
        "sentence",
        ["during", "medium-snow", ["and", "later-today-evening", "tomorrow-morning"]],
    ],
    "Güclü yağış bu gün səhərdən sonra dayanıb, bu gün axşam yenidən başlayacaq.": [
        "sentence",
        ["until-starting-again", "heavy-rain", "later-today-morning", "today-evening"],
    ],
    "Axşam tutqun hava başlayıb, gecə dayanacaq.": [
        "sentence",
        ["starting-continuing-until", "heavy-clouds", "evening", "night"],
    ],
    "Bu gün günortadan sonra yüngül sulu qar olacaq və sabah səhər dumanlı olacaq.": [
        "sentence",
        [
            "and",
            ["during", "light-sleet", "later-today-afternoon"],
            ["during", "fog", "tomorrow-morning"],
        ],
    ],
    "Bu gün səhər güclü külək başlayıb, bu gün günortadan sonra dayanacaq və sabah səhər sulu qar olacaq.": [
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
    "Bu gün gecə tutqun hava başlayacaq və sabah günortadan sonra güclü qar olacaq.": [
        "sentence",
        [
            "and",
            ["starting", "heavy-clouds", "later-today-night"],
            ["during", "heavy-snow", "tomorrow-afternoon"],
        ],
    ],
    "Bu gün gecə rütubətsiz olacaq və sabah axşam yüngül yağış başlayıb, sabah gecə dayanacaq.": [
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
    "Gecə qar (5 düym) olacaq.": [
        "sentence",
        ["during", ["parenthetical", "medium-snow", ["inches", 5]], "night"],
    ],
    "Bu gün səhərdən sonra yüngül qar (2 sm.) olacaq.": [
        "sentence",
        [
            "during",
            ["parenthetical", "light-snow", ["centimeters", 2]],
            "later-today-morning",
        ],
    ],
    "Gün boyu güclü qar (8–12 düym) olacaq.": [
        "sentence",
        ["for-day", ["parenthetical", "heavy-snow", ["inches", ["range", 8, 12]]]],
    ],
    "Günortadan sonra qar (1 sm.-dən aşağı) olacaq.": [
        "sentence",
        [
            "during",
            ["parenthetical", "medium-snow", ["less-than", ["centimeters", 1]]],
            "afternoon",
        ],
    ],
    "Həftə boyunca yağmursuz olacaq, sabah hava kəskin istiləşəcək və temperatur 85°F-yə qalxacaq.": [
        "sentence",
        [
            "with",
            ["for-week", "no-precipitation"],
            ["temperatures-peaking", ["fahrenheit", 85], "tomorrow"],
        ],
    ],
    "Həftə sonu qarışıq yağış olacaq, cümə axşamı temperatur 32°C-yə qalxacaq.": [
        "sentence",
        [
            "with",
            ["over-weekend", "mixed-precipitation"],
            ["temperatures-rising", ["celsius", 32], "thursday"],
        ],
    ],
    "Bazar ertəsi çiskin olacaq, cümə günü hava kəskin soyuyacaq və temperatur 15°F-yə düşəcək.": [
        "sentence",
        [
            "with",
            ["during", "very-light-rain", "monday"],
            ["temperatures-valleying", ["fahrenheit", 15], "friday"],
        ],
    ],
    "Çərşənbə axşamı və çərşənbə günü yüngül qar olacaq, bazar günü temperatur 0°C-yə düşəcək.": [
        "sentence",
        [
            "with",
            ["during", "light-snow", ["and", "tuesday", "wednesday"]],
            ["temperatures-falling", ["celsius", 0], "sunday"],
        ],
    ],
    "Bu gün ilə şənbə günü arası yağış olacaq, bazar ertəsi hava kəskin istiləşəcək və temperatur 100°F-yə qalxacaq.": [
        "sentence",
        [
            "with",
            ["during", "medium-precipitation", ["through", "today", "saturday"]],
            ["temperatures-peaking", ["fahrenheit", 100], "monday"],
        ],
    ],
    "Gün boyu qarışıq yağış (1–3 düym qar) olacaq.": [
        "sentence",
        [
            "for-day",
            ["parenthetical", "mixed-precipitation", ["inches", ["range", 1, 3]]],
        ],
    ],
    "Güclü Qar (1–3 düym)": [
        "title",
        ["parenthetical", "heavy-snow", ["inches", ["range", 1, 3]]],
    ],
    "Güclü Qar (3–5 sm.)": [
        "title",
        ["parenthetical", "heavy-snow", ["centimeters", ["range", 3, 5]]],
    ],
}
