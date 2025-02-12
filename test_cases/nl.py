# This would be one of your translations, as a Python dictionary
cases = {
    "Helder": ["title", "clear"],
    "Lichte neerslag": ["title", "very-light-precipitation"],
    "Lichte neerslag": ["title", "light-precipitation"],
    "Neerslag": ["title", "medium-precipitation"],
    "Zware neerslag": ["title", "heavy-precipitation"],
    "Motregen": ["title", "very-light-rain"],
    "Lichte regen": ["title", "light-rain"],
    "Regen": ["title", "medium-rain"],
    "Zware regenbuien": ["title", "heavy-rain"],
    "Lichte ijzel": ["title", "very-light-sleet"],
    "Lichte ijzel": ["title", "light-sleet"],
    "Ijzel": ["title", "medium-sleet"],
    "Zware ijzel": ["title", "heavy-sleet"],
    "Lichte sneeuwval": ["title", "very-light-snow"],
    "Sneeuwval": ["title", "light-snow"],
    "Sneeuw": ["title", "medium-snow"],
    "Zware sneeuwbuien": ["title", "heavy-snow"],
    "Veel wind": ["title", "medium-wind"],
    "Zware windstoten": ["title", "heavy-wind"],
    "Mist": ["title", "fog"],
    "Overwegend helder": ["title", "very-light-clouds"],
    "Licht bewolkt": ["title", "light-clouds"],
    "Overwegend bewolkt": ["title", "medium-clouds"],
    "Zwaar bewolkt": ["title", "heavy-clouds"],
    "Mogelijk lichte ijzel": ["title", "possible-light-sleet"],
    "Lage luchtvochtigheid en lichte wind": [
        "title",
        ["and", "low-humidity", "light-wind"],
    ],
    "Hoge luchtvochtigheid en licht bewolkt": [
        "title",
        ["and", "high-humidity", "light-clouds"],
    ],
    "Het komende uur helder.": ["sentence", ["for-hour", "clear"]],
    "Over 35 minuten lichte sneeuwval.": [
        "sentence",
        ["starting-in", "very-light-snow", ["minutes", 35]],
    ],
    "Lichte regen, stopt over 15 minuten.": [
        "sentence",
        ["stopping-in", "light-rain", ["minutes", 15]],
    ],
    "Zware ijzel begint over 20 minuten en stopt weer 30 minuten later.": [
        "sentence",
        [
            "starting-then-stopping-later",
            "heavy-sleet",
            ["minutes", 20],
            ["minutes", 30],
        ],
    ],
    "Regen stopt over 25 minuten maar begint 8 minuten later opnieuw.": [
        "sentence",
        [
            "stopping-then-starting-later",
            "medium-rain",
            ["minutes", 25],
            ["minutes", 8],
        ],
    ],
    "Overwegend bewolkt gedurende de dag.": ["sentence", ["for-day", "medium-clouds"]],
    "Vanaf de ochtend lichte ijzelvorming.": [
        "sentence",
        ["starting", "very-light-sleet", "morning"],
    ],
    "Veel wind tot vannacht.": ["sentence", ["until", "medium-wind", "today-night"]],
    "Zware neerslag tot de middag.": [
        "sentence",
        ["until", "heavy-precipitation", "afternoon"],
    ],
    "Lichte wind gedurende de middag.": [
        "sentence",
        ["during", "light-wind", "afternoon"],
    ],
    "Sneeuw gedurende later vanavond en morgenochtend.": [
        "sentence",
        ["during", "medium-snow", ["and", "later-today-evening", "tomorrow-morning"]],
    ],
    "Zware regenbuien tot later vanochtend en vanavond weer opnieuw.": [
        "sentence",
        ["until-starting-again", "heavy-rain", "later-today-morning", "today-evening"],
    ],
    "Zwaar bewolkt vanaf de avond, houdt aan tot de nacht.": [
        "sentence",
        ["starting-continuing-until", "heavy-clouds", "evening", "night"],
    ],
    "Later vanmiddag lichte ijzel en morgenochtend mist.": [
        "sentence",
        [
            "and",
            ["during", "light-sleet", "later-today-afternoon"],
            ["during", "fog", "tomorrow-morning"],
        ],
    ],
    "Zware windstoten vanaf de ochtend, houdt aan tot de middag, en morgenochtend ijzel.": [
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
    "Later vannacht zwaar bewolkt en morgenmiddag zware sneeuwbuien.": [
        "sentence",
        [
            "and",
            ["starting", "heavy-clouds", "later-today-night"],
            ["during", "heavy-snow", "tomorrow-afternoon"],
        ],
    ],
    "Vannacht lage luchtvochtigheid en lichte neerslag vanaf morgenavond, houdt aan tot morgennacht.": [
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
    "Sneeuw (5 inch) gedurende de nacht.": [
        "sentence",
        ["during", ["parenthetical", "medium-snow", ["inches", 5]], "night"],
    ],
    "Vanaf later vanochtend sneeuwval (2 cm).": [
        "sentence",
        [
            "starting",
            ["parenthetical", "light-snow", ["centimeters", 2]],
            "later-today-morning",
        ],
    ],
    "Zware sneeuwbuien (8 tot 12 inch) gedurende de dag.": [
        "sentence",
        ["for-day", ["parenthetical", "heavy-snow", ["inches", ["range", 8, 12]]]],
    ],
    "Sneeuw (minder dan 1 cm) gedurende de middag.": [
        "sentence",
        [
            "during",
            ["parenthetical", "medium-snow", ["centimeters", ["less-than", 1]]],
            "afternoon",
        ],
    ],
    "De hele week geen neerslag met een maximum temperatuur van 85\u00b0F morgen.": [
        "sentence",
        [
            "with",
            ["for-week", "no-precipitation"],
            ["temperatures-peaking", ["fahrenheit", 85], "tomorrow"],
        ],
    ],
    "Wisselende neerslag dit weekend met temperaturen stijgend tot 32\u00b0C op donderdag.": [
        "sentence",
        [
            "with",
            ["over-weekend", "mixed-precipitation"],
            ["temperatures-rising", ["celsius", 32], "thursday"],
        ],
    ],
    "Motregen vandaag met een minimum temperatuur van 15\u00b0F op vrijdag.": [
        "sentence",
        [
            "with",
            ["during", "very-light-rain", "today"],
            ["temperatures-valleying", ["fahrenheit", 15], "friday"],
        ],
    ],
    "Sneeuwval op maandag en dinsdag met temperaturen dalend tot 0\u00b0C op zondag.": [
        "sentence",
        [
            "with",
            ["during", "light-snow", ["and", "monday", "tuesday"]],
            ["temperatures-falling", ["celsius", 0], "sunday"],
        ],
    ],
    "Neerslag donderdag tot en met zaterdag met een maximum temperatuur van 100\u00b0F op maandag.": [
        "sentence",
        [
            "with",
            ["during", "medium-precipitation", ["through", "thursday", "saturday"]],
            ["temperatures-peaking", ["fahrenheit", 100], "monday"],
        ],
    ],
    "Vanaf vannacht lichte regen.": [
        "sentence",
        ["starting", "light-rain", "today-night"],
    ],
    "Mogelijk onweer": ["title", "possible-thunderstorm"],
    "Zware regenbuien en onweer": ["title", ["and", "heavy-rain", "thunderstorm"]],
    "De eerstvolgende voorspelling is tijdelijk niet beschikbaar omdat alle radar stations in de buurt offline zijn.": [
        "sentence",
        ["next-hour-forecast-status", "temporarily-unavailable", "station-offline"],
    ],
    "De eerstvolgende voorspelling is gedeeltelijk niet beschikbaar omdat de dekking van radar stations in de buurt niet volledig is.": [
        "sentence",
        ["next-hour-forecast-status", "partially-unavailable", "station-incomplete"],
    ],
    "De eerstvolgende voorspelling is niet beschikbaar omdat alle radar stations in de buurt offline zijn.": [
        "sentence",
        ["next-hour-forecast-status", "unavailable", "station-offline"],
    ],
}
