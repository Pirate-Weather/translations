# This would be one of your translations, as a Python dictionary
cases = {
    "Selge": ["title", "clear"],
    "Nõrga saju võimalus": ["title", "possible-very-light-precipitation"],
    "Nõrk sadu": ["title", "very-light-precipitation"],
    "Kerge saju võimalus": ["title", "possible-light-precipitation"],
    "Kerge sadu": ["title", "light-precipitation"],
    "Mõõdukas sadu": ["title", "medium-precipitation"],
    "Tugev sadu": ["title", "heavy-precipitation"],
    "Nõrga vihmasaju võimalus": ["title", "possible-very-light-rain"],
    "Nõrk vihmasadu": ["title", "very-light-rain"],
    "Kerge vihmasaju võimalus": ["title", "possible-light-rain"],
    "Kerge vihmasadu": ["title", "light-rain"],
    "Mõõdukas vihmasadu": ["title", "medium-rain"],
    "Tugev vihmasadu": ["title", "heavy-rain"],
    "Nõrga lörtsisaju võimalus": ["title", "possible-very-light-sleet"],
    "Nõrk lörtsisadu": ["title", "very-light-sleet"],
    "Kerge lörtsisaju võimalus": ["title", "possible-light-sleet"],
    "Kerge lörtsisadu": ["title", "light-sleet"],
    "Mõõdukas lörtsisadu": ["title", "medium-sleet"],
    "Tugev lörtsisadu": ["title", "heavy-sleet"],
    "Nõrga lumesaju võimalus": ["title", "possible-very-light-snow"],
    "Nõrk lumesadu": ["title", "very-light-snow"],
    "Kerge lumesaju võimalus": ["title", "possible-light-snow"],
    "Kerge lumesadu": ["title", "light-snow"],
    "Mõõdukas lumesadu": ["title", "medium-snow"],
    "Tugev lumesadu": ["title", "heavy-snow"],
    "Mõõdukas tuul": ["title", "medium-wind"],
    "Tugev tuul": ["title", "heavy-wind"],
    "Udu": ["title", "fog"],
    "Enamasti selge": ["title", "very-light-clouds"],
    "Vähene pilvisus": ["title", "light-clouds"],
    "Mõõdukas pilvisus": ["title", "medium-clouds"],
    "Pilves": ["title", "heavy-clouds"],
    "Nõrk vihmasadu ja tugev tuul": ["title", ["and", "very-light-rain", "heavy-wind"]],
    "Selge järgmised tund aega.": ["sentence", ["for-hour", "clear"]],
    "Nõrk lumesadu oodata 35 min. pärast.": [
        "sentence",
        ["starting-in", "very-light-snow", ["minutes", 35]],
    ],
    "Kerge vihmasadu lõppeb 15 min. pärast.": [
        "sentence",
        ["stopping-in", "light-rain", ["minutes", 15]],
    ],
    "Tugev lörtsisadu algab 20 min. pärast, lõppeb 30 min. hiljem.": [
        "sentence",
        [
            "starting-then-stopping-later",
            "heavy-sleet",
            ["minutes", 20],
            ["minutes", 30],
        ],
    ],
    "Mõõdukas vihmasadu lõppeb 25 min. pärast, algab uuesti 8 min. hiljem.": [
        "sentence",
        [
            "stopping-then-starting-later",
            "medium-rain",
            ["minutes", 25],
            ["minutes", 8],
        ],
    ],
    "Terve päev on mõõdukas pilvisus.": ["sentence", ["for-day", "medium-clouds"]],
    "Nõrk lörtsisadu alates hommikust.": [
        "sentence",
        ["starting", "very-light-sleet", "morning"],
    ],
    "Mõõdukas tuul kuni ööni.": ["sentence", ["until", "medium-wind", "today-night"]],
    "Tugev sadu kuni pärastlõunani.": [
        "sentence",
        ["until", "heavy-precipitation", "afternoon"],
    ],
    "Kerge tuul pärastlõunal.": ["sentence", ["during", "light-wind", "afternoon"]],
    "Mõõdukas lumesadu hiljem õhtul ja homme hommikul.": [
        "sentence",
        ["during", "medium-snow", ["and", "later-today-evening", "tomorrow-morning"]],
    ],
    "Tugev vihmasadu hiljem täna hommikul, ja jälle õhtul.": [
        "sentence",
        ["until-starting-again", "heavy-rain", "later-today-morning", "today-evening"],
    ],
    "Pilves õhtust ööni.": [
        "sentence",
        ["starting-continuing-until", "heavy-clouds", "evening", "night"],
    ],
    "Kerge lörtsisadu hiljem pärastlõunal ja udu homme hommikul.": [
        "sentence",
        [
            "and",
            ["during", "light-sleet", "later-today-afternoon"],
            ["during", "fog", "tomorrow-morning"],
        ],
    ],
    "Tugev tuul hommikust pärastlõunani ja mõõdukas lörtsisadu homme hommikul.": [
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
    "Pilves alates hilisemast ööst ja tugev lumesadu homme pärastlõunal.": [
        "sentence",
        [
            "and",
            ["starting", "heavy-clouds", "later-today-night"],
            ["during", "heavy-snow", "tomorrow-afternoon"],
        ],
    ],
    "Mõõdukas lumesadu (5 tolli) öösel.": [
        "sentence",
        ["during", ["parenthetical", "medium-snow", ["inches", 5]], "night"],
    ],
    "Kerge lumesadu (2 cm) hiljem täna hommikul.": [
        "sentence",
        [
            "during",
            ["parenthetical", "light-snow", ["centimeters", 2]],
            "later-today-morning",
        ],
    ],
    "Terve päev on tugev lumesadu (8\u201312 tolli).": [
        "sentence",
        ["for-day", ["parenthetical", "heavy-snow", ["inches", ["range", 8, 12]]]],
    ],
    "Mõõdukas lumesadu (alla 1 cm) pärastlõunal.": [
        "sentence",
        [
            "during",
            ["parenthetical", "medium-snow", ["less-than", ["centimeters", 1]]],
            "afternoon",
        ],
    ],
    "Kuiv nädal aega, temperatuur tõuseb homme kuni 85\u00b0F.": [
        "sentence",
        [
            "with",
            ["for-week", "no-precipitation"],
            ["temperatures-peaking", ["fahrenheit", 85], "tomorrow"],
        ],
    ],
    "Erinevad sademed nädalavahetusel, temperatuur tõuseb neljapäeval kuni 32\u00b0C.": [
        "sentence",
        [
            "with",
            ["over-weekend", "mixed-precipitation"],
            ["temperatures-rising", ["celsius", 32], "thursday"],
        ],
    ],
    "Nõrk vihmasadu esmaspäeval, temperatuur langeb reedel kuni 15\u00b0F.": [
        "sentence",
        [
            "with",
            ["during", "very-light-rain", "monday"],
            ["temperatures-valleying", ["fahrenheit", 15], "friday"],
        ],
    ],
    "Kerge lumesadu teisipäeval ja järgmisel kolmapäeval, temperatuur langeb pühapäeval kuni 0\u00b0C.": [
        "sentence",
        [
            "with",
            ["during", "light-snow", ["and", "tuesday", "next-wednesday"]],
            ["temperatures-falling", ["celsius", 0], "sunday"],
        ],
    ],
    "Mõõdukas sadu tänasest kuni laupäevani, temperatuur tõuseb esmaspäeval kuni 100\u00b0F.": [
        "sentence",
        [
            "with",
            ["during", "medium-precipitation", ["through", "today", "saturday"]],
            ["temperatures-peaking", ["fahrenheit", 100], "monday"],
        ],
    ],
    "Terve päev on erinevad sademed (1\u20133 tolli).": [
        "sentence",
        [
            "for-day",
            ["parenthetical", "mixed-precipitation", ["inches", ["range", 1, 3]]],
        ],
    ],
    "Tugev lumesadu (1\u20133 tolli)": [
        "title",
        ["parenthetical", "heavy-snow", ["inches", ["range", 1, 3]]],
    ],
    "Tugev lumesadu (3\u20135 cm)": [
        "title",
        ["parenthetical", "heavy-snow", ["centimeters", ["range", 3, 5]]],
    ],
    "Äikesetormi võimalus": ["title", "possible-thunderstorm"],
    "Tugev vihmasadu ja äikesetorm": ["title", ["and", "heavy-rain", "thunderstorm"]],
    "Suits": ["title", "smoke"],
    "Terve päev on suits.": ["sentence", ["for-day", "smoke"]],
    "Suits hommikul.": ["sentence", ["during", "smoke", "morning"]],
    "Suits kuni õhtuni.": ["sentence", ["until", "smoke", "today-evening"]],
    "Suits ja vähene pilvisus": ["title", ["and", "smoke", "light-clouds"]],
    "Terve päev on udu.": ["sentence", ["for-day", "haze"]],
    "Udu pärastlõunal.": ["sentence", ["during", "haze", "afternoon"]],
    "Uduvihm": ["title", "mist"],
    "Terve päev on uduvihm.": ["sentence", ["for-day", "mist"]],
    "Uduvihm öösel.": ["sentence", ["during", "mist", "night"]],
    "Uduvihm ja pilves": ["title", ["and", "mist", "heavy-clouds"]],
    "Äikesetorm järgmised tund aega.": ["sentence", ["for-hour", "thunderstorm"]],
    "Tugev jääkülma vihmasadu lõppeb 10 min. pärast, algab uuesti 32 min. hiljem.": [
        "sentence",
        [
            "stopping-then-starting-later",
            "heavy-freezing-rain",
            ["minutes", 10],
            ["minutes", 32],
        ],
    ],
    "Jääkülma nõrk vihmasadu oodata 49 min. pärast.": [
        "sentence",
        ["starting-in", "very-light-freezing-rain", ["minutes", 49]],
    ],
    "Mõõdukas vihmasadu täna, reedel, pühapäeval ja järgmisel kolmapäeval, temperatuur püsib umbes 20°C.": [
        "sentence",
        [
            "with",
            [
                "during",
                "medium-rain",
                ["list", "today", "friday", "sunday", "next-wednesday"],
            ],
            ["temperatures-steady", ["celsius", 20]],
        ],
    ],
    "Mõõdukas vihmasadu, lisaks äikesetormi võimalus alates pärastlõunast.": [
        "sentence",
        [
            "accompanied-by",
            "medium-rain",
            ["starting", "possible-thunderstorm", "today-afternoon"],
        ],
    ],
}
