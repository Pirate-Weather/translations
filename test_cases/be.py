# This would be one of your translations, as a Python dictionary
cases = {
    "Ясна": ["title", "clear"],
    "Магчымы Нязначныя Ападкі": ["title", "possible-very-light-precipitation"],
    "Нязначныя Ападкі": ["title", "very-light-precipitation"],
    "Магчымы Невялікія Ападкі": ["title", "possible-light-precipitation"],
    "Невялікія Ападкі": ["title", "light-precipitation"],
    "Ападкі": ["title", "medium-precipitation"],
    "Моцныя Ападкі": ["title", "heavy-precipitation"],
    "Магчымы Нязначны Дождж": ["title", "possible-very-light-rain"],
    "Нязначны Дождж": ["title", "very-light-rain"],
    "Магчымы Невялікі Дождж": ["title", "possible-light-rain"],
    "Невялікі Дождж": ["title", "light-rain"],
    "Дождж": ["title", "medium-rain"],
    "Моцны Дождж": ["title", "heavy-rain"],
    "Магчымы Нязначны Град": ["title", "possible-very-light-sleet"],
    "Нязначны Град": ["title", "very-light-sleet"],
    "Магчымы Невялікі Град": ["title", "possible-light-sleet"],
    "Невялікі Град": ["title", "light-sleet"],
    "Град": ["title", "medium-sleet"],
    "Моцны Град": ["title", "heavy-sleet"],
    "Магчымы Нязначны Снег": ["title", "possible-very-light-snow"],
    "Нязначны Снег": ["title", "very-light-snow"],
    "Магчымы Невялікі Снег": ["title", "possible-light-snow"],
    "Невялікі Снег": ["title", "light-snow"],
    "Снег": ["title", "medium-snow"],
    "Снегапад": ["title", "heavy-snow"],
    "Слабы Вецер": ["title", "light-wind"],
    "Вецер": ["title", "medium-wind"],
    "Моцны Вецер": ["title", "heavy-wind"],
    "Суха": ["title", "low-humidity"],
    "Вільготна": ["title", "high-humidity"],
    "Туман": ["title", "fog"],
    "Моцная Ясна": ["title", "very-light-clouds"],
    "Невялікая Воблачнасць": ["title", "light-clouds"],
    "Воблачна": ["title", "medium-clouds"],
    "Моцная Воблачнасць": ["title", "heavy-clouds"],
    "Суха і Слабы Вецер": ["title", ["and", "low-humidity", "light-wind"]],
    "Нязначны Дождж і Моцны Вецер": ["title", ["and", "very-light-rain", "heavy-wind"]],
    "Вільготна і Невялікая Воблачнасць": [
        "title",
        ["and", "high-humidity", "light-clouds"],
    ],
    "Ясна на працягу наступнай гадзіны.": ["sentence", ["for-hour", "clear"]],
    "Нязначны снег пачынаецца на працягу 35 хв.": [
        "sentence",
        ["starting-in", "very-light-snow", ["minutes", 35]],
    ],
    "Невялікі дождж заканчваецца на працягу 15 хв.": [
        "sentence",
        ["stopping-in", "light-rain", ["minutes", 15]],
    ],
    "Моцны град пачынаецца на працягу 20 хв, і заканчваецца праз 30 хв.": [
        "sentence",
        [
            "starting-then-stopping-later",
            "heavy-sleet",
            ["minutes", 20],
            ["minutes", 30],
        ],
    ],
    "Дождж заканчваецца на працягу 25 хв, і пачынаецца зноў праз 8 хв.": [
        "sentence",
        [
            "stopping-then-starting-later",
            "medium-rain",
            ["minutes", 25],
            ["minutes", 8],
        ],
    ],
    "Воблачна на працягу ўсяго дня.": ["sentence", ["for-day", "medium-clouds"]],
    "Нязначны град пачынаецца раніцай.": [
        "sentence",
        ["starting", "very-light-sleet", "morning"],
    ],
    "Вецер да сённяшняй ночы.": ["sentence", ["until", "medium-wind", "today-night"]],
    "Моцныя ападкі да сярэдзіны дня.": [
        "sentence",
        ["until", "heavy-precipitation", "afternoon"],
    ],
    "Слабы вецер днём.": ["sentence", ["during", "light-wind", "afternoon"]],
    "Снег сёння познім вечарам і заўтра раніцай.": [
        "sentence",
        ["during", "medium-snow", ["and", "later-today-evening", "tomorrow-morning"]],
    ],
    "Моцны дождж да сённяшняй позняй раніцы, пачынаючыся зноў сёння ўвечары.": [
        "sentence",
        ["until-starting-again", "heavy-rain", "later-today-morning", "today-evening"],
    ],
    "Моцная воблачнасць, пачынаючыся з вечара, і да ночы.": [
        "sentence",
        ["starting-continuing-until", "heavy-clouds", "evening", "night"],
    ],
    "Невялікі град сёння познім днём і туман заўтра раніцай.": [
        "sentence",
        [
            "and",
            ["during", "light-sleet", "later-today-afternoon"],
            ["during", "fog", "tomorrow-morning"],
        ],
    ],
    "Моцны вецер, пачынаючыся з раніцы, і да сярэдзіны дня, і град заўтра раніцай.": [
        "sentence",
        [
            "and",
            ["starting-continuing-until", "heavy-wind", "morning", "afternoon"],
            ["during", "medium-sleet", "tomorrow-morning"],
        ],
    ],
    "Моцная воблачнасць пачынаецца сёння позняй ноччу і снегапад заўтра днём.": [
        "sentence",
        [
            "and",
            ["starting", "heavy-clouds", "later-today-night"],
            ["during", "heavy-snow", "tomorrow-afternoon"],
        ],
    ],
    "Суха сёння ноччу і невялікія ападкі, пачынаючыся з заўтрашняга вечара, і да заўтрашняй ночы.": [
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
    "Снег (5 см.) ноччу.": [
        "sentence",
        ["during", ["parenthetical", "medium-snow", ["centimeters", 5]], "night"],
    ],
    "Невялікі снег (2 см.) сёння позняй раніцай.": [
        "sentence",
        [
            "during",
            ["parenthetical", "light-snow", ["centimeters", 2]],
            "later-today-morning",
        ],
    ],
    "Снег (менш за 1 см.) днём.": [
        "sentence",
        [
            "during",
            ["parenthetical", "medium-snow", ["less-than", ["centimeters", 1]]],
            "afternoon",
        ],
    ],
    "Без ападкаў на працягу ўсяго тыдня, з тэмпературай, што ўздымаецца да максімуму 35\u00b0C заўтра.": [
        "sentence",
        [
            "with",
            ["for-week", "no-precipitation"],
            ["temperatures-peaking", ["celsius", 35], "tomorrow"],
        ],
    ],
    "Змешаныя ападкі на працягу ўсіх выходных, з тэмпературай, што ўздымаецца да 32\u00b0C у чацвер.": [
        "sentence",
        [
            "with",
            ["over-weekend", "mixed-precipitation"],
            ["temperatures-rising", ["celsius", 32], "thursday"],
        ],
    ],
    "Нязначны дождж у панядзелак, з тэмпературай, якая апускаецца да 15\u00b0C у пятніцу.": [
        "sentence",
        [
            "with",
            ["during", "very-light-rain", "monday"],
            ["temperatures-valleying", ["celsius", 15], "friday"],
        ],
    ],
    "Невялікі снег у аўторак і сераду, з тэмпературай, якая апускаецца да мінімуму 0°C у нядзелю.": [
        "sentence",
        [
            "with",
            ["during", "light-snow", ["and", "tuesday", "wednesday"]],
            ["temperatures-falling", ["celsius", 0], "sunday"],
        ],
    ],
    "Ападкі сёння і да суботы, з тэмпературай, што ўздымаецца да максімуму 37°C у панядзелак.": [
        "sentence",
        [
            "with",
            ["during", "medium-precipitation", ["through", "today", "saturday"]],
            ["temperatures-peaking", ["celsius", 37], "monday"],
        ],
    ],
    "Магчымы Навальніцы": ["title", "possible-thunderstorm"],
    "Моцны Дождж і Навальніцы": ["title", ["and", "heavy-rain", "thunderstorm"]],
    "Невялікі снег у аўторак і наступную сераду, з тэмпературай, якая апускаецца да мінімуму 0°C у нядзелю.": [
        "sentence",
        [
            "with",
            ["during", "light-snow", ["and", "tuesday", "next-wednesday"]],
            ["temperatures-falling", ["celsius", 0], "sunday"],
        ],
    ],
}
