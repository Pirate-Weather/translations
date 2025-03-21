# This would be one of your translations, as a Python dictionary
cases = {
    "Glan": ["title", "clear"],
    "Seans Ar Frasaíocht An-éadrom": ["title", "possible-very-light-precipitation"],
    "Frasaíocht An-éadrom": ["title", "very-light-precipitation"],
    "Seans Ar Frasaíocht Éadrom": ["title", "possible-light-precipitation"],
    "Frasaíocht Éadrom": ["title", "light-precipitation"],
    "Frasaíocht": ["title", "medium-precipitation"],
    "Frasaíocht Throm": ["title", "heavy-precipitation"],
    "Seans Ar Fearthainn An-éadrom": ["title", "possible-very-light-rain"],
    "Fearthainn An-éadrom": ["title", "very-light-rain"],
    "Seans Ar Fearthainn Éadrom": ["title", "possible-light-rain"],
    "Fearthainn Éadrom": ["title", "light-rain"],
    "Fearthainn": ["title", "medium-rain"],
    "Fearthainn Throm": ["title", "heavy-rain"],
    "Seans Ar Flichshneachta An-éadrom": ["title", "possible-very-light-sleet"],
    "Flichshneachta An-éadrom": ["title", "very-light-sleet"],
    "Seans Ar Flichshneachta Éadrom": ["title", "possible-light-sleet"],
    "Flichshneachta Éadrom": ["title", "light-sleet"],
    "Flichshneachta": ["title", "medium-sleet"],
    "Flichshneachta Trom": ["title", "heavy-sleet"],
    "Seans Ar Sneachta An-éadrom": ["title", "possible-very-light-snow"],
    "Sneachta An-éadrom": ["title", "very-light-snow"],
    "Seans Ar Sneachta Éadrom": ["title", "possible-light-snow"],
    "Sneachta Éadrom": ["title", "light-snow"],
    "Sneachta": ["title", "medium-snow"],
    "Sneachta Trom": ["title", "heavy-snow"],
    "Laoithne Mheasarth": ["title", "medium-wind"],
    "Laoithne Láidir": ["title", "heavy-wind"],
    "Ceoch": ["title", "fog"],
    "Scamaill Glan": ["title", "very-light-clouds"],
    "Scamaill Bhána": ["title", "light-clouds"],
    "Scamaill Mheasartha": ["title", "medium-clouds"],
    "Scamaill Throma": ["title", "heavy-clouds"],
    "Bogthaise Íseal Agus Laoithne Éadrom": [
        "title",
        ["and", "low-humidity", "light-wind"],
    ],
    "Fearthainn An-éadrom Agus Laoithne Láidir": [
        "title",
        ["and", "very-light-rain", "heavy-wind"],
    ],
    "Bogthaise Ard Agus Scamaill Bhána": [
        "title",
        ["and", "high-humidity", "light-clouds"],
    ],
    "Glan ar feadh uair an chloig.": ["sentence", ["for-hour", "clear"]],
    "Sneachta an-éadrom ag tosú i 35 nóim.": [
        "sentence",
        ["starting-in", "very-light-snow", ["minutes", 35]],
    ],
    "Fearthainn éadrom ag stopadh i 15 nóim.": [
        "sentence",
        ["stopping-in", "light-rain", ["minutes", 15]],
    ],
    "Flichshneachta trom ag tosú i 20 nóim., ag stopadh i 30 nóim.": [
        "sentence",
        [
            "starting-then-stopping-later",
            "heavy-sleet",
            ["minutes", 20],
            ["minutes", 30],
        ],
    ],
    "Fearthainn ag stopadh i 25 nóim., ag tosú arís i 8 nóim.": [
        "sentence",
        [
            "stopping-then-starting-later",
            "medium-rain",
            ["minutes", 25],
            ["minutes", 8],
        ],
    ],
    "Scamaill mheasartha ar feadh an lae.": ["sentence", ["for-day", "medium-clouds"]],
    "Flichshneachta an-éadrom ag tosú ar maidin.": [
        "sentence",
        ["starting", "very-light-sleet", "morning"],
    ],
    "Laoithne mheasarth ag stopadh anocht.": [
        "sentence",
        ["until", "medium-wind", "today-night"],
    ],
    "Frasaíocht throm ag stopadh iarnóin.": [
        "sentence",
        ["until", "heavy-precipitation", "afternoon"],
    ],
    "Laoithne éadrom iarnóin.": ["sentence", ["during", "light-wind", "afternoon"]],
    "Sneachta níos déanaí ar tráthnóna inniu agus maidin amárach.": [
        "sentence",
        ["during", "medium-snow", ["and", "later-today-evening", "tomorrow-morning"]],
    ],
    "Fearthainn throm ag stopadh níos déanaí ar maidin inniu, ag tosú arís tráthnóna inniu.": [
        "sentence",
        ["until-starting-again", "heavy-rain", "later-today-morning", "today-evening"],
    ],
    "Scamaill throma ag tosú tráthnóna, ag stopadh anocht.": [
        "sentence",
        ["starting-continuing-until", "heavy-clouds", "evening", "night"],
    ],
    "Flichshneachta éadrom níos déanaí ar iarnóin inniu agus ceoch maidin amárach.": [
        "sentence",
        [
            "and",
            ["during", "light-sleet", "later-today-afternoon"],
            ["during", "fog", "tomorrow-morning"],
        ],
    ],
    "Laoithne láidir ag tosú maidin inniu, ag stopadh iarnóin inniu agus flichshneachta maidin amárach.": [
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
    "Scamaill throma ag tosú níos déanaí anocht agus sneachta trom iarnóin amárach.": [
        "sentence",
        [
            "and",
            ["starting", "heavy-clouds", "later-today-night"],
            ["during", "heavy-snow", "tomorrow-afternoon"],
        ],
    ],
    "Bogthaise íseal anocht agus frasaíocht éadrom ag tosú tráthnóna amárach, ag stopadh oiche amárach.": [
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
    "Sneachta (5 orl.) anocht.": [
        "sentence",
        ["during", ["parenthetical", "medium-snow", ["inches", 5]], "night"],
    ],
    "Sneachta éadrom (2 cm.) níos déanaí ar maidin inniu.": [
        "sentence",
        [
            "during",
            ["parenthetical", "light-snow", ["centimeters", 2]],
            "later-today-morning",
        ],
    ],
    "Sneachta trom (8\u201312 orl.) ar feadh an lae.": [
        "sentence",
        ["for-day", ["parenthetical", "heavy-snow", ["inches", ["range", 8, 12]]]],
    ],
    "Sneachta (< 1 cm.) iarnóin.": [
        "sentence",
        [
            "during",
            ["parenthetical", "medium-snow", ["less-than", ["centimeters", 1]]],
            "afternoon",
        ],
    ],
    "Ní bheidh frasaíocht ann ar feadh na seachtaine, le an teocht dul chomh hard le 85\u00b0F amárach.": [
        "sentence",
        [
            "with",
            ["for-week", "no-precipitation"],
            ["temperatures-peaking", ["fahrenheit", 85], "tomorrow"],
        ],
    ],
    "Frasaíocht éagsúil ar feadh an deireadh seachtaine, le an teteocht dul chomh hard le 32\u00b0C Déardaoin.": [
        "sentence",
        [
            "with",
            ["over-weekend", "mixed-precipitation"],
            ["temperatures-rising", ["celsius", 32], "thursday"],
        ],
    ],
    "Fearthainn an-éadrom Dé Luain, le an teocht dul chomh íseal le 15\u00b0F Dé hAoine.": [
        "sentence",
        [
            "with",
            ["during", "very-light-rain", "monday"],
            ["temperatures-valleying", ["fahrenheit", 15], "friday"],
        ],
    ],
    "Sneachta éadrom Dé Máirt agus Dé Céadaoin seo chugainn, le an teocht dul chomh íseal le 0\u00b0C Dé Domhnaigh.": [
        "sentence",
        [
            "with",
            ["during", "light-snow", ["and", "tuesday", "next-wednesday"]],
            ["temperatures-falling", ["celsius", 0], "sunday"],
        ],
    ],
    "Frasaíocht inniu go dtí Dé Sathairn, le an teocht dul chomh hard le 100\u00b0F Dé Luain.": [
        "sentence",
        [
            "with",
            ["during", "medium-precipitation", ["through", "today", "saturday"]],
            ["temperatures-peaking", ["fahrenheit", 100], "monday"],
        ],
    ],
    "Seans ar stoirm thoirní Dé Céadaoin seo chugainn agus Déardaoin seo chugainn.": [
        "sentence",
        ["during", "possible-thunderstorm", ["and", "next-wednesday", "next-thursday"]],
    ],
    "Níl réamhaisnéise an uair seo chugainn ar fáil i láthair na huaire mar go bhfuil gach stáisiún radair atá in aice láimhe as líne.": [
        "sentence",
        ["next-hour-forecast-status", "temporarily-unavailable", "station-offline"],
    ],
    "Níl réamhaisnéise an uair seo chugainn ar fáil go hiomlán mar go bhfuil bearnaí san fhaisnéis ó na stáisiúin radair atá in aice láimhe.": [
        "sentence",
        ["next-hour-forecast-status", "partially-unavailable", "station-incomplete"],
    ],
    "Níl réamhaisnéise an uair seo chugainn ar fáil mar go bhfuil gach stáisiún radair atá in aice láimhe as líne.": [
        "sentence",
        ["next-hour-forecast-status", "unavailable", "station-offline"],
    ],
}
