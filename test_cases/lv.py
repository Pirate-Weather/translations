# This would be one of your translations, as a Python dictionary
cases = {
    "Skaidrs": ["title", "clear"],
    "Iespējami nelieli nokrišņi": ["title", "possible-very-light-precipitation"],
    "Nelieli nokrišņi": ["title", "very-light-precipitation"],
    "Iespējami nelieli nokrišņi.": ["sentence", "possible-light-precipitation"],
    "Nelieli nokrišņi.": ["sentence", "light-precipitation"],
    "Nokrišņi": ["title", "medium-precipitation"],
    "Stipri nokrišņi": ["title", "heavy-precipitation"],
    "Iespējams smidzinošs lietus": ["title", "possible-very-light-rain"],
    "Smidzinošs lietus": ["title", "very-light-rain"],
    "Iespējams neliels lietus": ["title", "possible-light-rain"],
    "Neliels lietus": ["title", "light-rain"],
    "Lietus": ["title", "medium-rain"],
    "Stiprs lietus": ["title", "heavy-rain"],
    "Iespējams neliels slapjš sniegs": ["title", "possible-very-light-sleet"],
    "Neliels slapjš sniegs": ["title", "very-light-sleet"],
    "Iespējams neliels slapjš sniegs.": ["sentence", "possible-light-sleet"],
    "Neliels slapjš sniegs.": ["sentence", "light-sleet"],
    "Slapjš sniegs": ["title", "medium-sleet"],
    "Stiprs slapjš sniegs": ["title", "heavy-sleet"],
    "Iespējams neliels sniegs": ["title", "possible-very-light-snow"],
    "Neliels sniegs": ["title", "very-light-snow"],
    "Iespējams neliels sniegs.": ["sentence", "possible-light-snow"],
    "Neliels sniegs.": ["sentence", "light-snow"],
    "Sniegs": ["title", "medium-snow"],
    "Stiprs sniegs": ["title", "heavy-snow"],
    "Vējš": ["title", "medium-wind"],
    "Stiprs vējš": ["title", "heavy-wind"],
    "Migla": ["title", "fog"],
    "Pārsvarā skaidrs": ["title", "very-light-clouds"],
    "Daļēji mākoņains": ["title", "light-clouds"],
    "Pārsvarā mākoņains": ["title", "medium-clouds"],
    "Apmācies": ["title", "heavy-clouds"],
    "Sauss un lēns vējš": ["title", ["and", "low-humidity", "light-wind"]],
    "Smidzinošs lietus un stiprs vējš": [
        "title",
        ["and", "very-light-rain", "heavy-wind"],
    ],
    "Mitrs un daļēji mākoņains": ["title", ["and", "high-humidity", "light-clouds"]],
    "Nākamo stundu skaidrs.": ["sentence", ["for-hour", "clear"]],
    "Neliels sniegs sāksies nākamo 35 min. laikā.": [
        "sentence",
        ["starting-in", "very-light-snow", ["minutes", 35]],
    ],
    "Neliels lietus beigsies nākamo 15 min. laikā.": [
        "sentence",
        ["stopping-in", "light-rain", ["minutes", 15]],
    ],
    "Stiprs slapjš sniegs sāksies 20 min. laikā, beigsies 30 min. vēlāk.": [
        "sentence",
        [
            "starting-then-stopping-later",
            "heavy-sleet",
            ["minutes", 20],
            ["minutes", 30],
        ],
    ],
    "Lietus beigsies 25 min. laikā, atsāksies 8 min. vēlāk.": [
        "sentence",
        [
            "stopping-then-starting-later",
            "medium-rain",
            ["minutes", 25],
            ["minutes", 8],
        ],
    ],
    "Visu dienu pārsvarā mākoņains.": ["sentence", ["for-day", "medium-clouds"]],
    "No rīta sāksies neliels slapjš sniegs.": [
        "sentence",
        ["starting", "very-light-sleet", "morning"],
    ],
    "Vējš līdz naktij.": ["sentence", ["until", "medium-wind", "today-night"]],
    "Stipri nokrišņi līdz pēcpusdienai.": [
        "sentence",
        ["until", "heavy-precipitation", "afternoon"],
    ],
    "Pēcpusdienā lēns vējš.": ["sentence", ["during", "light-wind", "afternoon"]],
    "Vēlāk vakarā un rīt no rīta sniegs.": [
        "sentence",
        ["during", "medium-snow", ["and", "later-today-evening", "tomorrow-morning"]],
    ],
    "Stiprs lietus līdz rītam, atsāksies vakarā.": [
        "sentence",
        ["until-starting-again", "heavy-rain", "later-today-morning", "today-evening"],
    ],
    "No vakara līdz naktij apmācies.": [
        "sentence",
        ["starting-continuing-until", "heavy-clouds", "evening", "night"],
    ],
    "Vēlāk pēcpusdienā neliels slapjš sniegs un rīt no rīta migla.": [
        "sentence",
        [
            "and",
            ["during", "light-sleet", "later-today-afternoon"],
            ["during", "fog", "tomorrow-morning"],
        ],
    ],
    "No rīta līdz pēcpusdienai stiprs vējš un rīt no rīta slapjš sniegs.": [
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
    "Vēlāk naktī būs apmācies un rīt pēcpusdienā stiprs sniegs.": [
        "sentence",
        [
            "and",
            ["starting", "heavy-clouds", "later-today-night"],
            ["during", "heavy-snow", "tomorrow-afternoon"],
        ],
    ],
    "Naktī sauss un no rītvakara līdz rītdienas naktij nelieli nokrišņi.": [
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
    "Naktī sniegs (5 collas).": [
        "sentence",
        ["during", ["parenthetical", "medium-snow", ["inches", 5]], "night"],
    ],
    "Vēlāk no rīta neliels sniegs (2 cm.).": [
        "sentence",
        [
            "during",
            ["parenthetical", "light-snow", ["centimeters", 2]],
            "later-today-morning",
        ],
    ],
    "Visu dienu stiprs sniegs (8\u201312 collas).": [
        "sentence",
        ["for-day", ["parenthetical", "heavy-snow", ["inches", ["range", 8, 12]]]],
    ],
    "Pēcpusdienā sniegs (< 1 cm.).": [
        "sentence",
        [
            "during",
            ["parenthetical", "medium-snow", ["less-than", ["centimeters", 1]]],
            "afternoon",
        ],
    ],
    "Šonedēļ bez nokrišņiem, ar augstāko temperatūru 85\u00b0F rīt.": [
        "sentence",
        [
            "with",
            ["for-week", "no-precipitation"],
            ["temperatures-peaking", ["fahrenheit", 85], "tomorrow"],
        ],
    ],
    "Nedēļas nogalē jaukti nokrišņi, temperatūrai sasniedzot 32\u00b0C ceturtdien.": [
        "sentence",
        [
            "with",
            ["over-weekend", "mixed-precipitation"],
            ["temperatures-rising", ["celsius", 32], "thursday"],
        ],
    ],
    "Pirmdien smidzinošs lietus, ar zemāko temperatūru 15\u00b0F piektdien.": [
        "sentence",
        [
            "with",
            ["during", "very-light-rain", "monday"],
            ["temperatures-valleying", ["fahrenheit", 15], "friday"],
        ],
    ],
    "Otrdien un nākamtrešdien neliels sniegs, temperatūrai nokrītoties līdz 0\u00b0C svētdien.": [
        "sentence",
        [
            "with",
            ["during", "light-snow", ["and", "tuesday", "next-wednesday"]],
            ["temperatures-falling", ["celsius", 0], "sunday"],
        ],
    ],
    "No šodienas līdz sestdienai nokrišņi, ar augstāko temperatūru 100\u00b0F pirmdien.": [
        "sentence",
        [
            "with",
            ["during", "medium-precipitation", ["through", "today", "saturday"]],
            ["temperatures-peaking", ["fahrenheit", 100], "monday"],
        ],
    ],
    "Visu dienu jaukti nokrišņi (1\u20133 collas).": [
        "sentence",
        [
            "for-day",
            ["parenthetical", "mixed-precipitation", ["inches", ["range", 1, 3]]],
        ],
    ],
    "Stiprs sniegs (1\u20133 collas)": [
        "title",
        ["parenthetical", "heavy-snow", ["inches", ["range", 1, 3]]],
    ],
    "Stiprs sniegs (3\u20135 cm.)": [
        "title",
        ["parenthetical", "heavy-snow", ["centimeters", ["range", 3, 5]]],
    ],
    "Iespējams negaiss": ["title", "possible-thunderstorm"],
    "Stiprs lietus un negaiss": ["title", ["and", "heavy-rain", "thunderstorm"]],
    "Smidzinošs lietus sāksies nākamo < 1 min. laikā.": [
        "sentence",
        ["starting-in", "very-light-rain", ["less-than", ["minutes", 1]]],
    ],
    "Tuvākās stundas laikā, laikaziņas ir īslaicīgi nepieejamas, jo nav pieejami apgabala staciju radari.": [
        "sentence",
        ["next-hour-forecast-status", "temporarily-unavailable", "station-offline"],
    ],
    "Tuvākās stundas laikā, laikaziņas ir daļēji nepieejamas, jo ir traucējumi starp staciju radariem.": [
        "sentence",
        ["next-hour-forecast-status", "partially-unavailable", "station-incomplete"],
    ],
    "Tuvākās stundas laikā, laikaziņas ir nepieejamas, jo nav pieejami apgabala staciju radari.": [
        "sentence",
        ["next-hour-forecast-status", "unavailable", "station-offline"],
    ],
}
