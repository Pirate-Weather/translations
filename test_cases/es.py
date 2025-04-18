# This would be one of your translations, as a Python dictionary
cases = {
    "Despejado": ["title", "clear"],
    "Posibles Lluvias Ligeras": ["title", "possible-very-light-precipitation"],
    "Precipitación Ligera": ["title", "very-light-precipitation"],
    "Posibles Lluvias Ligeras": ["title", "possible-light-precipitation"],
    "Precipitación Ligera": ["title", "light-precipitation"],
    "Precipitación": ["title", "medium-precipitation"],
    "Fuerte Precipitación": ["title", "heavy-precipitation"],
    "Posible Llovizna": ["title", "possible-very-light-rain"],
    "Llovizna": ["title", "very-light-rain"],
    "Posible Lluvia Ligera": ["title", "possible-light-rain"],
    "Lluvia Ligera": ["title", "light-rain"],
    "Lluvia": ["title", "medium-rain"],
    "Fuertes Lluvias": ["title", "heavy-rain"],
    "Posible Aguanieve Ligera": ["title", "possible-very-light-sleet"],
    "Aguanieve Ligera": ["title", "very-light-sleet"],
    "Posible Aguanieve Ligera": ["title", "possible-light-sleet"],
    "Aguanieve Ligera": ["title", "light-sleet"],
    "Aguanieve": ["title", "medium-sleet"],
    "Fuertes Aguanieves": ["title", "heavy-sleet"],
    "Posible Nevada Ligera": ["title", "possible-very-light-snow"],
    "Nevadas Ligeras": ["title", "very-light-snow"],
    "Posible Nevada Ligera": ["title", "possible-light-snow"],
    "Nevadas Ligeras": ["title", "light-snow"],
    "Nevadas": ["title", "medium-snow"],
    "Fuertes Nevadas": ["title", "heavy-snow"],
    "Ventoso": ["title", "medium-wind"],
    "Peligrosamente Ventoso": ["title", "heavy-wind"],
    "Niebla": ["title", "fog"],
    "Mayormente Despejado": ["title", "very-light-clouds"],
    "Parcialmente Nublado": ["title", "light-clouds"],
    "Mayormente Nublado": ["title", "medium-clouds"],
    "Nublado": ["title", "heavy-clouds"],
    "Seco y Vientos Suaves": ["title", ["and", "low-humidity", "light-wind"]],
    "Llovizna y Peligrosamente Ventoso": [
        "title",
        ["and", "very-light-rain", "heavy-wind"],
    ],
    "Húmedo y Parcialmente Nublado": [
        "title",
        ["and", "high-humidity", "light-clouds"],
    ],
    "Despejado por la hora.": ["sentence", ["for-hour", "clear"]],
    "Nevadas ligeras comenzando en 35 min.": [
        "sentence",
        ["starting-in", "very-light-snow", ["minutes", 35]],
    ],
    "Lluvia ligera parando en 15 min.": [
        "sentence",
        ["stopping-in", "light-rain", ["minutes", 15]],
    ],
    "Fuertes aguanieves comenzando en 20 min., después parando en 30 min.": [
        "sentence",
        [
            "starting-then-stopping-later",
            "heavy-sleet",
            ["minutes", 20],
            ["minutes", 30],
        ],
    ],
    "Lluvia parando en 25 min., comenzando de nuevo 8 min. después.": [
        "sentence",
        [
            "stopping-then-starting-later",
            "medium-rain",
            ["minutes", 25],
            ["minutes", 8],
        ],
    ],
    "Mayormente nublado durante el día.": ["sentence", ["for-day", "medium-clouds"]],
    "Aguanieve ligera comenzando por la mañana.": [
        "sentence",
        ["starting", "very-light-sleet", "morning"],
    ],
    "Ventoso hasta esta noche.": ["sentence", ["until", "medium-wind", "today-night"]],
    "Fuerte precipitación hasta por la tarde.": [
        "sentence",
        ["until", "heavy-precipitation", "afternoon"],
    ],
    "Vientos suaves por la tarde.": ["sentence", ["during", "light-wind", "afternoon"]],
    "Nevadas después esta noche y mañana por la mañana.": [
        "sentence",
        ["during", "medium-snow", ["and", "later-today-evening", "tomorrow-morning"]],
    ],
    "Fuertes lluvias hasta después esta mañana, comenzando otra vez esta noche.": [
        "sentence",
        ["until-starting-again", "heavy-rain", "later-today-morning", "today-evening"],
    ],
    "Nublado comenzando por la noche, continuando hasta por la noche.": [
        "sentence",
        ["starting-continuing-until", "heavy-clouds", "evening", "night"],
    ],
    "Aguanieve ligera después esta tarde y niebla mañana por la mañana.": [
        "sentence",
        [
            "and",
            ["during", "light-sleet", "later-today-afternoon"],
            ["during", "fog", "tomorrow-morning"],
        ],
    ],
    "Peligrosamente ventoso comenzando esta mañana, continuando hasta esta tarde, y aguanieve mañana por la mañana.": [
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
    "Nublado comenzando después esta noche y fuertes nevadas mañana por la tarde.": [
        "sentence",
        [
            "and",
            ["starting", "heavy-clouds", "later-today-night"],
            ["during", "heavy-snow", "tomorrow-afternoon"],
        ],
    ],
    "Seco esta noche y precipitación ligera comenzando mañana por la noche, continuando hasta mañana por la noche.": [
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
    "Nevadas (5 in.) por la noche.": [
        "sentence",
        ["during", ["parenthetical", "medium-snow", ["inches", 5]], "night"],
    ],
    "Nevadas ligeras (2 cm.) después esta mañana.": [
        "sentence",
        [
            "during",
            ["parenthetical", "light-snow", ["centimeters", 2]],
            "later-today-morning",
        ],
    ],
    "Fuertes nevadas (8\u201312 in.) durante el día.": [
        "sentence",
        ["for-day", ["parenthetical", "heavy-snow", ["inches", ["range", 8, 12]]]],
    ],
    "Nevadas (bajo 1 cm.) por la tarde.": [
        "sentence",
        [
            "during",
            ["parenthetical", "medium-snow", ["less-than", ["centimeters", 1]]],
            "afternoon",
        ],
    ],
    "Sin precipitaciones durante la semana, con temperaturas alcanzando un máximo de 85\u00b0F mañana.": [
        "sentence",
        [
            "with",
            ["for-week", "no-precipitation"],
            ["temperatures-peaking", ["fahrenheit", 85], "tomorrow"],
        ],
    ],
    "Precipitación mixta sobre el fin de semana, con temperaturas llegando a 32\u00b0C el Jueves.": [
        "sentence",
        [
            "with",
            ["over-weekend", "mixed-precipitation"],
            ["temperatures-rising", ["celsius", 32], "thursday"],
        ],
    ],
    "Llovizna el Lunes, con temperaturas alcanzando un mínimo de 15\u00b0F el Viernes.": [
        "sentence",
        [
            "with",
            ["during", "very-light-rain", "monday"],
            ["temperatures-valleying", ["fahrenheit", 15], "friday"],
        ],
    ],
    "Nevadas ligeras el Martes y Miércoles, con temperaturas cayendo a 0\u00b0C el Domingo.": [
        "sentence",
        [
            "with",
            ["during", "light-snow", ["and", "tuesday", "wednesday"]],
            ["temperatures-falling", ["celsius", 0], "sunday"],
        ],
    ],
    "Precipitación hoy hasta el Sábado, con temperaturas alcanzando un máximo de 100\u00b0F el Lunes.": [
        "sentence",
        [
            "with",
            ["during", "medium-precipitation", ["through", "today", "saturday"]],
            ["temperatures-peaking", ["fahrenheit", 100], "monday"],
        ],
    ],
    "Tormentas posibles hasta el próximo Miércoles.": [
        "sentence",
        ["until", "possible-thunderstorm", "next-wednesday"],
    ],
}
