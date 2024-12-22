# This would be one of your translations, as a Python dictionary
cases = {
    "Pas": ["title", "clear"],
    "Karik Udan Uituan Deit": ["title", "possible-very-light-precipitation"],
    "Udan Uituan Deit": ["title", "very-light-precipitation"],
    "Karik Udan Uituan": ["title", "possible-light-precipitation"],
    "Udan Uituan": ["title", "light-precipitation"],
    "Udan": ["title", "medium-precipitation"],
    "Udan Bo'ot": ["title", "heavy-precipitation"],
    "Karik Udan Uituan Deit": ["title", "possible-very-light-rain"],
    "Udan Uituan Deit": ["title", "very-light-rain"],
    "Karik Udan Uituan": ["title", "possible-light-rain"],
    "Udan Uituan": ["title", "light-rain"],
    "Udan": ["title", "medium-rain"],
    "Udan Bo'ot": ["title", "heavy-rain"],
    "Karik Udan - Salju Kahur Uituan Deit": ["title", "possible-very-light-sleet"],
    "Udan - Salju Kahur Uituan Deit": ["title", "very-light-sleet"],
    "Karik Udan - Salju Kahur Uituan": ["title", "possible-light-sleet"],
    "Udan - Salju Kahur Uituan": ["title", "light-sleet"],
    "Udan - Salju Kahur": ["title", "medium-sleet"],
    "Udan - Salju Kahur Bo'ot": ["title", "heavy-sleet"],
    "Karik Salju Uituan Deit": ["title", "possible-very-light-snow"],
    "Salju Uituan Deit": ["title", "very-light-snow"],
    "Karik Salju Uituan": ["title", "possible-light-snow"],
    "Salju Uituan": ["title", "light-snow"],
    "Salju": ["title", "medium-snow"],
    "Salju Bo'ot": ["title", "heavy-snow"],
    "Anin": ["title", "medium-wind"],
    "Anin Bo'ot": ["title", "heavy-wind"],
    "Abu-Abu Taka Rai": ["title", "fog"],
    "Klaru Liu": ["title", "very-light-clouds"],
    "Abu-Abu Uituan": ["title", "light-clouds"],
    "Abu-Abu": ["title", "medium-clouds"],
    "Abu-Abu Taka Loron": ["title", "heavy-clouds"],
    "Maran Ho Anin Ki'ik": ["title", ["and", "low-humidity", "light-wind"]],
    "Bokon Ho Abu-Abu Uituan": ["title", ["and", "high-humidity", "light-clouds"]],
    "Pas ba oras ida.": ["sentence", ["for-hour", "clear"]],
    "Salju uituan deit hahu iha 35 min.": [
        "sentence",
        ["starting-in", "very-light-snow", ["minutes", 35]],
    ],
    "Udan uituan para iha 15 min.": [
        "sentence",
        ["stopping-in", "light-rain", ["minutes", 15]],
    ],
    "Udan - salju kahur bo'ot hahu iha 20 min., hein 30 min. para.": [
        "sentence",
        [
            "starting-then-stopping-later",
            "heavy-sleet",
            ["minutes", 20],
            ["minutes", 30],
        ],
    ],
    "Udan para iha 25 min., hein 8 min. hahu fali.": [
        "sentence",
        [
            "stopping-then-starting-later",
            "medium-rain",
            ["minutes", 25],
            ["minutes", 8],
        ],
    ],
    "Abu-abu loron tomak.": ["sentence", ["for-day", "medium-clouds"]],
    "Udan - salju kahur uituan deit hahu iha dader.": [
        "sentence",
        ["starting", "very-light-sleet", "morning"],
    ],
    "Anin to ohin kalan bo'ot.": ["sentence", ["until", "medium-wind", "today-night"]],
    "Udan bo'ot to lokraik.": [
        "sentence",
        ["until", "heavy-precipitation", "afternoon"],
    ],
    "Anin ki'ik lokraik.": ["sentence", ["during", "light-wind", "afternoon"]],
    "Salju orsida kalan ho aban dader.": [
        "sentence",
        ["during", "medium-snow", ["and", "later-today-evening", "tomorrow-morning"]],
    ],
    "Udan bo'ot to orsida ohin dader, hahu fali ohin kalan.": [
        "sentence",
        ["until-starting-again", "heavy-rain", "later-today-morning", "today-evening"],
    ],
    "Abu-abu taka loron hahu iha kalan, kontinua to kalan bo'ot.": [
        "sentence",
        ["starting-continuing-until", "heavy-clouds", "evening", "night"],
    ],
    "Udan - salju kahur uituan orsida lokraik ho abu-abu taka rai aban dader.": [
        "sentence",
        [
            "and",
            ["during", "light-sleet", "later-today-afternoon"],
            ["during", "fog", "tomorrow-morning"],
        ],
    ],
    "Anin bo'ot hahu ohin dader, kontinua to ohin lokraik, ho udan - salju kahur aban dader.": [
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
    "Abu-abu taka loron hahu orsida kalan bo'ot ho salju bo'ot aban lokraik.": [
        "sentence",
        [
            "and",
            ["starting", "heavy-clouds", "later-today-night"],
            ["during", "heavy-snow", "tomorrow-afternoon"],
        ],
    ],
    "Maran ohin kalan bo'ot ho udan uituan hahu aban kalan, kontinua to aban kalan bo'ot.": [
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
    "Salju (5 in.) iha kalan bo'ot.": [
        "sentence",
        ["during", ["parenthetical", "medium-snow", ["inches", 5]], "night"],
    ],
    "Salju uituan (2 cm.) orsida ohin dader.": [
        "sentence",
        [
            "during",
            ["parenthetical", "light-snow", ["centimeters", 2]],
            "later-today-morning",
        ],
    ],
    "Salju bo'ot (8\u201312 in.) loron tomak.": [
        "sentence",
        ["for-day", ["parenthetical", "heavy-snow", ["inches", ["range", 8, 12]]]],
    ],
    "Salju (1 cm. mai kraik) lokraik.": [
        "sentence",
        [
            "during",
            ["parenthetical", "medium-snow", ["less-than", ["centimeters", 1]]],
            "afternoon",
        ],
    ],
    "Udan la iha durante semana ida, ho temperatur la sai liu 85\u00b0F aban.": [
        "sentence",
        [
            "with",
            ["for-week", "no-precipitation"],
            ["temperatures-peaking", ["fahrenheit", 85], "tomorrow"],
        ],
    ],
    "Udan - maran kahur durante Sabadu - Domingu, ho temperatur sai to 32\u00b0C iha Kinta.": [
        "sentence",
        [
            "with",
            ["over-weekend", "mixed-precipitation"],
            ["temperatures-rising", ["celsius", 32], "thursday"],
        ],
    ],
    "Udan uituan deit ohin, ho temperatur la tun liu 15\u00b0F iha Sexta.": [
        "sentence",
        [
            "with",
            ["during", "very-light-rain", "today"],
            ["temperatures-valleying", ["fahrenheit", 15], "friday"],
        ],
    ],
    "Salju uituan iha Segunda ho Tersa, ho temperatur tun to 0\u00b0C iha Domingu.": [
        "sentence",
        [
            "with",
            ["during", "light-snow", ["and", "monday", "tuesday"]],
            ["temperatures-falling", ["celsius", 0], "sunday"],
        ],
    ],
    "Udan iha Kuarta to Sabadu, ho temperatur la sai liu 100\u00b0F iha Segunda.": [
        "sentence",
        [
            "with",
            ["during", "medium-precipitation", ["through", "wednesday", "saturday"]],
            ["temperatures-peaking", ["fahrenheit", 100], "monday"],
        ],
    ],
}
