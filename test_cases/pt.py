# This would be one of your translations, as a Python dictionary
cases = {
    "Limpo": ["title", "clear"],
    "Possíveis Aguaceiros Muito Fracos": ["title", "possible-very-light-precipitation"],
    "Aguaceiros Muito Fracos": ["title", "very-light-precipitation"],
    "Possíveis Aguaceiros Fracos": ["title", "possible-light-precipitation"],
    "Aguaceiros Fracos": ["title", "light-precipitation"],
    "Aguaceiros": ["title", "medium-precipitation"],
    "Aguaceiros Fortes": ["title", "heavy-precipitation"],
    "Possíveis Chuviscos": ["title", "possible-very-light-rain"],
    "Chuviscos": ["title", "very-light-rain"],
    "Possível Chuva Fraca": ["title", "possible-light-rain"],
    "Chuva Fraca": ["title", "light-rain"],
    "Chuva": ["title", "medium-rain"],
    "Chuva Forte": ["title", "heavy-rain"],
    "Possível Granizo Muito Fraco": ["title", "possible-very-light-sleet"],
    "Granizo Muito Fraco": ["title", "very-light-sleet"],
    "Possível Granizo Fraco": ["title", "possible-light-sleet"],
    "Granizo Fraco": ["title", "light-sleet"],
    "Granizo": ["title", "medium-sleet"],
    "Granizo Forte": ["title", "heavy-sleet"],
    "Possível Neve Muito Fraca": ["title", "possible-very-light-snow"],
    "Neve Muito Fraca": ["title", "very-light-snow"],
    "Possível Neve Fraca": ["title", "possible-light-snow"],
    "Neve Fraca": ["title", "light-snow"],
    "Neve": ["title", "medium-snow"],
    "Neve Forte": ["title", "heavy-snow"],
    "Vento Fraco": ["title", "light-wind"],
    "Vento": ["title", "medium-wind"],
    "Vento Forte": ["title", "heavy-wind"],
    "Seco": ["title", "low-humidity"],
    "Úmido": ["title", "high-humidity"],
    "Nevoeiro": ["title", "fog"],
    "Principalmente Claro": ["title", "very-light-clouds"],
    "Ligeiramente Nublado": ["title", "light-clouds"],
    "Nublado": ["title", "medium-clouds"],
    "Muito Nublado": ["title", "heavy-clouds"],
    "Seco e Vento Fraco": ["title", ["and", "low-humidity", "light-wind"]],
    "Chuviscos e Vento Forte": ["title", ["and", "very-light-rain", "heavy-wind"]],
    "Úmido e Ligeiramente Nublado": ["title", ["and", "high-humidity", "light-clouds"]],
    "Limpo na próxima hora.": ["sentence", ["for-hour", "clear"]],
    "Neve muito fraca dentro de 35 min.": [
        "sentence",
        ["starting-in", "very-light-snow", ["minutes", 35]],
    ],
    "Chuva fraca termina daqui a 15 min.": [
        "sentence",
        ["stopping-in", "light-rain", ["minutes", 15]],
    ],
    "Granizo forte dentro de 20 min, termina 30 min mais tarde.": [
        "sentence",
        [
            "starting-then-stopping-later",
            "heavy-sleet",
            ["minutes", 20],
            ["minutes", 30],
        ],
    ],
    "Chuva termina dentro de 25 min, recomeça 8 min mais tarde.": [
        "sentence",
        [
            "stopping-then-starting-later",
            "medium-rain",
            ["minutes", 25],
            ["minutes", 8],
        ],
    ],
    "Nublado durante todo o dia.": ["sentence", ["for-day", "medium-clouds"]],
    "Granizo muito fraco começa durante a manhã.": [
        "sentence",
        ["starting", "very-light-sleet", "morning"],
    ],
    "Vento até hoje de madrugada.": [
        "sentence",
        ["until", "medium-wind", "today-night"],
    ],
    "Aguaceiros fortes até tarde.": [
        "sentence",
        ["until", "heavy-precipitation", "afternoon"],
    ],
    "Vento fraco durante tarde.": ["sentence", ["during", "light-wind", "afternoon"]],
    "Neve durante noite de hoje e amanhã de manhã.": [
        "sentence",
        ["during", "medium-snow", ["and", "later-today-evening", "tomorrow-morning"]],
    ],
    "Chuva forte até manhã de hoje, recomeça hoje à noite.": [
        "sentence",
        ["until-starting-again", "heavy-rain", "later-today-morning", "today-evening"],
    ],
    "Muito nublado começa esta noite, continua até à madrugada.": [
        "sentence",
        ["starting-continuing-until", "heavy-clouds", "evening", "night"],
    ],
    "Granizo fraco durante tarde de hoje e nevoeiro durante amanhã de manhã.": [
        "sentence",
        [
            "and",
            ["during", "light-sleet", "later-today-afternoon"],
            ["during", "fog", "tomorrow-morning"],
        ],
    ],
    "Vento forte começa esta manhã, continua até à tarde, e granizo durante amanhã de manhã.": [
        "sentence",
        [
            "and",
            ["starting-continuing-until", "heavy-wind", "morning", "afternoon"],
            ["during", "medium-sleet", "tomorrow-morning"],
        ],
    ],
    "Muito nublado começa durante a de madrugada e neve forte durante amanhã à tarde.": [
        "sentence",
        [
            "and",
            ["starting", "heavy-clouds", "later-today-night"],
            ["during", "heavy-snow", "tomorrow-afternoon"],
        ],
    ],
    "Seco durante hoje de madrugada e aguaceiros fracos começa esta amanhã à noite, continua até à amanhã de madrugada.": [
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
    "Neve (5 cm.) durante madrugada.": [
        "sentence",
        ["during", ["parenthetical", "medium-snow", ["centimeters", 5]], "night"],
    ],
    "Neve fraca (2 cm.) durante manhã de hoje.": [
        "sentence",
        [
            "during",
            ["parenthetical", "light-snow", ["centimeters", 2]],
            "later-today-morning",
        ],
    ],
    "Neve (menos de 1 cm.) durante tarde.": [
        "sentence",
        [
            "during",
            ["parenthetical", "medium-snow", ["less-than", ["centimeters", 1]]],
            "afternoon",
        ],
    ],
    "Sem aguaceiros durante toda a semana, com as temperaturas a chegar a um máximo de 35\u00b0C amanhã.": [
        "sentence",
        [
            "with",
            ["for-week", "no-precipitation"],
            ["temperatures-peaking", ["celsius", 35], "tomorrow"],
        ],
    ],
    "Aguaceiros variados durante todo o fim de semana, com as temperaturas a subir aos 32\u00b0C quinta-feira.": [
        "sentence",
        [
            "with",
            ["over-weekend", "mixed-precipitation"],
            ["temperatures-rising", ["celsius", 32], "thursday"],
        ],
    ],
    "Chuviscos durante segunda-feira, com as temperaturas a descer até 15\u00b0C sexta-feira.": [
        "sentence",
        [
            "with",
            ["during", "very-light-rain", "monday"],
            ["temperatures-valleying", ["celsius", 15], "friday"],
        ],
    ],
    "Neve fraca durante terça-feira e quarta-feira, com as temperaturas a descer até um minimo de 0\u00b0C domingo.": [
        "sentence",
        [
            "with",
            ["during", "light-snow", ["and", "tuesday", "wednesday"]],
            ["temperatures-falling", ["celsius", 0], "sunday"],
        ],
    ],
    "Aguaceiros durante hoje durante sábado, com as temperaturas a chegar a um máximo de 37\u00b0C segunda-feira.": [
        "sentence",
        [
            "with",
            ["during", "medium-precipitation", ["through", "today", "saturday"]],
            ["temperatures-peaking", ["celsius", 37], "monday"],
        ],
    ],
    "Tempestades possíveis até próxima quarta-feira.": [
        "sentence",
        ["until", "possible-thunderstorm", "next-wednesday"],
    ],
}
