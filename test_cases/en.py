# This would be one of your translations, as a Python dictionary
cases = {
    "Clear": ["title", "clear"],
    "Possible Light Precipitation": ["title", "possible-very-light-precipitation"],
    "Light Precipitation": ["title", "very-light-precipitation"],
    "Precipitation": ["title", "medium-precipitation"],
    "Heavy Precipitation": ["title", "heavy-precipitation"],
    "Possible Drizzle": ["title", "possible-very-light-rain"],
    "Drizzle": ["title", "very-light-rain"],
    "Possible Light Rain": ["title", "possible-light-rain"],
    "Light Rain": ["title", "light-rain"],
    "Rain": ["title", "medium-rain"],
    "Heavy Rain": ["title", "heavy-rain"],
    "Possible Light Sleet": ["title", "possible-very-light-sleet"],
    "Light Sleet": ["title", "very-light-sleet"],
    "Sleet": ["title", "medium-sleet"],
    "Heavy Sleet": ["title", "heavy-sleet"],
    "Possible Flurries": ["title", "possible-very-light-snow"],
    "Flurries": ["title", "very-light-snow"],
    "Possible Light Snow": ["title", "possible-light-snow"],
    "Light Snow": ["title", "light-snow"],
    "Snow": ["title", "medium-snow"],
    "Heavy Snow": ["title", "heavy-snow"],
    "Thunderstorms": ["title", "thunderstorm"],
    "Possible Precipitation": ["title", "possible-medium-precipitation"],
    "Possible Heavy Precipitation": ["title", "possible-heavy-precipitation"],
    "Possible Rain": ["title", "possible-medium-rain"],
    "Possible Heavy Rain": ["title", "possible-heavy-rain"],
    "Possible Sleet": ["title", "possible-medium-sleet"],
    "Possible Heavy Sleet": ["title", "possible-heavy-sleet"],
    "Possible Snow": ["title", "possible-medium-snow"],
    "Possible Heavy Snow": ["title", "possible-heavy-snow"],
    "Possible Freezing Drizzle": ["title", "possible-very-light-freezing-rain"],
    "Freezing Drizzle": ["title", "very-light-freezing-rain"],
    "Possible Light Freezing Rain": ["title", "possible-light-freezing-rain"],
    "Light Freezing Rain": ["title", "light-freezing-rain"],
    "Possible Freezing Rain": ["title", "possible-medium-freezing-rain"],
    "Freezing Rain": ["title", "medium-freezing-rain"],
    "Possible Heavy Freezing Rain": ["title", "possible-heavy-freezing-rain"],
    "Heavy Freezing Rain": ["title", "heavy-freezing-rain"],
    "Possible Hail": ["title", "possible-hail"],
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
    "Light rain stopping in 15 min.": [
        "sentence",
        ["stopping-in", "light-rain", ["minutes", 15]],
    ],
    "Heavy sleet starting in 20 min., stopping 30 min. later.": [
        "sentence",
        [
            "starting-then-stopping-later",
            "heavy-sleet",
            ["minutes", 20],
            ["minutes", 30],
        ],
    ],
    "Rain stopping in 25 min., starting again 8 min. later.": [
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
    "Snow later this evening and tomorrow morning.": [
        "sentence",
        ["during", "medium-snow", ["and", "later-today-evening", "tomorrow-morning"]],
    ],
    "Heavy rain until later this morning, starting again this evening.": [
        "sentence",
        ["until-starting-again", "heavy-rain", "later-today-morning", "today-evening"],
    ],
    "Overcast starting in the evening, continuing until night.": [
        "sentence",
        ["starting-continuing-until", "heavy-clouds", "evening", "night"],
    ],
    "Light sleet later this afternoon and foggy tomorrow morning.": [
        "sentence",
        [
            "and",
            ["during", "light-sleet", "later-today-afternoon"],
            ["during", "fog", "tomorrow-morning"],
        ],
    ],
    "Dangerously windy starting this morning, continuing until this afternoon, and sleet tomorrow morning.": [
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
    "Overcast starting later tonight and heavy snow tomorrow afternoon.": [
        "sentence",
        [
            "and",
            ["starting", "heavy-clouds", "later-today-night"],
            ["during", "heavy-snow", "tomorrow-afternoon"],
        ],
    ],
    "Dry tonight and light precipitation starting tomorrow evening, continuing until tomorrow night.": [
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
    "Snow (5 in.) overnight.": [
        "sentence",
        ["during", ["parenthetical", "medium-snow", ["inches", 5]], "night"],
    ],
    "Light snow (2 cm.) later this morning.": [
        "sentence",
        [
            "during",
            ["parenthetical", "light-snow", ["centimeters", 2]],
            "later-today-morning",
        ],
    ],
    "Heavy snow (8–12 in.) throughout the day.": [
        "sentence",
        ["for-day", ["parenthetical", "heavy-snow", ["inches", ["range", 8, 12]]]],
    ],
    "Snow (< 1 cm.) in the afternoon.": [
        "sentence",
        [
            "during",
            ["parenthetical", "medium-snow", ["less-than", ["centimeters", 1]]],
            "afternoon",
        ],
    ],
    "No precipitation throughout the week, with high temperatures peaking at 85°F tomorrow.": [
        "sentence",
        [
            "with",
            ["for-week", "no-precipitation"],
            ["temperatures-peaking", ["fahrenheit", 85], "tomorrow"],
        ],
    ],
    "Mixed precipitation over the weekend, with high temperatures rising to 32°C on Thursday.": [
        "sentence",
        [
            "with",
            ["over-weekend", "mixed-precipitation"],
            ["temperatures-rising", ["celsius", 32], "thursday"],
        ],
    ],
    "Drizzle on Monday, with high temperatures bottoming out at 15°F on Friday.": [
        "sentence",
        [
            "with",
            ["during", "very-light-rain", "monday"],
            ["temperatures-valleying", ["fahrenheit", 15], "friday"],
        ],
    ],
    "Light snow on Tuesday and next Wednesday, with high temperatures falling to 0°C on Sunday.": [
        "sentence",
        [
            "with",
            ["during", "light-snow", ["and", "tuesday", "next-wednesday"]],
            ["temperatures-falling", ["celsius", 0], "sunday"],
        ],
    ],
    "Precipitation today through Saturday, with high temperatures peaking at 100°F on Monday.": [
        "sentence",
        [
            "with",
            ["during", "medium-precipitation", ["through", "today", "saturday"]],
            ["temperatures-peaking", ["fahrenheit", 100], "monday"],
        ],
    ],
    "Mixed precipitation (1–3 in. of snow) throughout the day.": [
        "sentence",
        [
            "for-day",
            ["parenthetical", "mixed-precipitation", ["inches", ["range", 1, 3]]],
        ],
    ],
    "Heavy Snow (1–3 in.)": [
        "title",
        ["parenthetical", "heavy-snow", ["inches", ["range", 1, 3]]],
    ],
    "Heavy Snow (3–5 cm.)": [
        "title",
        ["parenthetical", "heavy-snow", ["centimeters", ["range", 3, 5]]],
    ],
    "Rain (with a Chance of 2–4 in. of Snow)": [
        "title",
        ["parenthetical", "medium-rain", ["inches", ["range", 2, 4]]],
    ],
    "Possible Thunderstorms": ["title", "possible-thunderstorm"],
    "Heavy Rain and Thunderstorms": ["title", ["and", "heavy-rain", "thunderstorm"]],
    "Drizzle starting in < 1 min.": [
        "sentence",
        ["starting-in", "very-light-rain", ["less-than", ["minutes", 1]]],
    ],
    "Next hour forecasts are temporarily unavailable due to all nearby radar stations being offline.": [
        "sentence",
        ["next-hour-forecast-status", "temporarily-unavailable", "station-offline"],
    ],
    "Next hour forecasts are partially unavailable due to gaps in coverage from nearby radar stations.": [
        "sentence",
        ["next-hour-forecast-status", "partially-unavailable", "station-incomplete"],
    ],
    "Next hour forecasts are unavailable due to all nearby radar stations being offline.": [
        "sentence",
        ["next-hour-forecast-status", "unavailable", "station-offline"],
    ],
    "Drizzle and Thunderstorms": ["title", ["and", "very-light-rain", "thunderstorm"]],
    "Snow and Thunderstorms": ["title", ["and", "medium-snow", "thunderstorm"]],
    "Hail and Thunderstorms": ["title", ["and", "hail", "thunderstorm"]],
    "Light Freezing Rain (with a Chance of 2–4 in. of Snow)": [
        "title",
        ["parenthetical", "light-freezing-rain", ["inches", ["range", 2, 4]]],
    ],
    "Possible thunderstorms and hail in the evening.": [
        "sentence",
        [
            "during",
            ["and", "possible-thunderstorm", "hail"],
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
    "Freezing rain today and Sunday, with high temperatures peaking at 3°C on Wednesday.": [
        "sentence",
        [
            "with",
            ["during", "medium-freezing-rain", ["and", "today", "sunday"]],
            ["temperatures-peaking", ["celsius", 3], "wednesday"],
        ],
    ],
    "Possible thunderstorms over the weekend, with high temperatures rising to 104°F next Monday.": [
        "sentence",
        [
            "with",
            ["over-weekend", "possible-thunderstorm"],
            ["temperatures-rising", ["fahrenheit", 104], "next-monday"],
        ],
    ],
    "Thunderstorms for the hour.": ["sentence", ["for-hour", "thunderstorm"]],
    "Hail starting in 5 min., stopping 45 min. later.": [
        "sentence",
        [
            "starting-then-stopping-later",
            "hail",
            ["minutes", 5],
            ["minutes", 45],
        ],
    ],
    "Heavy freezing rain stopping in 10 min., starting again 32 min. later.": [
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
}
