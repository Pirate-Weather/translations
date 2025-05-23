# This would be one of your translations, as a Python dictionary
cases = {
    "Vedro": ["title", "clear"],
    "Moguće su veoma slabe padavine": ["title", "possible-very-light-precipitation"],
    "Slabe padavine": ["title", "very-light-precipitation"],
    "Moguće su slabe padavine": ["title", "possible-light-precipitation"],
    "Slabe padavine": ["title", "light-precipitation"],
    "Padavine": ["title", "medium-precipitation"],
    "Jake padavine": ["title", "heavy-precipitation"],
    "Moguća je veoma sitna kiša": ["title", "possible-very-light-rain"],
    "Veoma sitna kiša": ["title", "very-light-rain"],
    "Moguća je sitna kiša": ["title", "possible-light-rain"],
    "Sitna kiša": ["title", "light-rain"],
    "Kiša": ["title", "medium-rain"],
    "Jaka kiša": ["title", "heavy-rain"],
    "Moguća je veoma slaba susnežica": ["title", "possible-very-light-sleet"],
    "Veoma slaba susnežica": ["title", "very-light-sleet"],
    "Moguća je slaba susnežica": ["title", "possible-light-sleet"],
    "Slaba susnežica": ["title", "light-sleet"],
    "Susnežica": ["title", "medium-sleet"],
    "Jaka susnežica": ["title", "heavy-sleet"],
    "Moguć je veoma sitan sneg": ["title", "possible-very-light-snow"],
    "Veoma sitan sneg": ["title", "very-light-snow"],
    "Moguć je sitan sneg": ["title", "possible-light-snow"],
    "Sitan sneg": ["title", "light-snow"],
    "Sneg": ["title", "medium-snow"],
    "Jak sneg": ["title", "heavy-snow"],
    "Vetrovito": ["title", "medium-wind"],
    "Opasno vetrovito": ["title", "heavy-wind"],
    "Maglovito": ["title", "fog"],
    "Pretežno vedro": ["title", "very-light-clouds"],
    "Mestimično oblačno": ["title", "light-clouds"],
    "Pretežno oblačno": ["title", "medium-clouds"],
    "Oblačno": ["title", "heavy-clouds"],
    "Suvo i vetrovito": ["title", ["and", "low-humidity", "light-wind"]],
    "Veoma sitna kiša i opasno vetrovito": [
        "title",
        ["and", "very-light-rain", "heavy-wind"],
    ],
    "Vlažno i mestimično oblačno": ["title", ["and", "high-humidity", "light-clouds"]],
    "Vedro za ovaj sat.": ["sentence", ["for-hour", "clear"]],
    "Veoma sitan sneg počinje za 35 minuta.": [
        "sentence",
        ["starting-in", "very-light-snow", ["minutes", 35]],
    ],
    "Sitna kiša prestaje za 15 minuta.": [
        "sentence",
        ["stopping-in", "light-rain", ["minutes", 15]],
    ],
    "Jaka susnežica počinje za 20 minuta, onda prestaje za 30 minuta.": [
        "sentence",
        [
            "starting-then-stopping-later",
            "heavy-sleet",
            ["minutes", 20],
            ["minutes", 30],
        ],
    ],
    "Kiša prestaje za 25 minuta, onda počinje za 8 minuta.": [
        "sentence",
        [
            "stopping-then-starting-later",
            "medium-rain",
            ["minutes", 25],
            ["minutes", 8],
        ],
    ],
    "Pretežno oblačno tokom celog dana.": ["sentence", ["for-day", "medium-clouds"]],
    "Veoma slaba susnežica počinje ujutro.": [
        "sentence",
        ["starting", "very-light-sleet", "morning"],
    ],
    "Vetrovito do večeras.": ["sentence", ["until", "medium-wind", "today-night"]],
    "Jake padavine do popodne.": [
        "sentence",
        ["until", "heavy-precipitation", "afternoon"],
    ],
    "Vetrovito popodne.": ["sentence", ["during", "light-wind", "afternoon"]],
    "Sneg kasno uveče i sutra ujutro.": [
        "sentence",
        ["during", "medium-snow", ["and", "later-today-evening", "tomorrow-morning"]],
    ],
    "Jaka kiša kasnije ovog jutra i opet počinje uveče.": [
        "sentence",
        ["until-starting-again", "heavy-rain", "later-today-morning", "today-evening"],
    ],
    "Oblačno počev od uveče, nastaviće se tokom noći.": [
        "sentence",
        ["starting-continuing-until", "heavy-clouds", "evening", "night"],
    ],
    "Kasnije ovog popodneva slaba susnežica, sutra ujutro maglovito.": [
        "sentence",
        [
            "and",
            ["during", "light-sleet", "later-today-afternoon"],
            ["during", "fog", "tomorrow-morning"],
        ],
    ],
    "Opasno vetrovito počev od ovog jutra, nastaviće se ovog popodneva, sutra ujutro susnežica.": [
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
    "Oblačno počinje kasnije tokom noći, sutra popodne jak sneg.": [
        "sentence",
        [
            "and",
            ["starting", "heavy-clouds", "later-today-night"],
            ["during", "heavy-snow", "tomorrow-afternoon"],
        ],
    ],
    "Večeras suvo, slabe padavine počinju sutra uveče, nastaviće se tokom noći.": [
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
    "Sneg (5 inča) tokom noći.": [
        "sentence",
        ["during", ["parenthetical", "medium-snow", ["inches", 5]], "night"],
    ],
    "Sitan sneg (2cm) kasnije tokom ovog jutra.": [
        "sentence",
        [
            "during",
            ["parenthetical", "light-snow", ["centimeters", 2]],
            "later-today-morning",
        ],
    ],
    "Jak sneg (8\u201312 inča) tokom celog dana.": [
        "sentence",
        ["for-day", ["parenthetical", "heavy-snow", ["inches", ["range", 8, 12]]]],
    ],
    "Sneg (ispod 1cm) popodne.": [
        "sentence",
        [
            "during",
            ["parenthetical", "medium-snow", ["less-than", ["centimeters", 1]]],
            "afternoon",
        ],
    ],
    "Nema padavina tokom sedmice, sa temperaturom najviše do 85°F sutra.": [
        "sentence",
        [
            "with",
            ["for-week", "no-precipitation"],
            ["temperatures-peaking", ["fahrenheit", 85], "tomorrow"],
        ],
    ],
    "Različite padavine tokom vikenda, sa temperaturnim rastom do 32\u00b0C u četvrtak.": [
        "sentence",
        [
            "with",
            ["over-weekend", "mixed-precipitation"],
            ["temperatures-rising", ["celsius", 32], "thursday"],
        ],
    ],
    "Veoma sitna kiša u ponedeljak, sa temperaturom najniže do 15°F u petak.": [
        "sentence",
        [
            "with",
            ["during", "very-light-rain", "monday"],
            ["temperatures-valleying", ["fahrenheit", 15], "friday"],
        ],
    ],
    "Sitan sneg u utorak i sredu, sa temperaturnim padom do 0\u00b0C u nedelju.": [
        "sentence",
        [
            "with",
            ["during", "light-snow", ["and", "tuesday", "wednesday"]],
            ["temperatures-falling", ["celsius", 0], "sunday"],
        ],
    ],
    "Padavine od danas do subote, sa temperaturom najviše do 100\u00b0F u ponedeljak.": [
        "sentence",
        [
            "with",
            ["during", "medium-precipitation", ["through", "today", "saturday"]],
            ["temperatures-peaking", ["fahrenheit", 100], "monday"],
        ],
    ],
    "Padavine od danas do nedelje, sa temperaturom najviše do 100\u00b0F u utorak.": [
        "sentence",
        [
            "with",
            ["during", "medium-precipitation", ["through", "today", "sunday"]],
            ["temperatures-peaking", ["fahrenheit", 100], "tuesday"],
        ],
    ],
    "Padavine od danas do ponedeljka, sa temperaturom najviše do 100\u00b0F u sredu.": [
        "sentence",
        [
            "with",
            ["during", "medium-precipitation", ["through", "today", "monday"]],
            ["temperatures-peaking", ["fahrenheit", 100], "wednesday"],
        ],
    ],
    "Padavine od danas do utorka, sa temperaturom najviše do 100\u00b0F u četvrtak.": [
        "sentence",
        [
            "with",
            ["during", "medium-precipitation", ["through", "today", "tuesday"]],
            ["temperatures-peaking", ["fahrenheit", 100], "thursday"],
        ],
    ],
    "Padavine od danas do srede, sa temperaturom najviše do 100\u00b0F u petak.": [
        "sentence",
        [
            "with",
            ["during", "medium-precipitation", ["through", "today", "wednesday"]],
            ["temperatures-peaking", ["fahrenheit", 100], "friday"],
        ],
    ],
    "Padavine od danas do četvrtka, sa temperaturom najviše do 100\u00b0F u subotu.": [
        "sentence",
        [
            "with",
            ["during", "medium-precipitation", ["through", "today", "thursday"]],
            ["temperatures-peaking", ["fahrenheit", 100], "saturday"],
        ],
    ],
    "Padavine od danas do petka, sa temperaturom najviše do 100\u00b0F u nedelju.": [
        "sentence",
        [
            "with",
            ["during", "medium-precipitation", ["through", "today", "friday"]],
            ["temperatures-peaking", ["fahrenheit", 100], "sunday"],
        ],
    ],
}
