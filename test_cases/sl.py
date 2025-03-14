# This would be one of your translations, as a Python dictionary
cases = {
    "Jasno": ["title", "clear"],
    "Možne so rahle padavine": ["title", "possible-very-light-precipitation"],
    "Rahle padavine": ["title", "very-light-precipitation"],
    "Možne so rahle padavine": ["title", "possible-light-precipitation"],
    "Rahle padavine": ["title", "light-precipitation"],
    "Padavine": ["title", "medium-precipitation"],
    "Močne padavine": ["title", "heavy-precipitation"],
    "Možen je rahel dež": ["title", "possible-very-light-rain"],
    "Rosenje": ["title", "very-light-rain"],
    "Možen je rahel dež": ["title", "possible-light-rain"],
    "Rahel dež": ["title", "light-rain"],
    "Dež": ["title", "medium-rain"],
    "Močan dež": ["title", "heavy-rain"],
    "Možnost rahlega žleda": ["title", "possible-very-light-sleet"],
    "Rahel žled": ["title", "very-light-sleet"],
    "Možnost žleda": ["title", "possible-light-sleet"],
    "Rahel žled": ["title", "light-sleet"],
    "Dež s snegom": ["title", "medium-sleet"],
    "Žled": ["title", "heavy-sleet"],
    "Možno je rahlo sneženje": ["title", "possible-very-light-snow"],
    "Rahlo sneženje": ["title", "very-light-snow"],
    "Možnost rahlega sneženja": ["title", "possible-light-snow"],
    "Rahlo sneženje": ["title", "light-snow"],
    "Sneg": ["title", "medium-snow"],
    "Močno sneženje": ["title", "heavy-snow"],
    "Vetrovno": ["title", "medium-wind"],
    "Močni sunki vetra": ["title", "heavy-wind"],
    "Megleno": ["title", "fog"],
    "Pretežno jasno": ["title", "very-light-clouds"],
    "Delno oblačno": ["title", "light-clouds"],
    "Pretežno oblačno": ["title", "medium-clouds"],
    "Oblačno": ["title", "heavy-clouds"],
    "Suho in vetrovno": ["title", ["and", "low-humidity", "light-wind"]],
    "Rosenje in močni sunki vetra": ["title", ["and", "very-light-rain", "heavy-wind"]],
    "Vlažno in delno oblačno": ["title", ["and", "high-humidity", "light-clouds"]],
    "Jasno za uro.": ["sentence", ["for-hour", "clear"]],
    "Rahlo sneženje od 35 min.": [
        "sentence",
        ["starting-in", "very-light-snow", ["minutes", 35]],
    ],
    "Rahel dež do 15 min.": [
        "sentence",
        ["stopping-in", "light-rain", ["minutes", 15]],
    ],
    "Žled od 20 min., do 30 min. kasneje.": [
        "sentence",
        [
            "starting-then-stopping-later",
            "heavy-sleet",
            ["minutes", 20],
            ["minutes", 30],
        ],
    ],
    "Dež do 25 min., začelo bo zopet 8 min. kasneje.": [
        "sentence",
        [
            "stopping-then-starting-later",
            "medium-rain",
            ["minutes", 25],
            ["minutes", 8],
        ],
    ],
    "Pretežno oblačno čez dan.": ["sentence", ["for-day", "medium-clouds"]],
    "Rahel žled od zjutraj.": ["sentence", ["starting", "very-light-sleet", "morning"]],
    "Močne padavine do popoldan.": [
        "sentence",
        ["until", "heavy-precipitation", "afternoon"],
    ],
    "Vetrovno popoldan.": ["sentence", ["during", "light-wind", "afternoon"]],
    "Sneg drevi in jutri zjutraj.": [
        "sentence",
        ["during", "medium-snow", ["and", "later-today-evening", "tomorrow-morning"]],
    ],
    "Močan dež do kasneje to jutro, začelo bo zopet danes zvečer.": [
        "sentence",
        ["until-starting-again", "heavy-rain", "later-today-morning", "today-evening"],
    ],
    "Oblačno začel zvečer, do zvečer.": [
        "sentence",
        ["starting-continuing-until", "heavy-clouds", "evening", "night"],
    ],
    "Rahel žled kasneje popoldan in megleno jutri zjutraj.": [
        "sentence",
        [
            "and",
            ["during", "light-sleet", "later-today-afternoon"],
            ["during", "fog", "tomorrow-morning"],
        ],
    ],
    "Močni sunki vetra začel danes zjutraj, do danes popoldan, in dež s snegom jutri zjutraj.": [
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
    "Oblačno od danes čez noč in močno sneženje jutri popoldne.": [
        "sentence",
        [
            "and",
            ["starting", "heavy-clouds", "later-today-night"],
            ["during", "heavy-snow", "tomorrow-afternoon"],
        ],
    ],
    "Suho danes ponoči in rahle padavine začel jutri zvečer, do jutri zvečer.": [
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
    "Sneg (5 in.) zvečer.": [
        "sentence",
        ["during", ["parenthetical", "medium-snow", ["inches", 5]], "night"],
    ],
    "Rahlo sneženje (2 cm.) kasneje to jutro.": [
        "sentence",
        [
            "during",
            ["parenthetical", "light-snow", ["centimeters", 2]],
            "later-today-morning",
        ],
    ],
    "Močno sneženje (8\u201312 in.) čez dan.": [
        "sentence",
        ["for-day", ["parenthetical", "heavy-snow", ["inches", ["range", 8, 12]]]],
    ],
    "Sneg (manj kot 1 cm.) popoldan.": [
        "sentence",
        [
            "during",
            ["parenthetical", "medium-snow", ["less-than", ["centimeters", 1]]],
            "afternoon",
        ],
    ],
    "Brez padavin čez teden, s temperaturami do 85\u00b0F jutri.": [
        "sentence",
        [
            "with",
            ["for-week", "no-precipitation"],
            ["temperatures-peaking", ["fahrenheit", 85], "tomorrow"],
        ],
    ],
    "Možne padavine v soboto in nedeljo, s temperaturami do 32\u00b0C v četrtek.": [
        "sentence",
        [
            "with",
            ["over-weekend", "mixed-precipitation"],
            ["temperatures-rising", ["celsius", 32], "thursday"],
        ],
    ],
    "Rosenje v ponedeljek, s najnižjimi temperaturami okoli 15\u00b0F v petek.": [
        "sentence",
        [
            "with",
            ["during", "very-light-rain", "monday"],
            ["temperatures-valleying", ["fahrenheit", 15], "friday"],
        ],
    ],
    "Rahlo sneženje v torek in sredo, s temperaturami do 0\u00b0C v nedeljo.": [
        "sentence",
        [
            "with",
            ["during", "light-snow", ["and", "tuesday", "wednesday"]],
            ["temperatures-falling", ["celsius", 0], "sunday"],
        ],
    ],
    "Padavine danes do v soboto, s temperaturami do 100\u00b0F v ponedeljek.": [
        "sentence",
        [
            "with",
            ["during", "medium-precipitation", ["through", "today", "saturday"]],
            ["temperatures-peaking", ["fahrenheit", 100], "monday"],
        ],
    ],
    "Možne padavine (1\u20133 in.) čez dan.": [
        "sentence",
        [
            "for-day",
            ["parenthetical", "mixed-precipitation", ["inches", ["range", 1, 3]]],
        ],
    ],
    "Močno sneženje (1\u20133 in.)": [
        "title",
        ["parenthetical", "heavy-snow", ["inches", ["range", 1, 3]]],
    ],
    "Močno sneženje (3\u20135 cm.)": [
        "title",
        ["parenthetical", "heavy-snow", ["centimeters", ["range", 3, 5]]],
    ],
    "Urne napovedi začasno niso na voljo, ker so vse bližnje radarske postaje brez povezave.": [
        "sentence",
        ["next-hour-forecast-status", "temporarily-unavailable", "station-offline"],
    ],
    "Urne napovedi delno niso na voljo, ker imajo bližnje radarske postaje pomanjkljivo pokritost.": [
        "sentence",
        ["next-hour-forecast-status", "partially-unavailable", "station-incomplete"],
    ],
    "Urne napovedi niso na voljo, ker so vse bližnje radarske postaje brez povezave.": [
        "sentence",
        ["next-hour-forecast-status", "unavailable", "station-offline"],
    ],
}
