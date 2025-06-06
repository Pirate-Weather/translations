# This would be one of your translations, as a Python dictionary
cases = {
    "Bezchmurnie": ["title", "clear"],
    "Możliwe słabe opady": ["title", "possible-very-light-precipitation"],
    "Słabe opady": ["title", "very-light-precipitation"],
    "Możliwe niewielkie opady": ["title", "possible-light-precipitation"],
    "Niewielkie opady": ["title", "light-precipitation"],
    "Opady": ["title", "medium-precipitation"],
    "Silne opady": ["title", "heavy-precipitation"],
    "Możliwa mżawka": ["title", "possible-very-light-rain"],
    "Mżawka": ["title", "very-light-rain"],
    "Możliwy niewielki deszcz": ["title", "possible-light-rain"],
    "Niewielki deszcz": ["title", "light-rain"],
    "Deszcz": ["title", "medium-rain"],
    "Ulewa": ["title", "heavy-rain"],
    "Możliwe słabe opady deszczu ze śniegiem": ["title", "possible-very-light-sleet"],
    "Słabe opady deszczu ze śniegiem": ["title", "very-light-sleet"],
    "Możliwe niewielkie opady deszczu ze śniegiem": ["title", "possible-light-sleet"],
    "Niewielkie opady deszczu ze śniegiem": ["title", "light-sleet"],
    "Deszcz ze śniegiem": ["title", "medium-sleet"],
    "Deszcz ze śniegiem": ["title", "heavy-sleet"],
    "Możliwy drobny śnieg": ["title", "possible-very-light-snow"],
    "Drobny śnieg": ["title", "very-light-snow"],
    "Możliwy niewielki śnieg": ["title", "possible-light-snow"],
    "Niewielki śnieg": ["title", "light-snow"],
    "Śnieg": ["title", "medium-snow"],
    "Śnieżyca": ["title", "heavy-snow"],
    "Umiarkowany wiatr": ["title", "medium-wind"],
    "Silny wiatr": ["title", "heavy-wind"],
    "Mgła": ["title", "fog"],
    "Średnie bezchmurnie": ["title", "very-light-clouds"],
    "Niewielkie zachmurzenie": ["title", "light-clouds"],
    "Średnie zachmurzenie": ["title", "medium-clouds"],
    "Duże zachmurzenie": ["title", "heavy-clouds"],
    "Niska wilgotność, słaby wiatr": ["title", ["and", "low-humidity", "light-wind"]],
    "Mżawka, silny wiatr": ["title", ["and", "very-light-rain", "heavy-wind"]],
    "Duża wilgotność, niewielkie zachmurzenie": [
        "title",
        ["and", "high-humidity", "light-clouds"],
    ],
    "Bezchmurnie przez godzinę.": ["sentence", ["for-hour", "clear"]],
    "Drobny śnieg za 35 min.": [
        "sentence",
        ["starting-in", "very-light-snow", ["minutes", 35]],
    ],
    "Niewielki deszcz skończy się za 15 min.": [
        "sentence",
        ["stopping-in", "light-rain", ["minutes", 15]],
    ],
    "Deszcz ze śniegiem za 20 min., skończy się po 30 min.": [
        "sentence",
        [
            "starting-then-stopping-later",
            "heavy-sleet",
            ["minutes", 20],
            ["minutes", 30],
        ],
    ],
    "Deszcz skończy się za 25 min., ponownie zacznie 8 min. później.": [
        "sentence",
        [
            "stopping-then-starting-later",
            "medium-rain",
            ["minutes", 25],
            ["minutes", 8],
        ],
    ],
    "Średnie zachmurzenie w ciągu dnia.": ["sentence", ["for-day", "medium-clouds"]],
    "Rano słabe opady deszczu ze śniegiem.": [
        "sentence",
        ["starting", "very-light-sleet", "morning"],
    ],
    "Umiarkowany wiatr, ustanie nocą.": [
        "sentence",
        ["until", "medium-wind", "today-night"],
    ],
    "Silne opady, ustaną po południu.": [
        "sentence",
        ["until", "heavy-precipitation", "afternoon"],
    ],
    "Po południu słaby wiatr.": ["sentence", ["during", "light-wind", "afternoon"]],
    "Późnym wieczorem i jutro rano śnieg.": [
        "sentence",
        ["during", "medium-snow", ["and", "later-today-evening", "tomorrow-morning"]],
    ],
    "Ulewa, ustanie przed południem, wieczorem ponownie ulewa.": [
        "sentence",
        ["until-starting-again", "heavy-rain", "later-today-morning", "today-evening"],
    ],
    "Wieczorem duże zachmurzenie, skończy się nocą.": [
        "sentence",
        ["starting-continuing-until", "heavy-clouds", "evening", "night"],
    ],
    "Późnym popołudniem niewielkie opady deszczu ze śniegiem, jutro rano mgła.": [
        "sentence",
        [
            "and",
            ["during", "light-sleet", "later-today-afternoon"],
            ["during", "fog", "tomorrow-morning"],
        ],
    ],
    "Rano silny wiatr, skończy się po południu, jutro rano deszcz ze śniegiem.": [
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
    "Późno w nocy duże zachmurzenie, jutro po południu śnieżyca.": [
        "sentence",
        [
            "and",
            ["starting", "heavy-clouds", "later-today-night"],
            ["during", "heavy-snow", "tomorrow-afternoon"],
        ],
    ],
    "Nocą niska wilgotność, jutro wieczorem niewielkie opady, skończą się jutro w nocy.": [
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
    "Nocą śnieg (5 in).": [
        "sentence",
        ["during", ["parenthetical", "medium-snow", ["inches", 5]], "night"],
    ],
    "Przed południem niewielki śnieg (2 cm).": [
        "sentence",
        [
            "during",
            ["parenthetical", "light-snow", ["centimeters", 2]],
            "later-today-morning",
        ],
    ],
    "Śnieżyca (8\u201312 in) w ciągu dnia.": [
        "sentence",
        ["for-day", ["parenthetical", "heavy-snow", ["inches", ["range", 8, 12]]]],
    ],
    "Po południu śnieg (mniej niż 1 cm).": [
        "sentence",
        [
            "during",
            ["parenthetical", "medium-snow", ["less-than", ["centimeters", 1]]],
            "afternoon",
        ],
    ],
    "Brak opadów w ciągu tygodnia, jutro temperatura wzrośnie do 85\u00b0F.": [
        "sentence",
        [
            "with",
            ["for-week", "no-precipitation"],
            ["temperatures-peaking", ["fahrenheit", 85], "tomorrow"],
        ],
    ],
    "Przelotne opady w ciągu weekendu, w czwartek ocieplenie do 32\u00b0C.": [
        "sentence",
        [
            "with",
            ["over-weekend", "mixed-precipitation"],
            ["temperatures-rising", ["celsius", 32], "thursday"],
        ],
    ],
    "W poniedziałek mżawka, w piątek temperatura spadnie do 15\u00b0F.": [
        "sentence",
        [
            "with",
            ["during", "very-light-rain", "monday"],
            ["temperatures-valleying", ["fahrenheit", 15], "friday"],
        ],
    ],
    "We wtorek i przyszłą środę niewielki śnieg, w niedzielę ochłodzenie do 0\u00b0C.": [
        "sentence",
        [
            "with",
            ["during", "light-snow", ["and", "tuesday", "next-wednesday"]],
            ["temperatures-falling", ["celsius", 0], "sunday"],
        ],
    ],
    "Od dzisiaj do soboty opady, w poniedziałek temperatura wzrośnie do 100\u00b0F.": [
        "sentence",
        [
            "with",
            ["during", "medium-precipitation", ["through", "today", "saturday"]],
            ["temperatures-peaking", ["fahrenheit", 100], "monday"],
        ],
    ],
    "Przelotne opady (1\u20133 in śniegu) w ciągu dnia.": [
        "sentence",
        [
            "for-day",
            ["parenthetical", "mixed-precipitation", ["inches", ["range", 1, 3]]],
        ],
    ],
    "Śnieżyca (1\u20133 in)": [
        "title",
        ["parenthetical", "heavy-snow", ["inches", ["range", 1, 3]]],
    ],
    "Śnieżyca (3\u20135 cm)": [
        "title",
        ["parenthetical", "heavy-snow", ["centimeters", ["range", 3, 5]]],
    ],
    "Możliwa burza": ["title", "possible-thunderstorm"],
    "Ulewa, burza": ["title", ["and", "heavy-rain", "thunderstorm"]],
    "W poniedziałek i wtorek możliwy niewielki deszcz, we wtorek ochłodzenie do 18\u00b0C.": [
        "sentence",
        [
            "with",
            ["during", "possible-light-rain", ["and", "monday", "tuesday"]],
            ["temperatures-falling", ["celsius", 18], "tuesday"],
        ],
    ],
}
