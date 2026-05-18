# This would be one of your translations, as a Python dictionary
cases = {
    "Céu Limpo": ["title", "clear"],
    "Possibilidade De Aguaceiros Muito Fracos": [
        "title",
        "possible-very-light-precipitation",
    ],
    "Aguaceiros Muito Fracos": ["title", "very-light-precipitation"],
    "Possibilidade De Aguaceiros Fracos": ["title", "possible-light-precipitation"],
    "Aguaceiros Fracos": ["title", "light-precipitation"],
    "Aguaceiros": ["title", "medium-precipitation"],
    "Aguaceiros Fortes": ["title", "heavy-precipitation"],
    "Possibilidade De Chuviscos": ["title", "possible-very-light-rain"],
    "Chuviscos": ["title", "very-light-rain"],
    "Possibilidade De Chuva Fraca": ["title", "possible-light-rain"],
    "Chuva Fraca": ["title", "light-rain"],
    "Chuva": ["title", "medium-rain"],
    "Chuva Forte": ["title", "heavy-rain"],
    "Possibilidade De Chuva Congelada (chuva e Neve) Muito Fraca": [
        "title",
        "possible-very-light-sleet",
    ],
    "Chuva Congelada (chuva e Neve) Muito Fraca": ["title", "very-light-sleet"],
    "Possibilidade De Chuva Congelada (chuva e Neve) Fraca": [
        "title",
        "possible-light-sleet",
    ],
    "Chuva Congelada (chuva e Neve) Fraca": ["title", "light-sleet"],
    "Chuva Congelada (chuva e Neve)": ["title", "medium-sleet"],
    "Chuva Congelada (chuva e Neve) Forte": ["title", "heavy-sleet"],
    "Possibilidade De Neve Muito Fraca": ["title", "possible-very-light-snow"],
    "Neve Muito Fraca": ["title", "very-light-snow"],
    "Possibilidade De Neve Fraca": ["title", "possible-light-snow"],
    "Neve Fraca": ["title", "light-snow"],
    "Neve": ["title", "medium-snow"],
    "Neve Forte": ["title", "heavy-snow"],
    "Vento Fraco": ["title", "light-wind"],
    "Vento Moderado": ["title", "medium-wind"],
    "Vento Forte": ["title", "heavy-wind"],
    "Tempo Seco": ["title", "low-humidity"],
    "Tempo Úmido": ["title", "high-humidity"],
    "Nevoeiro": ["title", "fog"],
    "Céu Quase Limpo": ["title", "very-light-clouds"],
    "Céu Pouco Nublado": ["title", "light-clouds"],
    "Céu Nublado": ["title", "medium-clouds"],
    "Céu Encoberto": ["title", "heavy-clouds"],
    "Tempo Seco e Vento Fraco": ["title", ["and", "low-humidity", "light-wind"]],
    "Chuviscos e Vento Forte": ["title", ["and", "very-light-rain", "heavy-wind"]],
    "Tempo Úmido e Céu Pouco Nublado": [
        "title",
        ["and", "high-humidity", "light-clouds"],
    ],
    "Céu limpo na próxima hora.": ["sentence", ["for-hour", "clear"]],
    "Neve muito fraca começando em 35 min.": [
        "sentence",
        ["starting-in", "very-light-snow", ["minutes", 35]],
    ],
    "Chuva fraca terminando em 15 min.": [
        "sentence",
        ["stopping-in", "light-rain", ["minutes", 15]],
    ],
    "Chuva congelada (chuva e neve) forte começando de 20 min, terminando ao fim da 30 min.": [
        "sentence",
        [
            "starting-then-stopping-later",
            "heavy-sleet",
            ["minutes", 20],
            ["minutes", 30],
        ],
    ],
    "Chuva terminando em 25 min e recomeçando em 8 min.": [
        "sentence",
        [
            "stopping-then-starting-later",
            "medium-rain",
            ["minutes", 25],
            ["minutes", 8],
        ],
    ],
    "Céu nublado até ao fim do dia.": ["sentence", ["for-day", "medium-clouds"]],
    "Chuva congelada (chuva e neve) muito fraca começando de manhã.": [
        "sentence",
        ["starting", "very-light-sleet", "morning"],
    ],
    "Vento moderado até à amanhã de madrugada.": [
        "sentence",
        ["until", "medium-wind", "today-night"],
    ],
    "Aguaceiros fortes até à tarde.": [
        "sentence",
        ["until", "heavy-precipitation", "afternoon"],
    ],
    "Vento fraco durante tarde.": ["sentence", ["during", "light-wind", "afternoon"]],
    "Neve durante hoje ao final da noite e amanhã de manhã.": [
        "sentence",
        ["during", "medium-snow", ["and", "later-today-evening", "tomorrow-morning"]],
    ],
    "Chuva forte até à hoje ao final da manhã, recomeçando de hoje à noite.": [
        "sentence",
        ["until-starting-again", "heavy-rain", "later-today-morning", "today-evening"],
    ],
    "Céu encoberto começando de noite, continuando até de madrugada.": [
        "sentence",
        ["starting-continuing-until", "heavy-clouds", "evening", "night"],
    ],
    "Chuva congelada (chuva e neve) fraca durante hoje ao final da tarde e nevoeiro durante amanhã de manhã.": [
        "sentence",
        [
            "and",
            ["during", "light-sleet", "later-today-afternoon"],
            ["during", "fog", "tomorrow-morning"],
        ],
    ],
    "Vento forte começando de manhã, continuando até de tarde, e chuva congelada (chuva e neve) durante amanhã de manhã.": [
        "sentence",
        [
            "and",
            ["starting-continuing-until", "heavy-wind", "morning", "afternoon"],
            ["during", "medium-sleet", "tomorrow-morning"],
        ],
    ],
    "Céu encoberto começando de ao final da madrugada e neve forte durante amanhã à tarde.": [
        "sentence",
        [
            "and",
            ["starting", "heavy-clouds", "later-today-night"],
            ["during", "heavy-snow", "tomorrow-afternoon"],
        ],
    ],
    "Tempo seco durante amanhã de madrugada e aguaceiros fracos começando de amanhã à noite, continuando até de amanhã ao final da noite.": [
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
    "Neve (5 cm) durante madrugada.": [
        "sentence",
        ["during", ["parenthetical", "medium-snow", ["centimeters", 5]], "night"],
    ],
    "Neve fraca (2 cm) durante hoje ao final da manhã.": [
        "sentence",
        [
            "during",
            ["parenthetical", "light-snow", ["centimeters", 2]],
            "later-today-morning",
        ],
    ],
    "Neve (menos de 1 cm) durante tarde.": [
        "sentence",
        [
            "during",
            ["parenthetical", "medium-snow", ["less-than", ["centimeters", 1]]],
            "afternoon",
        ],
    ],
    "Sem precipitação durante a semana, com temperatura máxima de 35 \u00b0C, amanhã.": [
        "sentence",
        [
            "with",
            ["for-week", "no-precipitation"],
            ["temperatures-peaking", ["celsius", 35], "tomorrow"],
        ],
    ],
    "Aguaceiros mistos durante o fim de semana, com subida de temperatura até aos 32 \u00b0C, até quinta-feira.": [
        "sentence",
        [
            "with",
            ["over-weekend", "mixed-precipitation"],
            ["temperatures-rising", ["celsius", 32], "thursday"],
        ],
    ],
    "Chuviscos durante segunda-feira, com descida de temperatura até aos 15 \u00b0C, até sexta-feira.": [
        "sentence",
        [
            "with",
            ["during", "very-light-rain", "monday"],
            ["temperatures-valleying", ["celsius", 15], "friday"],
        ],
    ],
    "Neve fraca durante terça-feira e quarta-feira, com temperatura mínima de 0 \u00b0C, domingo.": [
        "sentence",
        [
            "with",
            ["during", "light-snow", ["and", "tuesday", "wednesday"]],
            ["temperatures-falling", ["celsius", 0], "sunday"],
        ],
    ],
    "Aguaceiros durante hoje durante sábado, com temperatura máxima de 37 \u00b0C, segunda-feira.": [
        "sentence",
        [
            "with",
            ["during", "medium-precipitation", ["through", "today", "saturday"]],
            ["temperatures-peaking", ["celsius", 37], "monday"],
        ],
    ],
    "Possibilidade de trovoada até à próxima quarta-feira.": [
        "sentence",
        ["until", "possible-thunderstorm", "next-wednesday"],
    ],
    "Fumo": ["title", "smoke"],
    "Fumo até ao fim do dia.": ["sentence", ["for-day", "smoke"]],
    "Fumo durante manhã.": ["sentence", ["during", "smoke", "morning"]],
    "Fumo até à hoje à noite.": ["sentence", ["until", "smoke", "today-evening"]],
    "Fumo e Céu Pouco Nublado": ["title", ["and", "smoke", "light-clouds"]],
    "Névoa Seca": ["title", "haze"],
    "Névoa seca até ao fim do dia.": ["sentence", ["for-day", "haze"]],
    "Névoa seca durante tarde.": ["sentence", ["during", "haze", "afternoon"]],
    "Névoa Seca e Tempo Úmido": ["title", ["and", "haze", "high-humidity"]],
    "Neblina até ao fim do dia.": ["sentence", ["for-day", "mist"]],
    "Neblina durante madrugada.": ["sentence", ["during", "mist", "night"]],
    "Neblina e Céu Encoberto": ["title", ["and", "mist", "heavy-clouds"]],
    "Trovoada na próxima hora.": ["sentence", ["for-hour", "thunderstorm"]],
    "Granizo começando de 5 min, terminando ao fim da 45 min.": [
        "sentence",
        [
            "starting-then-stopping-later",
            "hail",
            ["minutes", 5],
            ["minutes", 45],
        ],
    ],
    "Chuva congelante forte terminando em 10 min e recomeçando em 32 min.": [
        "sentence",
        [
            "stopping-then-starting-later",
            "heavy-freezing-rain",
            ["minutes", 10],
            ["minutes", 32],
        ],
    ],
    "Chuvisco congelante começando em 49 min.": [
        "sentence",
        ["starting-in", "very-light-freezing-rain", ["minutes", 49]],
    ],
}
