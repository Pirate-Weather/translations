# This would be one of your translations, as a Python dictionary
cases = {
    "Vedro": ["title", "clear"],
    "Moguće su slabe padaline": ["title", "possible-very-light-precipitation"],
    "Slabe padaline": ["title", "very-light-precipitation"],
    "Moguće su slabe padaline": ["title", "possible-light-precipitation"],
    "Slabe padaline": ["title", "light-precipitation"],
    "Padaline": ["title", "medium-precipitation"],
    "Jake padaline": ["title", "heavy-precipitation"],
    "Moguća je sitna kiša": ["title", "possible-very-light-rain"],
    "Sitna kiša": ["title", "very-light-rain"],
    "Moguća je sitna kiša": ["title", "possible-light-rain"],
    "Sitna kiša": ["title", "light-rain"],
    "Kiša": ["title", "medium-rain"],
    "Jaka kiša": ["title", "heavy-rain"],
    "Moguća je slaba susnježica": ["title", "possible-very-light-sleet"],
    "Slaba susnježica": ["title", "very-light-sleet"],
    "Moguća je slaba susnježica": ["title", "possible-light-sleet"],
    "Slaba susnježica": ["title", "light-sleet"],
    "Susnježica": ["title", "medium-sleet"],
    "Jaka susnježica": ["title", "heavy-sleet"],
    "Moguć je sitan snijeg": ["title", "possible-very-light-snow"],
    "Sitan snijeg": ["title", "very-light-snow"],
    "Moguć je sitan snijeg": ["title", "possible-light-snow"],
    "Sitan snijeg": ["title", "light-snow"],
    "Snijeg": ["title", "medium-snow"],
    "Jak snijeg": ["title", "heavy-snow"],
    "Vjetrovito": ["title", "medium-wind"],
    "Jako vjetrovito": ["title", "heavy-wind"],
    "Maglovito": ["title", "fog"],
    "Pretežno vedro": ["title", "very-light-clouds"],
    "Djelomice oblačno": ["title", "light-clouds"],
    "Pretežno oblačno": ["title", "medium-clouds"],
    "Oblačno": ["title", "heavy-clouds"],
    "Suho i malo vjetrovito": ["title", ["and", "low-humidity", "light-wind"]],
    "Sitna kiša i jako vjetrovito": ["title", ["and", "very-light-rain", "heavy-wind"]],
    "Vlažno i djelomice oblačno": ["title", ["and", "high-humidity", "light-clouds"]],
    "Vedro za sat.": ["sentence", ["for-hour", "clear"]],
    "Sitan snijeg počinje za 35 minuta.": [
        "sentence",
        ["starting-in", "very-light-snow", ["minutes", 35]],
    ],
    "Sitna kiša prestaje za 15 minuta.": [
        "sentence",
        ["stopping-in", "light-rain", ["minutes", 15]],
    ],
    "Jaka susnježica počinje za 20 minuta, pa prestaje za 30 minuta.": [
        "sentence",
        [
            "starting-then-stopping-later",
            "heavy-sleet",
            ["minutes", 20],
            ["minutes", 30],
        ],
    ],
    "Kiša prestaje za 25 minuta, pa počinje za 8 minuta.": [
        "sentence",
        [
            "stopping-then-starting-later",
            "medium-rain",
            ["minutes", 25],
            ["minutes", 8],
        ],
    ],
    "Pretežno oblačno tijekom cijelog dana.": [
        "sentence",
        ["for-day", "medium-clouds"],
    ],
    "Slaba susnježica od ujutro.": [
        "sentence",
        ["starting", "very-light-sleet", "morning"],
    ],
    "Vjetrovito do noćas.": ["sentence", ["until", "medium-wind", "today-night"]],
    "Jake padaline do popodne.": [
        "sentence",
        ["until", "heavy-precipitation", "afternoon"],
    ],
    "Malo vjetrovito popodne.": ["sentence", ["during", "light-wind", "afternoon"]],
    "Snijeg kasnije večeras i sutra ujutro.": [
        "sentence",
        ["during", "medium-snow", ["and", "later-today-evening", "tomorrow-morning"]],
    ],
    "Jaka kiša do kasnije ovog jutra, i opet počinje večeras.": [
        "sentence",
        ["until-starting-again", "heavy-rain", "later-today-morning", "today-evening"],
    ],
    "Oblačno počinje navečer, ostaje do u noći.": [
        "sentence",
        ["starting-continuing-until", "heavy-clouds", "evening", "night"],
    ],
    "Slaba susnježica kasnije poslijepodne i maglovito sutra ujutro.": [
        "sentence",
        [
            "and",
            ["during", "light-sleet", "later-today-afternoon"],
            ["during", "fog", "tomorrow-morning"],
        ],
    ],
    "Jako vjetrovito počinje ovo jutro, ostaje do poslijepodne, i susnježica sutra ujutro.": [
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
    "Oblačno od kasnije noćas i jak snijeg sutra popodne.": [
        "sentence",
        [
            "and",
            ["starting", "heavy-clouds", "later-today-night"],
            ["during", "heavy-snow", "tomorrow-afternoon"],
        ],
    ],
    "Suho noćas i slabe padaline počinje sutra navečer, ostaje do sutra u noći.": [
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
    "Snijeg (5 inča) u noći.": [
        "sentence",
        ["during", ["parenthetical", "medium-snow", ["inches", 5]], "night"],
    ],
    "Sitan snijeg (2 centimetra) kasnije ovog jutra.": [
        "sentence",
        [
            "during",
            ["parenthetical", "light-snow", ["centimeters", 2]],
            "later-today-morning",
        ],
    ],
    "Jak snijeg (8\u201312 inča) tijekom cijelog dana.": [
        "sentence",
        ["for-day", ["parenthetical", "heavy-snow", ["inches", ["range", 8, 12]]]],
    ],
    "Snijeg (ispod 1 centimetra) popodne.": [
        "sentence",
        [
            "during",
            ["parenthetical", "medium-snow", ["less-than", ["centimeters", 1]]],
            "afternoon",
        ],
    ],
    "Nema padalina tijekom tjedna, s maksimalnom temperaturom do 85°F sutra.": [
        "sentence",
        [
            "with",
            ["for-week", "no-precipitation"],
            ["temperatures-peaking", ["fahrenheit", 85], "tomorrow"],
        ],
    ],
    "Mješavina padalina tijekom vikenda, s temperaturom u porastu do 32\u00b0C u četvrtak.": [
        "sentence",
        [
            "with",
            ["over-weekend", "mixed-precipitation"],
            ["temperatures-rising", ["celsius", 32], "thursday"],
        ],
    ],
    "Sitna kiša u ponedjeljak, s najnižom temperaturom do 15°F u petak.": [
        "sentence",
        [
            "with",
            ["during", "very-light-rain", "monday"],
            ["temperatures-valleying", ["fahrenheit", 15], "friday"],
        ],
    ],
    "Sitan snijeg u utorak i sljedeću srijedu, s padom temperature do 0\u00b0C u nedjelju.": [
        "sentence",
        [
            "with",
            ["during", "light-snow", ["and", "tuesday", "next-wednesday"]],
            ["temperatures-falling", ["celsius", 0], "sunday"],
        ],
    ],
    "Padaline danas do u subotu, s maksimalnom temperaturom do 100\u00b0F u ponedjeljak.": [
        "sentence",
        [
            "with",
            ["during", "medium-precipitation", ["through", "today", "saturday"]],
            ["temperatures-peaking", ["fahrenheit", 100], "monday"],
        ],
    ],
    "Moguća grmljavina": ["title", "possible-thunderstorm"],
    "Jaka kiša i grmljavina": ["title", ["and", "heavy-rain", "thunderstorm"]],
}
