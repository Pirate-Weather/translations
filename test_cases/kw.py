# This would be one of your translations, as a Python dictionary
cases = {
    "Kler": ["title", "clear"],
    "Kodhans Skav Possybyl": ["title", "possible-very-light-precipitation"],
    "Kodhans Skav": ["title", "very-light-precipitation"],
    "Kodhans Skav Possybyl": ["title", "possible-light-precipitation"],
    "Kodhans Skav": ["title", "light-precipitation"],
    "Kodhans": ["title", "medium-precipitation"],
    "Kodhans Poos": ["title", "heavy-precipitation"],
    "Glaw Skav Possybyl": ["title", "possible-very-light-rain"],
    "Glaw Pur Skav": ["title", "very-light-rain"],
    "Glaw Skav Possybyl": ["title", "possible-light-rain"],
    "Glaw Skav": ["title", "light-rain"],
    "Glaw": ["title", "medium-rain"],
    "Glaw Poos": ["title", "heavy-rain"],
    "Erghlaw Skav Possybyl": ["title", "possible-very-light-sleet"],
    "Erghlaw Pur Skav": ["title", "very-light-sleet"],
    "Erghlaw Skav Possybyl": ["title", "possible-light-sleet"],
    "Erghlaw Skav": ["title", "light-sleet"],
    "Erghlaw": ["title", "medium-sleet"],
    "Erghlaw Poos": ["title", "heavy-sleet"],
    "Ergh Skav Possybyl": ["title", "possible-very-light-snow"],
    "Ergh Pur Skav": ["title", "very-light-snow"],
    "Ergh Skav Possybyl": ["title", "possible-light-snow"],
    "Ergh Skav": ["title", "light-snow"],
    "Ergh": ["title", "medium-snow"],
    "Ergh Poos": ["title", "heavy-snow"],
    "Gwynsek": ["title", "medium-wind"],
    "Gwynsek Bys Yn Peryl": ["title", "heavy-wind"],
    "Niwlek": ["title", "fog"],
    "Soprattuttu Chjaru": ["title", "very-light-clouds"],
    "Nebes Komolek": ["title", "light-clouds"],
    "Komolek": ["title", "medium-clouds"],
    "Komolek Poos": ["title", "heavy-clouds"],
    "Sygh Ha Nebes Gwynsek": ["title", ["and", "low-humidity", "light-wind"]],
    "Glaw Pur Skav Ha Gwynsek Bys Yn Peryl": [
        "title",
        ["and", "very-light-rain", "heavy-wind"],
    ],
    "Glyb Ha Nebes Komolek": ["title", ["and", "high-humidity", "light-clouds"]],
    "Kler rag an our.": ["sentence", ["for-hour", "clear"]],
    "Ergh pur skav ow talleth yn 35 myn.": [
        "sentence",
        ["starting-in", "very-light-snow", ["minutes", 35]],
    ],
    "Glaw skav ow hedhi yn 15 myn.": [
        "sentence",
        ["stopping-in", "light-rain", ["minutes", 15]],
    ],
    "Erghlaw poos ow talleth yn 20 myn., ow hedhi 30 myn. diwettha.": [
        "sentence",
        [
            "starting-then-stopping-later",
            "heavy-sleet",
            ["minutes", 20],
            ["minutes", 30],
        ],
    ],
    "Glaw ow hedhi yn 25 myn., ow tastalleth 8 myn. diwettha.": [
        "sentence",
        [
            "stopping-then-starting-later",
            "medium-rain",
            ["minutes", 25],
            ["minutes", 8],
        ],
    ],
    "Komolek dres oll an jydh.": ["sentence", ["for-day", "medium-clouds"]],
    "Erghlaw pur skav ow talleth y'n myttin.": [
        "sentence",
        ["starting", "very-light-sleet", "morning"],
    ],
    "Gwynsek bys y'n nos ma.": ["sentence", ["until", "medium-wind", "today-night"]],
    "Kodhans poos bys y'n dohajydh.": [
        "sentence",
        ["until", "heavy-precipitation", "afternoon"],
    ],
    "Nebes gwynsek y'n dohajydh.": ["sentence", ["during", "light-wind", "afternoon"]],
    "Ergh diwettha haneth ha ternos vyttin.": [
        "sentence",
        ["during", "medium-snow", ["and", "later-today-evening", "tomorrow-morning"]],
    ],
    "Glaw poos bys yn diwettha hedhyw vyttin, ow tastalleth haneth.": [
        "sentence",
        ["until-starting-again", "heavy-rain", "later-today-morning", "today-evening"],
    ],
    "Komolek poos ow talleth y'n gorthugher, ow pesya bys y'n nos.": [
        "sentence",
        ["starting-continuing-until", "heavy-clouds", "evening", "night"],
    ],
    "Erghlaw skav diwettha an dohajydh ma ha niwlek ternos vyttin.": [
        "sentence",
        [
            "and",
            ["during", "light-sleet", "later-today-afternoon"],
            ["during", "fog", "tomorrow-morning"],
        ],
    ],
    "Gwynsek bys yn peryl ow talleth hedhyw vyttin, ow pesya bys y'n dohajydh ma, hag erghlaw ternos vyttin.": [
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
    "Komolek poos ow talleth diwettha haneth hag ergh poos dohajydhweyth a-vorow.": [
        "sentence",
        [
            "and",
            ["starting", "heavy-clouds", "later-today-night"],
            ["during", "heavy-snow", "tomorrow-afternoon"],
        ],
    ],
    "Sygh y'n nos ma ha kodhans skav ow talleth gorthugherweyth a-vorow, ow pesya bys yn nosweyth a-vorow.": [
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
    "Ergh (5 mv.) y'n nos.": [
        "sentence",
        ["during", ["parenthetical", "medium-snow", ["inches", 5]], "night"],
    ],
    "Ergh skav (2 cm.) diwettha hedhyw vyttin.": [
        "sentence",
        [
            "during",
            ["parenthetical", "light-snow", ["centimeters", 2]],
            "later-today-morning",
        ],
    ],
    "Ergh poos (8\u201312 mv.) dres oll an jydh.": [
        "sentence",
        ["for-day", ["parenthetical", "heavy-snow", ["inches", ["range", 8, 12]]]],
    ],
    "Ergh (le ages 1 cm.) y'n dohajydh.": [
        "sentence",
        [
            "during",
            ["parenthetical", "medium-snow", ["less-than", ["centimeters", 1]]],
            "afternoon",
        ],
    ],
    "Kodhans vyth dres oll an seythun, gans ughella tempredhow a 85\u00b0F a-vorow.": [
        "sentence",
        [
            "with",
            ["for-week", "no-precipitation"],
            ["temperatures-peaking", ["fahrenheit", 85], "tomorrow"],
        ],
    ],
    "Kodhans kemyskys dres an bennseythun, gans tempredhow ow kressya dhe 32\u00b0C dy' Yow.": [
        "sentence",
        [
            "with",
            ["over-weekend", "mixed-precipitation"],
            ["temperatures-rising", ["celsius", 32], "thursday"],
        ],
    ],
    "Glaw pur skav dy' Lun, gans tempredhow ow hedhi kodha dhe 15\u00b0F dy' Gwener.": [
        "sentence",
        [
            "with",
            ["during", "very-light-rain", "monday"],
            ["temperatures-valleying", ["fahrenheit", 15], "friday"],
        ],
    ],
    "Ergh skav dy' Meurth ha dy' Mergher a dheu, gans tempredhow ow kodha dhe 0\u00b0C dy' Sul.": [
        "sentence",
        [
            "with",
            ["during", "light-snow", ["and", "tuesday", "next-wednesday"]],
            ["temperatures-falling", ["celsius", 0], "sunday"],
        ],
    ],
    "Kodhans hedhyw bys yn dy' Sadorn, gans ughella tempredhow a 100\u00b0F dy' Lun.": [
        "sentence",
        [
            "with",
            ["during", "medium-precipitation", ["through", "today", "saturday"]],
            ["temperatures-peaking", ["fahrenheit", 100], "monday"],
        ],
    ],
    "Kodhans kemyskys (1\u20133 mv. a ergh) dres oll an jydh.": [
        "sentence",
        [
            "for-day",
            ["parenthetical", "mixed-precipitation", ["inches", ["range", 1, 3]]],
        ],
    ],
    "Ergh Poos (1\u20133 Mv.)": [
        "title",
        ["parenthetical", "heavy-snow", ["inches", ["range", 1, 3]]],
    ],
    "Ergh Poos (3\u20135 cm.)": [
        "title",
        ["parenthetical", "heavy-snow", ["centimeters", ["range", 3, 5]]],
    ],
    "Tewedhow-Taran Possybyl": ["title", "possible-thunderstorm"],
    "Glaw Poos Ha Tewedhow-Taran": ["title", ["and", "heavy-rain", "thunderstorm"]],
    "Glaw pur skav ow talleth le ages 1 myn.": [
        "sentence",
        ["starting-in", "very-light-rain", ["less-than", ["minutes", 1]]],
    ],
    "Darganow herwydh an our yw ankavadow dres pols drefen bos pub gorsav radar y'n ranndir dhywarlinen.": [
        "sentence",
        ["next-hour-forecast-status", "temporarily-unavailable", "station-offline"],
    ],
    "Darganow herwydh an our yw ankavadow yn rann drefen bos aswaow y'n gorherans dhyworth gorsavow radar y'n ranndir.": [
        "sentence",
        ["next-hour-forecast-status", "partially-unavailable", "station-incomplete"],
    ],
    "Darganow herwydh an our yw ankavadow drefen bos pub gorsav radar y'n ranndir dhywarlinen.": [
        "sentence",
        ["next-hour-forecast-status", "unavailable", "station-offline"],
    ],
}
