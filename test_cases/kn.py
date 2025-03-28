# This would be one of your translations, as a Python dictionary
cases = {
    "ಸ್ಪಷ್ಟ": ["title", "clear"],
    "ಕಡಿಮೆಯಾದ ಸೋರುವಿಕೆ ಸಾಧ್ಯ": ["title", "possible-very-light-precipitation"],
    "ಕಡಿಮೆ ಸೋರುವಿಕೆ": ["title", "very-light-precipitation"],
    "ಕಡಿಮೆಯಾದ ಸೋರುವಿಕೆ ಸಾಧ್ಯ": ["title", "possible-light-precipitation"],
    "ಕಡಿಮೆ ಸೋರುವಿಕೆ": ["title", "light-precipitation"],
    "ಸೋರುವಿಕೆ": ["title", "medium-precipitation"],
    "ಭಾರೀ ಸೋರುವಿಕೆ": ["title", "heavy-precipitation"],
    "ಚಿಮುಕು ಸಾಧ್ಯ": ["title", "possible-very-light-rain"],
    "ಚಿಮುಕು": ["title", "very-light-rain"],
    "ಸ್ವಲ್ಪ ಮಳೆ ಸಾಧ್ಯ": ["title", "possible-light-rain"],
    "ಸ್ವಲ್ಪ ಮಳೆ": ["title", "light-rain"],
    "ಮಳೆ": ["title", "medium-rain"],
    "ಭಾರೀ ಮಳೆ": ["title", "heavy-rain"],
    "ಸ್ವಲ್ಪ ಹಿಮ ಮಳೆ ಸಾಧ್ಯ": ["title", "possible-very-light-sleet"],
    "ಸ್ವಲ್ಪ ಹಿಮ ಮಳೆ": ["title", "very-light-sleet"],
    "ಸ್ವಲ್ಪ ಹಿಮ ಮಳೆ ಸಾಧ್ಯ": ["title", "possible-light-sleet"],
    "ಸ್ವಲ್ಪ ಹಿಮ ಮಳೆ": ["title", "light-sleet"],
    "ಹಿಮ ಮಳೆ": ["title", "medium-sleet"],
    "ಭಾರೀ ಹಿಮ ಮಳೆ": ["title", "heavy-sleet"],
    "ಹಿಮಸುರಿತ ಸಾಧ್ಯ": ["title", "possible-very-light-snow"],
    "ಹಿಮಸುರಿತ": ["title", "very-light-snow"],
    "ಕಡಿಮೆ ಮಂಜು ಸಾಧ್ಯ": ["title", "possible-light-snow"],
    "ಕಡಿಮೆ ಮಂಜು": ["title", "light-snow"],
    "ಮಂಜು": ["title", "medium-snow"],
    "ಭಾರೀ ಮಂಜು": ["title", "heavy-snow"],
    "ಗಾಳಿಯಾಗಿ": ["title", "medium-wind"],
    "ಅಪಾಯಕಾರಿ ಗಾಳಿ": ["title", "heavy-wind"],
    "ಮಂಜಿನ": ["title", "fog"],
    "ಹೆಚ್ಚಾಗಿ ಸ್ಪಷ್ಟ": ["title", "very-light-clouds"],
    "ಸ್ವಲ್ಪ ಮಟ್ಟಿಗೆ ಮೋಡ": ["title", "light-clouds"],
    "ಹೆಚ್ಚಾಗಿ ಮೋಡ": ["title", "medium-clouds"],
    "ಕತ್ತಲು ಕವಿ": ["title", "heavy-clouds"],
    "ಒಣಗಿದ ಮತ್ತೆ ತಂಗಾಳಿಯಾಗಿ": ["title", ["and", "low-humidity", "light-wind"]],
    "ಚಿಮುಕು ಮತ್ತೆ ಅಪಾಯಕಾರಿ ಗಾಳಿ": ["title", ["and", "very-light-rain", "heavy-wind"]],
    "ಆದ್ರವಾದ ಮತ್ತೆ ಸ್ವಲ್ಪ ಮಟ್ಟಿಗೆ ಮೋಡ": ["title", ["and", "high-humidity", "light-clouds"]],
    "ಸ್ಪಷ್ಟ ಗಂಟೆಗೆ": ["sentence", ["for-hour", "clear"]],
    "ಹಿಮಸುರಿತ 35 ನಿಮಿಷ ಅಲ್ಲಿ ಶುರುವಾಗುತ್ತದೆ": [
        "sentence",
        ["starting-in", "very-light-snow", ["minutes", 35]],
    ],
    "ಸ್ವಲ್ಪ ಮಳೆ 15 ನಿಮಿಷ ಅಲ್ಲಿ ನಿಲ್ಲಲಿದೆ": [
        "sentence",
        ["stopping-in", "light-rain", ["minutes", 15]],
    ],
    "ಭಾರೀ ಹಿಮ ಮಳೆ 20 ನಿಮಿಷ ಶುರುವಾಗುವುದು ನಂತರ 30 ನಿಮಿಷ ನಲ್ಲಿ ನಿಲ್ಲುವುದು": [
        "sentence",
        [
            "starting-then-stopping-later",
            "heavy-sleet",
            ["minutes", 20],
            ["minutes", 30],
        ],
    ],
    "ಮಳೆ 25 ನಿಮಿಷ ನಿಲ್ಲುವುದು ನಂತರ 8 ನಿಮಿಷ ನಲ್ಲಿ ಮತ್ತೆ ಶುರುವಾಗುವುದು": [
        "sentence",
        [
            "stopping-then-starting-later",
            "medium-rain",
            ["minutes", 25],
            ["minutes", 8],
        ],
    ],
    "ಹೆಚ್ಚಾಗಿ ಮೋಡ ದಿನಪೂರ್ತಿ": ["sentence", ["for-day", "medium-clouds"]],
    "ಸ್ವಲ್ಪ ಹಿಮ ಮಳೆ ಬೆಳಿಗ್ಗೆ ಅಲ್ಲಿ ಶುರುವಾಗುತ್ತದೆ": [
        "sentence",
        ["starting", "very-light-sleet", "morning"],
    ],
    "ಗಾಳಿಯಾಗಿ ಇಂದು ರಾತ್ರಿ ವರೆಗೂ": ["sentence", ["until", "medium-wind", "today-night"]],
    "ಭಾರೀ ಸೋರುವಿಕೆ ಮದ್ಯಾಹ್ನ ವರೆಗೂ": ["sentence", ["until", "heavy-precipitation", "afternoon"]],
    "ತಂಗಾಳಿಯಾಗಿ ಮದ್ಯಾಹ್ನ ವೇಳೆಯಲ್ಲಿ": ["sentence", ["during", "light-wind", "afternoon"]],
    "ಮಂಜು ನಂತರ ಇಂದು ಸಂಜೆ ಮತ್ತೆ ನಾಳೆ ಬೆಳಿಗ್ಗೆ ವೇಳೆಯಲ್ಲಿ": [
        "sentence",
        ["during", "medium-snow", ["and", "later-today-evening", "tomorrow-morning"]],
    ],
    "ಭಾರೀ ಮಳೆ ನಂತರಇಂದು ಬೆಳಿಗ್ಗೆ ವರೆಗೂ ಮತ್ತೆ ಇಂದು ಸಂಜೆ ಶುರುವಾಗುವುದು": [
        "sentence",
        ["until-starting-again", "heavy-rain", "later-today-morning", "today-evening"],
    ],
    "ಕತ್ತಲು ಕವಿ ರಿಂದ ಪ್ರಾರಂಭವಾಗಿ ಸಂಜೆ ವರೆಗೆ, ಮತ್ತು ಒಂದೇ ರಾತ್ರಿಯಲ್ಲಿ ವರೆಗೂ ಮುಂದುವರೆಯುವುದು": [
        "sentence",
        ["starting-continuing-until", "heavy-clouds", "evening", "night"],
    ],
    "ಸ್ವಲ್ಪ ಹಿಮ ಮಳೆ ನಂತರಇಂದು ಮಧ್ಯಾಹ್ನ ವೇಳೆಯಲ್ಲಿ ಮತ್ತೆ ಮಂಜಿನ ನಾಳೆ ಬೆಳಿಗ್ಗೆ ವೇಳೆಯಲ್ಲಿ": [
        "sentence",
        [
            "and",
            ["during", "light-sleet", "later-today-afternoon"],
            ["during", "fog", "tomorrow-morning"],
        ],
    ],
    "ಅಪಾಯಕಾರಿ ಗಾಳಿ ರಿಂದ ಪ್ರಾರಂಭವಾಗಿ ಇಂದು ಬೆಳಿಗ್ಗೆ ವರೆಗೆ, ಮತ್ತು ಇಂದು ಮಧ್ಯಾಹ್ನ ವರೆಗೂ ಮುಂದುವರೆಯುವುದು ಮತ್ತೆ ಹಿಮ ಮಳೆ ನಾಳೆ ಬೆಳಿಗ್ಗೆ ವೇಳೆಯಲ್ಲಿ": [
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
    "ಕತ್ತಲು ಕವಿ ನಂತರ ಇಂದು ರಾತ್ರಿ ಅಲ್ಲಿ ಶುರುವಾಗುತ್ತದೆ ಮತ್ತೆ ಭಾರೀ ಮಂಜು ನಾಳೆ ಮದ್ಯಾಹ್ನ ವೇಳೆಯಲ್ಲಿ": [
        "sentence",
        [
            "and",
            ["starting", "heavy-clouds", "later-today-night"],
            ["during", "heavy-snow", "tomorrow-afternoon"],
        ],
    ],
    "ಒಣಗಿದ ಇಂದು ರಾತ್ರಿ ವೇಳೆಯಲ್ಲಿ ಮತ್ತೆ ಕಡಿಮೆ ಸೋರುವಿಕೆ ರಿಂದ ಪ್ರಾರಂಭವಾಗಿ ನಾಳೆ ಸಂಜೆ ವರೆಗೆ, ಮತ್ತು ನಾಳೆ ರಾತ್ರಿ ವರೆಗೂ ಮುಂದುವರೆಯುವುದು": [
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
    "ಮಂಜು (5 ಇಂಚುಗಳು) ಒಂದೇ ರಾತ್ರಿಯಲ್ಲಿ ವೇಳೆಯಲ್ಲಿ": [
        "sentence",
        ["during", ["parenthetical", "medium-snow", ["inches", 5]], "night"],
    ],
    "ಕಡಿಮೆ ಮಂಜು (2 ಸೆಂಟಿಮೀಟರ್ಗಳು) ನಂತರಇಂದು ಬೆಳಿಗ್ಗೆ ವೇಳೆಯಲ್ಲಿ": [
        "sentence",
        [
            "during",
            ["parenthetical", "light-snow", ["centimeters", 2]],
            "later-today-morning",
        ],
    ],
    "ಭಾರೀ ಮಂಜು (8\u201312 ಇಂಚುಗಳು) ದಿನಪೂರ್ತಿ": [
        "sentence",
        ["for-day", ["parenthetical", "heavy-snow", ["inches", ["range", 8, 12]]]],
    ],
    "ಮಂಜು (1 ಸೆಂಟಿಮೀಟರ್ಗಳು ಕ್ಕಿಂತ ಕಡಿಮೆ) ಮದ್ಯಾಹ್ನ ವೇಳೆಯಲ್ಲಿ": [
        "sentence",
        [
            "during",
            ["parenthetical", "medium-snow", ["less-than", ["centimeters", 1]]],
            "afternoon",
        ],
    ],
    "ಸೋರುವಿಕೆ ಇಲ್ಲ ವಾರ ಪೂರ್ತಿ 85\u00b0F ನಾಳೆ ನಲ್ಲಿ ತಾಪಮಾನ ಉತ್ತುಂಗಕ್ಕೇರುವುದು ಒಂದಿಗೆ": [
        "sentence",
        [
            "with",
            ["for-week", "no-precipitation"],
            ["temperatures-peaking", ["fahrenheit", 85], "tomorrow"],
        ],
    ],
    "ಮಿಶ್ರಿತ ಸೋರುವಿಕೆ ವಾರಾಂತ್ಯದಲ್ಲಿ ಅಧಿಕ ತಾಪಮಾನವು 32\u00b0C ಗುರುವಾರದಂದು ಕ್ಕೆ ಏರಿಕೆಯಾಗಿದೆ ಒಂದಿಗೆ": [
        "sentence",
        [
            "with",
            ["over-weekend", "mixed-precipitation"],
            ["temperatures-rising", ["celsius", 32], "thursday"],
        ],
    ],
    "ಚಿಮುಕು ಸೋಮವಾರದಂದು ವೇಳೆಯಲ್ಲಿ ಹೆಚ್ಚಿನ ತಾಪಮಾನ 15\u00b0F ಶುಕ್ರವಾರದಂದು ನಲ್ಲಿ ಕೆಳಗಿಳಿಯುವುದು ಒಂದಿಗೆ": [
        "sentence",
        [
            "with",
            ["during", "very-light-rain", "monday"],
            ["temperatures-valleying", ["fahrenheit", 15], "friday"],
        ],
    ],
    "ಕಡಿಮೆ ಮಂಜು ಮಂಗಳವಾರದಂದು ಮತ್ತೆ ಮುಂದಿನ ಬುಧವಾರ ವೇಳೆಯಲ್ಲಿ ಅಧಿಕ ತಾಪಮಾನವು 0\u00b0C ಭಾನುವಾರದಂದು ಕ್ಕೆ ಇಳಿದಿದೆ ಒಂದಿಗೆ": [
        "sentence",
        [
            "with",
            ["during", "light-snow", ["and", "tuesday", "next-wednesday"]],
            ["temperatures-falling", ["celsius", 0], "sunday"],
        ],
    ],
    "ಸೋರುವಿಕೆ ಇಂದು ರಿಂದ ಶನಿವಾರದಂದು ವೇಳೆಯಲ್ಲಿ 100\u00b0F ಸೋಮವಾರದಂದು ನಲ್ಲಿ ತಾಪಮಾನ ಉತ್ತುಂಗಕ್ಕೇರುವುದು ಒಂದಿಗೆ": [
        "sentence",
        [
            "with",
            ["during", "medium-precipitation", ["through", "today", "saturday"]],
            ["temperatures-peaking", ["fahrenheit", 100], "monday"],
        ],
    ],
    "ಮಿಶ್ರಿತ ಸೋರುವಿಕೆ (1\u20133 ಇಂಚುಗಳು) ದಿನಪೂರ್ತಿ": [
        "sentence",
        [
            "for-day",
            ["parenthetical", "mixed-precipitation", ["inches", ["range", 1, 3]]],
        ],
    ],
    "ಭಾರೀ ಮಂಜು (1\u20133 ಇಂಚುಗಳು)": [
        "title",
        ["parenthetical", "heavy-snow", ["inches", ["range", 1, 3]]],
    ],
    "ಭಾರೀ ಮಂಜು (3\u20135 ಸೆಂಟಿಮೀಟರ್ಗಳು)": [
        "title",
        ["parenthetical", "heavy-snow", ["centimeters", ["range", 3, 5]]],
    ],
    "ಗುಡುಗು ಸಾಧ್ಯ": ["title", "possible-thunderstorm"],
    "ಭಾರೀ ಮಳೆ ಮತ್ತೆ ಗುಡುಗು": ["title", ["and", "heavy-rain", "thunderstorm"]],
    "ಚಿಮುಕು 1 ನಿಮಿಷ ಕ್ಕಿಂತ ಕಡಿಮೆ ಅಲ್ಲಿ ಶುರುವಾಗುತ್ತದೆ": [
        "sentence",
        ["starting-in", "very-light-rain", ["less-than", ["minutes", 1]]],
    ],
}
