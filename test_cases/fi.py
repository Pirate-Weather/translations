# This would be one of your translations, as a Python dictionary
cases = {
    "Selkeää": ["title", "clear"],
    "Heikon sateen mahdollisuus": ["title", "possible-very-light-precipitation"],
    "Heikkoa sadetta": ["title", "very-light-precipitation"],
    "Sadekuurojen mahdollisuus": ["title", "possible-light-precipitation"],
    "Sadekuuroja": ["title", "light-precipitation"],
    "Sadetta": ["title", "medium-precipitation"],
    "Rankkasadetta": ["title", "heavy-precipitation"],
    "Heikon sateen mahdollisuus": ["title", "possible-very-light-rain"],
    "Heikkoa sadetta": ["title", "very-light-rain"],
    "Sadekuurojen mahdollisuus": ["title", "possible-light-rain"],
    "Sadekuuroja": ["title", "light-rain"],
    "Sadetta": ["title", "medium-rain"],
    "Rankkasadetta": ["title", "heavy-rain"],
    "Heikon räntäsateen mahdollisuus": ["title", "possible-very-light-sleet"],
    "Heikkoa räntäsadetta": ["title", "very-light-sleet"],
    "Räntäkuurojen mahdollisuus": ["title", "possible-light-sleet"],
    "Räntäkuuroja": ["title", "light-sleet"],
    "Räntäsadetta": ["title", "medium-sleet"],
    "Voimakasta räntäsadetta": ["title", "heavy-sleet"],
    "Heikon lumisateen mahdollisuus": ["title", "possible-very-light-snow"],
    "Heikkoa lumisadetta": ["title", "very-light-snow"],
    "Lumikuurojen mahdollisuus": ["title", "possible-light-snow"],
    "Lumikuuroja": ["title", "light-snow"],
    "Lumisadetta": ["title", "medium-snow"],
    "Rankkaa lumisadetta": ["title", "heavy-snow"],
    "Tuulista": ["title", "medium-wind"],
    "Myrskyisää": ["title", "heavy-wind"],
    "Sumua": ["title", "fog"],
    "Enimmäkseen selkeää": ["title", "very-light-clouds"],
    "Puolipilvistä": ["title", "light-clouds"],
    "Enimmäkseen pilvistä": ["title", "medium-clouds"],
    "Pilvistä": ["title", "heavy-clouds"],
    "Kuivaa ja heikkoa tuulta": ["title", ["and", "low-humidity", "light-wind"]],
    "Heikkoa sadetta ja myrskyisää": [
        "title",
        ["and", "very-light-rain", "heavy-wind"],
    ],
    "Kosteaa ja puolipilvistä": ["title", ["and", "high-humidity", "light-clouds"]],
    "Selkeää seuraavan tunnin ajan.": ["sentence", ["for-hour", "clear"]],
    "Heikkoa lumisadetta odotettavissa 35 min. kuluessa.": [
        "sentence",
        ["starting-in", "very-light-snow", ["minutes", 35]],
    ],
    "Sadekuuroja vielä 15 min.": [
        "sentence",
        ["stopping-in", "light-rain", ["minutes", 15]],
    ],
    "Voimakasta räntäsadetta 20 min. kuluessa, päättyen 30 min. myöhemmin.": [
        "sentence",
        [
            "starting-then-stopping-later",
            "heavy-sleet",
            ["minutes", 20],
            ["minutes", 30],
        ],
    ],
    "Sadetta vielä 25 min., alkaen uudestaan 8 min. myöhemmin.": [
        "sentence",
        [
            "stopping-then-starting-later",
            "medium-rain",
            ["minutes", 25],
            ["minutes", 8],
        ],
    ],
    "Enimmäkseen pilvistä päivän aikana.": ["sentence", ["for-day", "medium-clouds"]],
    "Heikkoa räntäsadetta aamusta.": [
        "sentence",
        ["starting", "very-light-sleet", "morning"],
    ],
    "Tuulista yöhön asti.": ["sentence", ["until", "medium-wind", "today-night"]],
    "Rankkasadetta iltapäivään asti.": [
        "sentence",
        ["until", "heavy-precipitation", "afternoon"],
    ],
    "Heikkoa tuulta iltapäivällä.": ["sentence", ["during", "light-wind", "afternoon"]],
    "Lumisadetta myöhemmin illalla ja huomisaamuna.": [
        "sentence",
        ["during", "medium-snow", ["and", "later-today-evening", "tomorrow-morning"]],
    ],
    "Rankkasadetta myöhemmin aamulla, ja jälleen illalla.": [
        "sentence",
        ["until-starting-again", "heavy-rain", "later-today-morning", "today-evening"],
    ],
    "Pilvistä illasta yöhön asti.": [
        "sentence",
        ["starting-continuing-until", "heavy-clouds", "evening", "night"],
    ],
    "Räntäkuuroja myöhemmin iltapäivällä ja sumua huomisaamuna.": [
        "sentence",
        [
            "and",
            ["during", "light-sleet", "later-today-afternoon"],
            ["during", "fog", "tomorrow-morning"],
        ],
    ],
    "Myrskyisää aamusta iltapäivään asti ja räntäsadetta huomisaamuna.": [
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
    "Pilvistä myöhemmästä yöstä alkaen ja rankkaa lumisadetta huomenna iltapäivällä.": [
        "sentence",
        [
            "and",
            ["starting", "heavy-clouds", "later-today-night"],
            ["during", "heavy-snow", "tomorrow-afternoon"],
        ],
    ],
    "Kuivaa yöllä ja sadekuuroja huomisesta illasta huomiseen yöhön asti.": [
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
    "Lumisadetta (5 tuumaa) yöllä.": [
        "sentence",
        ["during", ["parenthetical", "medium-snow", ["inches", 5]], "night"],
    ],
    "Lumikuuroja (2 cm) myöhemmin aamulla.": [
        "sentence",
        [
            "during",
            ["parenthetical", "light-snow", ["centimeters", 2]],
            "later-today-morning",
        ],
    ],
    "Rankkaa lumisadetta (8\u201312 tuumaa) päivän aikana.": [
        "sentence",
        ["for-day", ["parenthetical", "heavy-snow", ["inches", ["range", 8, 12]]]],
    ],
    "Lumisadetta (alle 1 cm) iltapäivällä.": [
        "sentence",
        [
            "during",
            ["parenthetical", "medium-snow", ["less-than", ["centimeters", 1]]],
            "afternoon",
        ],
    ],
    "Poutaa viikon ajan, lämpötilan noustessa lukemaan 85°F huomenna.": [
        "sentence",
        [
            "with",
            ["for-week", "no-precipitation"],
            ["temperatures-peaking", ["fahrenheit", 85], "tomorrow"],
        ],
    ],
    "Räntäsadetta viikonloppuna, lämpötilan noustessa lukemaan 32°C torstaina.": [
        "sentence",
        [
            "with",
            ["over-weekend", "mixed-precipitation"],
            ["temperatures-rising", ["celsius", 32], "thursday"],
        ],
    ],
    "Heikkoa sadetta maanantaina, lämpötilan käydessä lukemassa 15\u00b0F perjantaina.": [
        "sentence",
        [
            "with",
            ["during", "very-light-rain", "monday"],
            ["temperatures-valleying", ["fahrenheit", 15], "friday"],
        ],
    ],
    "Lumikuuroja tiistaina ja keskiviikkona, lämpötilan laskiessa lukemaan 0°C sunnuntaina.": [
        "sentence",
        [
            "with",
            ["during", "light-snow", ["and", "tuesday", "wednesday"]],
            ["temperatures-falling", ["celsius", 0], "sunday"],
        ],
    ],
    "Sadetta lauantaihin asti, lämpötilan noustessa lukemaan 100°F maanantaina.": [
        "sentence",
        [
            "with",
            ["during", "medium-precipitation", ["through", "today", "saturday"]],
            ["temperatures-peaking", ["fahrenheit", 100], "monday"],
        ],
    ],
    "Räntäsadetta (1\u20133 tuumaa) päivän aikana.": [
        "sentence",
        [
            "for-day",
            ["parenthetical", "mixed-precipitation", ["inches", ["range", 1, 3]]],
        ],
    ],
    "Rankkaa lumisadetta (1\u20133 tuumaa)": [
        "title",
        ["parenthetical", "heavy-snow", ["inches", ["range", 1, 3]]],
    ],
    "Rankkaa lumisadetta (3\u20135 cm)": [
        "title",
        ["parenthetical", "heavy-snow", ["centimeters", ["range", 3, 5]]],
    ],
}
