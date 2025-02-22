# This would be one of your translations, as a Python dictionary
cases = {
    "Senin": ["title", "clear"],
    "Posibile Precipitații Foarte Slabe": [
        "title",
        "possible-very-light-precipitation",
    ],
    "Precipitații Foarte Slabe": ["title", "very-light-precipitation"],
    "Posibile Precipitații Slabe": ["title", "possible-light-precipitation"],
    "Precipitații Slabe": ["title", "light-precipitation"],
    "Precipitații": ["title", "medium-precipitation"],
    "Precipitații Abundente": ["title", "heavy-precipitation"],
    "Posibil Burniță": ["title", "possible-very-light-rain"],
    "Burniță": ["title", "very-light-rain"],
    "Posibil Ploaie Ușoară": ["title", "possible-light-rain"],
    "Ploaie Ușoară": ["title", "light-rain"],
    "Ploaie": ["title", "medium-rain"],
    "Ploaie Torențială": ["title", "heavy-rain"],
    "Posibil Lapoviță": ["title", "possible-very-light-sleet"],
    "Lapoviță": ["title", "very-light-sleet"],
    "Posibil Lapoviță": ["title", "possible-light-sleet"],
    "Lapoviță": ["title", "light-sleet"],
    "Lapoviță": ["title", "medium-sleet"],
    "Lapoviță și Ninsoare": ["title", "heavy-sleet"],
    "Posibil Ninsoare Slabă": ["title", "possible-very-light-snow"],
    "Ninsoare Slabă": ["title", "very-light-snow"],
    "Posibil Ninsoare Slabă": ["title", "possible-light-snow"],
    "Ninsoare Slabă": ["title", "light-snow"],
    "Ninsoare": ["title", "medium-snow"],
    "Ninsoare Puternică": ["title", "heavy-snow"],
    "Bate Vântul": ["title", "medium-wind"],
    "Vânt Puternic": ["title", "heavy-wind"],
    "Ceață": ["title", "fog"],
    "Predominant Senin": ["title", "very-light-clouds"],
    "Parțial Noros": ["title", "light-clouds"],
    "Predominant Noros": ["title", "medium-clouds"],
    "Noros": ["title", "heavy-clouds"],
    "Umiditate Scăzută și Vânt Ușor": ["title", ["and", "low-humidity", "light-wind"]],
    "Burniță și Vânt Puternic": ["title", ["and", "very-light-rain", "heavy-wind"]],
    "Umiditate Ridicată și Parțial Noros": [
        "title",
        ["and", "high-humidity", "light-clouds"],
    ],
    "Senin în următoarea oră.": ["sentence", ["for-hour", "clear"]],
    "Ploaie torențială în următoarea oră.": ["sentence", ["for-hour", "heavy-rain"]],
    "Ploaie în următoarea oră.": ["sentence", ["for-hour", "medium-rain"]],
    "Ninsoare slabă, în 35 de minute.": [
        "sentence",
        ["starting-in", "very-light-snow", ["minutes", 35]],
    ],
    "Ploaie ușoară, durează 15 minute.": [
        "sentence",
        ["stopping-in", "light-rain", ["minutes", 15]],
    ],
    "Lapoviță și ninsoare peste 20 de minute, durează 30 de minute.": [
        "sentence",
        [
            "starting-then-stopping-later",
            "heavy-sleet",
            ["minutes", 20],
            ["minutes", 30],
        ],
    ],
    "Ploaie, se oprește în 25 de minute, începe din nou 8 minute mai târziu.": [
        "sentence",
        [
            "stopping-then-starting-later",
            "medium-rain",
            ["minutes", 25],
            ["minutes", 8],
        ],
    ],
    "Predominant noros de-a lungul zilei.": ["sentence", ["for-day", "medium-clouds"]],
    "Lapoviță, începând de dimineață.": [
        "sentence",
        ["starting", "very-light-sleet", "morning"],
    ],
    "Bate vântul până la noapte.": [
        "sentence",
        ["until", "medium-wind", "today-night"],
    ],
    "Precipitații abundente până după-masă.": [
        "sentence",
        ["until", "heavy-precipitation", "afternoon"],
    ],
    "Vânt ușor după-masă.": ["sentence", ["during", "light-wind", "afternoon"]],
    "Ninsoare mai târziu în această seară și mâine dimineață.": [
        "sentence",
        ["during", "medium-snow", ["and", "later-today-evening", "tomorrow-morning"]],
    ],
    "Ploaie torențială până mai târziu în această dimineață, începe din nou diseară.": [
        "sentence",
        ["until-starting-again", "heavy-rain", "later-today-morning", "today-evening"],
    ],
    "Noros începând de seara și până la noapte.": [
        "sentence",
        ["starting-continuing-until", "heavy-clouds", "evening", "night"],
    ],
    "Noros începând de mai târziu în această seară și până la noapte.": [
        "sentence",
        ["starting-continuing-until", "heavy-clouds", "later-today-evening", "night"],
    ],
    "Lapoviță mai târziu în această după-amiază și ceață mâine dimineață.": [
        "sentence",
        [
            "and",
            ["during", "light-sleet", "later-today-afternoon"],
            ["during", "fog", "tomorrow-morning"],
        ],
    ],
    "Vânt puternic începând de dimineață și până după-amiază și lapoviță mâine dimineață.": [
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
    "Noros, începând de la noapte și ninsoare puternică maine după-amiază.": [
        "sentence",
        [
            "and",
            ["starting", "heavy-clouds", "later-today-night"],
            ["during", "heavy-snow", "tomorrow-afternoon"],
        ],
    ],
    "Noros, începând de seara și ninsoare puternică maine după-amiază.": [
        "sentence",
        [
            "and",
            ["starting", "heavy-clouds", "evening"],
            ["during", "heavy-snow", "tomorrow-afternoon"],
        ],
    ],
    "Umiditate scăzută la noapte și precipitații slabe începând de mâine seară și până mâine noapte.": [
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
    "Ninsoare (5 in.) la noapte.": [
        "sentence",
        ["during", ["parenthetical", "medium-snow", ["inches", 5]], "night"],
    ],
    "Ninsoare slabă (2 cm.) mai târziu în această dimineață.": [
        "sentence",
        [
            "during",
            ["parenthetical", "light-snow", ["centimeters", 2]],
            "later-today-morning",
        ],
    ],
    "Ninsoare puternică (8\u201312 in.) de-a lungul zilei.": [
        "sentence",
        ["for-day", ["parenthetical", "heavy-snow", ["inches", ["range", 8, 12]]]],
    ],
    "Ninsoare (mai puțin de 1 cm.) după-masă.": [
        "sentence",
        [
            "during",
            ["parenthetical", "medium-snow", ["less-than", ["centimeters", 1]]],
            "afternoon",
        ],
    ],
    "Fără precipitații pe toată durata săptămânii, cu temperaturi ce ating un maxim de 85\u00b0F mâine.": [
        "sentence",
        [
            "with",
            ["for-week", "no-precipitation"],
            ["temperatures-peaking", ["fahrenheit", 85], "tomorrow"],
        ],
    ],
    "Precipitații mixte în weekend, cu temperaturi ce urcă până la 32\u00b0C joi.": [
        "sentence",
        [
            "with",
            ["over-weekend", "mixed-precipitation"],
            ["temperatures-rising", ["celsius", 32], "thursday"],
        ],
    ],
    "Burniță luni, cu temperaturi ce ating un minim de 15\u00b0F vineri.": [
        "sentence",
        [
            "with",
            ["during", "very-light-rain", "monday"],
            ["temperatures-valleying", ["fahrenheit", 15], "friday"],
        ],
    ],
    "Ninsoare slabă marți și miercurea viitoare, cu temperaturi ce coboară până la 0\u00b0C duminică.": [
        "sentence",
        [
            "with",
            ["during", "light-snow", ["and", "tuesday", "next-wednesday"]],
            ["temperatures-falling", ["celsius", 0], "sunday"],
        ],
    ],
    "Precipitații de azi până sâmbătă, cu temperaturi ce ating un maxim de 100\u00b0F luni.": [
        "sentence",
        [
            "with",
            ["during", "medium-precipitation", ["through", "today", "saturday"]],
            ["temperatures-peaking", ["fahrenheit", 100], "monday"],
        ],
    ],
    "Precipitații mixte (1\u20133 in. de zăpadă) de-a lungul zilei.": [
        "sentence",
        [
            "for-day",
            ["parenthetical", "mixed-precipitation", ["inches", ["range", 1, 3]]],
        ],
    ],
    "Ninsoare Puternică (1\u20133 in.)": [
        "title",
        ["parenthetical", "heavy-snow", ["inches", ["range", 1, 3]]],
    ],
    "Ninsoare Puternică (3\u20135 cm.)": [
        "title",
        ["parenthetical", "heavy-snow", ["centimeters", ["range", 3, 5]]],
    ],
    "Posibil Furtună": ["title", "possible-thunderstorm"],
    "Ploaie Torențială și Furtună": ["title", ["and", "heavy-rain", "thunderstorm"]],
    "Burniță, în mai puțin de 1 minut.": [
        "sentence",
        ["starting-in", "very-light-rain", ["less-than", ["minutes", 1]]],
    ],
}
