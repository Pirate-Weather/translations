# This would be one of your translations, as a Python dictionary
cases = {
    "Ясно": ["title", "clear"],
    "Возможны Незначительные Осадки": ["title", "possible-very-light-precipitation"],
    "Незначительные Осадки": ["title", "very-light-precipitation"],
    "Возможны Небольшие Осадки": ["title", "possible-light-precipitation"],
    "Небольшие Осадки": ["title", "light-precipitation"],
    "Осадки": ["title", "medium-precipitation"],
    "Сильные Осадки": ["title", "heavy-precipitation"],
    "Возможен Незначительный Дождь": ["title", "possible-very-light-rain"],
    "Незначительный Дождь": ["title", "very-light-rain"],
    "Возможен Небольшой Дождь": ["title", "possible-light-rain"],
    "Небольшой Дождь": ["title", "light-rain"],
    "Дождь": ["title", "medium-rain"],
    "Сильный Дождь": ["title", "heavy-rain"],
    "Возможен Незначительный Град": ["title", "possible-very-light-sleet"],
    "Незначительный Град": ["title", "very-light-sleet"],
    "Возможен Небольшой Град": ["title", "possible-light-sleet"],
    "Небольшой Град": ["title", "light-sleet"],
    "Град": ["title", "medium-sleet"],
    "Сильный Град": ["title", "heavy-sleet"],
    "Возможен Незначительный Снег": ["title", "possible-very-light-snow"],
    "Незначительный Снег": ["title", "very-light-snow"],
    "Возможен Небольшой Снег": ["title", "possible-light-snow"],
    "Небольшой Снег": ["title", "light-snow"],
    "Снег": ["title", "medium-snow"],
    "Снегопад": ["title", "heavy-snow"],
    "Слабый Ветер": ["title", "light-wind"],
    "Ветер": ["title", "medium-wind"],
    "Сильный Ветер": ["title", "heavy-wind"],
    "Сухо": ["title", "low-humidity"],
    "Влажно": ["title", "high-humidity"],
    "Туман": ["title", "fog"],
    "Почти Ясно": ["title", "very-light-clouds"],
    "Небольшая Облачность": ["title", "light-clouds"],
    "Облачно": ["title", "medium-clouds"],
    "Сильная Облачность": ["title", "heavy-clouds"],
    "Сухо и Слабый Ветер": ["title", ["and", "low-humidity", "light-wind"]],
    "Незначительный Дождь и Сильный Ветер": [
        "title",
        ["and", "very-light-rain", "heavy-wind"],
    ],
    "Влажно и Небольшая Облачность": [
        "title",
        ["and", "high-humidity", "light-clouds"],
    ],
    "Ясно в течение следующего часа.": ["sentence", ["for-hour", "clear"]],
    "Незначительный снег начинается в течение 35 мин.": [
        "sentence",
        ["starting-in", "very-light-snow", ["minutes", 35]],
    ],
    "Небольшой дождь заканчивается в течение 15 мин.": [
        "sentence",
        ["stopping-in", "light-rain", ["minutes", 15]],
    ],
    "Сильный град начинается в течение 20 мин, и заканчивается через 30 мин.": [
        "sentence",
        [
            "starting-then-stopping-later",
            "heavy-sleet",
            ["minutes", 20],
            ["minutes", 30],
        ],
    ],
    "Дождь заканчивается в течение 25 мин, и начинается снова через 8 мин.": [
        "sentence",
        [
            "stopping-then-starting-later",
            "medium-rain",
            ["minutes", 25],
            ["minutes", 8],
        ],
    ],
    "Облачно в течение всего дня.": ["sentence", ["for-day", "medium-clouds"]],
    "Незначительный град начинается утром.": [
        "sentence",
        ["starting", "very-light-sleet", "morning"],
    ],
    "Ветер до сегодняшней ночи.": ["sentence", ["until", "medium-wind", "today-night"]],
    "Сильные осадки до середины дня.": [
        "sentence",
        ["until", "heavy-precipitation", "afternoon"],
    ],
    "Слабый ветер днем.": ["sentence", ["during", "light-wind", "afternoon"]],
    "Снег сегодня поздним вечером и завтра утром.": [
        "sentence",
        ["during", "medium-snow", ["and", "later-today-evening", "tomorrow-morning"]],
    ],
    "Сильный дождь до сегодняшнего позднего утра, начинаясь снова сегодня вечером.": [
        "sentence",
        ["until-starting-again", "heavy-rain", "later-today-morning", "today-evening"],
    ],
    "Сильная облачность, начинаясь с вечера, и до ночи.": [
        "sentence",
        ["starting-continuing-until", "heavy-clouds", "evening", "night"],
    ],
    "Небольшой град сегодня поздним днем и туман завтра утром.": [
        "sentence",
        [
            "and",
            ["during", "light-sleet", "later-today-afternoon"],
            ["during", "fog", "tomorrow-morning"],
        ],
    ],
    "Сильный ветер, начинаясь с утра, и до середины дня, и град завтра утром.": [
        "sentence",
        [
            "and",
            ["starting-continuing-until", "heavy-wind", "morning", "afternoon"],
            ["during", "medium-sleet", "tomorrow-morning"],
        ],
    ],
    "Сильная облачность начинается сегодня поздней ночью и снегопад завтра днем.": [
        "sentence",
        [
            "and",
            ["starting", "heavy-clouds", "later-today-night"],
            ["during", "heavy-snow", "tomorrow-afternoon"],
        ],
    ],
    "Сухо сегодня ночью и небольшие осадки, начинаясь с завтрашнего вечера, и до завтрашней ночи.": [
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
    "Снег (5 см.) ночью.": [
        "sentence",
        ["during", ["parenthetical", "medium-snow", ["centimeters", 5]], "night"],
    ],
    "Небольшой снег (2 см.) сегодня поздним утром.": [
        "sentence",
        [
            "during",
            ["parenthetical", "light-snow", ["centimeters", 2]],
            "later-today-morning",
        ],
    ],
    "Снег (меньше 1 см.) днем.": [
        "sentence",
        [
            "during",
            ["parenthetical", "medium-snow", ["less-than", ["centimeters", 1]]],
            "afternoon",
        ],
    ],
    "Без осадков в течение всей недели, с температурой, поднимающейся до максимума 35\u00b0C завтра.": [
        "sentence",
        [
            "with",
            ["for-week", "no-precipitation"],
            ["temperatures-peaking", ["celsius", 35], "tomorrow"],
        ],
    ],
    "Смешанные осадки в течение всех выходных, с температурой, поднимающейся до 32\u00b0C в четверг.": [
        "sentence",
        [
            "with",
            ["over-weekend", "mixed-precipitation"],
            ["temperatures-rising", ["celsius", 32], "thursday"],
        ],
    ],
    "Незначительный дождь в понедельник, с температурой, опускающейся до 15\u00b0C в пятницу.": [
        "sentence",
        [
            "with",
            ["during", "very-light-rain", "monday"],
            ["temperatures-valleying", ["celsius", 15], "friday"],
        ],
    ],
    "Небольшой снег во вторник и в среду, с температурой, опускающейся до минимума 0°C в воскресенье.": [
        "sentence",
        [
            "with",
            ["during", "light-snow", ["and", "tuesday", "wednesday"]],
            ["temperatures-falling", ["celsius", 0], "sunday"],
        ],
    ],
    "Осадки сегодня и до субботы, с температурой, поднимающейся до максимума 37°C в понедельник.": [
        "sentence",
        [
            "with",
            ["during", "medium-precipitation", ["through", "today", "saturday"]],
            ["temperatures-peaking", ["celsius", 37], "monday"],
        ],
    ],
    "Возможны Грозы": ["title", "possible-thunderstorm"],
    "Сильный Дождь и Грозы": ["title", ["and", "heavy-rain", "thunderstorm"]],
    "Небольшой снег во вторник и в следующую среду, с температурой, опускающейся до минимума 0°C в воскресенье.": [
        "sentence",
        [
            "with",
            ["during", "light-snow", ["and", "tuesday", "next-wednesday"]],
            ["temperatures-falling", ["celsius", 0], "sunday"],
        ],
    ],
    "Дым": ["title", "smoke"],
    "Дым в течение всего дня.": ["sentence", ["for-day", "smoke"]],
    "Дым утром.": ["sentence", ["during", "smoke", "morning"]],
    "Дым до сегодняшнего вечера.": ["sentence", ["until", "smoke", "today-evening"]],
    "Дым и Небольшая Облачность": ["title", ["and", "smoke", "light-clouds"]],
    "Мгла": ["title", "haze"],
    "Мгла в течение всего дня.": ["sentence", ["for-day", "haze"]],
    "Мгла днем.": ["sentence", ["during", "haze", "afternoon"]],
    "Мгла и Влажно": ["title", ["and", "haze", "high-humidity"]],
    "Туман в течение всего дня.": ["sentence", ["for-day", "mist"]],
    "Туман ночью.": ["sentence", ["during", "mist", "night"]],
    "Туман и Сильная Облачность": ["title", ["and", "mist", "heavy-clouds"]],
    "Грозы в течение следующего часа.": ["sentence", ["for-hour", "thunderstorm"]],
    "Град начинается в течение 5 мин, и заканчивается через 45 мин.": [
        "sentence",
        [
            "starting-then-stopping-later",
            "hail",
            ["minutes", 5],
            ["minutes", 45],
        ],
    ],
    "Сильный ледяной дождь заканчивается в течение 10 мин, и начинается снова через 32 мин.": [
        "sentence",
        [
            "stopping-then-starting-later",
            "heavy-freezing-rain",
            ["minutes", 10],
            ["minutes", 32],
        ],
    ],
    "Ледяная морось начинается в течение 49 мин.": [
        "sentence",
        ["starting-in", "very-light-freezing-rain", ["minutes", 49]],
    ],
}
