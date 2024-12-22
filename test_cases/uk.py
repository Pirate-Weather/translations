# This would be one of your translations, as a Python dictionary
cases = {
    "Ясно": ["title", "clear"],
    "Можливі Незначні Опади": ["title", "possible-very-light-precipitation"],
    "Незначні Опади": ["title", "very-light-precipitation"],
    "Можливі Невеликі Опади": ["title", "possible-light-precipitation"],
    "Невеликі Опади": ["title", "light-precipitation"],
    "Опади": ["title", "medium-precipitation"],
    "Сильні Опади": ["title", "heavy-precipitation"],
    "Можливий Незначний Дощ": ["title", "possible-very-light-rain"],
    "Незначний Дощ": ["title", "very-light-rain"],
    "Можливий Невеликий Дощ": ["title", "possible-light-rain"],
    "Невеликий Дощ": ["title", "light-rain"],
    "Дощ": ["title", "medium-rain"],
    "Сильний Дощ": ["title", "heavy-rain"],
    "Можливий Незначний Град": ["title", "possible-very-light-sleet"],
    "Незначний Град": ["title", "very-light-sleet"],
    "Можливий Невеликий Град": ["title", "possible-light-sleet"],
    "Невеликий Град": ["title", "light-sleet"],
    "Град": ["title", "medium-sleet"],
    "Сильний Град": ["title", "heavy-sleet"],
    "Можливий Незначний Сніг": ["title", "possible-very-light-snow"],
    "Незначний Сніг": ["title", "very-light-snow"],
    "Можливий Невеликий Сніг": ["title", "possible-light-snow"],
    "Невеликий Сніг": ["title", "light-snow"],
    "Сніг": ["title", "medium-snow"],
    "Снігопад": ["title", "heavy-snow"],
    "Слабкий Вітер": ["title", "light-wind"],
    "Вітер": ["title", "medium-wind"],
    "Сильний Вітер": ["title", "heavy-wind"],
    "Сухо": ["title", "low-humidity"],
    "Волого": ["title", "high-humidity"],
    "Туман": ["title", "fog"],
    "Переважно Ясно": ["title", "very-light-clouds"],
    "Невелика Хмарність": ["title", "light-clouds"],
    "Хмарно": ["title", "medium-clouds"],
    "Сильна Хмарність": ["title", "heavy-clouds"],
    "Сухо і Слабкий Вітер": ["title", ["and", "low-humidity", "light-wind"]],
    "Незначний Дощ і Сильний Вітер": [
        "title",
        ["and", "very-light-rain", "heavy-wind"],
    ],
    "Волого і Невелика Хмарність": ["title", ["and", "high-humidity", "light-clouds"]],
    "Ясно протягом наступної години.": ["sentence", ["for-hour", "clear"]],
    "Незначний сніг починається за 35 хв.": [
        "sentence",
        ["starting-in", "very-light-snow", ["minutes", 35]],
    ],
    "Невеликий дощ закінчується за 15 хв.": [
        "sentence",
        ["stopping-in", "light-rain", ["minutes", 15]],
    ],
    "Сильний град починається за 20 хв., і закінчується за 30 хв.": [
        "sentence",
        [
            "starting-then-stopping-later",
            "heavy-sleet",
            ["minutes", 20],
            ["minutes", 30],
        ],
    ],
    "Дощ закінчується за 25 хв., і починається знову за 8 хв.": [
        "sentence",
        [
            "stopping-then-starting-later",
            "medium-rain",
            ["minutes", 25],
            ["minutes", 8],
        ],
    ],
    "Хмарно протягом всього дня.": ["sentence", ["for-day", "medium-clouds"]],
    "Незначний град починається вранці.": [
        "sentence",
        ["starting", "very-light-sleet", "morning"],
    ],
    "Вітер до сьогоднішньої ночі.": [
        "sentence",
        ["until", "medium-wind", "today-night"],
    ],
    "Сильні опади до середини дня.": [
        "sentence",
        ["until", "heavy-precipitation", "afternoon"],
    ],
    "Слабкий вітер вдень.": ["sentence", ["during", "light-wind", "afternoon"]],
    "Сніг сьогодні пізно ввечері і завтра вранці.": [
        "sentence",
        ["during", "medium-snow", ["and", "later-today-evening", "tomorrow-morning"]],
    ],
    "Сильний дощ до сьогоднішнього пізнього ранку, починаючись знову сьогодні ввечері.": [
        "sentence",
        ["until-starting-again", "heavy-rain", "later-today-morning", "today-evening"],
    ],
    "Сильна хмарність, починаючись з вечору, і до ночі.": [
        "sentence",
        ["starting-continuing-until", "heavy-clouds", "evening", "night"],
    ],
    "Невеликий град сьогодні пізно вдень і туман завтра вранці.": [
        "sentence",
        [
            "and",
            ["during", "light-sleet", "later-today-afternoon"],
            ["during", "fog", "tomorrow-morning"],
        ],
    ],
    "Сильний вітер, починаючись з ранку, і до середини дня, і град завтра вранці.": [
        "sentence",
        [
            "and",
            ["starting-continuing-until", "heavy-wind", "morning", "afternoon"],
            ["during", "medium-sleet", "tomorrow-morning"],
        ],
    ],
    "Сильна хмарність починається сьогодні пізно вночі і снігопад завтра вдень.": [
        "sentence",
        [
            "and",
            ["starting", "heavy-clouds", "later-today-night"],
            ["during", "heavy-snow", "tomorrow-afternoon"],
        ],
    ],
    "Сухо сьогодні вночі і невеликі опади, починаючись з завтрашнього вечору, і до завтрашньої ночі.": [
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
    "Сніг (5 см.) вночі.": [
        "sentence",
        ["during", ["parenthetical", "medium-snow", ["centimeters", 5]], "night"],
    ],
    "Невеликий сніг (2 см.) сьогодні пізно вранці.": [
        "sentence",
        [
            "during",
            ["parenthetical", "light-snow", ["centimeters", 2]],
            "later-today-morning",
        ],
    ],
    "Сніг (менше 1 см.) вдень.": [
        "sentence",
        [
            "during",
            ["parenthetical", "medium-snow", ["less-than", ["centimeters", 1]]],
            "afternoon",
        ],
    ],
    "Без опадів протягом всього тижня, з температурою, що піднімається до максимуму 35\u00b0C завтра.": [
        "sentence",
        [
            "with",
            ["for-week", "no-precipitation"],
            ["temperatures-peaking", ["celsius", 35], "tomorrow"],
        ],
    ],
    "Змішані опади протягом всіх вихідних, з температурою, що піднімається до 32\u00b0C в четвер.": [
        "sentence",
        [
            "with",
            ["over-weekend", "mixed-precipitation"],
            ["temperatures-rising", ["celsius", 32], "thursday"],
        ],
    ],
    "Незначний дощ в понеділок, з температурою, що знижується до 15\u00b0C в п'ятницю.": [
        "sentence",
        [
            "with",
            ["during", "very-light-rain", "monday"],
            ["temperatures-valleying", ["celsius", 15], "friday"],
        ],
    ],
    "Невеликий сніг у вівторок і в середу, з температурою, що знижується до мінімуму 0°C в неділю.": [
        "sentence",
        [
            "with",
            ["during", "light-snow", ["and", "tuesday", "wednesday"]],
            ["temperatures-falling", ["celsius", 0], "sunday"],
        ],
    ],
    "Опади сьогодні і до суботи, з температурою, що піднімається до максимуму 37°C в понеділок.": [
        "sentence",
        [
            "with",
            ["during", "medium-precipitation", ["through", "today", "saturday"]],
            ["temperatures-peaking", ["celsius", 37], "monday"],
        ],
    ],
    "Можливі Грози": ["title", "possible-thunderstorm"],
    "Сильний Дощ і Грози": ["title", ["and", "heavy-rain", "thunderstorm"]],
    "Невеликий сніг у вівторок і наступної середи, з температурою, що знижується до мінімуму 0°C в неділю.": [
        "sentence",
        [
            "with",
            ["during", "light-snow", ["and", "tuesday", "next-wednesday"]],
            ["temperatures-falling", ["celsius", 0], "sunday"],
        ],
    ],
}
