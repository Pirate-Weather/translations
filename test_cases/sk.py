# This would be one of your translations, as a Python dictionary
cases = {
    "Jasno": ["title", "clear"],
    "Možnosť veľmi slabých zrážok": ["title", "possible-very-light-precipitation"],
    "Slabé zrážky": ["title", "very-light-precipitation"],
    "Možnosť slabých zrážok": ["title", "possible-light-precipitation"],
    "Slabé zrážky": ["title", "light-precipitation"],
    "Zrážky": ["title", "medium-precipitation"],
    "Silné zrážky": ["title", "heavy-precipitation"],
    "Možnosť mrholenia": ["title", "possible-very-light-rain"],
    "Mrholenie": ["title", "very-light-rain"],
    "Možnosť slabého dažďa": ["title", "possible-light-rain"],
    "Slabý dážď": ["title", "light-rain"],
    "Dážď": ["title", "medium-rain"],
    "Vydatný dážď": ["title", "heavy-rain"],
    "Možnosť slabého dažďa so snehom": ["title", "possible-very-light-sleet"],
    "Slabý dážď so snehom": ["title", "very-light-sleet"],
    "Možnosť slabého dažďa so snehom": ["title", "possible-light-sleet"],
    "Slabý dážď so snehom": ["title", "light-sleet"],
    "Dážď so snehom": ["title", "medium-sleet"],
    "Vydatný dážď so snehom": ["title", "heavy-sleet"],
    "Možnosť slabého sneženia": ["title", "possible-very-light-snow"],
    "Slabé sneženie": ["title", "very-light-snow"],
    "Možnosť slabého sneženia": ["title", "possible-light-snow"],
    "Slabé sneženie": ["title", "light-snow"],
    "Sneženie": ["title", "medium-snow"],
    "Vydatné sneženie": ["title", "heavy-snow"],
    "Veterno": ["title", "medium-wind"],
    "Silný vietor": ["title", "heavy-wind"],
    "Hmlisto": ["title", "fog"],
    "Prevažne jasno": ["title", "very-light-clouds"],
    "Čiastočne zamračené": ["title", "light-clouds"],
    "Prevažne zamračené": ["title", "medium-clouds"],
    "Zamračené": ["title", "heavy-clouds"],
    "Nízka vlhkosť a slabý vietor": ["title", ["and", "low-humidity", "light-wind"]],
    "Mrholenie a silný vietor": ["title", ["and", "very-light-rain", "heavy-wind"]],
    "Vysoká vlhkosť a čiastočne zamračené": [
        "title",
        ["and", "high-humidity", "light-clouds"],
    ],
    "Jasno hodinu.": ["sentence", ["for-hour", "clear"]],
    "Slabé sneženie o 35 min.": [
        "sentence",
        ["starting-in", "very-light-snow", ["minutes", 35]],
    ],
    "Slabý dážď skončí o 15 min.": [
        "sentence",
        ["stopping-in", "light-rain", ["minutes", 15]],
    ],
    "Vydatný dážď so snehom o 20 min., skončí o 30 min. neskôr.": [
        "sentence",
        [
            "starting-then-stopping-later",
            "heavy-sleet",
            ["minutes", 20],
            ["minutes", 30],
        ],
    ],
    "Dážď skončí o 25 min. a začne znovu o 8 min. neskôr.": [
        "sentence",
        [
            "stopping-then-starting-later",
            "medium-rain",
            ["minutes", 25],
            ["minutes", 8],
        ],
    ],
    "Počas dňa prevažne zamračené.": ["sentence", ["for-day", "medium-clouds"]],
    "Od rána slabý dážď so snehom.": [
        "sentence",
        ["starting", "very-light-sleet", "morning"],
    ],
    "Veterno až do dnešnej noci.": [
        "sentence",
        ["until", "medium-wind", "today-night"],
    ],
    "Silné zrážky až do popoludnia.": [
        "sentence",
        ["until", "heavy-precipitation", "afternoon"],
    ],
    "Popoludní slabý vietor.": ["sentence", ["during", "light-wind", "afternoon"]],
    "Dnes neskoro večer a zajtra ráno sneženie.": [
        "sentence",
        ["during", "medium-snow", ["and", "later-today-evening", "tomorrow-morning"]],
    ],
    "Vydatný dážď až do dnešného dopoludnia, ktorý začne znovu dnes večer.": [
        "sentence",
        ["until-starting-again", "heavy-rain", "later-today-morning", "today-evening"],
    ],
    "Od dnešnej neskorej noci zamračené a zajtra popoludní vydatné sneženie.": [
        "sentence",
        ["starting-continuing-until", "heavy-clouds", "evening", "night"],
    ],
    "Od popoludnia čiastočne zamračené a pretrvá až do večera.": [
        "sentence",
        ["starting-continuing-until", "light-clouds", "afternoon", "evening"],
    ],
    "Dnes podvečer slabý dážď so snehom a zajtra ráno hmlisto.": [
        "sentence",
        [
            "and",
            ["during", "light-sleet", "later-today-afternoon"],
            ["during", "fog", "tomorrow-morning"],
        ],
    ],
    "Od dnešného rána silný vietor, ktorý pretrvá až do dnešného popoludnia a zajtra ráno dážď so snehom.": [
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
    "Od dnešnej neskorej noci zamračené a zajtra popoludní vydatné sneženie.": [
        "sentence",
        [
            "and",
            ["starting", "heavy-clouds", "later-today-night"],
            ["during", "heavy-snow", "tomorrow-afternoon"],
        ],
    ],
    "Dnes v noci nízka vlhkosť a od zajtrajšieho večera slabé zrážky, ktoré pretrvajú až do zajtrajšej noci.": [
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
    "V noci sneženie (5 in).": [
        "sentence",
        ["during", ["parenthetical", "medium-snow", ["inches", 5]], "night"],
    ],
    "Dnes dopoludnia slabé sneženie (2 cm).": [
        "sentence",
        [
            "during",
            ["parenthetical", "light-snow", ["centimeters", 2]],
            "later-today-morning",
        ],
    ],
    "Počas dňa vydatné sneženie (8-12 in).": [
        "sentence",
        ["for-day", ["parenthetical", "heavy-snow", ["inches", ["range", 8, 12]]]],
    ],
    "Popoludní sneženie (menej ako 1 cm).": [
        "sentence",
        [
            "during",
            ["parenthetical", "medium-snow", ["less-than", ["centimeters", 1]]],
            "afternoon",
        ],
    ],
    "Bez zrážok počas týždňa, zajtra s teplotným maximom 85°F.": [
        "sentence",
        [
            "with",
            ["for-week", "no-precipitation"],
            ["temperatures-peaking", ["fahrenheit", 85], "tomorrow"],
        ],
    ],
    "Zmiešané zrážky cez víkend, vo štvrtok s teplotami stúpajúcimi k 32°C.": [
        "sentence",
        [
            "with",
            ["over-weekend", "mixed-precipitation"],
            ["temperatures-rising", ["celsius", 32], "thursday"],
        ],
    ],
    "V pondelok mrholenie, v piatok s teplotným minimom 15°F.": [
        "sentence",
        [
            "with",
            ["during", "very-light-rain", "monday"],
            ["temperatures-valleying", ["fahrenheit", 15], "friday"],
        ],
    ],
    "V utorok a budúcu stredu slabé sneženie, v nedeľu s teplotami klesajúcimi k 0°C.": [
        "sentence",
        [
            "with",
            ["during", "light-snow", ["and", "tuesday", "next-wednesday"]],
            ["temperatures-falling", ["celsius", 0], "sunday"],
        ],
    ],
    "Od dnes do soboty zrážky, v pondelok s teplotným maximom 100°F.": [
        "sentence",
        [
            "with",
            ["during", "medium-precipitation", ["through", "today", "saturday"]],
            ["temperatures-peaking", ["fahrenheit", 100], "monday"],
        ],
    ],
    "Počas dňa zmiešané zrážky (1-3 in snehu).": [
        "sentence",
        [
            "for-day",
            ["parenthetical", "mixed-precipitation", ["inches", ["range", 1, 3]]],
        ],
    ],
    "Vydatné sneženie (1-3 in)": [
        "title",
        ["parenthetical", "heavy-snow", ["inches", ["range", 1, 3]]],
    ],
    "Vydatné sneženie (3-5 cm)": [
        "title",
        ["parenthetical", "heavy-snow", ["centimeters", ["range", 3, 5]]],
    ],
    "Možnosť búrok": ["title", "possible-thunderstorm"],
    "Vydatný dážď a búrky": ["title", ["and", "heavy-rain", "thunderstorm"]],
    "Búrky až do budúceho pondelka.": [
        "sentence",
        ["until", "thunderstorm", "next-monday"],
    ],
    "Predpoveď na ďalšiu hodinu je dočasne nedostupná, pretože všetky radarové stanice v okolí sú v režime offline.": [
        "sentence",
        ["next-hour-forecast-status", "temporarily-unavailable", "station-offline"],
    ],
    "Predpoveď na ďalšiu hodinu je čiastočne nedostupná, pretože vznikli medzery v pokrytí radarovými stanicami v okolí.": [
        "sentence",
        ["next-hour-forecast-status", "partially-unavailable", "station-incomplete"],
    ],
    "Predpoveď na ďalšiu hodinu je nedostupná, pretože všetky radarové stanice v okolí sú v režime offline.": [
        "sentence",
        ["next-hour-forecast-status", "unavailable", "station-offline"],
    ],
}
