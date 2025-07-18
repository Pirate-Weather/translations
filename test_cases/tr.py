# This would be one of your translations, as a Python dictionary
cases = {
    "Açık hava": ["title", "clear"],
    "Çok hafif yağış ihtimali": ["title", "possible-very-light-precipitation"],
    "Çok hafif yağış": ["title", "very-light-precipitation"],
    "Hafif yağış ihtimali": ["title", "possible-light-precipitation"],
    "Hafif yağış": ["title", "light-precipitation"],
    "Yağış": ["title", "medium-precipitation"],
    "Yoğun yağış": ["title", "heavy-precipitation"],
    "Çok hafif yağmur ihtimali": ["title", "possible-very-light-rain"],
    "Çok hafif yağmur": ["title", "very-light-rain"],
    "Hafif yağmur ihtimali": ["title", "possible-light-rain"],
    "Hafif yağmur": ["title", "light-rain"],
    "Yağmur": ["title", "medium-rain"],
    "Yoğun yağmur": ["title", "heavy-rain"],
    "Çok hafif karla karışık yağmur ihtimali": ["title", "possible-very-light-sleet"],
    "Çok hafif karla karışık yağmur": ["title", "very-light-sleet"],
    "Hafif karla karışık yağmur ihtimali": ["title", "possible-light-sleet"],
    "Hafif karla karışık yağmur": ["title", "light-sleet"],
    "Karla karışık yağmur": ["title", "medium-sleet"],
    "Yoğun karla karışık yağmur": ["title", "heavy-sleet"],
    "Çok hafif kar ihtimali": ["title", "possible-very-light-snow"],
    "Çok hafif kar": ["title", "very-light-snow"],
    "Hafif kar ihtimali": ["title", "possible-light-snow"],
    "Hafif kar": ["title", "light-snow"],
    "Kar": ["title", "medium-snow"],
    "Yoğun kar": ["title", "heavy-snow"],
    "Rüzgar": ["title", "medium-wind"],
    "Yoğun rüzgar": ["title", "heavy-wind"],
    "Sis": ["title", "fog"],
    "Çoğunlukla net": ["title", "very-light-clouds"],
    "Hafif bulutlanma": ["title", "light-clouds"],
    "Bulutlanma": ["title", "medium-clouds"],
    "Yoğun bulutlanma": ["title", "heavy-clouds"],
    "Düşük nem ve hafif rüzgar": ["title", ["and", "low-humidity", "light-wind"]],
    "Çok hafif yağmur ve yoğun rüzgar": [
        "title",
        ["and", "very-light-rain", "heavy-wind"],
    ],
    "Yoğun nem ve hafif bulutlanma": [
        "title",
        ["and", "high-humidity", "light-clouds"],
    ],
    " saat boyunca açık hava.": ["sentence", ["for-hour", "clear"]],
    "Çok hafif kar 35 dk. içinde başlayacak.": [
        "sentence",
        ["starting-in", "very-light-snow", ["minutes", 35]],
    ],
    "Hafif yağmur 15 dk. içinde duracak.": [
        "sentence",
        ["stopping-in", "light-rain", ["minutes", 15]],
    ],
    "Yoğun karla karışık yağmur 20 dk. içinde başlayacak, 30 dk. sonra duracak.": [
        "sentence",
        [
            "starting-then-stopping-later",
            "heavy-sleet",
            ["minutes", 20],
            ["minutes", 30],
        ],
    ],
    "Yağmur 25 dk. içinde duracak, 8 dk. sonra tekrar başlayacak.": [
        "sentence",
        [
            "stopping-then-starting-later",
            "medium-rain",
            ["minutes", 25],
            ["minutes", 8],
        ],
    ],
    "Bulutlanma gün boyunca devam edecek.": ["sentence", ["for-day", "medium-clouds"]],
    "Sabah çok hafif karla karışık yağmur başlayacak.": [
        "sentence",
        ["starting", "very-light-sleet", "morning"],
    ],
    "Hafif bulutlanma yarın sabah sona erecek.": [
        "sentence",
        ["until", "light-clouds", "tomorrow-morning"],
    ],
    "Rüzgar bu gece sona erecek.": [
        "sentence",
        ["until", "medium-wind", "today-night"],
    ],
    "Yoğun yağış öğleden sonra sona erecek.": [
        "sentence",
        ["until", "heavy-precipitation", "afternoon"],
    ],
    "Öğleden sonra hafif rüzgar.": ["sentence", ["during", "light-wind", "afternoon"]],
    "Bu akşamdan itibaren ve yarın sabah kar.": [
        "sentence",
        ["during", "medium-snow", ["and", "later-today-evening", "tomorrow-morning"]],
    ],
    "Yoğun yağmur bu sabahtan itibaren sona erecek, bu akşam tekrar başlayacak.": [
        "sentence",
        ["until-starting-again", "heavy-rain", "later-today-morning", "today-evening"],
    ],
    "Çok hafif yağmur bugün öğleden sonra başlayacak, bu akşamdan itibaren sona erecek.": [
        "sentence",
        [
            "starting-continuing-until",
            "very-light-rain",
            "today-afternoon",
            "later-today-evening",
        ],
    ],
    "Hafif yağmur bu akşam başlayacak, yarın sabah sona erecek.": [
        "sentence",
        [
            "starting-continuing-until",
            "light-rain",
            "today-evening",
            "tomorrow-morning",
        ],
    ],
    "Bulutlanma yarın sabah başlayacak, yarın gece sona erecek.": [
        "sentence",
        [
            "starting-continuing-until",
            "medium-clouds",
            "tomorrow-morning",
            "tomorrow-night",
        ],
    ],
    "Yoğun bulutlanma akşam başlayacak, gece sona erecek.": [
        "sentence",
        ["starting-continuing-until", "heavy-clouds", "evening", "night"],
    ],
    "Yoğun rüzgar bu sabah başlayacak, bugün öğleden sonra sona erecek ve yarın sabah karla karışık yağmur.": [
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
    "Bu gece düşük nem ve hafif yağış yarın akşam başlayacak, yarın gece sona erecek.": [
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
    "Bu öğleden sonradan itibaren hafif karla karışık yağmur ve yarın sabah sis.": [
        "sentence",
        [
            "and",
            ["during", "light-sleet", "later-today-afternoon"],
            ["during", "fog", "tomorrow-morning"],
        ],
    ],
    "Bu geceden itibaren yoğun bulutlanma başlayacak ve yarın öğleden sonra yoğun kar.": [
        "sentence",
        [
            "and",
            ["starting", "heavy-clouds", "later-today-night"],
            ["during", "heavy-snow", "tomorrow-afternoon"],
        ],
    ],
    "Gece kar (5 in.).": [
        "sentence",
        ["during", ["parenthetical", "medium-snow", ["inches", 5]], "night"],
    ],
    "Bu sabahtan itibaren hafif kar (2 cm.).": [
        "sentence",
        [
            "during",
            ["parenthetical", "light-snow", ["centimeters", 2]],
            "later-today-morning",
        ],
    ],
    "Yoğun kar (8\u201312 in.) gün boyunca devam edecek.": [
        "sentence",
        ["for-day", ["parenthetical", "heavy-snow", ["inches", ["range", 8, 12]]]],
    ],
    "Öğleden sonra kar (1 cm.'nin altında).": [
        "sentence",
        [
            "during",
            ["parenthetical", "medium-snow", ["less-than", ["centimeters", 1]]],
            "afternoon",
        ],
    ],
    "Hafta boyunca yağış yok, yarın yüksek sıcaklık 85\u00b0F.": [
        "sentence",
        [
            "with",
            ["for-week", "no-precipitation"],
            ["temperatures-peaking", ["fahrenheit", 85], "tomorrow"],
        ],
    ],
    "Hafta sonu karışık yağış, Perşembe sıcaklık 32\u00b0C'ye yükseliyor.": [
        "sentence",
        [
            "with",
            ["over-weekend", "mixed-precipitation"],
            ["temperatures-rising", ["celsius", 32], "thursday"],
        ],
    ],
    "Pazartesi çok hafif yağmur, Cuma hava soğuyor ve sıcaklık 15\u00b0F'ye düşüyor.": [
        "sentence",
        [
            "with",
            ["during", "very-light-rain", "monday"],
            ["temperatures-valleying", ["fahrenheit", 15], "friday"],
        ],
    ],
    "Salı ve Çarşamba hafif kar, Pazar sıcaklık 0\u00b0C'ye düşüyor.": [
        "sentence",
        [
            "with",
            ["during", "light-snow", ["and", "tuesday", "wednesday"]],
            ["temperatures-falling", ["celsius", 0], "sunday"],
        ],
    ],
    "Bugün ile Cumartesi arası yağış, Pazartesi yüksek sıcaklık 100\u00b0F.": [
        "sentence",
        [
            "with",
            ["during", "medium-precipitation", ["through", "today", "saturday"]],
            ["temperatures-peaking", ["fahrenheit", 100], "monday"],
        ],
    ],
    "Karışık yağış (1\u20133 in. kar) gün boyunca devam edecek.": [
        "sentence",
        [
            "for-day",
            ["parenthetical", "mixed-precipitation", ["inches", ["range", 1, 3]]],
        ],
    ],
    "Yoğun kar (1\u20133 in.)": [
        "title",
        ["parenthetical", "heavy-snow", ["inches", ["range", 1, 3]]],
    ],
    "Yoğun kar (3\u20135 cm.)": [
        "title",
        ["parenthetical", "heavy-snow", ["centimeters", ["range", 3, 5]]],
    ],
    "Haftaya Çarşamba'ya kadar yoğun yağmur": [
        "during",
        "heavy-rain",
        "next-wednesday",
    ],
    "Yakındaki tüm radar istasyonlarının çevrimdışı olması nedeniyle sonraki saat tahminleri geçici olarak kullanılamıyor.": [
        "sentence",
        ["next-hour-forecast-status", "temporarily-unavailable", "station-offline"],
    ],
    "Yakındaki tüm radar istasyonlarının kapsama alanı dışında olması nedeniyle sonraki saat tahminleri kısmen kullanılamıyor.": [
        "sentence",
        ["next-hour-forecast-status", "partially-unavailable", "station-incomplete"],
    ],
    "Yakındaki tüm radar istasyonlarının çevrimdışı olması nedeniyle sonraki saat tahminleri kullanılamıyor.": [
        "sentence",
        ["next-hour-forecast-status", "unavailable", "station-offline"],
    ],
    "Duman": ["title", "smoke"],
    "Duman gün boyunca devam edecek.": ["sentence", ["for-day", "smoke"]],
    "Sabah duman.": ["sentence", ["during", "smoke", "morning"]],
    "Duman bu akşam sona erecek.": ["sentence", ["until", "smoke", "today-evening"]],
    "Duman ve hafif bulutlanma": ["title", ["and", "smoke", "light-clouds"]],
    "Pus": ["title", "haze"],
    "Pus gün boyunca devam edecek.": ["sentence", ["for-day", "haze"]],
    "Öğleden sonra pus.": ["sentence", ["during", "haze", "afternoon"]],
    "Pus ve yoğun nem": ["title", ["and", "haze", "high-humidity"]],
    "Sis": ["title", "mist"],
    "Sis gün boyunca devam edecek.": ["sentence", ["for-day", "mist"]],
    "Gece sis.": ["sentence", ["during", "mist", "night"]],
    "Sis ve yoğun bulutlanma": ["title", ["and", "mist", "heavy-clouds"]],
}
