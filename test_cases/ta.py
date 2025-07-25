# This would be one of your translations, as a Python dictionary
cases = {
    "தெளிவு": ["title", "clear"],
    "மிக லேசான நீர்க்கசிவுச் சாத்தியம்": ["title", "possible-very-light-precipitation"],
    "லேசான நீர்க்கசிவு": ["title", "very-light-precipitation"],
    "லேசான நீர்க்கசிவுச் சாத்தியம்": ["title", "possible-light-precipitation"],
    "லேசான நீர்க்கசிவு": ["title", "light-precipitation"],
    "நீர்க்கசிவு": ["title", "medium-precipitation"],
    "பலத்த நீர்க்கசிவு": ["title", "heavy-precipitation"],
    "தூரல் சாத்தியம்": ["title", "possible-very-light-rain"],
    "தூரல்": ["title", "very-light-rain"],
    "லேசான மழைச் சாத்தியம்": ["title", "possible-light-rain"],
    "லேசான மழை": ["title", "light-rain"],
    "மழை": ["title", "medium-rain"],
    "கனத்த மழை": ["title", "heavy-rain"],
    "லேசான ஆலங்கட்டி மழைச் சாத்தியம்": ["title", "possible-very-light-sleet"],
    "லேசான ஆலங்கட்டி மழை": ["title", "very-light-sleet"],
    "லேசான ஆலங்கட்டி மழைச் சாத்தியம்": ["title", "possible-light-sleet"],
    "லேசான ஆலங்கட்டி மழை": ["title", "light-sleet"],
    "ஆலங்கட்டி மழை": ["title", "medium-sleet"],
    "கனத்த ஆலங்கட்டி மழை": ["title", "heavy-sleet"],
    "பனிப்பொழிவுச் சாத்தியம்": ["title", "possible-very-light-snow"],
    "பனிப்பொழிவு": ["title", "very-light-snow"],
    "லேசான பனிச் சாத்தியம்": ["title", "possible-light-snow"],
    "லேசான பனி": ["title", "light-snow"],
    "பனி": ["title", "medium-snow"],
    "கடும் பனி": ["title", "heavy-snow"],
    "வேகக்காற்று": ["title", "medium-wind"],
    "ஆபத்தான வேகக்காற்று": ["title", "heavy-wind"],
    "மூடுபனி": ["title", "fog"],
    "பெரும்பாலும் தெளிவு": ["title", "very-light-clouds"],
    "லேசான மேகமூட்டம்": ["title", "light-clouds"],
    "பெரும்பாலும் மேகமூட்டம்": ["title", "medium-clouds"],
    "மேகம்": ["title", "heavy-clouds"],
    "வறட்சி மற்றும் தென்றல் காற்று": ["title", ["and", "low-humidity", "light-wind"]],
    "தூரல் மற்றும் ஆபத்தான வேகக்காற்று": ["title", ["and", "very-light-rain", "heavy-wind"]],
    "ஈரப்பதம் மற்றும் லேசான மேகமூட்டம்": ["title", ["and", "high-humidity", "light-clouds"]],
    "தெளிவு மணி நேரத்திற்கு": ["sentence", ["for-hour", "clear"]],
    "35 நிமிடங்கள் இல் பனிப்பொழிவு துவக்கம்": [
        "sentence",
        ["starting-in", "very-light-snow", ["minutes", 35]],
    ],
    "15 நிமிடங்கள் இல் லேசான மழை இன் நிறுத்தம்": [
        "sentence",
        ["stopping-in", "light-rain", ["minutes", 15]],
    ],
    "20 நிமிடங்கள் இல் கனத்த ஆலங்கட்டி மழை துவக்கம், பின்னர் 30 நிமிடங்கள் இல் நிறுத்தம்": [
        "sentence",
        [
            "starting-then-stopping-later",
            "heavy-sleet",
            ["minutes", 20],
            ["minutes", 30],
        ],
    ],
    "25 நிமிடங்கள் இல் மழை இன் நிறுத்தம், பின்னர் 8 நிமிடங்கள் இல் மீண்டும் துவக்கம்": [
        "sentence",
        [
            "stopping-then-starting-later",
            "medium-rain",
            ["minutes", 25],
            ["minutes", 8],
        ],
    ],
    "பெரும்பாலும் மேகமூட்டம் நாள் முழுவதும்": ["sentence", ["for-day", "medium-clouds"]],
    "லேசான ஆலங்கட்டி மழை துவக்கம் காலை": [
        "sentence",
        ["starting", "very-light-sleet", "morning"],
    ],
    "வேகக்காற்று லிருந்து இன்றிரவு வரை": [
        "sentence",
        ["until", "medium-wind", "today-night"],
    ],
    "பலத்த நீர்க்கசிவு லிருந்து மதியம் வரை": [
        "sentence",
        ["until", "heavy-precipitation", "afternoon"],
    ],
    "தென்றல் காற்று மதியம் றின் போது": ["sentence", ["during", "light-wind", "afternoon"]],
    "பனி இன்றைய பின்மாலை மற்றும் நாளைக் காலை றின் போது": [
        "sentence",
        ["during", "medium-snow", ["and", "later-today-evening", "tomorrow-morning"]],
    ],
    "கனத்த மழை முதல் பிற்காலைப் பொழுது வரை, மீண்டும் இன்று மாலை இல் துவக்கம்": [
        "sentence",
        ["until-starting-again", "heavy-rain", "later-today-morning", "today-evening"],
    ],
    "மேகம், மாலை வரையிலும், ஒரே இரவில் வரை தொடர்ச்சியாக": [
        "sentence",
        ["starting-continuing-until", "heavy-clouds", "evening", "night"],
    ],
    "லேசான ஆலங்கட்டி மழை இன்று மதியத்திற்குப் பிற்பாடு றின் போது மற்றும் மூடுபனி நாளைக் காலை றின் போது": [
        "sentence",
        [
            "and",
            ["during", "light-sleet", "later-today-afternoon"],
            ["during", "fog", "tomorrow-morning"],
        ],
    ],
    "ஆபத்தான வேகக்காற்று, இக்காலை வரையிலும், இன்று மதியம் வரை தொடர்ச்சியாக மற்றும் ஆலங்கட்டி மழை நாளைக் காலை றின் போது": [
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
    "மேகம் துவக்கம் பின் இரவு மற்றும் கடும் பனி நாளை மதியம் றின் போது": [
        "sentence",
        [
            "and",
            ["starting", "heavy-clouds", "later-today-night"],
            ["during", "heavy-snow", "tomorrow-afternoon"],
        ],
    ],
    "வறட்சி இன்றிரவு றின் போது மற்றும் லேசான நீர்க்கசிவு, நாளை மாலை வரையிலும், நாளை இரவு வரை தொடர்ச்சியாக": [
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
    "பனி(5 இன்ச்) ஒரே இரவில் றின் போது": [
        "sentence",
        ["during", ["parenthetical", "medium-snow", ["inches", 5]], "night"],
    ],
    "லேசான பனி(2 செ.மீ) பிற்காலைப் பொழுது றின் போது": [
        "sentence",
        [
            "during",
            ["parenthetical", "light-snow", ["centimeters", 2]],
            "later-today-morning",
        ],
    ],
    "கடும் பனி(8\u201312 இன்ச்) நாள் முழுவதும்": [
        "sentence",
        ["for-day", ["parenthetical", "heavy-snow", ["inches", ["range", 8, 12]]]],
    ],
    "பனி(1 செ.மீ ற்கு குறைவாக) மதியம் றின் போது": [
        "sentence",
        [
            "during",
            ["parenthetical", "medium-snow", ["less-than", ["centimeters", 1]]],
            "afternoon",
        ],
    ],
    "நீர்க்கசிவு இல்லை வாரம் முழுதும், உயர் வெப்பம் உச்சமாக 85\u00b0F நாளை இல் உடன்": [
        "sentence",
        [
            "with",
            ["for-week", "no-precipitation"],
            ["temperatures-peaking", ["fahrenheit", 85], "tomorrow"],
        ],
    ],
    "கலவையான நீர்க்கசிவு வார இறுதியில், உயர் வெப்பம் 32\u00b0C வியாழன் அன்று ற்கு உயர்கிறது உடன்": [
        "sentence",
        [
            "with",
            ["over-weekend", "mixed-precipitation"],
            ["temperatures-rising", ["celsius", 32], "thursday"],
        ],
    ],
    "தூரல் திங்கள் அன்று றின் போது, உயர் வெப்பம் 15\u00b0F வெள்ளி அன்று இல் வெளியேற்றம் உடன்": [
        "sentence",
        [
            "with",
            ["during", "very-light-rain", "monday"],
            ["temperatures-valleying", ["fahrenheit", 15], "friday"],
        ],
    ],
    "லேசான பனி செவ்வாய் அன்று மற்றும் அடுத்த புதன் றின் போது, உயர் வெப்பம் 0\u00b0C ஞாயிறு அன்று ற்கு வீழ்தல் உடன்": [
        "sentence",
        [
            "with",
            ["during", "light-snow", ["and", "tuesday", "next-wednesday"]],
            ["temperatures-falling", ["celsius", 0], "sunday"],
        ],
    ],
    "நீர்க்கசிவு இன்று, சனி அன்று மூலமாக றின் போது, உயர் வெப்பம் உச்சமாக 100\u00b0F திங்கள் அன்று இல் உடன்": [
        "sentence",
        [
            "with",
            ["during", "medium-precipitation", ["through", "today", "saturday"]],
            ["temperatures-peaking", ["fahrenheit", 100], "monday"],
        ],
    ],
    "கலவையான நீர்க்கசிவு(1\u20133 இன்ச்) நாள் முழுவதும்": [
        "sentence",
        [
            "for-day",
            ["parenthetical", "mixed-precipitation", ["inches", ["range", 1, 3]]],
        ],
    ],
    "கடும் பனி(1\u20133 இன்ச்)": [
        "title",
        ["parenthetical", "heavy-snow", ["inches", ["range", 1, 3]]],
    ],
    "கடும் பனி(3\u20135 செ.மீ)": [
        "title",
        ["parenthetical", "heavy-snow", ["centimeters", ["range", 3, 5]]],
    ],
    "இடிமழைச் சாத்தியம்": ["title", "possible-thunderstorm"],
    "கனத்த மழை மற்றும் இடிமழை": ["title", ["and", "heavy-rain", "thunderstorm"]],
    "1 நிமிடங்கள் ற்கு குறைவாக இல் தூரல் துவக்கம்": [
        "sentence",
        ["starting-in", "very-light-rain", ["less-than", ["minutes", 1]]],
    ],
    "புகை": ["title", "smoke"],
    "புகை நாள் முழுவதும்": ["sentence", ["for-day", "smoke"]],
    "புகை காலை றின் போது": ["sentence", ["during", "smoke", "morning"]],
    "புகை லிருந்து இன்று மாலை வரை": ["sentence", ["until", "smoke", "today-evening"]],
    "புகை மற்றும் லேசான மேகமூட்டம்": ["title", ["and", "smoke", "light-clouds"]],
    "மூடுபனி": ["title", "haze"],
    "மூடுபனி நாள் முழுவதும்": ["sentence", ["for-day", "haze"]],
    "மூடுபனி மதியம் றின் போது": ["sentence", ["during", "haze", "afternoon"]],
    "மூடுபனி மற்றும் ஈரப்பதம்": ["title", ["and", "haze", "high-humidity"]],
    "பனிமூட்டம்": ["title", "mist"],
    "பனிமூட்டம் நாள் முழுவதும்": ["sentence", ["for-day", "mist"]],
    "பனிமூட்டம் ஒரே இரவில் றின் போது": ["sentence", ["during", "mist", "night"]],
    "பனிமூட்டம் மற்றும் மேகம்": ["title", ["and", "mist", "heavy-clouds"]],
}
