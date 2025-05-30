# This would be one of your translations, as a Python dictionary
cases = {
    "Klara Ĉielo": ["title", "clear"],
    "Malforta Precipitaĵo Eblas": ["title", "possible-very-light-precipitation"],
    "Malforta Precipitaĵo": ["title", "very-light-precipitation"],
    "Malforta Precipitaĵo Eblas": ["title", "possible-light-precipitation"],
    "Malforta Precipitaĵo": ["title", "light-precipitation"],
    "Precipitaĵo": ["title", "medium-precipitation"],
    "Forta Precipitaĵo": ["title", "heavy-precipitation"],
    "Drizlo Eblas": ["title", "possible-very-light-rain"],
    "Drizlo": ["title", "very-light-rain"],
    "Malforta Pluvo Eblas": ["title", "possible-light-rain"],
    "Malforta Pluvo": ["title", "light-rain"],
    "Pluvo": ["title", "medium-rain"],
    "Forta Pluvo": ["title", "heavy-rain"],
    "Malforta Glaciumo Eblas": ["title", "possible-very-light-sleet"],
    "Malforta Glaciumo": ["title", "very-light-sleet"],
    "Malforta Glaciumo Eblas": ["title", "possible-light-sleet"],
    "Malforta Glaciumo": ["title", "light-sleet"],
    "Glaciumo": ["title", "medium-sleet"],
    "Forta Glaciumo": ["title", "heavy-sleet"],
    "Malforta Neĝo Eblas": ["title", "possible-very-light-snow"],
    "Malforta Neĝo": ["title", "very-light-snow"],
    "Malforta Neĝo Eblas": ["title", "possible-light-snow"],
    "Malforta Neĝo": ["title", "light-snow"],
    "Neĝo": ["title", "medium-snow"],
    "Forta Neĝo": ["title", "heavy-snow"],
    "Vento": ["title", "medium-wind"],
    "Forta Vento": ["title", "heavy-wind"],
    "Nebulo": ["title", "fog"],
    "Plejparte Klara": ["title", "very-light-clouds"],
    "Malmultaj Nuboj": ["title", "light-clouds"],
    "Nuboj": ["title", "medium-clouds"],
    "Multaj Nuboj": ["title", "heavy-clouds"],
    "Seka Humideco kaj Malforta Vento": [
        "title",
        ["and", "low-humidity", "light-wind"],
    ],
    "Drizlo kaj Forta Vento": ["title", ["and", "very-light-rain", "heavy-wind"]],
    "Alta Humideco kaj Malmultaj Nuboj": [
        "title",
        ["and", "high-humidity", "light-clouds"],
    ],
    "Fulmotondroj Eblas": ["title", "possible-thunderstorm"],
    "Forta Pluvo kaj Fulmotondroj": ["title", ["and", "heavy-rain", "thunderstorm"]],
    "Klara ĉielo por unu horo.": ["sentence", ["for-hour", "clear"]],
    "Malforta neĝo komenciĝos post 35 minutoj.": [
        "sentence",
        ["starting-in", "very-light-snow", ["minutes", 35]],
    ],
    "Malforta pluvo ĉesiĝos post 15 minutoj.": [
        "sentence",
        ["stopping-in", "light-rain", ["minutes", 15]],
    ],
    "Forta glaciumo komenciĝos post 20 minutoj kaj ĉesiĝos 30 minutoj poste.": [
        "sentence",
        [
            "starting-then-stopping-later",
            "heavy-sleet",
            ["minutes", 20],
            ["minutes", 30],
        ],
    ],
    "Pluvo ĉesiĝos post 25 minutoj kaj rekomenciĝos 8 minutoj poste.": [
        "sentence",
        [
            "stopping-then-starting-later",
            "medium-rain",
            ["minutes", 25],
            ["minutes", 8],
        ],
    ],
    "Nuboj dum la tago.": ["sentence", ["for-day", "medium-clouds"]],
    "Malforta glaciumo komenciĝos je la mateno.": [
        "sentence",
        ["starting", "very-light-sleet", "morning"],
    ],
    "Vento ĝis la nokto.": ["sentence", ["until", "medium-wind", "today-night"]],
    "Forta precipitaĵo ĝis la tagmezo.": [
        "sentence",
        ["until", "heavy-precipitation", "afternoon"],
    ],
    "Malforta vento dum la tagmezo.": [
        "sentence",
        ["during", "light-wind", "afternoon"],
    ],
    "Neĝo dum la malfrua vespero kaj morgaŭ mateno.": [
        "sentence",
        ["during", "medium-snow", ["and", "later-today-evening", "tomorrow-morning"]],
    ],
    "Forta pluvo ĝis la malfrua mateno, rekomenciĝos je la vespero.": [
        "sentence",
        ["until-starting-again", "heavy-rain", "later-today-morning", "today-evening"],
    ],
    "Multaj nuboj komenciĝos je la vespero, daŭros ĝis la nokto.": [
        "sentence",
        ["starting-continuing-until", "heavy-clouds", "evening", "night"],
    ],
    "Multaj nuboj komenciĝos je la mateno, daŭros ĝis la vespero.": [
        "sentence",
        ["starting-continuing-until", "heavy-clouds", "morning", "evening"],
    ],
    "Malforta glaciumo dum la malfrua tagmezo kaj nebulo dum morgaŭ mateno.": [
        "sentence",
        [
            "and",
            ["during", "light-sleet", "later-today-afternoon"],
            ["during", "fog", "tomorrow-morning"],
        ],
    ],
    "Forta vento komenciĝos je la mateno, daŭros ĝis la tagmezo, kaj glaciumo dum morgaŭ mateno.": [
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
    "Multaj nuboj komenciĝos je la malfrua nokto kaj forta neĝo dum morgaŭ tagmezo.": [
        "sentence",
        [
            "and",
            ["starting", "heavy-clouds", "later-today-night"],
            ["during", "heavy-snow", "tomorrow-afternoon"],
        ],
    ],
    "Seka humideco dum la nokto kaj malforta precipitaĵo komenciĝos je morgaŭ vespero, daŭros ĝis morgaŭ nokto.": [
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
    "Neĝo (5 in.) dum la nokto.": [
        "sentence",
        ["during", ["parenthetical", "medium-snow", ["inches", 5]], "night"],
    ],
    "Malforta neĝo (2 cm.) dum la malfrua mateno.": [
        "sentence",
        [
            "during",
            ["parenthetical", "light-snow", ["centimeters", 2]],
            "later-today-morning",
        ],
    ],
    "Forta neĝo (8\u201312 in.) dum la tago.": [
        "sentence",
        ["for-day", ["parenthetical", "heavy-snow", ["inches", ["range", 8, 12]]]],
    ],
    "Neĝo (malpli ol 1 cm.) dum la tagmezo.": [
        "sentence",
        [
            "during",
            ["parenthetical", "medium-snow", ["less-than", ["centimeters", 1]]],
            "afternoon",
        ],
    ],
    "Neniu precipitaĵo dum la semajno, kaj la temperaturo atingos sian maksimon je 85\u00b0F morgaŭ.": [
        "sentence",
        [
            "with",
            ["for-week", "no-precipitation"],
            ["temperatures-peaking", ["fahrenheit", 85], "tomorrow"],
        ],
    ],
    "Miksita precipitaĵo dum la semajnfino, kaj la temperaturo plialtiĝos ĝis 32\u00b0C ĵaŭdon.": [
        "sentence",
        [
            "with",
            ["over-weekend", "mixed-precipitation"],
            ["temperatures-rising", ["celsius", 32], "thursday"],
        ],
    ],
    "Drizlo dum hodiaŭ, kaj la temperaturo atingos sian minimumon je 15\u00b0F vendredon.": [
        "sentence",
        [
            "with",
            ["during", "very-light-rain", "today"],
            ["temperatures-valleying", ["fahrenheit", 15], "friday"],
        ],
    ],
    "Malforta neĝo dum lundo kaj mardo, kaj la temperaturo malplialtiĝos ĝis 0\u00b0C dimanĉon.": [
        "sentence",
        [
            "with",
            ["during", "light-snow", ["and", "monday", "tuesday"]],
            ["temperatures-falling", ["celsius", 0], "sunday"],
        ],
    ],
    "Precipitaĵo dum hodiaŭ ĝis sabato, kaj la temperaturo atingos sian maksimon je 100\u00b0F lundon.": [
        "sentence",
        [
            "with",
            ["during", "medium-precipitation", ["through", "today", "saturday"]],
            ["temperatures-peaking", ["fahrenheit", 100], "monday"],
        ],
    ],
    "Miksita precipitaĵo (1\u20133 in.) dum la tago.": [
        "sentence",
        [
            "for-day",
            ["parenthetical", "mixed-precipitation", ["inches", ["range", 1, 3]]],
        ],
    ],
    "Forta Neĝo (1\u20133 in.)": [
        "title",
        ["parenthetical", "heavy-snow", ["inches", ["range", 1, 3]]],
    ],
    "Forta Neĝo (3\u20135 cm.)": [
        "title",
        ["parenthetical", "heavy-snow", ["centimeters", ["range", 3, 5]]],
    ],
    "Fulmotondroj eblas dum la venonta mekredo kaj ĵaŭdo.": [
        "sentence",
        ["during", "possible-thunderstorm", ["and", "next-wednesday", "next-thursday"]],
    ],
    "Malforta pluvo komenciĝos je la tagmezo.": [
        "sentence",
        ["starting", "light-rain", "afternoon"],
    ],
    "Malforta pluvo ĝis la vespero.": ["sentence", ["until", "light-rain", "evening"]],
    "Drizlo ĝis la tagmezo, rekomenciĝos je la nokto.": [
        "sentence",
        ["until-starting-again", "very-light-rain", "afternoon", "night"],
    ],
    "Fulmotondroj eblas ĝis la venonta mekredo.": [
        "sentence",
        ["until", "possible-thunderstorm", "next-wednesday"],
    ],
}
