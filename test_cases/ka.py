# This would be one of your translations, as a Python dictionary
cases = {
    "მოწმენდილი": ["title", "clear"],
    "მოსალოდნელია სუსტი ნალექი": ["title", "possible-very-light-precipitation"],
    "სუსტი ნალექი": ["title", "very-light-precipitation"],
    "მოსალოდნელია მცირე ნალექი": ["title", "possible-light-precipitation"],
    "მცირე ნალექი": ["title", "light-precipitation"],
    "ნალექი": ["title", "medium-precipitation"],
    "ძლიერი ნალექი": ["title", "heavy-precipitation"],
    "მოსალოდნელია სუსტი წვიმა": ["title", "possible-very-light-rain"],
    "სუსტი წვიმა": ["title", "very-light-rain"],
    "მოსალოდნელია მცირე წვიმა": ["title", "possible-light-rain"],
    "მცირე წვიმა": ["title", "light-rain"],
    "წვიმა": ["title", "medium-rain"],
    "ძლიერი წვიმა": ["title", "heavy-rain"],
    "მოსალოდნელია სუსტი თოვლჭყაპი": ["title", "possible-very-light-sleet"],
    "სუსტი თოვლჭყაპი": ["title", "very-light-sleet"],
    "მოსალოდნელია მცირე თოვლჭყაპი": ["title", "possible-light-sleet"],
    "მცირე თოვლჭყაპი": ["title", "light-sleet"],
    "თოვლჭყაპი": ["title", "medium-sleet"],
    "ძლიერი თოვლჭყაპი": ["title", "heavy-sleet"],
    "მოსალოდნელია სუსტი თოვლი": ["title", "possible-very-light-snow"],
    "სუსტი თოვლი": ["title", "very-light-snow"],
    "მოსალოდნელია მცირე თოვლი": ["title", "possible-light-snow"],
    "მცირე თოვლი": ["title", "light-snow"],
    "თოვლი": ["title", "medium-snow"],
    "ძლიერი თოვლი": ["title", "heavy-snow"],
    "ქარი": ["title", "medium-wind"],
    "ძლიერი ქარი": ["title", "heavy-wind"],
    "ნისლი": ["title", "fog"],
    "უმეტესად მოწმენდილი": ["title", "very-light-clouds"],
    "ნაწილობრივ ღრუბლიანი": ["title", "light-clouds"],
    "უმეტესად ღრუბლიანი": ["title", "medium-clouds"],
    "მოღრუბლულობა": ["title", "heavy-clouds"],
    "მშრალი და სუსტი ქარი": ["title", ["and", "low-humidity", "light-wind"]],
    "სუსტი წვიმა და ძლიერი ქარი": ["title", ["and", "very-light-rain", "heavy-wind"]],
    "ტენიანი და ნაწილობრივ ღრუბლიანი": [
        "title",
        ["and", "high-humidity", "light-clouds"],
    ],
    "მოწმენდილი ამ დროისთვის.": ["sentence", ["for-hour", "clear"]],
    "სუსტი თოვლი დაიწყება 35 წთ.": [
        "sentence",
        ["starting-in", "very-light-snow", ["minutes", 35]],
    ],
    "მცირე წვიმა შეწყდება 15 წთ.": [
        "sentence",
        ["stopping-in", "light-rain", ["minutes", 15]],
    ],
    "ძლიერი თოვლჭყაპი დაიწყება 20 წთ., შეწყდება 30 წთ. მოგვიანებით.": [
        "sentence",
        [
            "starting-then-stopping-later",
            "heavy-sleet",
            ["minutes", 20],
            ["minutes", 30],
        ],
    ],
    "წვიმა შეწყდება 25 წთ., დაიწყება კვლავ 8 წთ. მოგვიანებით.": [
        "sentence",
        [
            "stopping-then-starting-later",
            "medium-rain",
            ["minutes", 25],
            ["minutes", 8],
        ],
    ],
    "უმეტესად ღრუბლიანი მთელი დღის განმავლობაში.": [
        "sentence",
        ["for-day", "medium-clouds"],
    ],
    "სუსტი თოვლჭყაპი დაიწყება დილას.": [
        "sentence",
        ["starting", "very-light-sleet", "morning"],
    ],
    "ქარი გაგრძელდება ღამე.": ["sentence", ["until", "medium-wind", "today-night"]],
    "ძლიერი ნალექი გაგრძელდება შუადღეს.": [
        "sentence",
        ["until", "heavy-precipitation", "afternoon"],
    ],
    "სუსტი ქარი შუადღეს.": ["sentence", ["during", "light-wind", "afternoon"]],
    "თოვლი ამ საღამოს და ხვალ დილით.": [
        "sentence",
        ["during", "medium-snow", ["and", "later-today-evening", "tomorrow-morning"]],
    ],
    "ძლიერი წვიმა დღეს დილით, დაიწყება კვლავ საღამოს.": [
        "sentence",
        ["until-starting-again", "heavy-rain", "later-today-morning", "today-evening"],
    ],
    "მოღრუბლულობა დაიწყება საღამოს, გაგრძელდება ღამე.": [
        "sentence",
        ["starting-continuing-until", "heavy-clouds", "evening", "night"],
    ],
    "მცირე თოვლჭყაპი ნაშუადღევს და ნისლი ხვალ დილით.": [
        "sentence",
        [
            "and",
            ["during", "light-sleet", "later-today-afternoon"],
            ["during", "fog", "tomorrow-morning"],
        ],
    ],
    "ძლიერი ქარი დაიწყება დილით, გაგრძელდება შუადღეს და თოვლჭყაპი ხვალ დილით.": [
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
    "მოღრუბლულობა დაიწყება გვიან ღამით და ძლიერი თოვლი ხვალ შუადღეს.": [
        "sentence",
        [
            "and",
            ["starting", "heavy-clouds", "later-today-night"],
            ["during", "heavy-snow", "tomorrow-afternoon"],
        ],
    ],
    "მშრალი ღამე და მცირე ნალექი დაიწყება ხვალ საღამოს, გაგრძელდება ხვალ ღამით.": [
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
    "თოვლი (5 ინ.) ღამე.": [
        "sentence",
        ["during", ["parenthetical", "medium-snow", ["inches", 5]], "night"],
    ],
    "მცირე თოვლი (2 სმ.) დღეს დილით.": [
        "sentence",
        [
            "during",
            ["parenthetical", "light-snow", ["centimeters", 2]],
            "later-today-morning",
        ],
    ],
    "ძლიერი თოვლი (8\u201312 ინ.) მთელი დღის განმავლობაში.": [
        "sentence",
        ["for-day", ["parenthetical", "heavy-snow", ["inches", ["range", 8, 12]]]],
    ],
    "თოვლი (< 1 სმ.) შუადღეს.": [
        "sentence",
        [
            "during",
            ["parenthetical", "medium-snow", ["less-than", ["centimeters", 1]]],
            "afternoon",
        ],
    ],
    "უნალექო მთელი კვირის განმავლობაში, ტემპერატურა პიკს აღწევს 85°F ხვალ.": [
        "sentence",
        [
            "with",
            ["for-week", "no-precipitation"],
            ["temperatures-peaking", ["fahrenheit", 85], "tomorrow"],
        ],
    ],
    "ცვალებადი ნალექი შაბათ-კვირას, ტემპერატურა მოიმატებს 32°C ხუთშაბათს.": [
        "sentence",
        [
            "with",
            ["over-weekend", "mixed-precipitation"],
            ["temperatures-rising", ["celsius", 32], "thursday"],
        ],
    ],
    "სუსტი წვიმა ორშაბათს, ტემპერატურა დაიწევს 15°F პარასკევს.": [
        "sentence",
        [
            "with",
            ["during", "very-light-rain", "monday"],
            ["temperatures-valleying", ["fahrenheit", 15], "friday"],
        ],
    ],
    "მცირე თოვლი სამშაბათს და შემდეგ ოთხშაბათს, ტემპერატურა დაეცემა 0°C კვირას.": [
        "sentence",
        [
            "with",
            ["during", "light-snow", ["and", "tuesday", "next-wednesday"]],
            ["temperatures-falling", ["celsius", 0], "sunday"],
        ],
    ],
    "ნალექი დღეს შაბათს, ტემპერატურა პიკს აღწევს 100°F ორშაბათს.": [
        "sentence",
        [
            "with",
            ["during", "medium-precipitation", ["through", "today", "saturday"]],
            ["temperatures-peaking", ["fahrenheit", 100], "monday"],
        ],
    ],
    "ცვალებადი ნალექი (1–3 ინ. თოვლის გარეშე) მთელი დღის განმავლობაში.": [
        "sentence",
        [
            "for-day",
            ["parenthetical", "mixed-precipitation", ["inches", ["range", 1, 3]]],
        ],
    ],
    "ძლიერი თოვლი (1\u20133 ინ.)": [
        "title",
        ["parenthetical", "heavy-snow", ["inches", ["range", 1, 3]]],
    ],
    "ძლიერი თოვლი (3\u20135 სმ.)": [
        "title",
        ["parenthetical", "heavy-snow", ["centimeters", ["range", 3, 5]]],
    ],
    "მოსალოდნელია ჭექა-ქუხილი": ["title", "possible-thunderstorm"],
    "ძლიერი წვიმა და ჭექა-ქუხილი": ["title", ["and", "heavy-rain", "thunderstorm"]],
    "სუსტი წვიმა დაიწყება < 1 წთ.": [
        "sentence",
        ["starting-in", "very-light-rain", ["less-than", ["minutes", 1]]],
    ],
}
