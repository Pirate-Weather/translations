# This would be one of your translations, as a Python dictionary
cases = {
    "Ясно": ["title", "clear"],
    "Възможни Незначителни Превалявания": [
        "title",
        "possible-very-light-precipitation",
    ],
    "Незначителни Превалявания": ["title", "very-light-precipitation"],
    "Възможни Леки Превалявания": ["title", "possible-light-precipitation"],
    "Леки Превалявания": ["title", "light-precipitation"],
    "Превалявания": ["title", "medium-precipitation"],
    "Силни Превалявания": ["title", "heavy-precipitation"],
    "Възможен Ръмеж": ["title", "possible-very-light-rain"],
    "Ръмеж": ["title", "very-light-rain"],
    "Възможен Слаб Дъжд": ["title", "possible-light-rain"],
    "Слаб Дъжд": ["title", "light-rain"],
    "Дъжд": ["title", "medium-rain"],
    "Силен Дъжд": ["title", "heavy-rain"],
    "Възможна Много Слаба Градушка": ["title", "possible-very-light-sleet"],
    "Много Слаба Градушка": ["title", "very-light-sleet"],
    "Възможна Слаба Градушка": ["title", "possible-light-sleet"],
    "Слаба Градушка": ["title", "light-sleet"],
    "Градушка": ["title", "medium-sleet"],
    "Силна Градушка": ["title", "heavy-sleet"],
    "Възможен Много Слаб Сняг": ["title", "possible-very-light-snow"],
    "Много Слаб Сняг": ["title", "very-light-snow"],
    "Възможен Слаб Сняг": ["title", "possible-light-snow"],
    "Слаб Сняг": ["title", "light-snow"],
    "Снеговалеж": ["title", "medium-snow"],
    "Силен Снеговалеж": ["title", "heavy-snow"],
    "Слаб Вятър": ["title", "light-wind"],
    "Умерен Вятър": ["title", "medium-wind"],
    "Силен Вятър": ["title", "heavy-wind"],
    "Сухо": ["title", "low-humidity"],
    "Влажно": ["title", "high-humidity"],
    "Мъгла": ["title", "fog"],
    "Предимно Ясно": ["title", "very-light-clouds"],
    "Незначителна Облачност": ["title", "light-clouds"],
    "Облачно": ["title", "medium-clouds"],
    "Гъста Облачност": ["title", "heavy-clouds"],
    "Сухо и Слаб Вятър": ["title", ["and", "low-humidity", "light-wind"]],
    "Ръмеж и Силен Вятър": ["title", ["and", "very-light-rain", "heavy-wind"]],
    "Влажно и Незначителна Облачност": [
        "title",
        ["and", "high-humidity", "light-clouds"],
    ],
    "Ясно през следващия час.": ["sentence", ["for-hour", "clear"]],
    "Много слаб сняг започва след 35 мин.": [
        "sentence",
        ["starting-in", "very-light-snow", ["minutes", 35]],
    ],
    "Слаб дъжд приключва до 15 мин.": [
        "sentence",
        ["stopping-in", "light-rain", ["minutes", 15]],
    ],
    "Силна градушка започва след 20 мин, и приключва до 30 мин по-късно.": [
        "sentence",
        [
            "starting-then-stopping-later",
            "heavy-sleet",
            ["minutes", 20],
            ["minutes", 30],
        ],
    ],
    "Дъжд приключва до 25 мин, и започва отново след 80 мин.": [
        "sentence",
        [
            "stopping-then-starting-later",
            "medium-rain",
            ["minutes", 25],
            ["minutes", 80],
        ],
    ],
    "Облачно през целия ден.": ["sentence", ["for-day", "medium-clouds"]],
    "Много слаба градушка започва сутринта.": [
        "sentence",
        ["starting", "very-light-sleet", "morning"],
    ],
    "Умерен вятър през нощта.": ["sentence", ["until", "medium-wind", "today-night"]],
    "Силни превалявания следобед.": [
        "sentence",
        ["until", "heavy-precipitation", "afternoon"],
    ],
    "Слаб вятър следобед.": ["sentence", ["during", "light-wind", "afternoon"]],
    "Снеговалеж по-късно вечерта и утре сутринта.": [
        "sentence",
        ["during", "medium-snow", ["and", "later-today-evening", "tomorrow-morning"]],
    ],
    "Силен дъжд до по-късно тази сутрин, започва отново вечерта.": [
        "sentence",
        ["until-starting-again", "heavy-rain", "later-today-morning", "today-evening"],
    ],
    "Гъста облачност, започва от вечерта, до през нощта.": [
        "sentence",
        ["starting-continuing-until", "heavy-clouds", "evening", "night"],
    ],
    "Слаба градушка по-късно днес следобед и мъгла утре сутринта.": [
        "sentence",
        [
            "and",
            ["during", "light-sleet", "later-today-afternoon"],
            ["during", "fog", "tomorrow-morning"],
        ],
    ],
    "Силен вятър, започва от сутринта, до следобед, и градушка утре сутринта.": [
        "sentence",
        [
            "and",
            ["starting-continuing-until", "heavy-wind", "morning", "afternoon"],
            ["during", "medium-sleet", "tomorrow-morning"],
        ],
    ],
    "Гъста облачност започва по-късно през нощта и силен снеговалеж утре следобед.": [
        "sentence",
        [
            "and",
            ["starting", "heavy-clouds", "later-today-night"],
            ["during", "heavy-snow", "tomorrow-afternoon"],
        ],
    ],
    "Сухо през нощта и леки превалявания, започва от утре вечерта, до утре през нощта.": [
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
    "Снеговалеж (5 см.) през нощта.": [
        "sentence",
        ["during", ["parenthetical", "medium-snow", ["centimeters", 5]], "night"],
    ],
    "Слаб сняг (2 см.) по-късно тази сутрин.": [
        "sentence",
        [
            "during",
            ["parenthetical", "light-snow", ["centimeters", 2]],
            "later-today-morning",
        ],
    ],
    "Силен снеговалеж (8–12 in.) през целия ден.": [
        "sentence",
        ["for-day", ["parenthetical", "heavy-snow", ["inches", ["range", 8, 12]]]],
    ],
    "Снеговалеж (по-малко 1 см.) следобед.": [
        "sentence",
        [
            "during",
            ["parenthetical", "medium-snow", ["less-than", ["centimeters", 1]]],
            "afternoon",
        ],
    ],
    "Без превалявания през седмицата, с максимални температури, достигащи 35°F утре.": [
        "sentence",
        [
            "with",
            ["for-week", "no-precipitation"],
            ["temperatures-peaking", ["fahrenheit", 35], "tomorrow"],
        ],
    ],
    "Смесени превалявания през уикенда, с максимални температури, покачващи се до 32°C в четвъртък.": [
        "sentence",
        [
            "with",
            ["over-weekend", "mixed-precipitation"],
            ["temperatures-rising", ["celsius", 32], "thursday"],
        ],
    ],
    "Ръмеж в понеделник, с максимални температури, падащи до 15°C в петък.": [
        "sentence",
        [
            "with",
            ["during", "very-light-rain", "monday"],
            ["temperatures-valleying", ["celsius", 15], "friday"],
        ],
    ],
    "Слаб сняг във вторник и в сряда, с максимални температури, падащи до минимум 0°C в неделя.": [
        "sentence",
        [
            "with",
            ["during", "light-snow", ["and", "tuesday", "wednesday"]],
            ["temperatures-falling", ["celsius", 0], "sunday"],
        ],
    ],
    "Превалявания от днес до събота, с максимални температури, достигащи 37°C в понеделник.": [
        "sentence",
        [
            "with",
            ["during", "medium-precipitation", ["through", "today", "saturday"]],
            ["temperatures-peaking", ["celsius", 37], "monday"],
        ],
    ],
    "Смесени превалявания (1–3 in.) през целия ден.": [
        "sentence",
        [
            "for-day",
            ["parenthetical", "mixed-precipitation", ["inches", ["range", 1, 3]]],
        ],
    ],
    "Слаб сняг във вторник и следващата сряда, с максимални температури, падащи до минимум 0\u00b0C в неделя.": [
        "sentence",
        [
            "with",
            ["during", "light-snow", ["and", "tuesday", "next-wednesday"]],
            ["temperatures-falling", ["celsius", 0], "sunday"],
        ],
    ],
    "Възможна Гръмотевична Буря": ["title", "possible-thunderstorm"],
    "Силен Дъжд и Гръмотевична Буря": ["title", ["and", "heavy-rain", "thunderstorm"]],
    "Прогнозата за идния час временно не е на разположение поради това че всички близки станции не са на линия.": [
        "sentence",
        ["next-hour-forecast-status", "temporarily-unavailable", "station-offline"],
    ],
    "Прогнозата за идния час е частична поради пропуски в покритието от близки станции.": [
        "sentence",
        ["next-hour-forecast-status", "partially-unavailable", "station-incomplete"],
    ],
}
