# This would be one of your translations, as a Python dictionary
cases = {
    "Vedro": ["title", "clear"],
    "Moguće su slabe padavine": ["title", "possible-very-light-precipitation"],
    "Slabe padavine": ["title", "very-light-precipitation"],
    "Moguće su slabe padavine": ["title", "possible-light-precipitation"],
    "Slabe padavine": ["title", "light-precipitation"],
    "Padavine": ["title", "medium-precipitation"],
    "Jake padavine": ["title", "heavy-precipitation"],
    "Moguće je sitna kiša": ["title", "possible-very-light-rain"],
    "Sitna kiša": ["title", "very-light-rain"],
    "Moguće je sitna kiša": ["title", "possible-light-rain"],
    "Sitna kiša": ["title", "light-rain"],
    "Kiša": ["title", "medium-rain"],
    "Jaka kiša": ["title", "heavy-rain"],
    "Moguće je slaba susnježica": ["title", "possible-very-light-sleet"],
    "Slaba susnježica": ["title", "very-light-sleet"],
    "Moguće je slaba susnježica": ["title", "possible-light-sleet"],
    "Slaba susnježica": ["title", "light-sleet"],
    "Susnježica": ["title", "medium-sleet"],
    "Jaka susnježica": ["title", "heavy-sleet"],
    "Moguće je sitan snijeg": ["title", "possible-very-light-snow"],
    "Sitan snijeg": ["title", "very-light-snow"],
    "Moguće je sitan snijeg": ["title", "possible-light-snow"],
    "Sitan snijeg": ["title", "light-snow"],
    "Snijeg": ["title", "medium-snow"],
    "Jak snijeg": ["title", "heavy-snow"],
    "Vjetrovito": ["title", "medium-wind"],
    "Opasno vjetrovito": ["title", "heavy-wind"],
    "Maglovito": ["title", "fog"],
    "Pretežno vedro": ["title", "very-light-clouds"],
    "Djelom oblačno": ["title", "light-clouds"],
    "Pretežno oblačno": ["title", "medium-clouds"],
    "Oblačno": ["title", "heavy-clouds"],
    "Suho i vjetrovito": ["title", ["and", "low-humidity", "light-wind"]],
    "Sitna kiša i opasno vjetrovito": [
        "title",
        ["and", "very-light-rain", "heavy-wind"],
    ],
    "Vlažno i djelom oblačno": ["title", ["and", "high-humidity", "light-clouds"]],
    "Vedro za ovaj sat.": ["sentence", ["for-hour", "clear"]],
    "Sitan snijeg počinje za 35 minuta.": [
        "sentence",
        ["starting-in", "very-light-snow", ["minutes", 35]],
    ],
    "Sitna kiša prekida za 15 minuta.": [
        "sentence",
        ["stopping-in", "light-rain", ["minutes", 15]],
    ],
    "Jaka susnježica počinje za 20 minuta, ondak prekida za 30 minuta.": [
        "sentence",
        [
            "starting-then-stopping-later",
            "heavy-sleet",
            ["minutes", 20],
            ["minutes", 30],
        ],
    ],
    "Kiša prekida za 25 minuta, ondak počinje za 8 minuta.": [
        "sentence",
        [
            "stopping-then-starting-later",
            "medium-rain",
            ["minutes", 25],
            ["minutes", 8],
        ],
    ],
    "Pretežno oblačno tokom cijelog dana.": ["sentence", ["for-day", "medium-clouds"]],
    "Slaba susnježica počinje ujutro.": [
        "sentence",
        ["starting", "very-light-sleet", "morning"],
    ],
    "Vjetrovito do u noć.": ["sentence", ["until", "medium-wind", "today-night"]],
    "Jake padavine do popodne.": [
        "sentence",
        ["until", "heavy-precipitation", "afternoon"],
    ],
    "Vjetrovito popodne.": ["sentence", ["during", "light-wind", "afternoon"]],
    "Snijeg kasnije večeras i sutra ujutro.": [
        "sentence",
        ["during", "medium-snow", ["and", "later-today-evening", "tomorrow-morning"]],
    ],
    "Jaka kiša do kasnije ovog jutra, i opet poćinje večeras.": [
        "sentence",
        ["until-starting-again", "heavy-rain", "later-today-morning", "today-evening"],
    ],
    "Oblačno poćinje uveče, ostaje do u noć.": [
        "sentence",
        ["starting-continuing-until", "heavy-clouds", "evening", "night"],
    ],
    "Slaba susnježica kasnije ove podne i maglovito sutra ujutro.": [
        "sentence",
        [
            "and",
            ["during", "light-sleet", "later-today-afternoon"],
            ["during", "fog", "tomorrow-morning"],
        ],
    ],
    "Opasno vjetrovito poćinje ovo jutro, ostaje do ove podne, i susnježica sutra ujutro.": [
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
    "Oblačno počinje kasnije u noć i jak snijeg sutra popodne.": [
        "sentence",
        [
            "and",
            ["starting", "heavy-clouds", "later-today-night"],
            ["during", "heavy-snow", "tomorrow-afternoon"],
        ],
    ],
    "Suho u noć i slabe padavine poćinje sutra uveče, ostaje do sutra u noć.": [
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
    "Snijeg (5 inča) u noć.": [
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
    "Jak snijeg (8\u201312 inča) tokom cijelog dana.": [
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
    "Nema padavina tokom sedmice, sa temperaturom najviše do 85°F sutra.": [
        "sentence",
        [
            "with",
            ["for-week", "no-precipitation"],
            ["temperatures-peaking", ["fahrenheit", 85], "tomorrow"],
        ],
    ],
    "Različite padavine tokom vikenda, sa temperaturom raste do 32\u00b0C u četvrtak.": [
        "sentence",
        [
            "with",
            ["over-weekend", "mixed-precipitation"],
            ["temperatures-rising", ["celsius", 32], "thursday"],
        ],
    ],
    "Sitna kiša u ponedjeljak, sa temperaturom najniže do 15°F u petak.": [
        "sentence",
        [
            "with",
            ["during", "very-light-rain", "monday"],
            ["temperatures-valleying", ["fahrenheit", 15], "friday"],
        ],
    ],
    "Sitan snijeg u utorak i srijeda, sa temperaturom pada do 0\u00b0C u nedjelju.": [
        "sentence",
        [
            "with",
            ["during", "light-snow", ["and", "tuesday", "wednesday"]],
            ["temperatures-falling", ["celsius", 0], "sunday"],
        ],
    ],
    "Padavine danas do u subotu, sa temperaturom najviše do 100\u00b0F u ponedjeljak.": [
        "sentence",
        [
            "with",
            ["during", "medium-precipitation", ["through", "today", "saturday"]],
            ["temperatures-peaking", ["fahrenheit", 100], "monday"],
        ],
    ],
    "Dim": ['title', 'smoke'],
    "Dim tokom cijelog dana.": ['sentence', ['for-day', 'smoke']],
    "Dim ujutro.": ['sentence', ['during', 'smoke', 'morning']],
    "Dim do večeras.": ['sentence', ['until', 'smoke', 'today-evening']],
    "Dim i djelom oblačno": ['title', ['and', 'smoke', 'light-clouds']],
    "Izmaglica": ['title', 'haze'],
    "Izmaglica tokom cijelog dana.": ['sentence', ['for-day', 'haze']],
    "Izmaglica popodne.": ['sentence', ['during', 'haze', 'afternoon']],
    "Izmaglica i vlažno": ['title', ['and', 'haze', 'high-humidity']],
    "Magla": ['title', 'mist'],
    "Magla tokom cijelog dana.": ['sentence', ['for-day', 'mist']],
    "Magla u noć.": ['sentence', ['during', 'mist', 'night']],
    "Magla i oblačno": ['title', ['and', 'mist', 'heavy-clouds']],
    "Grmljavine za ovaj sat.": ["sentence", ["for-hour", "thunderstorm"]],
    "Grmljavina sa gradom počinje za 5 minuta, ondak prekida za 45 minuta.": [
        "sentence",
        [
            "starting-then-stopping-later",
            "hail",
            ["minutes", 5],
            ["minutes", 45],
        ],
    ],
    "Jaka ledena kiša prekida za 10 minuta, ondak počinje za 32 minuta.": [
        "sentence",
        [
            "stopping-then-starting-later",
            "heavy-freezing-rain",
            ["minutes", 10],
            ["minutes", 32],
        ],
    ],
    "Ledena kiša počinje za 49 minuta.": [
        "sentence",
        ["starting-in", "very-light-freezing-rain", ["minutes", 49]],
    ],
}
