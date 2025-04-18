# This would be one of your translations, as a Python dictionary
cases = {
    "Cerah": ["title", "clear"],
    "Kemungkinan Hujan Ringan": ["title", "possible-very-light-precipitation"],
    "Hujan Ringan": ["title", "very-light-precipitation"],
    "Kemungkinan Hujan Ringan": ["title", "possible-light-precipitation"],
    "Hujan Ringan": ["title", "light-precipitation"],
    "Hujan": ["title", "medium-precipitation"],
    "Hujan Lebat": ["title", "heavy-precipitation"],
    "Kemungkinan Hujan Ringan": ["title", "possible-very-light-rain"],
    "Hujan Ringan": ["title", "very-light-rain"],
    "Kemungkinan Hujan Ringan": ["title", "possible-light-rain"],
    "Hujan Ringan": ["title", "light-rain"],
    "Hujan": ["title", "medium-rain"],
    "Hujan Lebat": ["title", "heavy-rain"],
    "Kemungkinan Hujan Salju Ringan": ["title", "possible-very-light-sleet"],
    "Hujan Salju Ringan": ["title", "very-light-sleet"],
    "Kemungkinan Hujan Salju Ringan": ["title", "possible-light-sleet"],
    "Hujan Salju Ringan": ["title", "light-sleet"],
    "Hujan Salju": ["title", "medium-sleet"],
    "Hujan Salju Lebat": ["title", "heavy-sleet"],
    "Kemungkinan Salju Ringan": ["title", "possible-very-light-snow"],
    "Salju Ringan": ["title", "very-light-snow"],
    "Kemungkinan Salju Ringan": ["title", "possible-light-snow"],
    "Salju Ringan": ["title", "light-snow"],
    "Salju": ["title", "medium-snow"],
    "Salju Besar": ["title", "heavy-snow"],
    "Berangin": ["title", "medium-wind"],
    "Berangin Besar": ["title", "heavy-wind"],
    "Berkabut": ["title", "fog"],
    "Sebagian Besar Cerah": ["title", "very-light-clouds"],
    "Sedikit Berawan": ["title", "light-clouds"],
    "Berawan": ["title", "medium-clouds"],
    "Berawan Besar": ["title", "heavy-clouds"],
    "Kering Dan Berangin Ringan": ["title", ["and", "low-humidity", "light-wind"]],
    "Hujan Ringan Dan Berangin Besar": [
        "title",
        ["and", "very-light-rain", "heavy-wind"],
    ],
    "Lembab Dan Sedikit Berawan": ["title", ["and", "high-humidity", "light-clouds"]],
    "Cerah pada jam.": ["sentence", ["for-hour", "clear"]],
    "Salju ringan mulai pada 35 min.": [
        "sentence",
        ["starting-in", "very-light-snow", ["minutes", 35]],
    ],
    "Hujan ringan berhenti pada 15 min.": [
        "sentence",
        ["stopping-in", "light-rain", ["minutes", 15]],
    ],
    "Hujan salju lebat mulai pada 20 min., berhenti 30 min. nanti.": [
        "sentence",
        [
            "starting-then-stopping-later",
            "heavy-sleet",
            ["minutes", 20],
            ["minutes", 30],
        ],
    ],
    "Hujan berhenti pada 25 min., berhenti lagi 8 min. nanti.": [
        "sentence",
        [
            "stopping-then-starting-later",
            "medium-rain",
            ["minutes", 25],
            ["minutes", 8],
        ],
    ],
    "Berawan selama sehari.": ["sentence", ["for-day", "medium-clouds"]],
    "Hujan salju ringan mulai pada pagi hari.": [
        "sentence",
        ["starting", "very-light-sleet", "morning"],
    ],
    "Berangin sampai malam ini.": ["sentence", ["until", "medium-wind", "today-night"]],
    "Hujan lebat sampai pada sore hari.": [
        "sentence",
        ["until", "heavy-precipitation", "afternoon"],
    ],
    "Berangin ringan pada sore hari.": [
        "sentence",
        ["during", "light-wind", "afternoon"],
    ],
    "Salju nanti malam ini dan besok pagi.": [
        "sentence",
        ["during", "medium-snow", ["and", "later-today-evening", "tomorrow-morning"]],
    ],
    "Hujan lebat sampai nanti pagi ini, mulai kembali malam ini.": [
        "sentence",
        ["until-starting-again", "heavy-rain", "later-today-morning", "today-evening"],
    ],
    "Berawan besar mulai pada malam hari, berlanjut sampai tengah malam.": [
        "sentence",
        ["starting-continuing-until", "heavy-clouds", "evening", "night"],
    ],
    "Hujan salju ringan nanti sore ini dan berkabut besok pagi.": [
        "sentence",
        [
            "and",
            ["during", "light-sleet", "later-today-afternoon"],
            ["during", "fog", "tomorrow-morning"],
        ],
    ],
    "Berangin besar mulai pagi ini, berlanjut sampai sore ini, dan hujan salju besok pagi.": [
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
    "Berawan besar mulai nanti malam ini dan salju besar besok sore.": [
        "sentence",
        [
            "and",
            ["starting", "heavy-clouds", "later-today-night"],
            ["during", "heavy-snow", "tomorrow-afternoon"],
        ],
    ],
    "Kering malam ini dan hujan ringan mulai besok malam, berlanjut sampai besok tengah malam.": [
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
    "Salju (5 in.) tengah malam.": [
        "sentence",
        ["during", ["parenthetical", "medium-snow", ["inches", 5]], "night"],
    ],
    "Salju ringan (2 cm.) nanti pagi ini.": [
        "sentence",
        [
            "during",
            ["parenthetical", "light-snow", ["centimeters", 2]],
            "later-today-morning",
        ],
    ],
    "Salju besar (8\u201312 in.) selama sehari.": [
        "sentence",
        ["for-day", ["parenthetical", "heavy-snow", ["inches", ["range", 8, 12]]]],
    ],
    "Salju (dibawah 1 cm.) pada sore hari.": [
        "sentence",
        [
            "during",
            ["parenthetical", "medium-snow", ["less-than", ["centimeters", 1]]],
            "afternoon",
        ],
    ],
    "Tidak hujan selama seminggu, dengan suhu memuncak pada 85\u00b0F besok.": [
        "sentence",
        [
            "with",
            ["for-week", "no-precipitation"],
            ["temperatures-peaking", ["fahrenheit", 85], "tomorrow"],
        ],
    ],
    "Hujan ringan selama akhir minggu, dengan suhu naik ke 32\u00b0C pada hari Kamis.": [
        "sentence",
        [
            "with",
            ["over-weekend", "mixed-precipitation"],
            ["temperatures-rising", ["celsius", 32], "thursday"],
        ],
    ],
    "Hujan ringan pada hari Senin, dengan suhu menurun pada 15\u00b0F pada hari Jum'at.": [
        "sentence",
        [
            "with",
            ["during", "very-light-rain", "monday"],
            ["temperatures-valleying", ["fahrenheit", 15], "friday"],
        ],
    ],
    "Salju ringan pada hari Selasa dan Rabu, dengan suhu turun pada 0\u00b0C pada hari Minggu.": [
        "sentence",
        [
            "with",
            ["during", "light-snow", ["and", "tuesday", "wednesday"]],
            ["temperatures-falling", ["celsius", 0], "sunday"],
        ],
    ],
    "Hujan hari ini melalui pada hari Sabtu, dengan suhu memuncak pada 100\u00b0F pada hari Senin.": [
        "sentence",
        [
            "with",
            ["during", "medium-precipitation", ["through", "today", "saturday"]],
            ["temperatures-peaking", ["fahrenheit", 100], "monday"],
        ],
    ],
    "Hujan ringan (1\u20133 in. oleh salju) selama sehari.": [
        "sentence",
        [
            "for-day",
            ["parenthetical", "mixed-precipitation", ["inches", ["range", 1, 3]]],
        ],
    ],
    "Salju Besar (1\u20133 in.)": [
        "title",
        ["parenthetical", "heavy-snow", ["inches", ["range", 1, 3]]],
    ],
    "Kemungkinan Badai": ["title", "possible-thunderstorm"],
    "Salju Besar (3\u20135 cm.)": [
        "title",
        ["parenthetical", "heavy-snow", ["centimeters", ["range", 3, 5]]],
    ],
}
