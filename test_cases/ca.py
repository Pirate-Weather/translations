# This would be one of your translations, as a Python dictionary
cases = {
    "Clar": ["title", "clear"],
    "Possibles Pluges Lleugeres": ["title", "possible-very-light-precipitation"],
    "Precipitacions Lleugeres": ["title", "very-light-precipitation"],
    "Possibles Pluges Lleugeres": ["title", "possible-light-precipitation"],
    "Precipitacions Lleugeres": ["title", "light-precipitation"],
    "Precipitació": ["title", "medium-precipitation"],
    "Fortes Precipitacions": ["title", "heavy-precipitation"],
    "Possible Plugim": ["title", "possible-very-light-rain"],
    "Plugim": ["title", "very-light-rain"],
    "Possible Plugim": ["title", "possible-light-rain"],
    "Pluja Lleugera": ["title", "light-rain"],
    "Pluja": ["title", "medium-rain"],
    "Pluges Fortes": ["title", "heavy-rain"],
    "Aiguaneu": ["title", "possible-very-light-sleet"],
    "Aiguaneu": ["title", "very-light-sleet"],
    "Possible Aiguaneu": ["title", "possible-light-sleet"],
    "Aiguaneu": ["title", "light-sleet"],
    "Aiguaneu": ["title", "medium-sleet"],
    "Fortes Aiguaneu": ["title", "heavy-sleet"],
    "Possible Nevada Lleugera": ["title", "possible-very-light-snow"],
    "Lleugeres Nevades": ["title", "very-light-snow"],
    "Possible Nevada Lleugera": ["title", "possible-light-snow"],
    "Lleugeres Nevades": ["title", "light-snow"],
    "Nevades": ["title", "medium-snow"],
    "Fortes Nevades": ["title", "heavy-snow"],
    "Ventós": ["title", "medium-wind"],
    "Perillosament Ventós": ["title", "heavy-wind"],
    "Ennuvolat": ["title", "fog"],
    "Majoritariament Clar": ["title", "very-light-clouds"],
    "Parcialment Ennuvolat": ["title", "light-clouds"],
    "Majoritariament Ennuvolat": ["title", "medium-clouds"],
    "Ennuvolat": ["title", "heavy-clouds"],
    "Sec i Vents Fluixos": ["title", ["and", "low-humidity", "light-wind"]],
    "Plugim i Perillosament Ventós": [
        "title",
        ["and", "very-light-rain", "heavy-wind"],
    ],
    "Humit i Parcialment Ennuvolat": [
        "title",
        ["and", "high-humidity", "light-clouds"],
    ],
    "Clar cada hora.": ["sentence", ["for-hour", "clear"]],
    "Lleugeres nevades començant 35 min.": [
        "sentence",
        ["starting-in", "very-light-snow", ["minutes", 35]],
    ],
    "Pluja lleugera parant a 15 min.": [
        "sentence",
        ["stopping-in", "light-rain", ["minutes", 15]],
    ],
    "Fortes aiguaneu començant d'aquí 20 min., després parant al cap 30 min.": [
        "sentence",
        [
            "starting-then-stopping-later",
            "heavy-sleet",
            ["minutes", 20],
            ["minutes", 30],
        ],
    ],
    "Pluja parant d'aquí 25 min., tornant a començar al cap 8 min.": [
        "sentence",
        [
            "stopping-then-starting-later",
            "medium-rain",
            ["minutes", 25],
            ["minutes", 8],
        ],
    ],
    "Majoritariament ennuvolat durant el dia.": [
        "sentence",
        ["for-day", "medium-clouds"],
    ],
    "Aiguaneu començant al matí.": [
        "sentence",
        ["starting", "very-light-sleet", "morning"],
    ],
    "Ventós aquesta nit.": ["sentence", ["until", "medium-wind", "today-night"]],
    "Fortes precipitacions a la tarda.": [
        "sentence",
        ["until", "heavy-precipitation", "afternoon"],
    ],
    "Vents fluixos a la tarda.": ["sentence", ["during", "light-wind", "afternoon"]],
    "Nevades durant el vespre i demà al matí.": [
        "sentence",
        ["during", "medium-snow", ["and", "later-today-evening", "tomorrow-morning"]],
    ],
    "Pluges fortes durant el matí, començant aquest vespre.": [
        "sentence",
        ["until-starting-again", "heavy-rain", "later-today-morning", "today-evening"],
    ],
    "Ennuvolat començant al vespre, continuant a la nit.": [
        "sentence",
        ["starting-continuing-until", "heavy-clouds", "evening", "night"],
    ],
    "Aiguaneu durant la tarda i ennuvolat demà al matí.": [
        "sentence",
        [
            "and",
            ["during", "light-sleet", "later-today-afternoon"],
            ["during", "fog", "tomorrow-morning"],
        ],
    ],
    "Perillosament ventós començant aquest matí, continuant aquesta tarda, i aiguaneu demà al matí.": [
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
    "Ennuvolat començant durant la nit i fortes nevades demà a la tarda.": [
        "sentence",
        [
            "and",
            ["starting", "heavy-clouds", "later-today-night"],
            ["during", "heavy-snow", "tomorrow-afternoon"],
        ],
    ],
    "Sec aquesta nit i precipitacions lleugeres començant demà al vespre, continuant demà a la nit.": [
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
    "Nevades (5 in.) a la nit.": [
        "sentence",
        ["during", ["parenthetical", "medium-snow", ["inches", 5]], "night"],
    ],
    "Lleugeres nevades (2 cm.) durant el matí.": [
        "sentence",
        [
            "during",
            ["parenthetical", "light-snow", ["centimeters", 2]],
            "later-today-morning",
        ],
    ],
    "Fortes nevades (8–12 in.) durant el dia.": [
        "sentence",
        ["for-day", ["parenthetical", "heavy-snow", ["inches", ["range", 8, 12]]]],
    ],
    "Nevades (menys de 1 cm.) a la tarda.": [
        "sentence",
        [
            "during",
            ["parenthetical", "medium-snow", ["less-than", ["centimeters", 1]]],
            "afternoon",
        ],
    ],
    "Sense precipitacions durant la setmana, amb temperatures aconseguint un màxim de 85\u00b0F demà.": [
        "sentence",
        [
            "with",
            ["for-week", "no-precipitation"],
            ["temperatures-peaking", ["fahrenheit", 85], "tomorrow"],
        ],
    ],
    "Precipitacions mixtes cap al cap de setmana, amb temperatures arribant a 32\u00b0C el dijous.": [
        "sentence",
        [
            "with",
            ["over-weekend", "mixed-precipitation"],
            ["temperatures-rising", ["celsius", 32], "thursday"],
        ],
    ],
    "Plugim el dilluns, amb temperatures aconseguint un mínim de 15\u00b0F el divendres.": [
        "sentence",
        [
            "with",
            ["during", "very-light-rain", "monday"],
            ["temperatures-valleying", ["fahrenheit", 15], "friday"],
        ],
    ],
    "Lleugeres nevades el dimarts i dimecres, amb temperatures per sota a 0\u00b0C el diumenge.": [
        "sentence",
        [
            "with",
            ["during", "light-snow", ["and", "tuesday", "wednesday"]],
            ["temperatures-falling", ["celsius", 0], "sunday"],
        ],
    ],
    "Precipitació avui fins a el dissabte, amb temperatures aconseguint un màxim de 100\u00b0F el dilluns.": [
        "sentence",
        [
            "with",
            ["during", "medium-precipitation", ["through", "today", "saturday"]],
            ["temperatures-peaking", ["fahrenheit", 100], "monday"],
        ],
    ],
    "Precipitacions mixtes (1\u20133 in.) durant el dia.": [
        "sentence",
        [
            "for-day",
            ["parenthetical", "mixed-precipitation", ["inches", ["range", 1, 3]]],
        ],
    ],
    "Fortes Nevades (1\u20133 In.)": [
        "title",
        ["parenthetical", "heavy-snow", ["inches", ["range", 1, 3]]],
    ],
    "Fortes Nevades (3\u20135 Cm.)": [
        "title",
        ["parenthetical", "heavy-snow", ["centimeters", ["range", 3, 5]]],
    ],
    "Possibles Tempestes": ["title", "possible-thunderstorm"],
    "Pluges Fortes i Tempesta": ["title", ["and", "heavy-rain", "thunderstorm"]],
}
