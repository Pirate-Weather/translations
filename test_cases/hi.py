# This would be one of your translations, as a Python dictionary
cases = {
    "साफ़": ["title", "clear"],
    "संभावित हल्की वर्षा": ["title", "possible-very-light-precipitation"],
    "हल्की वर्षा": ["title", "very-light-precipitation"],
    "संभावित हल्की वर्षा": ["title", "possible-light-precipitation"],
    "हल्की वर्षा": ["title", "light-precipitation"],
    "वर्षा": ["title", "medium-precipitation"],
    "भारी वर्षा": ["title", "heavy-precipitation"],
    "संभावित बूंदाबांदी": ["title", "possible-very-light-rain"],
    "बूंदाबांदी": ["title", "very-light-rain"],
    "संभावित हल्की बारिश": ["title", "possible-light-rain"],
    "हल्की बारिश": ["title", "light-rain"],
    "बारिश": ["title", "medium-rain"],
    "भारी बारिश": ["title", "heavy-rain"],
    "संभावित हल्की ओला वृष्टि": ["title", "possible-very-light-sleet"],
    "हल्की ओला वृष्टि": ["title", "very-light-sleet"],
    "संभावित हल्की ओला वृष्टि": ["title", "possible-light-sleet"],
    "हल्की ओला वृष्टि": ["title", "light-sleet"],
    "ओला वृष्टि": ["title", "medium-sleet"],
    "भारी ओला वृष्टि": ["title", "heavy-sleet"],
    "संभावित आंधी": ["title", "possible-very-light-snow"],
    "आंधी": ["title", "very-light-snow"],
    "संभावित हल्की बर्फ़बारी": ["title", "possible-light-snow"],
    "हल्की बर्फ़बारी": ["title", "light-snow"],
    "बर्फ़बारी": ["title", "medium-snow"],
    "भारी बर्फ़बारी": ["title", "heavy-snow"],
    "तेज़ हवाएं": ["title", "medium-wind"],
    "गंभीर रूप से तेज़ हवाएं": ["title", "heavy-wind"],
    "धुंधला": ["title", "fog"],
    "अधिकतर साफ़": ["title", "very-light-clouds"],
    "सामान्य बादल": ["title", "light-clouds"],
    "बादलों से आच्छादित": ["title", "medium-clouds"],
    "मेघयुक्त": ["title", "heavy-clouds"],
    "शुष्क और तूफानी": ["title", ["and", "low-humidity", "light-wind"]],
    "बूंदाबांदी और गंभीर रूप से तेज़ हवाएं": ["title", ["and", "very-light-rain", "heavy-wind"]],
    "आर्द्र और सामान्य बादल": ["title", ["and", "high-humidity", "light-clouds"]],
    "एक घंटे के लिए साफ़": ["sentence", ["for-hour", "clear"]],
    "आंधी 35 मिनट में शुरू हो रहा": [
        "sentence",
        ["starting-in", "very-light-snow", ["minutes", 35]],
    ],
    "हल्की बारिश 15 मिनट में बंद हो रहा": [
        "sentence",
        ["stopping-in", "light-rain", ["minutes", 15]],
    ],
    "भारी ओला वृष्टि 20 मिनट में शुरू हो रहा, बाद में 30 मिनट में बंद हो रहा": [
        "sentence",
        [
            "starting-then-stopping-later",
            "heavy-sleet",
            ["minutes", 20],
            ["minutes", 30],
        ],
    ],
    "बारिश 25 मिनट में बंद हो रहा, बाद में फिर से 8 मिनट पर शुरू हो रहा": [
        "sentence",
        [
            "stopping-then-starting-later",
            "medium-rain",
            ["minutes", 25],
            ["minutes", 8],
        ],
    ],
    "सारे दिन बादलों से आच्छादित": ["sentence", ["for-day", "medium-clouds"]],
    "हल्की ओला वृष्टि सुबह से शुरू": ["sentence", ["starting", "very-light-sleet", "morning"]],
    "तेज़ हवाएं आज रात तक": ["sentence", ["until", "medium-wind", "today-night"]],
    "भारी वर्षा दोपहर तक": ["sentence", ["until", "heavy-precipitation", "afternoon"]],
    "तूफानी दोपहर के दौरान": ["sentence", ["during", "light-wind", "afternoon"]],
    "बर्फ़बारी इस शाम बाद में और कल सुबह के दौरान": [
        "sentence",
        ["during", "medium-snow", ["and", "later-today-evening", "tomorrow-morning"]],
    ],
    "भारी बारिश इस सुबह बाद में तक, इस शाम से दोबारा शुरू": [
        "sentence",
        ["until-starting-again", "heavy-rain", "later-today-morning", "today-evening"],
    ],
    "मेघयुक्त शाम तक, रातोंरात तक जारी": [
        "sentence",
        ["starting-continuing-until", "heavy-clouds", "evening", "night"],
    ],
    "हल्की ओला वृष्टि इस दोपहर बाद में के दौरान और धुंधला कल सुबह के दौरान": [
        "sentence",
        [
            "and",
            ["during", "light-sleet", "later-today-afternoon"],
            ["during", "fog", "tomorrow-morning"],
        ],
    ],
    "गंभीर रूप से तेज़ हवाएं इस सुबह तक, इस दोपहर तक जारी और ओला वृष्टि कल सुबह के दौरान": [
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
    "मेघयुक्त आज रात बाद में से शुरू और भारी बर्फ़बारी कल दोपहर के दौरान": [
        "sentence",
        [
            "and",
            ["starting", "heavy-clouds", "later-today-night"],
            ["during", "heavy-snow", "tomorrow-afternoon"],
        ],
    ],
    "शुष्क आज रात के दौरान और हल्की वर्षा कल शाम तक, कल रात तक जारी": [
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
    "बर्फ़बारी(5 इंच) रातोंरात के दौरान": [
        "sentence",
        ["during", ["parenthetical", "medium-snow", ["inches", 5]], "night"],
    ],
    "हल्की बर्फ़बारी(2 सेंटीमीटर) इस सुबह बाद में के दौरान": [
        "sentence",
        [
            "during",
            ["parenthetical", "light-snow", ["centimeters", 2]],
            "later-today-morning",
        ],
    ],
    "सारे दिन भारी बर्फ़बारी(8\u201312 इंच)": [
        "sentence",
        ["for-day", ["parenthetical", "heavy-snow", ["inches", ["range", 8, 12]]]],
    ],
    "बर्फ़बारी(1 सेंटीमीटर से कम) दोपहर के दौरान": [
        "sentence",
        [
            "during",
            ["parenthetical", "medium-snow", ["less-than", ["centimeters", 1]]],
            "afternoon",
        ],
    ],
    "पूरे सप्ताह में कोई वर्षा नहीं के साथ उच्च तापमान की 85\u00b0F कल पर बढ़ोत्तरी": [
        "sentence",
        [
            "with",
            ["for-week", "no-precipitation"],
            ["temperatures-peaking", ["fahrenheit", 85], "tomorrow"],
        ],
    ],
    "सप्ताहांत में मिश्रित वर्षा के साथ उच्च तापमान की 32\u00b0C गुरुवार को तक बढ़ोत्तरी": [
        "sentence",
        [
            "with",
            ["over-weekend", "mixed-precipitation"],
            ["temperatures-rising", ["celsius", 32], "thursday"],
        ],
    ],
    "बूंदाबांदी सोमवार को के दौरान के साथ उच्च तापमान का 15\u00b0F शुक्रवार को पर अधस्तलन": [
        "sentence",
        [
            "with",
            ["during", "very-light-rain", "monday"],
            ["temperatures-valleying", ["fahrenheit", 15], "friday"],
        ],
    ],
    "हल्की बर्फ़बारी मंगलवार को और अगले बुधवार के दौरान के साथ उच्च तापमान का 0\u00b0C रविवार को तक गिरना": [
        "sentence",
        [
            "with",
            ["during", "light-snow", ["and", "tuesday", "next-wednesday"]],
            ["temperatures-falling", ["celsius", 0], "sunday"],
        ],
    ],
    "वर्षा शनिवार को के माध्यम से आज के दौरान के साथ उच्च तापमान की 100\u00b0F सोमवार को पर बढ़ोत्तरी": [
        "sentence",
        [
            "with",
            ["during", "medium-precipitation", ["through", "today", "saturday"]],
            ["temperatures-peaking", ["fahrenheit", 100], "monday"],
        ],
    ],
    "सारे दिन मिश्रित वर्षा(1\u20133 इंच)": [
        "sentence",
        [
            "for-day",
            ["parenthetical", "mixed-precipitation", ["inches", ["range", 1, 3]]],
        ],
    ],
    "भारी बर्फ़बारी(1\u20133 इंच)": [
        "title",
        ["parenthetical", "heavy-snow", ["inches", ["range", 1, 3]]],
    ],
    "भारी बर्फ़बारी(3\u20135 सेंटीमीटर)": [
        "title",
        ["parenthetical", "heavy-snow", ["centimeters", ["range", 3, 5]]],
    ],
    "संभावित तड़ित वृष्टि": ["title", "possible-thunderstorm"],
    "भारी बारिश और तड़ित वृष्टि": ["title", ["and", "heavy-rain", "thunderstorm"]],
    "बूंदाबांदी 1 मिनट से कम में शुरू हो रहा": [
        "sentence",
        ["starting-in", "very-light-rain", ["less-than", ["minutes", 1]]],
    ],
}
