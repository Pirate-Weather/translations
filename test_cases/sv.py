# This would be one of your translations, as a Python dictionary
cases = {
    "Klart": ["title", "clear"],
    "Möjligtvis mycket lätt nederbörd": ["title", "possible-very-light-precipitation"],
    "Mycket lätt nederbörd": ["title", "very-light-precipitation"],
    "Möjligtvis lätt nederbörd": ["title", "possible-light-precipitation"],
    "Lätt nederbörd": ["title", "light-precipitation"],
    "Nederbörd": ["title", "medium-precipitation"],
    "Kraftigt nederbörd": ["title", "heavy-precipitation"],
    "Möjligtvis lite duggregn": ["title", "possible-very-light-rain"],
    "Duggregn": ["title", "very-light-rain"],
    "Möjligtvis lätta regnskurar": ["title", "possible-light-rain"],
    "Regnskurar": ["title", "light-rain"],
    "Regn": ["title", "medium-rain"],
    "Skyfall": ["title", "heavy-rain"],
    "Möjligtvis mycket lätt snöblandat regn": ["title", "possible-very-light-sleet"],
    "Mycket lätt snöblandat regn": ["title", "very-light-sleet"],
    "Möjligtvis lätt snöblandat regn": ["title", "possible-light-sleet"],
    "Lätt snöblandat regn": ["title", "light-sleet"],
    "Snöblandat regn": ["title", "medium-sleet"],
    "Tungt snöblandat regn": ["title", "heavy-sleet"],
    "Möjligtvis lätt snöby": ["title", "possible-very-light-snow"],
    "Lätt snöby": ["title", "very-light-snow"],
    "Möjligtvis lätt snöfall": ["title", "possible-light-snow"],
    "Lätt snöfall": ["title", "light-snow"],
    "Snöby": ["title", "medium-snow"],
    "Rikligt med snö": ["title", "heavy-snow"],
    "Hård vind": ["title", "medium-wind"],
    "Storm": ["title", "heavy-wind"],
    "Dimma": ["title", "fog"],
    "Mestadels klart": ["title", "very-light-clouds"],
    "Lätt molnighet": ["title", "light-clouds"],
    "Molnigt": ["title", "medium-clouds"],
    "Mulet": ["title", "heavy-clouds"],
    "Torka och måttlig vind": ["title", ["and", "low-humidity", "light-wind"]],
    "Duggregn och storm": ["title", ["and", "very-light-rain", "heavy-wind"]],
    "Fuktigt och lätt molnighet": ["title", ["and", "high-humidity", "light-clouds"]],
    "Klart under närmaste timme.": ["sentence", ["for-hour", "clear"]],
    "Lätt snöby som startar om 35 min.": [
        "sentence",
        ["starting-in", "very-light-snow", ["minutes", 35]],
    ],
    "Regnskurar som avtar om 15 min.": [
        "sentence",
        ["stopping-in", "light-rain", ["minutes", 15]],
    ],
    "Tungt snöblandat regn som startar om 20 min., avtar 30 min. senare.": [
        "sentence",
        [
            "starting-then-stopping-later",
            "heavy-sleet",
            ["minutes", 20],
            ["minutes", 30],
        ],
    ],
    "Regn avtar om 25 min., startar igen 8 min. senare.": [
        "sentence",
        [
            "stopping-then-starting-later",
            "medium-rain",
            ["minutes", 25],
            ["minutes", 8],
        ],
    ],
    "Molnigt under dagen.": ["sentence", ["for-day", "medium-clouds"]],
    "Mycket lätt snöblandat regn som startar på morgonen.": [
        "sentence",
        ["starting", "very-light-sleet", "morning"],
    ],
    "Hård vind fram till ikväll.": [
        "sentence",
        ["until", "medium-wind", "today-night"],
    ],
    "Kraftigt nederbörd fram till eftermiddagen.": [
        "sentence",
        ["until", "heavy-precipitation", "afternoon"],
    ],
    "Måttlig vind under eftermiddagen.": [
        "sentence",
        ["during", "light-wind", "afternoon"],
    ],
    "Snöby senare under kvällen och imorgon bitti.": [
        "sentence",
        ["during", "medium-snow", ["and", "later-today-evening", "tomorrow-morning"]],
    ],
    "Skyfall fram till senare under morgonen, som startar igen under kvällen.": [
        "sentence",
        ["until-starting-again", "heavy-rain", "later-today-morning", "today-evening"],
    ],
    "Mulet som startar under kvällen, fortsätter fram till natten.": [
        "sentence",
        ["starting-continuing-until", "heavy-clouds", "evening", "night"],
    ],
    "Lätt snöblandat regn senare under eftermiddagen och dimma imorgon bitti.": [
        "sentence",
        [
            "and",
            ["during", "light-sleet", "later-today-afternoon"],
            ["during", "fog", "tomorrow-morning"],
        ],
    ],
    "Storm som startar under morgonen, fortsätter fram till på eftermiddagen och snöblandat regn imorgon bitti.": [
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
    "Mulet som startar senare ikväll och rikligt med snö imorgon eftermiddag.": [
        "sentence",
        [
            "and",
            ["starting", "heavy-clouds", "later-today-night"],
            ["during", "heavy-snow", "tomorrow-afternoon"],
        ],
    ],
    "Torka ikväll och lätt nederbörd som startar imorgon kväll, fortsätter fram till imorgon natt.": [
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
    "Snöby (5 in.) över natten.": [
        "sentence",
        ["during", ["parenthetical", "medium-snow", ["inches", 5]], "night"],
    ],
    "Lätt snöfall (2 cm.) senare under morgonen.": [
        "sentence",
        [
            "during",
            ["parenthetical", "light-snow", ["centimeters", 2]],
            "later-today-morning",
        ],
    ],
    "Rikligt med snö (8\u201312 in.) under dagen.": [
        "sentence",
        ["for-day", ["parenthetical", "heavy-snow", ["inches", ["range", 8, 12]]]],
    ],
    "Snöby (under 1 cm.) under eftermiddagen.": [
        "sentence",
        [
            "during",
            ["parenthetical", "medium-snow", ["less-than", ["centimeters", 1]]],
            "afternoon",
        ],
    ],
    "Ingen mätbar nederbörd under veckan, med temperaturer upp till 85\u00b0F imorgon.": [
        "sentence",
        [
            "with",
            ["for-week", "no-precipitation"],
            ["temperatures-peaking", ["fahrenheit", 85], "tomorrow"],
        ],
    ],
    "Blandad nederbörd över helgen, med temperaturer som stiger till 32\u00b0C under torsdagen.": [
        "sentence",
        [
            "with",
            ["over-weekend", "mixed-precipitation"],
            ["temperatures-rising", ["celsius", 32], "thursday"],
        ],
    ],
    "Duggregn på måndag, med temperaturer som stannar på 15\u00b0F under fredagen.": [
        "sentence",
        [
            "with",
            ["during", "very-light-rain", "monday"],
            ["temperatures-valleying", ["fahrenheit", 15], "friday"],
        ],
    ],
    "Lätt snöfall på tisdag och onsdag, med temperaturer som sjunker till 0\u00b0C under söndagen.": [
        "sentence",
        [
            "with",
            ["during", "light-snow", ["and", "tuesday", "wednesday"]],
            ["temperatures-falling", ["celsius", 0], "sunday"],
        ],
    ],
    "Lätt snöfall på tisdag och nästa onsdag, med temperaturer som sjunker till 0\u00b0C under söndagen.": [
        "sentence",
        [
            "with",
            ["during", "light-snow", ["and", "tuesday", "next-wednesday"]],
            ["temperatures-falling", ["celsius", 0], "sunday"],
        ],
    ],
    "Nederbörd idag fram till på lördag, med temperaturer upp till 100\u00b0F under måndagen.": [
        "sentence",
        [
            "with",
            ["during", "medium-precipitation", ["through", "today", "saturday"]],
            ["temperatures-peaking", ["fahrenheit", 100], "monday"],
        ],
    ],
    "Risk för åska": ["title", "possible-thunderstorm"],
    "Skyfall och åska": ["title", ["and", "heavy-rain", "thunderstorm"]],
    "Rök": ["title", "smoke"],
    "Rök under dagen.": ["sentence", ["for-day", "smoke"]],
    "Rök på morgonen.": ["sentence", ["during", "smoke", "morning"]],
    "Rök fram till kvällen.": ["sentence", ["until", "smoke", "today-evening"]],
    "Rök och lätt molnighet": ["title", ["and", "smoke", "light-clouds"]],
    "Dis": ["title", "haze"],
    "Dis under dagen.": ["sentence", ["for-day", "haze"]],
    "Dis under eftermiddagen.": ["sentence", ["during", "haze", "afternoon"]],
    "Dis och fuktigt": ["title", ["and", "haze", "high-humidity"]],
    "Dimma under dagen.": ["sentence", ["for-day", "mist"]],
    "Dimma över natten.": ["sentence", ["during", "mist", "night"]],
    "Dimma och mulet": ["title", ["and", "mist", "heavy-clouds"]],
}
