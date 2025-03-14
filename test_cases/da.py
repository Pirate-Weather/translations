# This would be one of your translations, as a Python dictionary
cases = {
    "Klart": ["title", "clear"],
    "Mulighed for meget let nedbør": ["title", "possible-very-light-precipitation"],
    "Meget let nedbør": ["title", "very-light-precipitation"],
    "Mulighed for let nedbør": ["title", "possible-light-precipitation"],
    "Let nedbør": ["title", "light-precipitation"],
    "Nedbør": ["title", "medium-precipitation"],
    "Kraftig regn": ["title", "heavy-precipitation"],
    "Mulighed for let støvregn": ["title", "possible-very-light-rain"],
    "Støvregn": ["title", "very-light-rain"],
    "Mulighed for lette regnbyger": ["title", "possible-light-rain"],
    "Regnbyger": ["title", "light-rain"],
    "Regn": ["title", "medium-rain"],
    "Kraftige regnbyger": ["title", "heavy-rain"],
    "Mulighed for meget let slud": ["title", "possible-very-light-sleet"],
    "Meget let slud": ["title", "very-light-sleet"],
    "Mulighed for let slud": ["title", "possible-light-sleet"],
    "Let slud": ["title", "light-sleet"],
    "Slud": ["title", "medium-sleet"],
    "Kraftig slud": ["title", "heavy-sleet"],
    "Mulighed for meget let sne": ["title", "possible-very-light-snow"],
    "Meget let sne": ["title", "very-light-snow"],
    "Mulighed for let sne": ["title", "possible-light-snow"],
    "Let sne": ["title", "light-snow"],
    "Sne": ["title", "medium-snow"],
    "Rigelig med sne": ["title", "heavy-snow"],
    "Stærk vind": ["title", "medium-wind"],
    "Storm": ["title", "heavy-wind"],
    "Tåge": ["title", "fog"],
    "For det meste klart": ["title", "very-light-clouds"],
    "Let skyet": ["title", "light-clouds"],
    "Skyet": ["title", "medium-clouds"],
    "Overskyet": ["title", "heavy-clouds"],
    "Tørt og let vind": ["title", ["and", "low-humidity", "light-wind"]],
    "Støvregn og storm": ["title", ["and", "very-light-rain", "heavy-wind"]],
    "Fugtigt og let skyet": ["title", ["and", "high-humidity", "light-clouds"]],
    "Klart i løbet af de næste par timer.": ["sentence", ["for-hour", "clear"]],
    "Meget let sne om 35 min.": [
        "sentence",
        ["starting-in", "very-light-snow", ["minutes", 35]],
    ],
    "Regnbyger der aftager om 15 min.": [
        "sentence",
        ["stopping-in", "light-rain", ["minutes", 15]],
    ],
    "Kraftig slud om 20 min., aftager 30 min. senere.": [
        "sentence",
        [
            "starting-then-stopping-later",
            "heavy-sleet",
            ["minutes", 20],
            ["minutes", 30],
        ],
    ],
    "Regn aftager om 25 min., begynder igen 8 min. senere.": [
        "sentence",
        [
            "stopping-then-starting-later",
            "medium-rain",
            ["minutes", 25],
            ["minutes", 8],
        ],
    ],
    "Skyet i løbet af dagen.": ["sentence", ["for-day", "medium-clouds"]],
    "Meget let slud om morgenen.": [
        "sentence",
        ["starting", "very-light-sleet", "morning"],
    ],
    "Stærk vind indtil i nat.": ["sentence", ["until", "medium-wind", "today-night"]],
    "Kraftig regn indtil om eftermiddagen.": [
        "sentence",
        ["until", "heavy-precipitation", "afternoon"],
    ],
    "Let vind om eftermiddagen.": ["sentence", ["during", "light-wind", "afternoon"]],
    "Sne senere i aften og i morgen tidlig.": [
        "sentence",
        ["during", "medium-snow", ["and", "later-today-evening", "tomorrow-morning"]],
    ],
    "Kraftige regnbyger indtil senere på formiddagen, kommer igen i aften.": [
        "sentence",
        ["until-starting-again", "heavy-rain", "later-today-morning", "today-evening"],
    ],
    "Overskyet om aftenen, fortsætter indtil natten.": [
        "sentence",
        ["starting-continuing-until", "heavy-clouds", "evening", "night"],
    ],
    "Let slud senere i eftermiddag og tåge i morgen tidlig.": [
        "sentence",
        [
            "and",
            ["during", "light-sleet", "later-today-afternoon"],
            ["during", "fog", "tomorrow-morning"],
        ],
    ],
    "Storm på formiddagen, fortsætter indtil i eftermiddag, og slud i morgen tidlig.": [
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
    "Overskyet senere i nat og rigelig med sne i morgen eftermiddag.": [
        "sentence",
        [
            "and",
            ["starting", "heavy-clouds", "later-today-night"],
            ["during", "heavy-snow", "tomorrow-afternoon"],
        ],
    ],
    "Tørt i nat og let nedbør i morgen aften, fortsætter indtil i morgen nat.": [
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
    "Sne (5 tommer) om natten.": [
        "sentence",
        ["during", ["parenthetical", "medium-snow", ["inches", 5]], "night"],
    ],
    "Let sne (2 cm) senere på formiddagen.": [
        "sentence",
        [
            "during",
            ["parenthetical", "light-snow", ["centimeters", 2]],
            "later-today-morning",
        ],
    ],
    "Rigelig med sne (8\u201312 tommer) i løbet af dagen.": [
        "sentence",
        ["for-day", ["parenthetical", "heavy-snow", ["inches", ["range", 8, 12]]]],
    ],
    "Sne (under 1 cm) om eftermiddagen.": [
        "sentence",
        [
            "during",
            ["parenthetical", "medium-snow", ["less-than", ["centimeters", 1]]],
            "afternoon",
        ],
    ],
    "Ingen målbar nedbør i løbet af ugen, med temperaturer op til 85\u00b0F i morgen.": [
        "sentence",
        [
            "with",
            ["for-week", "no-precipitation"],
            ["temperatures-peaking", ["fahrenheit", 85], "tomorrow"],
        ],
    ],
    "Blandet nedbør over weekenden, med temperaturer stigende til 32\u00b0C om torsdagen.": [
        "sentence",
        [
            "with",
            ["over-weekend", "mixed-precipitation"],
            ["temperatures-rising", ["celsius", 32], "thursday"],
        ],
    ],
    "Støvregn på mandag, med temperaturer der stopper ved 15\u00b0F om fredagen.": [
        "sentence",
        [
            "with",
            ["during", "very-light-rain", "monday"],
            ["temperatures-valleying", ["fahrenheit", 15], "friday"],
        ],
    ],
    "Let sne på tirsdag og onsdag, med temperaturer faldende til 0\u00b0C om søndagen.": [
        "sentence",
        [
            "with",
            ["during", "light-snow", ["and", "tuesday", "wednesday"]],
            ["temperatures-falling", ["celsius", 0], "sunday"],
        ],
    ],
    "Nedbør i dag indtil på lørdag, med temperaturer op til 100\u00b0F om mandagen.": [
        "sentence",
        [
            "with",
            ["during", "medium-precipitation", ["through", "today", "saturday"]],
            ["temperatures-peaking", ["fahrenheit", 100], "monday"],
        ],
    ],
    "Let sne på tirsdag og næste onsdag, med temperaturer faldende til 0\u00b0C om søndagen.": [
        "sentence",
        [
            "with",
            ["during", "light-snow", ["and", "tuesday", "next-wednesday"]],
            ["temperatures-falling", ["celsius", 0], "sunday"],
        ],
    ],
    "Tordenvejr kan forekomme": ["title", "possible-thunderstorm"],
    "Kraftige regnbyger og tordenvejr": [
        "title",
        ["and", "heavy-rain", "thunderstorm"],
    ],
}
