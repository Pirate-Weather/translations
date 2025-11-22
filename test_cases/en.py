# This file contains the English test cases as a mapping from the
# expected output string to the machine-readable expression. These
# expected strings were regenerated to match the current behavior
# of `pirateweather_translations/lang/en.py`.
cases = {
    "Breezy in the afternoon.": ["sentence", ["during", "light-wind", "afternoon"]],
    "Clear": ["title", "clear"],
    "Clear for the hour.": ["sentence", ["for-hour", "clear"]],
    "Dangerously Windy": ["title", "heavy-wind"],
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
    "Drizzle": ["title", "very-light-rain"],
    "Drizzle and Dangerously Windy": [
        "title",
        ["and", "very-light-rain", "heavy-wind"],
    ],
    "Drizzle and Thunderstorms": ["title", ["and", "very-light-rain", "thunderstorm"]],
    "Drizzle on Monday, with highs dipping to 15°F on Friday.": [
        "sentence",
        [
            "with",
            ["during", "very-light-rain", "monday"],
            ["temperatures-valleying", ["fahrenheit", 15], "friday"],
        ],
    ],
    "Drizzle starting in < 1 min.": [
        "sentence",
        ["starting-in", "very-light-rain", ["less-than", ["minutes", 1]]],
    ],
    "Dry and Breezy": ["title", ["and", "low-humidity", "light-wind"]],
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
    "Flurries": ["title", "very-light-snow"],
    "Flurries starting in 35 min.": [
        "sentence",
        ["starting-in", "very-light-snow", ["minutes", 35]],
    ],
    "Foggy": ["title", "fog"],
    "Freezing Drizzle": ["title", "very-light-freezing-rain"],
    "Freezing Rain": ["title", "medium-freezing-rain"],
    "Freezing drizzle starting in 49 min.": [
        "sentence",
        ["starting-in", "very-light-freezing-rain", ["minutes", 49]],
    ],
    "Freezing drizzle throughout the day.": [
        "sentence",
        ["for-day", "very-light-freezing-rain"],
    ],
    "Freezing rain today and Sunday, with highs reaching 3°C on Wednesday.": [
        "sentence",
        [
            "with",
            ["during", "medium-freezing-rain", ["and", "today", "sunday"]],
            ["temperatures-peaking", ["celsius", 3], "wednesday"],
        ],
    ],
    "Hail": ["title", "hail"],
    "Hail and Thunderstorms": ["title", ["and", "hail", "thunderstorm"]],
    "Hail starting in 5 min., ending 45 min. later.": [
        "sentence",
        ["starting-then-stopping-later", "hail", ["minutes", 5], ["minutes", 45]],
    ],
    "Hazy": ["title", "haze"],
    "Hazy and Humid": ["title", ["and", "haze", "high-humidity"]],
    "Hazy in the afternoon.": ["sentence", ["during", "haze", "afternoon"]],
    "Hazy throughout the day.": ["sentence", ["for-day", "haze"]],
    "Heavy Freezing Rain": ["title", "heavy-freezing-rain"],
    "Heavy Precipitation": ["title", "heavy-precipitation"],
    "Heavy Rain": ["title", "heavy-rain"],
    "Heavy Rain and Thunderstorms": ["title", ["and", "heavy-rain", "thunderstorm"]],
    "Heavy Sleet": ["title", "heavy-sleet"],
    "Heavy Snow": ["title", "heavy-snow"],
    "Heavy Snow (1–3 in.)": [
        "title",
        ["parenthetical", "heavy-snow", ["inches", ["range", 1, 3]]],
    ],
    "Heavy Snow (3–5 cm.)": [
        "title",
        ["parenthetical", "heavy-snow", ["centimeters", ["range", 3, 5]]],
    ],
    "Heavy freezing rain ending in 10 min., returning 32 min. later.": [
        "sentence",
        [
            "stopping-then-starting-later",
            "heavy-freezing-rain",
            ["minutes", 10],
            ["minutes", 32],
        ],
    ],
    "Heavy precipitation until afternoon.": [
        "sentence",
        ["until", "heavy-precipitation", "afternoon"],
    ],
    "Heavy rain until later this morning, returning this evening.": [
        "sentence",
        ["until-starting-again", "heavy-rain", "later-today-morning", "today-evening"],
    ],
    "Heavy sleet starting in 20 min., ending 30 min. later.": [
        "sentence",
        [
            "starting-then-stopping-later",
            "heavy-sleet",
            ["minutes", 20],
            ["minutes", 30],
        ],
    ],
    "Heavy snow (8–12 in.) throughout the day.": [
        "sentence",
        ["for-day", ["parenthetical", "heavy-snow", ["inches", ["range", 8, 12]]]],
    ],
    "Humid and Partly Cloudy": ["title", ["and", "high-humidity", "light-clouds"]],
    "Light Freezing Rain": ["title", "light-freezing-rain"],
    "Light Freezing Rain (with a Chance of 2–4 in. of Snow)": [
        "title",
        ["parenthetical", "light-freezing-rain", ["inches", ["range", 2, 4]]],
    ],
    "Light Precipitation": ["title", "very-light-precipitation"],
    "Light Rain": ["title", "light-rain"],
    "Light Sleet": ["title", "very-light-sleet"],
    "Light Snow": ["title", "light-snow"],
    "Light rain ending in 15 min.": [
        "sentence",
        ["stopping-in", "light-rain", ["minutes", 15]],
    ],
    "Light sleet later this afternoon and foggy tomorrow morning.": [
        "sentence",
        [
            "and",
            ["during", "light-sleet", "later-today-afternoon"],
            ["during", "fog", "tomorrow-morning"],
        ],
    ],
    "Light sleet starting in the morning.": [
        "sentence",
        ["starting", "very-light-sleet", "morning"],
    ],
    "Light snow (2 cm.) later this morning.": [
        "sentence",
        [
            "during",
            ["parenthetical", "light-snow", ["centimeters", 2]],
            "later-today-morning",
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
    "Misty": ["title", "mist"],
    "Misty and Overcast": ["title", ["and", "mist", "heavy-clouds"]],
    "Misty overnight.": ["sentence", ["during", "mist", "night"]],
    "Misty throughout the day.": ["sentence", ["for-day", "mist"]],
    "Mixed precipitation (1–3 in. of snow) throughout the day.": [
        "sentence",
        [
            "for-day",
            ["parenthetical", "mixed-precipitation", ["inches", ["range", 1, 3]]],
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
    "Mostly Clear": ["title", "very-light-clouds"],
    "Mostly Cloudy": ["title", "medium-clouds"],
    "Mostly cloudy throughout the day.": ["sentence", ["for-day", "medium-clouds"]],
    "Next hour forecasts are partially unavailable due to gaps in coverage from nearby radar stations.": [
        "sentence",
        ["next-hour-forecast-status", "partially-unavailable", "station-incomplete"],
    ],
    "Next hour forecasts are temporarily unavailable due to all nearby radar stations being offline.": [
        "sentence",
        ["next-hour-forecast-status", "temporarily-unavailable", "station-offline"],
    ],
    "Next hour forecasts are unavailable due to all nearby radar stations being offline.": [
        "sentence",
        ["next-hour-forecast-status", "unavailable", "station-offline"],
    ],
    "No precipitation throughout the week, with highs reaching 85°F tomorrow.": [
        "sentence",
        [
            "with",
            ["for-week", "no-precipitation"],
            ["temperatures-peaking", ["fahrenheit", 85], "tomorrow"],
        ],
    ],
    "Overcast": ["title", "heavy-clouds"],
    "Overcast from evening until night.": [
        "sentence",
        ["starting-continuing-until", "heavy-clouds", "evening", "night"],
    ],
    "Overcast starting later tonight and heavy snow tomorrow afternoon.": [
        "sentence",
        [
            "and",
            ["starting", "heavy-clouds", "later-today-night"],
            ["during", "heavy-snow", "tomorrow-afternoon"],
        ],
    ],
    "Partly Cloudy": ["title", "light-clouds"],
    "Possible Drizzle": ["title", "possible-very-light-rain"],
    "Possible Flurries": ["title", "possible-very-light-snow"],
    "Possible Freezing Drizzle": ["title", "possible-very-light-freezing-rain"],
    "Possible Freezing Rain": ["title", "possible-medium-freezing-rain"],
    "Possible Hail": ["title", "possible-hail"],
    "Possible Heavy Freezing Rain": ["title", "possible-heavy-freezing-rain"],
    "Possible Heavy Precipitation": ["title", "possible-heavy-precipitation"],
    "Possible Heavy Rain": ["title", "possible-heavy-rain"],
    "Possible Heavy Sleet": ["title", "possible-heavy-sleet"],
    "Possible Heavy Snow": ["title", "possible-heavy-snow"],
    "Possible Light Freezing Rain": ["title", "possible-light-freezing-rain"],
    "Possible Light Precipitation": ["title", "possible-very-light-precipitation"],
    "Possible Light Rain": ["title", "possible-light-rain"],
    "Possible Light Sleet": ["title", "possible-very-light-sleet"],
    "Possible Light Snow": ["title", "possible-light-snow"],
    "Possible Precipitation": ["title", "possible-medium-precipitation"],
    "Possible Rain": ["title", "possible-medium-rain"],
    "Possible Sleet": ["title", "possible-medium-sleet"],
    "Possible Snow": ["title", "possible-medium-snow"],
    "Possible Thunderstorms": ["title", "possible-thunderstorm"],
    "Possible thunderstorms and hail in the evening.": [
        "sentence",
        ["during", ["and", "possible-thunderstorm", "hail"], "evening"],
    ],
    "Possible thunderstorms over the weekend, with highs climbing to 104°F next Monday.": [
        "sentence",
        [
            "with",
            ["over-weekend", "possible-thunderstorm"],
            ["temperatures-rising", ["fahrenheit", 104], "next-monday"],
        ],
    ],
    "Precipitation": ["title", "medium-precipitation"],
    "Precipitation today through Saturday, with highs reaching 100°F on Monday.": [
        "sentence",
        [
            "with",
            ["during", "medium-precipitation", ["through", "today", "saturday"]],
            ["temperatures-peaking", ["fahrenheit", 100], "monday"],
        ],
    ],
    "Rain": ["title", "medium-rain"],
    "Rain (with a Chance of 2–4 in. of Snow)": [
        "title",
        ["parenthetical", "medium-rain", ["inches", ["range", 2, 4]]],
    ],
    "Rain ending in 25 min., returning 8 min. later.": [
        "sentence",
        [
            "stopping-then-starting-later",
            "medium-rain",
            ["minutes", 25],
            ["minutes", 8],
        ],
    ],
    "Sleet": ["title", "medium-sleet"],
    "Smoke": ["title", "smoke"],
    "Smoke and Partly Cloudy": ["title", ["and", "smoke", "light-clouds"]],
    "Smoke in the morning.": ["sentence", ["during", "smoke", "morning"]],
    "Smoke throughout the day.": ["sentence", ["for-day", "smoke"]],
    "Smoke until this evening.": ["sentence", ["until", "smoke", "today-evening"]],
    "Snow": ["title", "medium-snow"],
    "Snow (5 in.) overnight.": [
        "sentence",
        ["during", ["parenthetical", "medium-snow", ["inches", 5]], "night"],
    ],
    "Snow (< 1 cm.) in the afternoon.": [
        "sentence",
        [
            "during",
            ["parenthetical", "medium-snow", ["less-than", ["centimeters", 1]]],
            "afternoon",
        ],
    ],
    "Snow and Thunderstorms": ["title", ["and", "medium-snow", "thunderstorm"]],
    "Snow later this evening and tomorrow morning.": [
        "sentence",
        ["during", "medium-snow", ["and", "later-today-evening", "tomorrow-morning"]],
    ],
    "Thunderstorms": ["title", "thunderstorm"],
    "Thunderstorms for the hour.": ["sentence", ["for-hour", "thunderstorm"]],
    "Windy": ["title", "medium-wind"],
    "Windy until tonight.": ["sentence", ["until", "medium-wind", "today-night"]],
}
