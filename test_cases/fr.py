# This would be one of your translations, as a Python dictionary
cases = {
    "Ciel Dégagé": ["title", "clear"],
    "Très Faibles Précipitations Possibles": [
        "title",
        "possible-very-light-precipitation",
    ],
    "Très Faibles Précipitations": ["title", "very-light-precipitation"],
    "Faibles Précipitations Possibles": ["title", "possible-light-precipitation"],
    "Faibles Précipitations": ["title", "light-precipitation"],
    "Précipitations": ["title", "medium-precipitation"],
    "Fortes Précipitations": ["title", "heavy-precipitation"],
    "Bruine Possible": ["title", "possible-very-light-rain"],
    "Bruine": ["title", "very-light-rain"],
    "Pluie Faible Possible": ["title", "possible-light-rain"],
    "Pluie Faible": ["title", "light-rain"],
    "Pluie": ["title", "medium-rain"],
    "Pluie Forte": ["title", "heavy-rain"],
    "Très Faible Neige Fondante Possible": ["title", "possible-very-light-sleet"],
    "Très Faible Neige Fondante": ["title", "very-light-sleet"],
    "Faible Neige Fondante Possible": ["title", "possible-light-sleet"],
    "Faible Neige Fondante": ["title", "light-sleet"],
    "Neige Fondante": ["title", "medium-sleet"],
    "Forte Neige Fondante": ["title", "heavy-sleet"],
    "Averses De Neige Possibles": ["title", "possible-very-light-snow"],
    "Averses De Neige": ["title", "very-light-snow"],
    "Neige Faible Possible": ["title", "possible-light-snow"],
    "Neige Faible": ["title", "light-snow"],
    "Neige": ["title", "medium-snow"],
    "Neige Abondante": ["title", "heavy-snow"],
    "Vent Moyen": ["title", "medium-wind"],
    "Vent Fort": ["title", "heavy-wind"],
    "Brumeux": ["title", "fog"],
    "En Grande Partie Clair": ["title", "very-light-clouds"],
    "Faibles Passages Nuageux": ["title", "light-clouds"],
    "Ciel Nuageux": ["title", "medium-clouds"],
    "Ciel Couvert": ["title", "heavy-clouds"],
    "Temps Sec et Vent Faible": ["title", ["and", "low-humidity", "light-wind"]],
    "Bruine et Vent Fort": ["title", ["and", "very-light-rain", "heavy-wind"]],
    "Temps Humide et Faibles Passages Nuageux": [
        "title",
        ["and", "high-humidity", "light-clouds"],
    ],
    "Ciel dégagé pendant la prochaine heure.": ["sentence", ["for-hour", "clear"]],
    "Averses de neige commençant dans 35 min.": [
        "sentence",
        ["starting-in", "very-light-snow", ["minutes", 35]],
    ],
    "Pluie faible se terminant dans 15 min.": [
        "sentence",
        ["stopping-in", "light-rain", ["minutes", 15]],
    ],
    "Forte neige fondante commençant dans 20 min., se terminant 30 min. plus tard.": [
        "sentence",
        [
            "starting-then-stopping-later",
            "heavy-sleet",
            ["minutes", 20],
            ["minutes", 30],
        ],
    ],
    "Pluie se terminant dans 25 min., et reprenant 8 min. plus tard.": [
        "sentence",
        [
            "stopping-then-starting-later",
            "medium-rain",
            ["minutes", 25],
            ["minutes", 8],
        ],
    ],
    "Ciel nuageux toute la journée.": ["sentence", ["for-day", "medium-clouds"]],
    "Très faible neige fondante commençant dans la matinée.": [
        "sentence",
        ["starting", "very-light-sleet", "morning"],
    ],
    "Vent moyen jusqu’à cette nuit.": [
        "sentence",
        ["until", "medium-wind", "today-night"],
    ],
    "Fortes précipitations jusque dans l’après-midi.": [
        "sentence",
        ["until", "heavy-precipitation", "afternoon"],
    ],
    "Vent faible dans l’après-midi.": [
        "sentence",
        ["during", "light-wind", "afternoon"],
    ],
    "Neige dans la soirée et demain matin.": [
        "sentence",
        ["during", "medium-snow", ["and", "later-today-evening", "tomorrow-morning"]],
    ],
    "Pluie forte jusque dans la matinée, reprenant ce soir.": [
        "sentence",
        ["until-starting-again", "heavy-rain", "later-today-morning", "today-evening"],
    ],
    "Ciel couvert commençant dans la soirée, se prolongeant jusque dans la nuit.": [
        "sentence",
        ["starting-continuing-until", "heavy-clouds", "evening", "night"],
    ],
    "Faible neige fondante dans l’après-midi et brumeux demain matin.": [
        "sentence",
        [
            "and",
            ["during", "light-sleet", "later-today-afternoon"],
            ["during", "fog", "tomorrow-morning"],
        ],
    ],
    "Vent fort commençant ce matin, se prolongeant jusqu’à cet après-midi, et neige fondante demain matin.": [
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
    "Ciel se couvrant dans la nuit et neige abondante demain après-midi.": [
        "sentence",
        [
            "and",
            ["starting", "heavy-clouds", "later-today-night"],
            ["during", "heavy-snow", "tomorrow-afternoon"],
        ],
    ],
    "Temps sec cette nuit et faibles précipitations commençant demain soir, se prolongeant jusqu’à demain pendant la nuit.": [
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
    "Neige (5 in.) dans la nuit.": [
        "sentence",
        ["during", ["parenthetical", "medium-snow", ["inches", 5]], "night"],
    ],
    "Neige faible (2 cm.) dans la matinée.": [
        "sentence",
        [
            "during",
            ["parenthetical", "light-snow", ["centimeters", 2]],
            "later-today-morning",
        ],
    ],
    "Neige abondante (8\u201312 in.) toute la journée.": [
        "sentence",
        ["for-day", ["parenthetical", "heavy-snow", ["inches", ["range", 8, 12]]]],
    ],
    "Neige (moins de 1 cm.) dans l’après-midi.": [
        "sentence",
        [
            "during",
            ["parenthetical", "medium-snow", ["less-than", ["centimeters", 1]]],
            "afternoon",
        ],
    ],
    "Pas de précipitations pendant toute la semaine, avec des températures maximales atteignant 85\u00b0F demain.": [
        "sentence",
        [
            "with",
            ["for-week", "no-precipitation"],
            ["temperatures-peaking", ["fahrenheit", 85], "tomorrow"],
        ],
    ],
    "Précipitations mixtes pendant tout le week-end, avec des températures maximales montant jusqu’à 32\u00b0C jeudi.": [
        "sentence",
        [
            "with",
            ["over-weekend", "mixed-precipitation"],
            ["temperatures-rising", ["celsius", 32], "thursday"],
        ],
    ],
    "Bruine aujourd’hui, avec des températures maximales atteignant 15\u00b0F vendredi.": [
        "sentence",
        [
            "with",
            ["during", "very-light-rain", "today"],
            ["temperatures-valleying", ["fahrenheit", 15], "friday"],
        ],
    ],
    "Neige faible lundi et mardi, avec des températures maximales descendant jusqu’à 0\u00b0C dimanche.": [
        "sentence",
        [
            "with",
            ["during", "light-snow", ["and", "monday", "tuesday"]],
            ["temperatures-falling", ["celsius", 0], "sunday"],
        ],
    ],
    "Précipitations mercredi jusqu’à samedi, avec des températures maximales atteignant 100\u00b0F lundi.": [
        "sentence",
        [
            "with",
            ["during", "medium-precipitation", ["through", "wednesday", "saturday"]],
            ["temperatures-peaking", ["fahrenheit", 100], "monday"],
        ],
    ],
    "Orages possibles mercredi prochain et jeudi prochain.": [
        "sentence",
        ["during", "possible-thunderstorm", ["and", "next-wednesday", "next-thursday"]],
    ],
    "Les prévisions pour la prochaine heure sont temporairement indisponibles car les stations radars voisines sont hors-ligne.": [
        "sentence",
        ["next-hour-forecast-status", "temporarily-unavailable", "station-offline"],
    ],
    "Les prévisions pour la prochaine heure sont partiellement indisponibles car il y a des lacunes dans la couverture des stations radars voisines.": [
        "sentence",
        ["next-hour-forecast-status", "partially-unavailable", "station-incomplete"],
    ],
    "Les prévisions pour la prochaine heure sont indisponibles car les stations radars voisines sont hors-ligne.": [
        "sentence",
        ["next-hour-forecast-status", "unavailable", "station-offline"],
    ],
}
