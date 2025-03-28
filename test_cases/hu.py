# This would be one of your translations, as a Python dictionary
cases = {
    "Derült": ["title", "clear"],
    "Szitáló csapadék lehetséges": ["title", "possible-very-light-precipitation"],
    "Szitáló csapadék": ["title", "very-light-precipitation"],
    "Gyenge csapadék lehetséges": ["title", "possible-light-precipitation"],
    "Gyenge csapadék": ["title", "light-precipitation"],
    "Csapadék": ["title", "medium-precipitation"],
    "Intenzív csapadék": ["title", "heavy-precipitation"],
    "Gyenge szitálás lehetséges": ["title", "possible-very-light-rain"],
    "Gyenge szitálás": ["title", "very-light-rain"],
    "Gyenge eső lehetséges": ["title", "possible-light-rain"],
    "Gyenge eső": ["title", "light-rain"],
    "Eső": ["title", "medium-rain"],
    "Intenzív eső": ["title", "heavy-rain"],
    "Ónos szitálás lehetséges": ["title", "possible-very-light-sleet"],
    "Ónos szitálás": ["title", "very-light-sleet"],
    "Gyenge ónos eső lehetséges": ["title", "possible-light-sleet"],
    "Gyenge ónos eső": ["title", "light-sleet"],
    "Ónos eső": ["title", "medium-sleet"],
    "Havas eső": ["title", "heavy-sleet"],
    "Hószállingózás lehetséges": ["title", "possible-very-light-snow"],
    "Hószállingózás": ["title", "very-light-snow"],
    "Gyenge havazás lehetséges": ["title", "possible-light-snow"],
    "Gyenge havazás": ["title", "light-snow"],
    "Havazás": ["title", "medium-snow"],
    "Intenzív havazás": ["title", "heavy-snow"],
    "Mérsékelt szél": ["title", "medium-wind"],
    "Erős szél": ["title", "heavy-wind"],
    "Ködös idő": ["title", "fog"],
    "Erős derült": ["title", "very-light-clouds"],
    "Közepes felhősödés": ["title", "light-clouds"],
    "Erős felhősödés": ["title", "medium-clouds"],
    "Borult idő": ["title", "heavy-clouds"],
    "Száraz idő és enyhe szél": ["title", ["and", "low-humidity", "light-wind"]],
    "Gyenge szitálás és erős szél": ["title", ["and", "very-light-rain", "heavy-wind"]],
    "Párás idő és közepes felhősödés": [
        "title",
        ["and", "high-humidity", "light-clouds"],
    ],
    "Derült ebben az órában.": ["sentence", ["for-hour", "clear"]],
    "Hószállingózás 35 perc múlva.": [
        "sentence",
        ["starting-in", "very-light-snow", ["minutes", 35]],
    ],
    "Gyenge eső 15 perc múlva véget ér.": [
        "sentence",
        ["stopping-in", "light-rain", ["minutes", 15]],
    ],
    "Havas eső 20 perc múlva, 30 percig.": [
        "sentence",
        [
            "starting-then-stopping-later",
            "heavy-sleet",
            ["minutes", 20],
            ["minutes", 30],
        ],
    ],
    "Eső 25 perc múlva véget ér, de 8 perc elteltével újra várható.": [
        "sentence",
        [
            "stopping-then-starting-later",
            "medium-rain",
            ["minutes", 25],
            ["minutes", 8],
        ],
    ],
    "Erős felhősödés egész nap.": ["sentence", ["for-day", "medium-clouds"]],
    "Ónos szitálás lesz reggel.": [
        "sentence",
        ["starting", "very-light-sleet", "morning"],
    ],
    "Mérsékelt szél ma éjjel.": ["sentence", ["until", "medium-wind", "today-night"]],
    "Intenzív csapadék délután.": [
        "sentence",
        ["until", "heavy-precipitation", "afternoon"],
    ],
    "Enyhe szél délután.": ["sentence", ["during", "light-wind", "afternoon"]],
    "Havazás ma késő este és holnap reggel.": [
        "sentence",
        ["during", "medium-snow", ["and", "later-today-evening", "tomorrow-morning"]],
    ],
    "Intenzív eső ma késő délelőtt, majd ma este ismét.": [
        "sentence",
        ["until-starting-again", "heavy-rain", "later-today-morning", "today-evening"],
    ],
    "Borult idő kezdődik este, éjjel folytatódik.": [
        "sentence",
        ["starting-continuing-until", "heavy-clouds", "evening", "night"],
    ],
    "Gyenge ónos eső ma késő délután és ködös idő holnap reggel.": [
        "sentence",
        [
            "and",
            ["during", "light-sleet", "later-today-afternoon"],
            ["during", "fog", "tomorrow-morning"],
        ],
    ],
    "Erős szél kezdődik ma reggel, ma délután folytatódik és ónos eső holnap reggel.": [
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
    "Borult idő lesz ma késő éjjel és intenzív havazás holnap délután.": [
        "sentence",
        [
            "and",
            ["starting", "heavy-clouds", "later-today-night"],
            ["during", "heavy-snow", "tomorrow-afternoon"],
        ],
    ],
    "Száraz idő ma éjjel és gyenge csapadék kezdődik holnap este, holnap éjjel folytatódik.": [
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
    "Havazás (5 in.) éjjel.": [
        "sentence",
        ["during", ["parenthetical", "medium-snow", ["inches", 5]], "night"],
    ],
    "Gyenge havazás (2 cm.) ma késő délelőtt.": [
        "sentence",
        [
            "during",
            ["parenthetical", "light-snow", ["centimeters", 2]],
            "later-today-morning",
        ],
    ],
    "Intenzív havazás (8\u201312 in.) egész nap.": [
        "sentence",
        ["for-day", ["parenthetical", "heavy-snow", ["inches", ["range", 8, 12]]]],
    ],
    "Havazás (1 cm. alatt) délután.": [
        "sentence",
        [
            "during",
            ["parenthetical", "medium-snow", ["less-than", ["centimeters", 1]]],
            "afternoon",
        ],
    ],
    "Csapadékmentes idő ezen a héten, 85\u00b0F csúcshőmérséklettel holnap.": [
        "sentence",
        [
            "with",
            ["for-week", "no-precipitation"],
            ["temperatures-peaking", ["fahrenheit", 85], "tomorrow"],
        ],
    ],
    "Vegyes csapadék a hétvégén, 32\u00b0C-ra emelkedő hőmérséklettel csütörtöki nap.": [
        "sentence",
        [
            "with",
            ["over-weekend", "mixed-precipitation"],
            ["temperatures-rising", ["celsius", 32], "thursday"],
        ],
    ],
    "Gyenge szitálás hétfői nap, 15\u00b0F minimum hőmérséklettel pénteki nap.": [
        "sentence",
        [
            "with",
            ["during", "very-light-rain", "monday"],
            ["temperatures-valleying", ["fahrenheit", 15], "friday"],
        ],
    ],
    "Gyenge havazás keddi nap és szerdai nap, 0\u00b0C-ra eső hőmérséklettel vasárnap.": [
        "sentence",
        [
            "with",
            ["during", "light-snow", ["and", "tuesday", "wednesday"]],
            ["temperatures-falling", ["celsius", 0], "sunday"],
        ],
    ],
    "Csapadék ma és szombati nap között, 100\u00b0F csúcshőmérséklettel hétfői nap.": [
        "sentence",
        [
            "with",
            ["during", "medium-precipitation", ["through", "today", "saturday"]],
            ["temperatures-peaking", ["fahrenheit", 100], "monday"],
        ],
    ],
    "Vegyes csapadék (1\u20133 in. hó) egész nap.": [
        "sentence",
        [
            "for-day",
            ["parenthetical", "mixed-precipitation", ["inches", ["range", 1, 3]]],
        ],
    ],
    "Intenzív havazás (1\u20133 in.)": [
        "title",
        ["parenthetical", "heavy-snow", ["inches", ["range", 1, 3]]],
    ],
    "Intenzív havazás (3\u20135 cm.)": [
        "title",
        ["parenthetical", "heavy-snow", ["centimeters", ["range", 3, 5]]],
    ],
}
