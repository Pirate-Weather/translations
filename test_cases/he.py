# This would be one of your translations, as a Python dictionary
cases = {
    "בהיר": ["title", "clear"],
    "אפשרות נמוך מאוד למשקעים": ["title", "possible-very-light-precipitation"],
    "משקעים קלים": ["title", "very-light-precipitation"],
    "אפשרות נמוך למשקעים": ["title", "possible-light-precipitation"],
    "משקעים קלים": ["title", "light-precipitation"],
    "משקעים": ["title", "medium-precipitation"],
    "משקעים כבדים": ["title", "heavy-precipitation"],
    "אפשרות לטפטוף": ["title", "possible-very-light-rain"],
    "טפטוף": ["title", "very-light-rain"],
    "אפשרות לגשם קל": ["title", "possible-light-rain"],
    "גשם קל": ["title", "light-rain"],
    "גשם": ["title", "medium-rain"],
    "גשם כבד": ["title", "heavy-rain"],
    "אפשרות לשלג-קרח קל מאוד": ["title", "possible-very-light-sleet"],
    "שלג-קרח קל": ["title", "very-light-sleet"],
    "אפשרות לשלג-קרח קל": ["title", "possible-light-sleet"],
    "שלג-קרח קל": ["title", "light-sleet"],
    "שלג-קרח": ["title", "medium-sleet"],
    "שלג-קרח כבד": ["title", "heavy-sleet"],
    "אפשרות לשלג קל מאוד": ["title", "possible-very-light-snow"],
    "שלג קל מאוד": ["title", "very-light-snow"],
    "אפשרות לשלג קל": ["title", "possible-light-snow"],
    "שלג קל": ["title", "light-snow"],
    "שלג": ["title", "medium-snow"],
    "שלג כבד": ["title", "heavy-snow"],
    "רוח": ["title", "medium-wind"],
    "רוח חזקה": ["title", "heavy-wind"],
    "ערפל": ["title", "fog"],
    "ברור בעיקר": ["title", "very-light-clouds"],
    "עננות חלקית": ["title", "light-clouds"],
    "מעונן חלקית": ["title", "medium-clouds"],
    "עננות": ["title", "heavy-clouds"],
    "יבש ורוח קלה": ["title", ["and", "low-humidity", "light-wind"]],
    "טפטוף ורוח חזקה": ["title", ["and", "very-light-rain", "heavy-wind"]],
    "לחות גבוהה ועננות חלקית": ["title", ["and", "high-humidity", "light-clouds"]],
    "בהיר לשעה הקרובה.": ["sentence", ["for-hour", "clear"]],
    "שלג קל מאוד יתחיל בעוד 35 דקות.": [
        "sentence",
        ["starting-in", "very-light-snow", ["minutes", 35]],
    ],
    "גשם קל יפסק בעוד 15 דקות.": [
        "sentence",
        ["stopping-in", "light-rain", ["minutes", 15]],
    ],
    "שלג-קרח כבד יתחיל בעוד 20 דקות, יפסק אחרי 30 דקות.": [
        "sentence",
        [
            "starting-then-stopping-later",
            "heavy-sleet",
            ["minutes", 20],
            ["minutes", 30],
        ],
    ],
    "גשם יפסק בעוד 25 דקות, יתחדש לאחר 8 דקות.": [
        "sentence",
        [
            "stopping-then-starting-later",
            "medium-rain",
            ["minutes", 25],
            ["minutes", 8],
        ],
    ],
    "מעונן חלקית לאורך היום.": ["sentence", ["for-day", "medium-clouds"]],
    "שלג-קרח קל מתחיל בבוקר.": [
        "sentence",
        ["starting", "very-light-sleet", "morning"],
    ],
    "רוח עד הלילה.": ["sentence", ["until", "medium-wind", "today-night"]],
    "משקעים כבדים עד אחר הצהרים.": [
        "sentence",
        ["until", "heavy-precipitation", "afternoon"],
    ],
    "רוח קלה אחר הצהרים.": ["sentence", ["during", "light-wind", "afternoon"]],
    "שלג מאוחר יותר הערב ומחר בבוקר.": [
        "sentence",
        ["during", "medium-snow", ["and", "later-today-evening", "tomorrow-morning"]],
    ],
    "גשם כבד עד מאוחר יותר בבוקר, ויתחדש הערב.": [
        "sentence",
        ["until-starting-again", "heavy-rain", "later-today-morning", "today-evening"],
    ],
    "עננות מהערב, ימשך עד הלילה.": [
        "sentence",
        ["starting-continuing-until", "heavy-clouds", "evening", "night"],
    ],
    "שלג-קרח קל מאוחר יותר אחר הצהרים וערפל מחר בבוקר.": [
        "sentence",
        [
            "and",
            ["during", "light-sleet", "later-today-afternoon"],
            ["during", "fog", "tomorrow-morning"],
        ],
    ],
    "רוח חזקה מהבוקר, ימשך עד אחרי הצהרים, ושלג-קרח מחר בבוקר.": [
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
    "עננות מתחיל מאוחר יותר הלילה ושלג כבד מחר אחרי הצהרים.": [
        "sentence",
        [
            "and",
            ["starting", "heavy-clouds", "later-today-night"],
            ["during", "heavy-snow", "tomorrow-afternoon"],
        ],
    ],
    "יבש הלילה ומשקעים קלים ממחר בערב, ימשך עד מחר בלילה.": [
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
    "שלג (5 אינץ׳) הלילה.": [
        "sentence",
        ["during", ["parenthetical", "medium-snow", ["inches", 5]], "night"],
    ],
    "שלג קל (2 סֿ״מ) מאוחר יותר בבוקר.": [
        "sentence",
        [
            "during",
            ["parenthetical", "light-snow", ["centimeters", 2]],
            "later-today-morning",
        ],
    ],
    "שלג כבד (8–12 אינץ׳) לאורך היום.": [
        "sentence",
        ["for-day", ["parenthetical", "heavy-snow", ["inches", ["range", 8, 12]]]],
    ],
    "שלג (פחות מסֿ״מ) אחר הצהרים.": [
        "sentence",
        [
            "during",
            ["parenthetical", "medium-snow", ["less-than", ["centimeters", 1]]],
            "afternoon",
        ],
    ],
    "ללא משקעים במשך השבוע, וחום גבוה יגיע לשיא של 85 מעלות פרנהייט מחר.": [
        "sentence",
        [
            "with",
            ["for-week", "no-precipitation"],
            ["temperatures-peaking", ["fahrenheit", 85], "tomorrow"],
        ],
    ],
    "משקעים מעורבים לאורך הסוף שבוע, וחום גבוה יטפס ל-32 מעלות צלסיוס בחמישי.": [
        "sentence",
        [
            "with",
            ["over-weekend", "mixed-precipitation"],
            ["temperatures-rising", ["celsius", 32], "thursday"],
        ],
    ],
    "טפטוף בשני, וחום גבוה ירד עד 15 מעלות פרנהייט בשישי.": [
        "sentence",
        [
            "with",
            ["during", "very-light-rain", "monday"],
            ["temperatures-valleying", ["fahrenheit", 15], "friday"],
        ],
    ],
    "שלג קל בשלישי ורביעי הבא, וחום גבוה יפול ל-0 מעלות צלסיוס בראשון.": [
        "sentence",
        [
            "with",
            ["during", "light-snow", ["and", "tuesday", "next-wednesday"]],
            ["temperatures-falling", ["celsius", 0], "sunday"],
        ],
    ],
    "משקעים היום עד שבת, וחום גבוה יגיע לשיא של 100 מעלות פרנהייט בשני.": [
        "sentence",
        [
            "with",
            ["during", "medium-precipitation", ["through", "today", "saturday"]],
            ["temperatures-peaking", ["fahrenheit", 100], "monday"],
        ],
    ],
    "משקעים מעורבים (1–3 אינץ׳ של שלג) לאורך היום.": [
        "sentence",
        [
            "for-day",
            ["parenthetical", "mixed-precipitation", ["inches", ["range", 1, 3]]],
        ],
    ],
    "שלג כבד (1–3 אינץ׳)": [
        "title",
        ["parenthetical", "heavy-snow", ["inches", ["range", 1, 3]]],
    ],
    "שלג כבד (3–5 סֿ״מ)": [
        "title",
        ["parenthetical", "heavy-snow", ["centimeters", ["range", 3, 5]]],
    ],
    "אפשרות לסופת ברקים": ["title", "possible-thunderstorm"],
    "גשם כבד וסופת ברקים": ["title", ["and", "heavy-rain", "thunderstorm"]],
    "טפטוף יתחיל בעוד פחות מדקה.": [
        "sentence",
        ["starting-in", "very-light-rain", ["less-than", ["minutes", 1]]],
    ],
}
