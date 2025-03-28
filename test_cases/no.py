# This would be one of your translations, as a Python dictionary
cases = {
    "Klart": ["title", "clear"],
    "Sjanse for veldig lett nedbør": ["title", "possible-very-light-precipitation"],
    "Veldig lett nedbør": ["title", "very-light-precipitation"],
    "Sjanse for lett nedbør": ["title", "possible-light-precipitation"],
    "Lett nedbør": ["title", "light-precipitation"],
    "Nedbør": ["title", "medium-precipitation"],
    "Kraftig regn": ["title", "heavy-precipitation"],
    "Sjanse for lett duskregn": ["title", "possible-very-light-rain"],
    "Duskregn": ["title", "very-light-rain"],
    "Sjanse for lette regnbyger": ["title", "possible-light-rain"],
    "Regnbyger": ["title", "light-rain"],
    "Regn": ["title", "medium-rain"],
    "Kraftige regnbyger": ["title", "heavy-rain"],
    "Sjanse for veldig lett sludd": ["title", "possible-very-light-sleet"],
    "Veldig lett sludd": ["title", "very-light-sleet"],
    "Sjanse for lett sludd": ["title", "possible-light-sleet"],
    "Lett sludd": ["title", "light-sleet"],
    "Sludd": ["title", "medium-sleet"],
    "Kraftig sludd": ["title", "heavy-sleet"],
    "Sjanse for vedlig lett snø": ["title", "possible-very-light-snow"],
    "Veldig lett snø": ["title", "very-light-snow"],
    "Sjanse for lett snø": ["title", "possible-light-snow"],
    "Lett snø": ["title", "light-snow"],
    "Snø": ["title", "medium-snow"],
    "Rikelig med snø": ["title", "heavy-snow"],
    "Sterk vind": ["title", "medium-wind"],
    "Storm": ["title", "heavy-wind"],
    "Tåke": ["title", "fog"],
    "Stort sett klart": ["title", "very-light-clouds"],
    "Lettskyet": ["title", "light-clouds"],
    "Skyet": ["title", "medium-clouds"],
    "Overskyet": ["title", "heavy-clouds"],
    "Tørke og lett vind": ["title", ["and", "low-humidity", "light-wind"]],
    "Duskregn og storm": ["title", ["and", "very-light-rain", "heavy-wind"]],
    "Fuktig og lettskyet": ["title", ["and", "high-humidity", "light-clouds"]],
    "Klart i løpet av de neste timene.": ["sentence", ["for-hour", "clear"]],
    "Veldig lett snø som starter om 35 min.": [
        "sentence",
        ["starting-in", "very-light-snow", ["minutes", 35]],
    ],
    "Regnbyger som avtar om 15 min.": [
        "sentence",
        ["stopping-in", "light-rain", ["minutes", 15]],
    ],
    "Kraftig sludd som starter om 20 min., avtar 30 min. senere.": [
        "sentence",
        [
            "starting-then-stopping-later",
            "heavy-sleet",
            ["minutes", 20],
            ["minutes", 30],
        ],
    ],
    "Regn avtar om 25 min., starter igjen 8 min. senere.": [
        "sentence",
        [
            "stopping-then-starting-later",
            "medium-rain",
            ["minutes", 25],
            ["minutes", 8],
        ],
    ],
    "Skyet i løpet av dagen.": ["sentence", ["for-day", "medium-clouds"]],
    "Veldig lett sludd som starter om morgenen.": [
        "sentence",
        ["starting", "very-light-sleet", "morning"],
    ],
    "Sterk vind fram til i kveld.": [
        "sentence",
        ["until", "medium-wind", "today-night"],
    ],
    "Kraftig regn fram til på ettermiddagen.": [
        "sentence",
        ["until", "heavy-precipitation", "afternoon"],
    ],
    "Lett vind på ettermiddagen.": ["sentence", ["during", "light-wind", "afternoon"]],
    "Snø senere på kvelden og i morgen tidlig.": [
        "sentence",
        ["during", "medium-snow", ["and", "later-today-evening", "tomorrow-morning"]],
    ],
    "Kraftige regnbyger fram til senere på morgenen, som starter igjen i løpet av kvelden.": [
        "sentence",
        ["until-starting-again", "heavy-rain", "later-today-morning", "today-evening"],
    ],
    "Overskyet som starter om kvelden, fortsetter fram til om natten.": [
        "sentence",
        ["starting-continuing-until", "heavy-clouds", "evening", "night"],
    ],
    "Lett sludd senere på ettermiddagen og tåke i morgen tidlig.": [
        "sentence",
        [
            "and",
            ["during", "light-sleet", "later-today-afternoon"],
            ["during", "fog", "tomorrow-morning"],
        ],
    ],
    "Storm som starter i løpet av formiddagen, fortsetter fram til på ettermiddagen og sludd i morgen tidlig.": [
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
    "Overskyet som starter senere i kveld og rikelig med snø i morgen ettermiddag.": [
        "sentence",
        [
            "and",
            ["starting", "heavy-clouds", "later-today-night"],
            ["during", "heavy-snow", "tomorrow-afternoon"],
        ],
    ],
    "Tørke i kveld og lett nedbør som starter i morgen kveld, fortsetter fram til i morgen natt.": [
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
    "Snø (5 in.) om natten.": [
        "sentence",
        ["during", ["parenthetical", "medium-snow", ["inches", 5]], "night"],
    ],
    "Lett snø (2 cm.) senere på morgenen.": [
        "sentence",
        [
            "during",
            ["parenthetical", "light-snow", ["centimeters", 2]],
            "later-today-morning",
        ],
    ],
    "Rikelig med snø (8\u201312 in.) i løpet av dagen.": [
        "sentence",
        ["for-day", ["parenthetical", "heavy-snow", ["inches", ["range", 8, 12]]]],
    ],
    "Snø (under 1 cm.) på ettermiddagen.": [
        "sentence",
        [
            "during",
            ["parenthetical", "medium-snow", ["less-than", ["centimeters", 1]]],
            "afternoon",
        ],
    ],
    "Ingen målbar nedbør i løpet av uken, med temperaturer opptil 85\u00b0F i morgen.": [
        "sentence",
        [
            "with",
            ["for-week", "no-precipitation"],
            ["temperatures-peaking", ["fahrenheit", 85], "tomorrow"],
        ],
    ],
    "Blandet nedbør over helgen, med temperaturer som stiger til 32\u00b0C på torsdag.": [
        "sentence",
        [
            "with",
            ["over-weekend", "mixed-precipitation"],
            ["temperatures-rising", ["celsius", 32], "thursday"],
        ],
    ],
    "Duskregn på mandag, med temperaturer som stopper på 15\u00b0F på fredag.": [
        "sentence",
        [
            "with",
            ["during", "very-light-rain", "monday"],
            ["temperatures-valleying", ["fahrenheit", 15], "friday"],
        ],
    ],
    "Lett snø på tirsdag og onsdag, med temperaturer som synker til 0\u00b0C på søndag.": [
        "sentence",
        [
            "with",
            ["during", "light-snow", ["and", "tuesday", "wednesday"]],
            ["temperatures-falling", ["celsius", 0], "sunday"],
        ],
    ],
    "Nedbør i dag fram til på lørdag, med temperaturer opptil 100\u00b0F på mandag.": [
        "sentence",
        [
            "with",
            ["during", "medium-precipitation", ["through", "today", "saturday"]],
            ["temperatures-peaking", ["fahrenheit", 100], "monday"],
        ],
    ],
    "Lett snø på tirsdag og neste onsdag, med temperaturer som synker til 0\u00b0C på søndag.": [
        "sentence",
        [
            "with",
            ["during", "light-snow", ["and", "tuesday", "next-wednesday"]],
            ["temperatures-falling", ["celsius", 0], "sunday"],
        ],
    ],
    "Tordenvær kan forekomme": ["title", "possible-thunderstorm"],
    "Kraftige regnbyger og tordenvær": ["title", ["and", "heavy-rain", "thunderstorm"]],
    "Værvarsel for neste time er midertidlig ikke tilgjengelig på grunn av ingen kontakt med radarstasjoner i nærheten.": [
        "sentence",
        ["next-hour-forecast-status", "temporarily-unavailable", "station-offline"],
    ],
    "Værvarsel for neste time er delvis ikke tilgjengelig på grunn av hull i dekningen fra radarstasjoner i nærheten.": [
        "sentence",
        ["next-hour-forecast-status", "partially-unavailable", "station-incomplete"],
    ],
    "Værvarsel for neste time er ikke tilgjengelig på grunn av ingen kontakt med radarstasjoner i nærheten.": [
        "sentence",
        ["next-hour-forecast-status", "unavailable", "station-offline"],
    ],
}
