# This would be one of your translations, as a Python dictionary
cases = {
    "Klar": ["title", "clear"],
    "Leichter Niederschlag": ["title", "very-light-precipitation"],
    "Leichter Niederschlag": ["title", "light-precipitation"],
    "Niederschlag": ["title", "medium-precipitation"],
    "Schwerer Niederschlag": ["title", "heavy-precipitation"],
    "Nieselregen": ["title", "very-light-rain"],
    "Leichter Regen": ["title", "light-rain"],
    "Regen": ["title", "medium-rain"],
    "Regenschauer": ["title", "heavy-rain"],
    "Leichter Graupelregen": ["title", "very-light-sleet"],
    "Leichter Graupelregen": ["title", "light-sleet"],
    "Graupelregen": ["title", "medium-sleet"],
    "Graupelschauer": ["title", "heavy-sleet"],
    "Leichter Schneefall": ["title", "very-light-snow"],
    "Leichter Schneefall": ["title", "light-snow"],
    "Schneefall": ["title", "medium-snow"],
    "Starker Schneefall": ["title", "heavy-snow"],
    "Frische Brise": ["title", "medium-wind"],
    "Sturm": ["title", "heavy-wind"],
    "Nebel": ["title", "fog"],
    "Überwiegend Klar": ["title", "very-light-clouds"],
    "Leicht bewölkt": ["title", "light-clouds"],
    "Überwiegend bewölkt": ["title", "medium-clouds"],
    "Stark bewölkt": ["title", "heavy-clouds"],
    "Niedrige Luftfeuchtigkeit und leichter Wind": [
        "title",
        ["and", "low-humidity", "light-wind"],
    ],
    "Hohe Luftfeuchtigkeit und leicht bewölkt": [
        "title",
        ["and", "high-humidity", "light-clouds"],
    ],
    "In der kommenden Stunde Klar.": ["sentence", ["for-hour", "clear"]],
    "In 35 Min. leichter Schneefall.": [
        "sentence",
        ["starting-in", "very-light-snow", ["minutes", 35]],
    ],
    "Leichter Regen, endet in 15 Min.": [
        "sentence",
        ["stopping-in", "light-rain", ["minutes", 15]],
    ],
    "Graupelschauer in 20 Min. für 30 Min.": [
        "sentence",
        [
            "starting-then-stopping-later",
            "heavy-sleet",
            ["minutes", 20],
            ["minutes", 30],
        ],
    ],
    "Regen endet in 25 Min. und beginnt 8 Min. danach erneut.": [
        "sentence",
        [
            "stopping-then-starting-later",
            "medium-rain",
            ["minutes", 25],
            ["minutes", 8],
        ],
    ],
    "Den ganzen Tag lang überwiegend bewölkt.": [
        "sentence",
        ["for-day", "medium-clouds"],
    ],
    "Vormittags leichter Graupelregen.": [
        "sentence",
        ["starting", "very-light-sleet", "morning"],
    ],
    "Frische Brise bis heute Nacht.": [
        "sentence",
        ["until", "medium-wind", "today-night"],
    ],
    "Schwerer Niederschlag bis Nachmittag.": [
        "sentence",
        ["until", "heavy-precipitation", "afternoon"],
    ],
    "Leichter Wind am Nachmittag.": ["sentence", ["during", "light-wind", "afternoon"]],
    "Schneefall am späteren Abend und morgen Vormittag.": [
        "sentence",
        ["during", "medium-snow", ["and", "later-today-evening", "tomorrow-morning"]],
    ],
    "Regenschauer bis zum späteren Vormittag und heute Abend wieder.": [
        "sentence",
        ["until-starting-again", "heavy-rain", "later-today-morning", "today-evening"],
    ],
    "Stark bewölkt abends und nächtlich.": [
        "sentence",
        ["starting-continuing-until", "heavy-clouds", "evening", "night"],
    ],
    "Stark bewölkt von vormittags bis abends.": [
        "sentence",
        ["starting-continuing-until", "heavy-clouds", "morning", "evening"],
    ],
    "Am späteren Nachmittag leichter Graupelregen und morgen Vormittag Nebel.": [
        "sentence",
        [
            "and",
            ["during", "light-sleet", "later-today-afternoon"],
            ["during", "fog", "tomorrow-morning"],
        ],
    ],
    "Sturm von heute Vormittag bis heute Nachmittag sowie morgen Vormittag Graupelregen.": [
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
    "Heute in der späteren Nacht stark bewölkt und morgen Nachmittag starker Schneefall.": [
        "sentence",
        [
            "and",
            ["starting", "heavy-clouds", "later-today-night"],
            ["during", "heavy-snow", "tomorrow-afternoon"],
        ],
    ],
    "Heute Nacht niedrige Luftfeuchtigkeit sowie leichter Niederschlag von morgen Abend bis morgen Nacht.": [
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
    "Schneefall (5 Zoll) in der Nacht.": [
        "sentence",
        ["during", ["parenthetical", "medium-snow", ["inches", 5]], "night"],
    ],
    "Leichter Schneefall (2 cm) am späteren Vormittag.": [
        "sentence",
        [
            "during",
            ["parenthetical", "light-snow", ["centimeters", 2]],
            "later-today-morning",
        ],
    ],
    "Den ganzen Tag lang starker Schneefall (8 bis 12 Zoll).": [
        "sentence",
        ["for-day", ["parenthetical", "heavy-snow", ["inches", ["range", 8, 12]]]],
    ],
    "Schneefall (weniger als 1 cm) am Nachmittag.": [
        "sentence",
        [
            "during",
            ["parenthetical", "medium-snow", ["centimeters", ["less-than", 1]]],
            "afternoon",
        ],
    ],
    "Die ganze Woche kein Niederschlag mit einem Temperaturmaximum von 85\u00b0F morgen.": [
        "sentence",
        [
            "with",
            ["for-week", "no-precipitation"],
            ["temperatures-peaking", ["fahrenheit", 85], "tomorrow"],
        ],
    ],
    "Wechselnder Niederschlag am Wochenende mit steigender Temperatur von 32\u00b0C am Donnerstag.": [
        "sentence",
        [
            "with",
            ["over-weekend", "mixed-precipitation"],
            ["temperatures-rising", ["celsius", 32], "thursday"],
        ],
    ],
    "Nieselregen heute mit einem Temperaturminimum von 15\u00b0F am Freitag.": [
        "sentence",
        [
            "with",
            ["during", "very-light-rain", "today"],
            ["temperatures-valleying", ["fahrenheit", 15], "friday"],
        ],
    ],
    "Leichter Schneefall am Montag und Dienstag mit fallender Temperatur von 0\u00b0C am Sonntag.": [
        "sentence",
        [
            "with",
            ["during", "light-snow", ["and", "monday", "tuesday"]],
            ["temperatures-falling", ["celsius", 0], "sunday"],
        ],
    ],
    "Niederschlag von Donnerstag bis Samstag mit einem Temperaturmaximum von 100\u00b0F am Montag.": [
        "sentence",
        [
            "with",
            ["during", "medium-precipitation", ["through", "thursday", "saturday"]],
            ["temperatures-peaking", ["fahrenheit", 100], "monday"],
        ],
    ],
    "Nachmittags leichter Regen.": [
        "sentence",
        ["starting", "light-rain", "afternoon"],
    ],
    "Leichter Regen bis abends.": ["sentence", ["until", "light-rain", "evening"]],
    "Nieselregen bis zum Nachmittag und Nacht.": [
        "sentence",
        ["until-starting-again", "very-light-rain", "afternoon", "night"],
    ],
    "Gewitter möglich bis am nächsten Mittwoch.": [
        "sentence",
        ["until", "possible-thunderstorm", "next-wednesday"],
    ],
    "Leichter Regen heute.": ["sentence", ["during", "light-rain", "today"]],
    "Leichter Regen morgen.": ["sentence", ["during", "light-rain", "tomorrow"]],
}
