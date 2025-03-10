# This would be one of your translations, as a Python dictionary
cases = {
    "Jasno": ["title", "clear"],
    "Možnost velmi slabých srážek": ["title", "possible-very-light-precipitation"],
    "Slabé srážky": ["title", "very-light-precipitation"],
    "Možnost slabých srážek": ["title", "possible-light-precipitation"],
    "Slabé srážky": ["title", "light-precipitation"],
    "Srážky": ["title", "medium-precipitation"],
    "Silné srážky": ["title", "heavy-precipitation"],
    "Možnost mrholení": ["title", "possible-very-light-rain"],
    "Mrholení": ["title", "very-light-rain"],
    "Možnost slabého deště": ["title", "possible-light-rain"],
    "Slabý déšť": ["title", "light-rain"],
    "Déšť": ["title", "medium-rain"],
    "Vydatný déšť": ["title", "heavy-rain"],
    "Možnost slabého deště se sněhem": ["title", "possible-very-light-sleet"],
    "Slabý déšť se sněhem": ["title", "very-light-sleet"],
    "Možnost slabého deště se sněhem": ["title", "possible-light-sleet"],
    "Slabý déšť se sněhem": ["title", "light-sleet"],
    "Déšť se sněhem": ["title", "medium-sleet"],
    "Vydatný déšť se sněhem": ["title", "heavy-sleet"],
    "Možnost slabého sněžení": ["title", "possible-very-light-snow"],
    "Slabé sněžení": ["title", "very-light-snow"],
    "Možnost slabého sněžení": ["title", "possible-light-snow"],
    "Slabé sněžení": ["title", "light-snow"],
    "Sněžení": ["title", "medium-snow"],
    "Vydatné sněžení": ["title", "heavy-snow"],
    "Větrno": ["title", "medium-wind"],
    "Silný vítr": ["title", "heavy-wind"],
    "Mlhavo": ["title", "fog"],
    "Převážně jasno": ["title", "very-light-clouds"],
    "Částečně oblačno": ["title", "light-clouds"],
    "Převážně oblačno": ["title", "medium-clouds"],
    "Zataženo": ["title", "heavy-clouds"],
    "Nízká vlhkost a slabý vítr": ["title", ["and", "low-humidity", "light-wind"]],
    "Mrholení a silný vítr": ["title", ["and", "very-light-rain", "heavy-wind"]],
    "Vysoká vlhkost a částečně oblačno": [
        "title",
        ["and", "high-humidity", "light-clouds"],
    ],
    "Jasno hodinu.": ["sentence", ["for-hour", "clear"]],
    "Slabé sněžení za 35 min.": [
        "sentence",
        ["starting-in", "very-light-snow", ["minutes", 35]],
    ],
    "Slabý déšť skončí za 15 min.": [
        "sentence",
        ["stopping-in", "light-rain", ["minutes", 15]],
    ],
    "Vydatný déšť se sněhem za 20 min., skončí o 30 min. později.": [
        "sentence",
        [
            "starting-then-stopping-later",
            "heavy-sleet",
            ["minutes", 20],
            ["minutes", 30],
        ],
    ],
    "Déšť skončí za 25 min. a začne znovu o 8 min. později.": [
        "sentence",
        [
            "stopping-then-starting-later",
            "medium-rain",
            ["minutes", 25],
            ["minutes", 8],
        ],
    ],
    "Během dne převážně oblačno.": ["sentence", ["for-day", "medium-clouds"]],
    "Od rána slabý déšť se sněhem.": [
        "sentence",
        ["starting", "very-light-sleet", "morning"],
    ],
    "Větrno až do dnešní noci.": ["sentence", ["until", "medium-wind", "today-night"]],
    "Silné srážky až do odpoledne.": [
        "sentence",
        ["until", "heavy-precipitation", "afternoon"],
    ],
    "Odpoledne slabý vítr.": ["sentence", ["during", "light-wind", "afternoon"]],
    "Dnes pozdě večer a zítra ráno sněžení.": [
        "sentence",
        ["during", "medium-snow", ["and", "later-today-evening", "tomorrow-morning"]],
    ],
    "Vydatný déšť až do dnešního dopoledne, který začne znovu dnes večer.": [
        "sentence",
        ["until-starting-again", "heavy-rain", "later-today-morning", "today-evening"],
    ],
    "Od dnešní pozdní noci zataženo a zítra odpoledne vydatné sněžení.": [
        "sentence",
        ["starting-continuing-until", "heavy-clouds", "evening", "night"],
    ],
    "Od odpoledne částečně oblačno a přetrvá až do večera.": [
        "sentence",
        ["starting-continuing-until", "light-clouds", "afternoon", "evening"],
    ],
    "Dnes podvečer slabý déšť se sněhem a zítra ráno mlhavo.": [
        "sentence",
        [
            "and",
            ["during", "light-sleet", "later-today-afternoon"],
            ["during", "fog", "tomorrow-morning"],
        ],
    ],
    "Od dnešního rána silný vítr, který přetrvá až do dnešního odpoledne a zítra ráno déšť se sněhem.": [
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
    "Od dnešní pozdní noci zataženo a zítra odpoledne vydatné sněžení.": [
        "sentence",
        [
            "and",
            ["starting", "heavy-clouds", "later-today-night"],
            ["during", "heavy-snow", "tomorrow-afternoon"],
        ],
    ],
    "Dnes v noci nízká vlhkost a od zítřejšího večera slabé srážky, které přetrvají až do zítřejší noci.": [
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
    "V noci sněžení (5 in).": [
        "sentence",
        ["during", ["parenthetical", "medium-snow", ["inches", 5]], "night"],
    ],
    "Dnes dopoledne slabé sněžení (2 cm).": [
        "sentence",
        [
            "during",
            ["parenthetical", "light-snow", ["centimeters", 2]],
            "later-today-morning",
        ],
    ],
    "Během dne vydatné sněžení (8-12 in).": [
        "sentence",
        ["for-day", ["parenthetical", "heavy-snow", ["inches", ["range", 8, 12]]]],
    ],
    "Odpoledne sněžení (méně než 1 cm).": [
        "sentence",
        [
            "during",
            ["parenthetical", "medium-snow", ["less-than", ["centimeters", 1]]],
            "afternoon",
        ],
    ],
    "Bez srážek během týdne, zítra s teplotním maximem 85°F.": [
        "sentence",
        [
            "with",
            ["for-week", "no-precipitation"],
            ["temperatures-peaking", ["fahrenheit", 85], "tomorrow"],
        ],
    ],
    "Smíšené srážky přes víkend, ve čtvrtek s teplotami stoupajícími k 32°C.": [
        "sentence",
        [
            "with",
            ["over-weekend", "mixed-precipitation"],
            ["temperatures-rising", ["celsius", 32], "thursday"],
        ],
    ],
    "V pondělí mrholení, v pátek s teplotním minimem 15°F.": [
        "sentence",
        [
            "with",
            ["during", "very-light-rain", "monday"],
            ["temperatures-valleying", ["fahrenheit", 15], "friday"],
        ],
    ],
    "V úterý a ve středu slabé sněžení, v neděli s teplotami klesajícími k 0°C.": [
        "sentence",
        [
            "with",
            ["during", "light-snow", ["and", "tuesday", "wednesday"]],
            ["temperatures-falling", ["celsius", 0], "sunday"],
        ],
    ],
    "Od dnes do soboty srážky, v pondělí s teplotním maximem 100°F.": [
        "sentence",
        [
            "with",
            ["during", "medium-precipitation", ["through", "today", "saturday"]],
            ["temperatures-peaking", ["fahrenheit", 100], "monday"],
        ],
    ],
    "Během dne smíšené srážky (1-3 in sněhu).": [
        "sentence",
        [
            "for-day",
            ["parenthetical", "mixed-precipitation", ["inches", ["range", 1, 3]]],
        ],
    ],
    "Vydatné sněžení (1-3 in)": [
        "title",
        ["parenthetical", "heavy-snow", ["inches", ["range", 1, 3]]],
    ],
    "Vydatné sněžení (3-5 cm)": [
        "title",
        ["parenthetical", "heavy-snow", ["centimeters", ["range", 3, 5]]],
    ],
    "V úterý a příští středu slabé sněžení, v neděli s teplotami klesajícími k 0°C.": [
        "sentence",
        [
            "with",
            ["during", "light-snow", ["and", "tuesday", "next-wednesday"]],
            ["temperatures-falling", ["celsius", 0], "sunday"],
        ],
    ],
    "Možnost bouřek": ["title", "possible-thunderstorm"],
    "Vydatný déšť a bouřky": ["title", ["and", "heavy-rain", "thunderstorm"]],
}
