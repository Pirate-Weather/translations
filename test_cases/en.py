# This would be one of your translations, as a Python dictionary
cases = {
    "Clear": ["title", "clear"],
    "Chance of Light Precipitation": [
        "title",
        ["chance-of", "very-light-precipitation"],
    ],
    "Light Precipitation": ["title", "very-light-precipitation"],
    "Precipitation": ["title", "medium-precipitation"],
    "Heavy Precipitation": ["title", "heavy-precipitation"],
    "Chance of Drizzle": ["title", ["chance-of", "very-light-rain"]],
    "Drizzle": ["title", "very-light-rain"],
    "Chance of Light Rain": ["title", ["chance-of", "light-rain"]],
    "Light Rain": ["title", "light-rain"],
    "Rain": ["title", "medium-rain"],
    "Heavy Rain": ["title", "heavy-rain"],
    "Chance of Light Sleet": ["title", ["chance-of", "very-light-sleet"]],
    "Light Sleet": ["title", "very-light-sleet"],
    "Sleet": ["title", "medium-sleet"],
    "Heavy Sleet": ["title", "heavy-sleet"],
    "Chance of Flurries": ["title", ["chance-of", "very-light-snow"]],
    "Flurries": ["title", "very-light-snow"],
    "Chance of Light Snow": ["title", ["chance-of", "light-snow"]],
    "Light Snow": ["title", "light-snow"],
    "Snow": ["title", "medium-snow"],
    "Heavy Snow": ["title", "heavy-snow"],
    "Thunderstorms": ["title", "thunderstorm"],
    "Chance of Precipitation": ["title", ["chance-of", "medium-precipitation"]],
    "Chance of Heavy Precipitation": ["title", ["chance-of", "heavy-precipitation"]],
    "Chance of Rain": ["title", ["chance-of", "medium-rain"]],
    "Chance of Heavy Rain": ["title", ["chance-of", "heavy-rain"]],
    "Chance of Sleet": ["title", ["chance-of", "medium-sleet"]],
    "Chance of Heavy Sleet": ["title", ["chance-of", "heavy-sleet"]],
    "Chance of Snow": ["title", ["chance-of", "medium-snow"]],
    "Chance of Heavy Snow": ["title", ["chance-of", "heavy-snow"]],
    "Chance of Freezing Drizzle": ["title", ["chance-of", "very-light-freezing-rain"]],
    "Freezing Drizzle": ["title", "very-light-freezing-rain"],
    "Chance of Light Freezing Rain": ["title", ["chance-of", "light-freezing-rain"]],
    "Light Freezing Rain": ["title", "light-freezing-rain"],
    "Chance of Freezing Rain": ["title", ["chance-of", "medium-freezing-rain"]],
    "Freezing Rain": ["title", "medium-freezing-rain"],
    "Chance of Heavy Freezing Rain": ["title", ["chance-of", "heavy-freezing-rain"]],
    "Heavy Freezing Rain": ["title", "heavy-freezing-rain"],
    "Chance of Hail": ["title", ["chance-of", "hail"]],
    "Hail": ["title", "hail"],
    "Windy": ["title", "medium-wind"],
    "Dangerously Windy": ["title", "heavy-wind"],
    "Foggy": ["title", "fog"],
    "Mostly Clear": ["title", "very-light-clouds"],
    "Partly Cloudy": ["title", "light-clouds"],
    "Mostly Cloudy": ["title", "medium-clouds"],
    "Overcast": ["title", "heavy-clouds"],
    "Dry and Breezy": ["title", ["and", "low-humidity", "light-wind"]],
    "Drizzle and Dangerously Windy": [
        "title",
        ["and", "very-light-rain", "heavy-wind"],
    ],
    "Humid and Partly Cloudy": ["title", ["and", "high-humidity", "light-clouds"]],
    "Clear for the hour.": ["sentence", ["for-hour", "clear"]],
    "Flurries starting in 35 min.": [
        "sentence",
        ["starting-in", "very-light-snow", ["minutes", 35]],
    ],
    "Light rain ending in 15 min.": [
        "sentence",
        ["stopping-in", "light-rain", ["minutes", 15]],
    ],
    "Heavy sleet starting in 20 min, ending 30 min later.": [
        "sentence",
        [
            "starting-then-stopping-later",
            "heavy-sleet",
            ["minutes", 20],
            ["minutes", 30],
        ],
    ],
    "Rain ending in 25 min, returning 8 min later.": [
        "sentence",
        [
            "stopping-then-starting-later",
            "medium-rain",
            ["minutes", 25],
            ["minutes", 8],
        ],
    ],
    "Mostly cloudy throughout the day.": ["sentence", ["for-day", "medium-clouds"]],
    "Light sleet starting in the morning.": [
        "sentence",
        ["starting", "very-light-sleet", "morning"],
    ],
    "Windy until tonight.": ["sentence", ["until", "medium-wind", "today-night"]],
    "Heavy precipitation until afternoon.": [
        "sentence",
        ["until", "heavy-precipitation", "afternoon"],
    ],
    "Breezy in the afternoon.": ["sentence", ["during", "light-wind", "afternoon"]],
    "Snow this evening and tomorrow morning.": [
        "sentence",
        ["during", "medium-snow", ["and", "today-evening", "tomorrow-morning"]],
    ],
    "Heavy rain until this morning, returning this evening.": [
        "sentence",
        ["until-starting-again", "heavy-rain", "today-morning", "today-evening"],
    ],
    "Drizzle until afternoon, returning this evening.": [
        "sentence",
        ["until-starting-again", "very-light-rain", "afternoon", "today-evening"],
    ],
    "Drizzle until this afternoon, returning tomorrow morning.": [
        "sentence",
        [
            "until-starting-again",
            "very-light-rain",
            "today-afternoon",
            "tomorrow-morning",
        ],
    ],
    "Drizzle until night, returning tomorrow morning.": [
        "sentence",
        ["until-starting-again", "very-light-rain", "night", "tomorrow-morning"],
    ],
    "Overcast from evening until night.": [
        "sentence",
        ["starting-continuing-until", "heavy-clouds", "evening", "night"],
    ],
    "Light sleet this afternoon and foggy tomorrow morning.": [
        "sentence",
        [
            "and",
            ["during", "light-sleet", "today-afternoon"],
            ["during", "fog", "tomorrow-morning"],
        ],
    ],
    "Dangerously windy from this morning until this afternoon and sleet tomorrow morning.": [
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
    "Overcast starting tonight and heavy snow tomorrow afternoon.": [
        "sentence",
        [
            "and",
            ["starting", "heavy-clouds", "today-night"],
            ["during", "heavy-snow", "tomorrow-afternoon"],
        ],
    ],
    "Dry tonight and light precipitation from tomorrow evening until tomorrow night.": [
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
    "Snow accumulations of 5 in expected overnight.": [
        "sentence",
        ["during", ["parenthetical", "medium-snow", ["inches", 5]], "night"],
    ],
    "Light snow accumulations of 2 cm expected this morning.": [
        "sentence",
        [
            "during",
            ["parenthetical", "light-snow", ["centimeters", 2]],
            "today-morning",
        ],
    ],
    "Heavy snow accumulations of 8–12 in expected throughout the day.": [
        "sentence",
        ["for-day", ["parenthetical", "heavy-snow", ["inches", ["range", 8, 12]]]],
    ],
    "Snow accumulations of less than 1 cm expected in the afternoon.": [
        "sentence",
        [
            "during",
            ["parenthetical", "medium-snow", ["less-than", ["centimeters", 1]]],
            "afternoon",
        ],
    ],
    "No precipitation throughout the week, with highs reaching 85°F tomorrow.": [
        "sentence",
        [
            "with",
            ["for-week", "no-precipitation"],
            ["temperatures-peaking", ["fahrenheit", 85], "tomorrow"],
        ],
    ],
    "Mixed precipitation over the weekend, with highs climbing to 32°C on Thursday.": [
        "sentence",
        [
            "with",
            ["over-weekend", "mixed-precipitation"],
            ["temperatures-rising", ["celsius", 32], "thursday"],
        ],
    ],
    "Drizzle on Monday, with highs dipping to 15°F on Friday.": [
        "sentence",
        [
            "with",
            ["during", "very-light-rain", "monday"],
            ["temperatures-valleying", ["fahrenheit", 15], "friday"],
        ],
    ],
    "Light snow on Tuesday and next Wednesday, with highs falling to 0°C on Sunday.": [
        "sentence",
        [
            "with",
            ["during", "light-snow", ["and", "tuesday", "next-wednesday"]],
            ["temperatures-falling", ["celsius", 0], "sunday"],
        ],
    ],
    "Precipitation today through Saturday, with highs reaching 100°F on Monday.": [
        "sentence",
        [
            "with",
            ["during", "medium-precipitation", ["through", "today", "saturday"]],
            ["temperatures-peaking", ["fahrenheit", 100], "monday"],
        ],
    ],
    "Mixed precipitation accumulations of 1–3 in expected throughout the day.": [
        "sentence",
        [
            "for-day",
            ["parenthetical", "mixed-precipitation", ["inches", ["range", 1, 3]]],
        ],
    ],
    "Heavy Snow Accumulations of 1–3 in Expected": [
        "title",
        ["parenthetical", "heavy-snow", ["inches", ["range", 1, 3]]],
    ],
    "Heavy Snow Accumulations of 3–5 cm Expected": [
        "title",
        ["parenthetical", "heavy-snow", ["centimeters", ["range", 3, 5]]],
    ],
    "Rain Accumulations of 2–4 in Expected": [
        "title",
        ["parenthetical", "medium-rain", ["inches", ["range", 2, 4]]],
    ],
    "Chance of Thunderstorms": ["title", ["chance-of", "thunderstorm"]],
    "Heavy Rain and Thunderstorms": ["title", ["and", "heavy-rain", "thunderstorm"]],
    "Drizzle starting in less than 1 min.": [
        "sentence",
        ["starting-in", "very-light-rain", ["less-than", ["minutes", 1]]],
    ],
    "Next hour forecasts are temporarily unavailable due to missing model data.": [
        "sentence",
        ["next-hour-forecast-status", "temporarily-unavailable", "station-offline"],
    ],
    "Next hour forecasts are temporarily unavailable due to missing model data.": [
        "sentence",
        ["next-hour-forecast-status", "temporarily-unavailable", "station-offline"],
    ],
    "Next hour forecasts are unavailable due to missing model data.": [
        "sentence",
        ["next-hour-forecast-status", "unavailable", "station-offline"],
    ],
    "Drizzle and Thunderstorms": ["title", ["and", "very-light-rain", "thunderstorm"]],
    "Snow and Thunderstorms": ["title", ["and", "medium-snow", "thunderstorm"]],
    "Hail and Thunderstorms": ["title", ["and", "hail", "thunderstorm"]],
    "Light Freezing Rain Accumulations of 2–4 in Expected": [
        "title",
        ["parenthetical", "light-freezing-rain", ["inches", ["range", 2, 4]]],
    ],
    "Chance of thunderstorms and hail in the evening.": [
        "sentence",
        [
            "during",
            ["and", ["chance-of", "thunderstorm"], "hail"],
            "evening",
        ],
    ],
    "Freezing drizzle throughout the day.": [
        "sentence",
        [
            "for-day",
            "very-light-freezing-rain",
        ],
    ],
    "Freezing rain today and Sunday, with highs reaching 3°C on Wednesday.": [
        "sentence",
        [
            "with",
            ["during", "medium-freezing-rain", ["and", "today", "sunday"]],
            ["temperatures-peaking", ["celsius", 3], "wednesday"],
        ],
    ],
    "Chance of thunderstorms over the weekend, with highs climbing to 104°F next Monday.": [
        "sentence",
        [
            "with",
            ["over-weekend", ["chance-of", "thunderstorm"]],
            ["temperatures-rising", ["fahrenheit", 104], "next-monday"],
        ],
    ],
    "Thunderstorms for the hour.": ["sentence", ["for-hour", "thunderstorm"]],
    "Hail starting in 5 min, ending 45 min later.": [
        "sentence",
        [
            "starting-then-stopping-later",
            "hail",
            ["minutes", 5],
            ["minutes", 45],
        ],
    ],
    "Heavy freezing rain ending in 10 min, returning 32 min later.": [
        "sentence",
        [
            "stopping-then-starting-later",
            "heavy-freezing-rain",
            ["minutes", 10],
            ["minutes", 32],
        ],
    ],
    "Freezing drizzle starting in 49 min.": [
        "sentence",
        ["starting-in", "very-light-freezing-rain", ["minutes", 49]],
    ],
    "Smoke": ["title", "smoke"],
    "Smoke throughout the day.": ["sentence", ["for-day", "smoke"]],
    "Smoke in the morning.": ["sentence", ["during", "smoke", "morning"]],
    "Smoke until this evening.": ["sentence", ["until", "smoke", "today-evening"]],
    "Smoke and Partly Cloudy": ["title", ["and", "smoke", "light-clouds"]],
    "Hazy": ["title", "haze"],
    "Hazy throughout the day.": ["sentence", ["for-day", "haze"]],
    "Hazy in the afternoon.": ["sentence", ["during", "haze", "afternoon"]],
    "Hazy and Humid": ["title", ["and", "haze", "high-humidity"]],
    "Misty": ["title", "mist"],
    "Misty throughout the day.": ["sentence", ["for-day", "mist"]],
    "Misty overnight.": ["sentence", ["during", "mist", "night"]],
    "Misty and Overcast": ["title", ["and", "mist", "heavy-clouds"]],
    "Clear. Light rain.": ["sentence", ["multiple-sentences", "clear", "light-rain"]],
    "Clearing partly cloudy.": ["sentence", ["clearing", "light-clouds"]],
    "Increasing clouds tonight.": ["sentence", ["increasing", "today-night"]],
}
