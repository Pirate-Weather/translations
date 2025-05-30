# This would be one of your translations, as a Python dictionary
cases = {
    "Clir": ["title", "clear"],
    "Gwlybaniaeth ysgafn yn bosib": ["title", "possible-very-light-precipitation"],
    "Sych a gwyntoedd ysgafn": ["title", ["and", "low-humidity", "light-wind"]],
    "Glaw mân a gwyntoedd cryfion": ["title", ["and", "very-light-rain", "heavy-wind"]],
    "Clòs a chymylog": ["title", ["and", "high-humidity", "medium-clouds"]],
    "Clir am yr awr.": ["sentence", ["for-hour", "clear"]],
    "Eira ysgafn yn cychwyn mewn 35 munud.": [
        "sentence",
        ["starting-in", "very-light-snow", ["minutes", 35]],
    ],
    "Glaw ysgafn yn dod i ben mewn 15 munud.": [
        "sentence",
        ["stopping-in", "light-rain", ["minutes", 15]],
    ],
    "Eirlaw trwm yn cychwyn mewn 20 munud, ac yn dod i ben 30 munud wedyn.": [
        "sentence",
        [
            "starting-then-stopping-later",
            "heavy-sleet",
            ["minutes", 20],
            ["minutes", 30],
        ],
    ],
    "Glaw yn dod i ben mewn 25 munud, gan gychwyn eto 8 munud wedyn.": [
        "sentence",
        [
            "stopping-then-starting-later",
            "medium-rain",
            ["minutes", 25],
            ["minutes", 8],
        ],
    ],
    "Cymylog drwy’r dydd.": ["sentence", ["for-day", "medium-clouds"]],
    "Eirlaw ysgafn yn cychwyn yn y bore.": [
        "sentence",
        ["starting", "very-light-sleet", "morning"],
    ],
    "Gwyntog hyd at heno.": ["sentence", ["until", "medium-wind", "today-night"]],
    "Gwlybaniaeth trwm hyd at y prynhawn.": [
        "sentence",
        ["until", "heavy-precipitation", "afternoon"],
    ],
    "Gwyntoedd ysgafn yn y prynhawn.": [
        "sentence",
        ["during", "light-wind", "afternoon"],
    ],
    "Eira yn hwyrach fin nos heno a bore yfory.": [
        "sentence",
        ["during", "medium-snow", ["and", "later-today-evening", "tomorrow-morning"]],
    ],
    "Glaw trwm hyd at hwyrach bore yma, gan gychwyn eto gyda’r hwyr heno.": [
        "sentence",
        ["until-starting-again", "heavy-rain", "later-today-morning", "today-evening"],
    ],
    "Cymylau trwchus yn cychwyn gyda’r hwyr, gan barhau hyd at y nos.": [
        "sentence",
        ["starting-continuing-until", "heavy-clouds", "evening", "night"],
    ],
    "Eirlaw ysgafn yn hwyrach prynhawn yma a niwlog bore yfory.": [
        "sentence",
        [
            "and",
            ["during", "light-sleet", "later-today-afternoon"],
            ["during", "fog", "tomorrow-morning"],
        ],
    ],
    "Gwyntoedd cryfion yn cychwyn y bore yma, gan barhau hyd at y prynhawn yma, ac eirlaw bore yfory.": [
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
    "Cymylau trwchus yn cychwyn yn hwyrach heno ac eira trwm prynhawn yfory.": [
        "sentence",
        [
            "and",
            ["starting", "heavy-clouds", "later-today-night"],
            ["during", "heavy-snow", "tomorrow-afternoon"],
        ],
    ],
    "Sych heno a gwlybaniaeth ysgafn yn cychwyn fin nos yfory, gan barhau hyd at nos yfory.": [
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
    "Eira (5 modfedd) dros nos.": [
        "sentence",
        ["during", ["parenthetical", "medium-snow", ["inches", 5]], "night"],
    ],
    "Eira ysgafn (2cm) yn hwyrach bore yma.": [
        "sentence",
        [
            "during",
            ["parenthetical", "light-snow", ["centimeters", 2]],
            "later-today-morning",
        ],
    ],
    "Eira trwm (8–12 modfedd) drwy’r dydd.": [
        "sentence",
        ["for-day", ["parenthetical", "heavy-snow", ["inches", ["range", 8, 12]]]],
    ],
    "Eira (llai nag 11cm) yn y prynhawn.": [
        "sentence",
        [
            "during",
            ["parenthetical", "medium-snow", ["less-than", ["centimeters", 11]]],
            "afternoon",
        ],
    ],
    "Dim gwlybaniaeth drwy’r wythnos, gyda’r tymheredd ar ei uchaf yn 85°F yfory.": [
        "sentence",
        [
            "with",
            ["for-week", "no-precipitation"],
            ["temperatures-peaking", ["fahrenheit", 85], "tomorrow"],
        ],
    ],
    "Gwlybaniaeth cymysg dros y penwythnos, gyda’r tymheredd yn codi i 32°C ar ddydd Iau.": [
        "sentence",
        [
            "with",
            ["over-weekend", "mixed-precipitation"],
            ["temperatures-rising", ["celsius", 32], "thursday"],
        ],
    ],
    "Glaw mân ar ddydd Llun, gyda’r tymheredd ar ei isaf yn 15°F ar ddydd Gwener.": [
        "sentence",
        [
            "with",
            ["during", "very-light-rain", "monday"],
            ["temperatures-valleying", ["fahrenheit", 15], "friday"],
        ],
    ],
    "Eira ysgafn ar ddydd Mawrth a dydd Mercher, gyda’r tymheredd yn gostwng i 0°C ar ddydd Sul.": [
        "sentence",
        [
            "with",
            ["during", "light-snow", ["and", "tuesday", "wednesday"]],
            ["temperatures-falling", ["celsius", 0], "sunday"],
        ],
    ],
    "Gwlybaniaeth o heddiw hyd at ddydd Sadwrn, gyda’r tymheredd ar ei uchaf yn 100°F ar ddydd Llun.": [
        "sentence",
        [
            "with",
            ["during", "medium-precipitation", ["through", "today", "saturday"]],
            ["temperatures-peaking", ["fahrenheit", 100], "monday"],
        ],
    ],
    "Gwlybaniaeth o ddydd Gwener hyd at ddydd Sadwrn, gyda’r tymheredd ar ei uchaf yn 100°F ar ddydd Llun.": [
        "sentence",
        [
            "with",
            ["during", "medium-precipitation", ["through", "friday", "saturday"]],
            ["temperatures-peaking", ["fahrenheit", 100], "monday"],
        ],
    ],
    "Glaw ysgafn yn bosib yn y bore a’r prynhawn.": [
        "sentence",
        ["during", "possible-light-rain", ["and", "morning", "afternoon"]],
    ],
    "Dydi rhagolygon yr awr nesa ddim ar gael ar hyn o bryd oherwydd diffyg gwybodaeth o orsafoedd radar gerllaw.": [
        "sentence",
        ["next-hour-forecast-status", "temporarily-unavailable", "station-offline"],
    ],
    "Dydi rhagolygon yr awr nesa ddim yn gyflawn oherwydd bylchau yn narpariaeth gorsafoedd radar gerllaw.": [
        "sentence",
        ["next-hour-forecast-status", "partially-unavailable", "station-incomplete"],
    ],
    "Dydi rhagolygon yr awr nesa ddim ar gael oherwydd diffyg gwybodaeth o orsafoedd radar gerllaw.": [
        "sentence",
        ["next-hour-forecast-status", "unavailable", "station-offline"],
    ],
}
