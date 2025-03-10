# This would be one of your translations, as a Python dictionary
cases = {
    "स्वच्छ": ["title", "clear"],
    "पावसाच्या हलक्या सरींची शक्यता": ["title", "possible-very-light-precipitation"],
    "अत्यल्प पाऊस": ["title", "very-light-precipitation"],
    "अत्यल्प पावसाची शक्यता": ["title", "possible-light-precipitation"],
    "थोडासा पाऊस": ["title", "light-precipitation"],
    "मध्यम पाऊस": ["title", "medium-precipitation"],
    "मुसळधार पाऊस": ["title", "heavy-precipitation"],
    "पावसाच्या हलक्या सरी": ["title", "possible-very-light-rain"],
    "थोड्या प्रमाणात पाऊस": ["title", "very-light-rain"],
    "रिमझिम पावसाची शक्यता": ["title", "possible-light-rain"],
    "रिमझिम पाऊस": ["title", "light-rain"],
    "मध्यम स्वरूपाच्या पावसाची शक्यता": ["title", "medium-rain"],
    "मुसळधार पाऊस": ["title", "heavy-rain"],
    "थोड्या प्रमाणात गारा पडण्याची शक्यता": ["title", "possible-very-light-sleet"],
    "अत्यल्प प्रमाणात गारा पडण्याची शक्यता": ["title", "very-light-sleet"],
    "थोड्या प्रमाणात गारा पडण्याची शक्यता": ["title", "possible-light-sleet"],
    "अल्प स्वरूपाच्या गारपिटीची शक्यता": ["title", "light-sleet"],
    "मध्यम प्रमाणात गारा पडण्याची शक्यता": ["title", "medium-sleet"],
    "गारपीट": ["title", "heavy-sleet"],
    "अत्यल्प हिमवर्षावाची शक्यता": ["title", "possible-very-light-snow"],
    "अल्प हिमवर्षावाची शक्यता": ["title", "very-light-snow"],
    "थोड्याफार प्रमाणात हिमवर्षावाची शक्यता": ["title", "possible-light-snow"],
    "हलक्याशा हिमवर्षावाची शक्यता": ["title", "light-snow"],
    "मध्यम प्रमाणात हिमवर्षाव": ["title", "medium-snow"],
    "मोठ्या प्रमाणात हिमवर्षावाची शक्यता": ["title", "heavy-snow"],
    "मध्यम प्रमाणात वारा": ["title", "medium-wind"],
    "सोसाट्याचा वारा": ["title", "heavy-wind"],
    "धुके": ["title", "fog"],
    "बहुतांशी स्पष्ट": ["title", "very-light-clouds"],
    "अंशतः ढगाळ": ["title", "light-clouds"],
    "मुख्यतः ढगाळ": ["title", "medium-clouds"],
    "ढगाळ": ["title", "heavy-clouds"],
    "कमी आर्द्रता आणि वादळ": ["title", ["and", "low-humidity", "light-wind"]],
    "थोड्या प्रमाणात पाऊस आणि सोसाट्याचा वारा": [
        "title",
        ["and", "very-light-rain", "heavy-wind"],
    ],
    "उच्च आर्द्रता आणि अंशतः ढगाळ": ["title", ["and", "high-humidity", "light-clouds"]],
    "स्वच्छ तासासाठी": ["sentence", ["for-hour", "clear"]],
    "अल्प हिमवर्षावाची शक्यता 35 मिनट चालू होत आहे": [
        "sentence",
        ["starting-in", "very-light-snow", ["minutes", 35]],
    ],
    "रिमझिम पाऊस 15 मिनट बंद होत आहे": [
        "sentence",
        ["stopping-in", "light-rain", ["minutes", 15]],
    ],
    "गारपीट 20 मिनट सुरु होईल त्यानंतर बंद 30 मिनट नंतर": [
        "sentence",
        [
            "starting-then-stopping-later",
            "heavy-sleet",
            ["minutes", 20],
            ["minutes", 30],
        ],
    ],
    "मध्यम स्वरूपाच्या पावसाची शक्यता 25 मिनट बंद होईल त्यानंतर चालू 8 मिनट नंतर": [
        "sentence",
        [
            "stopping-then-starting-later",
            "medium-rain",
            ["minutes", 25],
            ["minutes", 8],
        ],
    ],
    "मुख्यतः ढगाळ दिवसासाठी": ["sentence", ["for-day", "medium-clouds"]],
    "अत्यल्प प्रमाणात गारा पडण्याची शक्यता सुरु सकाळी": [
        "sentence",
        ["starting", "very-light-sleet", "morning"],
    ],
    "मध्यम प्रमाणात वारा पर्यंत आज रात्री": [
        "sentence",
        ["until", "medium-wind", "today-night"],
    ],
    "मुसळधार पाऊस पर्यंत दुपारी": [
        "sentence",
        ["until", "heavy-precipitation", "afternoon"],
    ],
    "दरम्यान वादळ दुपारी": ["sentence", ["during", "light-wind", "afternoon"]],
    "दरम्यान मध्यम प्रमाणात हिमवर्षाव आज संध्याकाळ नंतर आणि उद्या सकाळी": [
        "sentence",
        ["during", "medium-snow", ["and", "later-today-evening", "tomorrow-morning"]],
    ],
    "मुसळधार पाऊस आज सकाळ नंतर पुन्हा चालू होई पर्यंत आज संध्याकाळी": [
        "sentence",
        ["until-starting-again", "heavy-rain", "later-today-morning", "today-evening"],
    ],
    "ढगाळ संध्याकाळी पर्यंत सुरू पुढे होईपर्यंत रात्री": [
        "sentence",
        ["starting-continuing-until", "heavy-clouds", "evening", "night"],
    ],
    "दरम्यान अल्प स्वरूपाच्या गारपिटीची शक्यता आज दुपार नंतर आणि दरम्यान धुके उद्या सकाळी": [
        "sentence",
        [
            "and",
            ["during", "light-sleet", "later-today-afternoon"],
            ["during", "fog", "tomorrow-morning"],
        ],
    ],
    "सोसाट्याचा वारा आज सकाळी पर्यंत सुरू पुढे होईपर्यंत आज दुपारी आणि दरम्यान मध्यम प्रमाणात गारा पडण्याची शक्यता उद्या सकाळी": [
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
    "ढगाळ सुरु आज रात्री नंतर आणि दरम्यान मोठ्या प्रमाणात हिमवर्षावाची शक्यता उद्या दुपारी": [
        "sentence",
        [
            "and",
            ["starting", "heavy-clouds", "later-today-night"],
            ["during", "heavy-snow", "tomorrow-afternoon"],
        ],
    ],
    "दरम्यान कमी आर्द्रता आज रात्री आणि थोडासा पाऊस उद्या संध्याकाळी पर्यंत सुरू पुढे होईपर्यंत उद्या रात्री": [
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
    "दरम्यान मध्यम प्रमाणात हिमवर्षाव (5 इंच) रात्री": [
        "sentence",
        ["during", ["parenthetical", "medium-snow", ["inches", 5]], "night"],
    ],
    "दरम्यान हलक्याशा हिमवर्षावाची शक्यता (2 सेंटीमीटर) आज सकाळ नंतर": [
        "sentence",
        [
            "during",
            ["parenthetical", "light-snow", ["centimeters", 2]],
            "later-today-morning",
        ],
    ],
    "मोठ्या प्रमाणात हिमवर्षावाची शक्यता (8\u201312 इंच) दिवसासाठी": [
        "sentence",
        ["for-day", ["parenthetical", "heavy-snow", ["inches", ["range", 8, 12]]]],
    ],
    "दरम्यान मध्यम प्रमाणात हिमवर्षाव (1 सेंटीमीटर पेक्षा कमी) दुपारी": [
        "sentence",
        [
            "during",
            ["parenthetical", "medium-snow", ["less-than", ["centimeters", 1]]],
            "afternoon",
        ],
    ],
    "पाऊस नाही आठवड्यासाठी च्या बरोबर तापमान मोठ्या प्रमाणात वाढत आहे 85\u00b0F उद्या": [
        "sentence",
        [
            "with",
            ["for-week", "no-precipitation"],
            ["temperatures-peaking", ["fahrenheit", 85], "tomorrow"],
        ],
    ],
    "मिश्र पर्जन्य आठवड्याचा शेवटी च्या बरोबर तापमान 32\u00b0C गुरुवारी प्रमाणात वाढत आहे": [
        "sentence",
        [
            "with",
            ["over-weekend", "mixed-precipitation"],
            ["temperatures-rising", ["celsius", 32], "thursday"],
        ],
    ],
    "दरम्यान थोड्या प्रमाणात पाऊस सोमवारी च्या बरोबर तापमान 15\u00b0F शुक्रवारी मोठ्या प्रमाणात कमी होत आहे": [
        "sentence",
        [
            "with",
            ["during", "very-light-rain", "monday"],
            ["temperatures-valleying", ["fahrenheit", 15], "friday"],
        ],
    ],
    "दरम्यान हलक्याशा हिमवर्षावाची शक्यता मंगळवारी आणि पुढच्या बुधवारी च्या बरोबर तापमान 0\u00b0C रविवारी कमी होत आहे": [
        "sentence",
        [
            "with",
            ["during", "light-snow", ["and", "tuesday", "next-wednesday"]],
            ["temperatures-falling", ["celsius", 0], "sunday"],
        ],
    ],
    "दरम्यान मध्यम पाऊस आज, माध्यमातून शनिवारी च्या बरोबर तापमान मोठ्या प्रमाणात वाढत आहे 100\u00b0F सोमवारी": [
        "sentence",
        [
            "with",
            ["during", "medium-precipitation", ["through", "today", "saturday"]],
            ["temperatures-peaking", ["fahrenheit", 100], "monday"],
        ],
    ],
    "मिश्र पर्जन्य (1\u20133 इंच) दिवसासाठी": [
        "sentence",
        [
            "for-day",
            ["parenthetical", "mixed-precipitation", ["inches", ["range", 1, 3]]],
        ],
    ],
    "मोठ्या प्रमाणात हिमवर्षावाची शक्यता (1\u20133 इंच)": [
        "title",
        ["parenthetical", "heavy-snow", ["inches", ["range", 1, 3]]],
    ],
    "मोठ्या प्रमाणात हिमवर्षावाची शक्यता (3\u20135 सेंटीमीटर)": [
        "title",
        ["parenthetical", "heavy-snow", ["centimeters", ["range", 3, 5]]],
    ],
    "गडगडाटी वादळाची शक्यता": ["title", "possible-thunderstorm"],
    "मुसळधार पाऊस आणि गडगडाटी वादळ": ["title", ["and", "heavy-rain", "thunderstorm"]],
    "थोड्या प्रमाणात पाऊस 1 मिनट पेक्षा कमी चालू होत आहे": [
        "sentence",
        ["starting-in", "very-light-rain", ["less-than", ["minutes", 1]]],
    ],
}
