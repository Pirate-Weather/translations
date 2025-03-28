# This would be one of your translations, as a Python dictionary
cases = {
    "Heiðskýrt": ["title", "clear"],
    "Möguleiki á lítilsháttar úrkomu": ["title", "possible-very-light-precipitation"],
    "Lítilsháttar úrkoma": ["title", "very-light-precipitation"],
    "Möguleiki á smávægilegri úrkomu": ["title", "possible-light-precipitation"],
    "Smávægileg úrkoma": ["title", "light-precipitation"],
    "Úrkoma": ["title", "medium-precipitation"],
    "Mikil úrkoma": ["title", "heavy-precipitation"],
    "Líkur á úða": ["title", "possible-very-light-rain"],
    "Úði": ["title", "very-light-rain"],
    "Líkur á skúrum": ["title", "possible-light-rain"],
    "Skúrir": ["title", "light-rain"],
    "Rigning": ["title", "medium-rain"],
    "Mikil rigning": ["title", "heavy-rain"],
    "Líkur á lítilsháttar slyddu": ["title", "possible-very-light-sleet"],
    "Lítilsháttar slydda": ["title", "very-light-sleet"],
    "Líkur á smávægilegri slyddu": ["title", "possible-light-sleet"],
    "Smávægileg slydda": ["title", "light-sleet"],
    "Slydda": ["title", "medium-sleet"],
    "Mikil slydda": ["title", "heavy-sleet"],
    "Líkur á lítilsháttar snjókomu": ["title", "possible-very-light-snow"],
    "Lítilsháttar snjókoma": ["title", "very-light-snow"],
    "Líkur á smávægilegri snjókomu": ["title", "possible-light-snow"],
    "Smávægileg snjókoma": ["title", "light-snow"],
    "Snjókoma": ["title", "medium-snow"],
    "Mikil snjókoma": ["title", "heavy-snow"],
    "Rok": ["title", "medium-wind"],
    "Hávaðarok": ["title", "heavy-wind"],
    "Þoka": ["title", "fog"],
    "Að mestu leyti skýrt": ["title", "very-light-clouds"],
    "Skýjað að hluta til": ["title", "light-clouds"],
    "Skýjað": ["title", "medium-clouds"],
    "Alskýjað": ["title", "heavy-clouds"],
    "Lítill raki og gola": ["title", ["and", "low-humidity", "light-wind"]],
    "Úði og hávaðarok": ["title", ["and", "very-light-rain", "heavy-wind"]],
    "Mikill raki og skýjað að hluta til": [
        "title",
        ["and", "high-humidity", "light-clouds"],
    ],
    "Heiðskýrt næsta klukkutímann.": ["sentence", ["for-hour", "clear"]],
    "Lítilsháttar snjókoma sem byrjar eftir 35 mín.": [
        "sentence",
        ["starting-in", "very-light-snow", ["minutes", 35]],
    ],
    "Skúrir, líkur eftir 15 mín.": [
        "sentence",
        ["stopping-in", "light-rain", ["minutes", 15]],
    ],
    "Mikil slydda sem byrjar eftir 20 mín., líkur 30 mín. seinna.": [
        "sentence",
        [
            "starting-then-stopping-later",
            "heavy-sleet",
            ["minutes", 20],
            ["minutes", 30],
        ],
    ],
    "Rigning sem líkur eftir 25 mín., byrjar aftur 8 mín. seinna.": [
        "sentence",
        [
            "stopping-then-starting-later",
            "medium-rain",
            ["minutes", 25],
            ["minutes", 8],
        ],
    ],
    "Skýjað yfir daginn.": ["sentence", ["for-day", "medium-clouds"]],
    "Lítilsháttar slydda, byrjar um morguninn.": [
        "sentence",
        ["starting", "very-light-sleet", "morning"],
    ],
    "Rok þangað til í nótt.": ["sentence", ["until", "medium-wind", "today-night"]],
    "Mikil úrkoma þangað til í síðdeginu.": [
        "sentence",
        ["until", "heavy-precipitation", "afternoon"],
    ],
    "Gola í síðdeginu.": ["sentence", ["during", "light-wind", "afternoon"]],
    "Snjókoma seinna í kvöld og í fyrramálið.": [
        "sentence",
        ["during", "medium-snow", ["and", "later-today-evening", "tomorrow-morning"]],
    ],
    "Mikil rigning þangað til seinna um morguninn, byrjar aftur í kvöld.": [
        "sentence",
        ["until-starting-again", "heavy-rain", "later-today-morning", "today-evening"],
    ],
    "Alskýjað, byrjar um kvöldið og heldur áfram yfir nóttina.": [
        "sentence",
        ["starting-continuing-until", "heavy-clouds", "evening", "night"],
    ],
    "Smávægileg slydda seinnipart dags og þoka í fyrramálið.": [
        "sentence",
        [
            "and",
            ["during", "light-sleet", "later-today-afternoon"],
            ["during", "fog", "tomorrow-morning"],
        ],
    ],
    "Hávaðarok, byrjar þennan morguninn og heldur áfram yfir þennan eftirmiðsdag - slydda í fyrramálið.": [
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
    "Alskýjað, byrjar seinna í nótt - mikil snjókoma seinnipart morgundags.": [
        "sentence",
        [
            "and",
            ["starting", "heavy-clouds", "later-today-night"],
            ["during", "heavy-snow", "tomorrow-afternoon"],
        ],
    ],
    "Lítill raki í nótt og smávægileg úrkoma, byrjar annað kvöld og heldur áfram yfir næstu nótt.": [
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
    "Snjókoma (5 in.) yfir nóttina.": [
        "sentence",
        ["during", ["parenthetical", "medium-snow", ["inches", 5]], "night"],
    ],
    "Smávægileg snjókoma (2 cm.) seinna um morguninn.": [
        "sentence",
        [
            "during",
            ["parenthetical", "light-snow", ["centimeters", 2]],
            "later-today-morning",
        ],
    ],
    "Mikil snjókoma (8\u201312 in.) yfir daginn.": [
        "sentence",
        ["for-day", ["parenthetical", "heavy-snow", ["inches", ["range", 8, 12]]]],
    ],
    "Snjókoma (undir 1 cm.) í síðdeginu.": [
        "sentence",
        [
            "during",
            ["parenthetical", "medium-snow", ["less-than", ["centimeters", 1]]],
            "afternoon",
        ],
    ],
    "Engin úrkoma yfir vikuna, með hita upp að 85\u00b0F á morgun.": [
        "sentence",
        [
            "with",
            ["for-week", "no-precipitation"],
            ["temperatures-peaking", ["fahrenheit", 85], "tomorrow"],
        ],
    ],
    "Úrkoma með köflum yfir helgina, með hita að nálgast 32\u00b0C á fimmtudag.": [
        "sentence",
        [
            "with",
            ["over-weekend", "mixed-precipitation"],
            ["temperatures-rising", ["celsius", 32], "thursday"],
        ],
    ],
    "Úði á mánudag, með hita niður í 15\u00b0F á föstudag.": [
        "sentence",
        [
            "with",
            ["during", "very-light-rain", "monday"],
            ["temperatures-valleying", ["fahrenheit", 15], "friday"],
        ],
    ],
    "Smávægileg snjókoma á þriðjudag og miðvikudag, með hita að falla niður í 0\u00b0C á sunnudag.": [
        "sentence",
        [
            "with",
            ["during", "light-snow", ["and", "tuesday", "wednesday"]],
            ["temperatures-falling", ["celsius", 0], "sunday"],
        ],
    ],
    "Úrkoma í dag þangað til á laugardag, með hita upp að 100\u00b0F á mánudag.": [
        "sentence",
        [
            "with",
            ["during", "medium-precipitation", ["through", "today", "saturday"]],
            ["temperatures-peaking", ["fahrenheit", 100], "monday"],
        ],
    ],
    "Úrkoma með köflum (1\u20133 in.) yfir daginn.": [
        "sentence",
        [
            "for-day",
            ["parenthetical", "mixed-precipitation", ["inches", ["range", 1, 3]]],
        ],
    ],
    "Mikil snjókoma (1\u20133 in.)": [
        "title",
        ["parenthetical", "heavy-snow", ["inches", ["range", 1, 3]]],
    ],
    "Mikil snjókoma (3\u20135 cm.)": [
        "title",
        ["parenthetical", "heavy-snow", ["centimeters", ["range", 3, 5]]],
    ],
}
