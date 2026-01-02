# This would be one of your translations, as a Python dictionary
cases = {
    "Earclay": ["title", "clear"],
    "Ossiblepay Ightlay Ecipitationpray": [
        "title",
        "possible-very-light-precipitation",
    ],
    "Ightlay Ecipitationpray": ["title", "very-light-precipitation"],
    "Ossiblepay Ightlay Ecipitationpray": ["title", "possible-light-precipitation"],
    "Ightlay Ecipitationpray": ["title", "light-precipitation"],
    "Ecipitationpray": ["title", "medium-precipitation"],
    "Eavyhay Ecipitationpray": ["title", "heavy-precipitation"],
    "Ossiblepay Izzledray": ["title", "possible-very-light-rain"],
    "Izzledray": ["title", "very-light-rain"],
    "Ossiblepay Ightlay Ainray": ["title", "possible-light-rain"],
    "Ightlay Ainray": ["title", "light-rain"],
    "Ainray": ["title", "medium-rain"],
    "Eavyhay Ainray": ["title", "heavy-rain"],
    "Ossiblepay Ightlay Eetslay": ["title", "possible-very-light-sleet"],
    "Ightlay Eetslay": ["title", "very-light-sleet"],
    "Eetslay": ["title", "medium-sleet"],
    "Eavyhay Eetslay": ["title", "heavy-sleet"],
    "Ossiblepay Urriesflay": ["title", "possible-very-light-snow"],
    "Urriesflay": ["title", "very-light-snow"],
    "Ossiblepay Ightlay Owsnay": ["title", "possible-light-snow"],
    "Ightlay Owsnay": ["title", "light-snow"],
    "Owsnay": ["title", "medium-snow"],
    "Eavyhay Owsnay": ["title", "heavy-snow"],
    "Indyway": ["title", "medium-wind"],
    "Angerouslyday Indyway": ["title", "heavy-wind"],
    "Oggyfay": ["title", "fog"],
    "Ostlymay Earclay": ["title", "very-light-clouds"],
    "Artlypay Oudyclay": ["title", "light-clouds"],
    "Ostlymay Oudyclay": ["title", "medium-clouds"],
    "Overcastway": ["title", "heavy-clouds"],
    "Ydray andway Eezybray": ["title", ["and", "low-humidity", "light-wind"]],
    "Izzledray andway Angerouslyday Indyway": [
        "title",
        ["and", "very-light-rain", "heavy-wind"],
    ],
    "Umidhay andway Artlypay Oudyclay": [
        "title",
        ["and", "high-humidity", "light-clouds"],
    ],
    "Earclay orfay ethay hourway.": ["sentence", ["for-hour", "clear"]],
    "Urriesflay artingstay inway 35 min.": [
        "sentence",
        ["starting-in", "very-light-snow", ["minutes", 35]],
    ],
    "Ightlay ainray endingway inway 15 min.": [
        "sentence",
        ["stopping-in", "light-rain", ["minutes", 15]],
    ],
    "Eavyhay eetslay artingstay inway 20 min, endingway 30 min aterlay.": [
        "sentence",
        [
            "starting-then-stopping-later",
            "heavy-sleet",
            ["minutes", 20],
            ["minutes", 30],
        ],
    ],
    "Ainray endingway inway 25 min, eturningray 8 min aterlay.": [
        "sentence",
        [
            "stopping-then-starting-later",
            "medium-rain",
            ["minutes", 25],
            ["minutes", 8],
        ],
    ],
    "Ostlymay oudyclay oughoutthray ethay ayday.": [
        "sentence",
        ["for-day", "medium-clouds"],
    ],
    "Ightlay eetslay artingstay inway ethay orningmay.": [
        "sentence",
        ["starting", "very-light-sleet", "morning"],
    ],
    "Indyway untilway onighttay.": [
        "sentence",
        ["until", "medium-wind", "today-night"],
    ],
    "Eavyhay ecipitationpray untilway afternoonway.": [
        "sentence",
        ["until", "heavy-precipitation", "afternoon"],
    ],
    "Eezybray inway ethay afternoonway.": [
        "sentence",
        ["during", "light-wind", "afternoon"],
    ],
    "Owsnay aterlay isthay eveningway andway omorrowtay orningmay.": [
        "sentence",
        ["during", "medium-snow", ["and", "later-today-evening", "tomorrow-morning"]],
    ],
    "Eavyhay ainray untilway aterlay isthay orningmay, eturningray isthay eveningway.": [
        "sentence",
        ["until-starting-again", "heavy-rain", "later-today-morning", "today-evening"],
    ],
    "Overcastway omfray eveningway untilway ightnay.": [
        "sentence",
        ["starting-continuing-until", "heavy-clouds", "evening", "night"],
    ],
    "Ightlay eetslay aterlay isthay afternoonway andway oggyfay omorrowtay orningmay.": [
        "sentence",
        [
            "and",
            ["during", "light-sleet", "later-today-afternoon"],
            ["during", "fog", "tomorrow-morning"],
        ],
    ],
    "Angerouslyday indyway omfray isthay orningmay untilway isthay afternoonway andway eetslay omorrowtay orningmay.": [
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
    "Overcastway artingstay aterlay onighttay andway eavyhay owsnay omorrowtay afternoonway.": [
        "sentence",
        [
            "and",
            ["starting", "heavy-clouds", "later-today-night"],
            ["during", "heavy-snow", "tomorrow-afternoon"],
        ],
    ],
    "Ydray onighttay andway ightlay ecipitationpray omfray omorrowtay eveningway untilway omorrowtay ightnay.": [
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
    "Owsnay (5 in) overnightway.": [
        "sentence",
        ["during", ["parenthetical", "medium-snow", ["inches", 5]], "night"],
    ],
    "Ightlay owsnay (2 cm) aterlay isthay orningmay.": [
        "sentence",
        [
            "during",
            ["parenthetical", "light-snow", ["centimeters", 2]],
            "later-today-morning",
        ],
    ],
    "Eavyhay owsnay (8\u201312 in) oughoutthray ethay ayday.": [
        "sentence",
        ["for-day", ["parenthetical", "heavy-snow", ["inches", ["range", 8, 12]]]],
    ],
    "Owsnay (underway 1 cm) inway ethay afternoonway.": [
        "sentence",
        [
            "during",
            ["parenthetical", "medium-snow", ["less-than", ["centimeters", 1]]],
            "afternoon",
        ],
    ],
    "Onay ecipitationpray oughoutthray ethay eekway, ithway ighshay eachingray 85\u00b0F omorrowtay.": [
        "sentence",
        [
            "with",
            ["for-week", "no-precipitation"],
            ["temperatures-peaking", ["fahrenheit", 85], "tomorrow"],
        ],
    ],
    "Ixedmay ecipitationpray overway ethay eekendway, ithway ighshay imbingclay otay 32\u00b0C onway ursdaythay.": [
        "sentence",
        [
            "with",
            ["over-weekend", "mixed-precipitation"],
            ["temperatures-rising", ["celsius", 32], "thursday"],
        ],
    ],
    "Izzledray onway ondaymay, ithway ighshay ippingday otay 15\u00b0F onway idayfray.": [
        "sentence",
        [
            "with",
            ["during", "very-light-rain", "monday"],
            ["temperatures-valleying", ["fahrenheit", 15], "friday"],
        ],
    ],
    "Ightlay owsnay onway uesdaytay andway extnay ednesdayway, ithway ighshay allingfay otay 0\u00b0C onway undaysay.": [
        "sentence",
        [
            "with",
            ["during", "light-snow", ["and", "tuesday", "next-wednesday"]],
            ["temperatures-falling", ["celsius", 0], "sunday"],
        ],
    ],
    "Ecipitationpray odaytay oughthray aturdaysay, ithway ighshay eachingray 100\u00b0F onway ondaymay.": [
        "sentence",
        [
            "with",
            ["during", "medium-precipitation", ["through", "today", "saturday"]],
            ["temperatures-peaking", ["fahrenheit", 100], "monday"],
        ],
    ],
    "Ossiblepay Understormsthay": ["title", "possible-thunderstorm"],
    "Eavyhay Ainray andway Understormsthay": [
        "title",
        ["and", "heavy-rain", "thunderstorm"],
    ],
    "Extnay hourway orecastsfay areway emporarilytay unavailableway ueday otay allway earbynay adarray tationssay eingbay offlineway.": [
        "sentence",
        ["next-hour-forecast-status", "temporarily-unavailable", "station-offline"],
    ],
    "Extnay hourway orecastsfay areway artiallypay unavailableway ueday otay apsgay inway overagecay romfay earbynay adarray ationsstay.": [
        "sentence",
        ["next-hour-forecast-status", "partially-unavailable", "station-incomplete"],
    ],
    "Extnay hourway orecastsfay areway unavailableway ueday otay allway earbynay adarray tationssay eingbay offlineway.": [
        "sentence",
        ["next-hour-forecast-status", "unavailable", "station-offline"],
    ],
    "Okesmay": ["title", "smoke"],
    "Okesmay oughoutthray ethay ayday.": ["sentence", ["for-day", "smoke"]],
    "Okesmay inway ethay orningmay.": ["sentence", ["during", "smoke", "morning"]],
    "Okesmay untilway isthay eveningway.": [
        "sentence",
        ["until", "smoke", "today-evening"],
    ],
    "Okesmay andway Artlypay Oudyclay": ["title", ["and", "smoke", "light-clouds"]],
    "Azehay": ["title", "haze"],
    "Azehay oughoutthray ethay ayday.": ["sentence", ["for-day", "haze"]],
    "Azehay inway ethay afternoonway.": ["sentence", ["during", "haze", "afternoon"]],
    "Azehay andway Umidhay": ["title", ["and", "haze", "high-humidity"]],
    "Istymay": ["title", "mist"],
    "Istymay oughoutthray ethay ayday.": ["sentence", ["for-day", "mist"]],
    "Istymay overnightway.": ["sentence", ["during", "mist", "night"]],
    "Istymay andway Overcastway": ["title", ["and", "mist", "heavy-clouds"]],
}
