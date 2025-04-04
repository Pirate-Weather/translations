# This would be one of your translations, as a Python dictionary
cases = {
    "Sereno": ["title", "clear"],
    "Possibilità Di Precipitazioni Molto Leggere": [
        "title",
        "possible-very-light-precipitation",
    ],
    "Precipitazioni Molto Leggere": ["title", "very-light-precipitation"],
    "Possibilità Di Precipitazioni Leggere": ["title", "possible-light-precipitation"],
    "Precipitazioni Leggere": ["title", "light-precipitation"],
    "Precipitazioni": ["title", "medium-precipitation"],
    "Forti Precipitazioni": ["title", "heavy-precipitation"],
    "Possibilità Di Pioggia Molto Leggera": ["title", "possible-very-light-rain"],
    "Pioggia Molto Leggera": ["title", "very-light-rain"],
    "Possibilità Di Pioggia Leggera": ["title", "possible-light-rain"],
    "Pioggia Leggera": ["title", "light-rain"],
    "Pioggia": ["title", "medium-rain"],
    "Temporali": ["title", "heavy-rain"],
    "Possibilità Di Nevischio Molto Leggero": ["title", "possible-very-light-sleet"],
    "Nevischio Molto Leggero": ["title", "very-light-sleet"],
    "Possibilità Di Nevischio Leggero": ["title", "possible-light-sleet"],
    "Nevischio Leggero": ["title", "light-sleet"],
    "Nevischio": ["title", "medium-sleet"],
    "Forte Nevischio": ["title", "heavy-sleet"],
    "Possibilità Di Nevicate Molto Leggere": ["title", "possible-very-light-snow"],
    "Nevicate Molto Leggere": ["title", "very-light-snow"],
    "Possibilità Di Neve Leggera": ["title", "possible-light-snow"],
    "Neve Leggera": ["title", "light-snow"],
    "Nevicate": ["title", "medium-snow"],
    "Forti Nevicate": ["title", "heavy-snow"],
    "Vento": ["title", "medium-wind"],
    "Forte Vento": ["title", "heavy-wind"],
    "Nebbia": ["title", "fog"],
    "Prevalentemente Sereno": ["title", "very-light-clouds"],
    "Poco Nuvoloso": ["title", "light-clouds"],
    "Nubi Sparse": ["title", "medium-clouds"],
    "Nuvoloso": ["title", "heavy-clouds"],
    "Bassa Umidità e Venticello": ["title", ["and", "low-humidity", "light-wind"]],
    "Pioggia Molto Leggera e Forte Vento": [
        "title",
        ["and", "very-light-rain", "heavy-wind"],
    ],
    "Umido e Poco Nuvoloso": ["title", ["and", "high-humidity", "light-clouds"]],
    "Sereno per un ora.": ["sentence", ["for-hour", "clear"]],
    "Nevicate molto leggere tra 35 min.": [
        "sentence",
        ["starting-in", "very-light-snow", ["minutes", 35]],
    ],
    "Pioggia leggera per 15 min.": [
        "sentence",
        ["stopping-in", "light-rain", ["minutes", 15]],
    ],
    "Forte nevischio a partire tra 20 min. per 30 min.": [
        "sentence",
        [
            "starting-then-stopping-later",
            "heavy-sleet",
            ["minutes", 20],
            ["minutes", 30],
        ],
    ],
    "Pioggia per altri 25 min., per ricominciare 8 min. più tardi.": [
        "sentence",
        [
            "stopping-then-starting-later",
            "medium-rain",
            ["minutes", 25],
            ["minutes", 8],
        ],
    ],
    "Nubi sparse durante il giorno.": ["sentence", ["for-day", "medium-clouds"]],
    "Nevischio molto leggero a partire da mattina.": [
        "sentence",
        ["starting", "very-light-sleet", "morning"],
    ],
    "Vento fino a stanotte.": ["sentence", ["until", "medium-wind", "today-night"]],
    "Forti precipitazioni fino a pomeriggio.": [
        "sentence",
        ["until", "heavy-precipitation", "afternoon"],
    ],
    "Venticello nel pomeriggio.": ["sentence", ["during", "light-wind", "afternoon"]],
    "Nevicate a sera inoltrata e domani mattina.": [
        "sentence",
        ["during", "medium-snow", ["and", "later-today-evening", "tomorrow-morning"]],
    ],
    "Temporali fino a a mattina inoltrata, ricominciando da stasera.": [
        "sentence",
        ["until-starting-again", "heavy-rain", "later-today-morning", "today-evening"],
    ],
    "Nuvoloso a partire da sera, fino a notte.": [
        "sentence",
        ["starting-continuing-until", "heavy-clouds", "evening", "night"],
    ],
    "Nevischio leggero a pomeriggio inoltrato e nebbia domani mattina.": [
        "sentence",
        [
            "and",
            ["during", "light-sleet", "later-today-afternoon"],
            ["during", "fog", "tomorrow-morning"],
        ],
    ],
    "Forte vento a partire da stamattina, fino a questo pomeriggio, e nevischio domani mattina.": [
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
    "Nuvoloso a partire da notte inoltrata e forti nevicate domani pomeriggio.": [
        "sentence",
        [
            "and",
            ["starting", "heavy-clouds", "later-today-night"],
            ["during", "heavy-snow", "tomorrow-afternoon"],
        ],
    ],
    "Bassa umidità stanotte e precipitazioni leggere a partire da domani sera, fino a domani notte.": [
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
    "Nevicate (5 in.) nella notte.": [
        "sentence",
        ["during", ["parenthetical", "medium-snow", ["inches", 5]], "night"],
    ],
    "Neve leggera (2 cm.) a mattina inoltrata.": [
        "sentence",
        [
            "during",
            ["parenthetical", "light-snow", ["centimeters", 2]],
            "later-today-morning",
        ],
    ],
    "Forti nevicate (8\u201312 in.) durante il giorno.": [
        "sentence",
        ["for-day", ["parenthetical", "heavy-snow", ["inches", ["range", 8, 12]]]],
    ],
    "Nevicate (meno di 1 cm.) nel pomeriggio.": [
        "sentence",
        [
            "during",
            ["parenthetical", "medium-snow", ["less-than", ["centimeters", 1]]],
            "afternoon",
        ],
    ],
    "Nessuna precipitazione durante la settimana, con temperatura massima di 85°F domani.": [
        "sentence",
        [
            "with",
            ["for-week", "no-precipitation"],
            ["temperatures-peaking", ["fahrenheit", 85], "tomorrow"],
        ],
    ],
    "Precipitazioni miste tutto il week end, con temperature in aumento fino a 32\u00b0C Giovedì.": [
        "sentence",
        [
            "with",
            ["over-weekend", "mixed-precipitation"],
            ["temperatures-rising", ["celsius", 32], "thursday"],
        ],
    ],
    "Pioggia molto leggera Lunedì, con temperatura minima di 15\u00b0F Venerdì.": [
        "sentence",
        [
            "with",
            ["during", "very-light-rain", "monday"],
            ["temperatures-valleying", ["fahrenheit", 15], "friday"],
        ],
    ],
    "Neve leggera Martedì e il prossimo Mercoledì, con temperature in diminuzione fino a 0\u00b0C Domenica.": [
        "sentence",
        [
            "with",
            ["during", "light-snow", ["and", "tuesday", "next-wednesday"]],
            ["temperatures-falling", ["celsius", 0], "sunday"],
        ],
    ],
    "Precipitazioni oggi fino a Sabato, con temperatura massima di 100\u00b0F Lunedì.": [
        "sentence",
        [
            "with",
            ["during", "medium-precipitation", ["through", "today", "saturday"]],
            ["temperatures-peaking", ["fahrenheit", 100], "monday"],
        ],
    ],
    "Precipitazioni miste (1\u20133 in. di neve) durante il giorno.": [
        "sentence",
        [
            "for-day",
            ["parenthetical", "mixed-precipitation", ["inches", ["range", 1, 3]]],
        ],
    ],
    "Forti Nevicate (1\u20133 In.)": [
        "title",
        ["parenthetical", "heavy-snow", ["inches", ["range", 1, 3]]],
    ],
    "Forti Nevicate (3\u20135 Cm.)": [
        "title",
        ["parenthetical", "heavy-snow", ["centimeters", ["range", 3, 5]]],
    ],
    "Possibili Nubifragi": ["title", "possible-thunderstorm"],
    "Temporali e Nubifragi": ["title", ["and", "heavy-rain", "thunderstorm"]],
}
