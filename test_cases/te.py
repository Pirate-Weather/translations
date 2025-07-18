# This would be one of your translations, as a Python dictionary
cases = {
    "స్పష్టమైన": ["title", "clear"],
    "సంభవించే తేలికపాటి వర్షపాతం": ["title", "possible-very-light-precipitation"],
    "తేలికపాటి వర్షపాతం": ["title", "very-light-precipitation"],
    "కాగల తేలికపాటి వర్షపాతం": ["title", "possible-light-precipitation"],
    "తేలికపాటి వర్షపాతం": ["title", "light-precipitation"],
    "వర్షపాతం": ["title", "medium-precipitation"],
    "భారీగ వచ్చే వర్షపాతం": ["title", "heavy-precipitation"],
    "కాగల చినుకులు": ["title", "possible-very-light-rain"],
    "చినుకులు": ["title", "very-light-rain"],
    "తేలికపాటి వర్షం": ["title", "possible-light-rain"],
    "తేలికపాటి వర్షం": ["title", "light-rain"],
    "వర్షం": ["title", "medium-rain"],
    "భారీవర్షం": ["title", "heavy-rain"],
    "కాగల తేలికపాటి వడగండ్లవాన": ["title", "possible-very-light-sleet"],
    "తేలికపాటి వడగండ్లవాన": ["title", "very-light-sleet"],
    "కాగల తేలికపాటి వడగండ్లవాన": ["title", "possible-light-sleet"],
    "తేలికపాటి వడగండ్లవాన": ["title", "light-sleet"],
    "వడగండ్లవాన": ["title", "medium-sleet"],
    "భారీగ వచ్చే వడగండ్లవాన": ["title", "heavy-sleet"],
    "రాబోయే సుడిగాలి": ["title", "possible-very-light-snow"],
    "సుడిగాలి": ["title", "very-light-snow"],
    "అయ్యే తేలికపాటి మంచు": ["title", "possible-light-snow"],
    "తేలికపాటి మంచు": ["title", "light-snow"],
    "మంచు": ["title", "medium-snow"],
    "భారీ మంచు": ["title", "heavy-snow"],
    "గాలులతో": ["title", "medium-wind"],
    "ప్రమాదకరమైన గాలులతో": ["title", "heavy-wind"],
    "పొగమంచు": ["title", "fog"],
    "చాలావరకు స్పష్టమైన": ["title", "very-light-clouds"],
    "పాక్షికంగా మేఘావృతం": ["title", "light-clouds"],
    "చాలావరకు మేఘావృతంగా": ["title", "medium-clouds"],
    "మబ్బులతో": ["title", "heavy-clouds"],
    "పొడి మరియు గాలులతో": ["title", ["and", "low-humidity", "light-wind"]],
    "చినుకులు మరియు ప్రమాదకరమైన గాలులతో": ["title", ["and", "very-light-rain", "heavy-wind"]],
    "ఆర్ద్ర మరియు పాక్షికంగా మేఘావృతం": ["title", ["and", "high-humidity", "light-clouds"]],
    "ఒక గంట కు స్పష్టమైన": ["sentence", ["for-hour", "clear"]],
    "35 నిమిషం లో మొదలయ్యే సుడిగాలి": [
        "sentence",
        ["starting-in", "very-light-snow", ["minutes", 35]],
    ],
    "15 నిమిషం లో తేలికపాటి వర్షం ఆగిపోవటం": [
        "sentence",
        ["stopping-in", "light-rain", ["minutes", 15]],
    ],
    "20 నిమిషం లో మొదలయ్యే భారీగ వచ్చే వడగండ్లవాన, తర్వాత 30 నిమిషం ని ఆపింది": [
        "sentence",
        [
            "starting-then-stopping-later",
            "heavy-sleet",
            ["minutes", 20],
            ["minutes", 30],
        ],
    ],
    "25 నిమిషం లో వర్షం ఆగిపోయిన తరువాత 8 నిమిషం లో మళ్లీ ప్రారంభించబడుతుంది": [
        "sentence",
        [
            "stopping-then-starting-later",
            "medium-rain",
            ["minutes", 25],
            ["minutes", 8],
        ],
    ],
    "రోజు మొత్తం చాలావరకు మేఘావృతంగా గానే ఉంటుంది": ["sentence", ["for-day", "medium-clouds"]],
    "ఉదయం మొదలయ్యే తేలికపాటి వడగండ్లవాన": [
        "sentence",
        ["starting", "very-light-sleet", "morning"],
    ],
    "ఈ రాత్రి వచ్చే వరుకు గాలులతో": ["sentence", ["until", "medium-wind", "today-night"]],
    "మధ్యాహ్నం వచ్చే వరుకు భారీగ వచ్చే వర్షపాతం": [
        "sentence",
        ["until", "heavy-precipitation", "afternoon"],
    ],
    "గాలులతో మధ్యాహ్నం అప్పుడు": ["sentence", ["during", "light-wind", "afternoon"]],
    "మంచు ఈ సాయంత్రం తరువాత మరియు రేపు ప్రొద్దున అప్పుడు": [
        "sentence",
        ["during", "medium-snow", ["and", "later-today-evening", "tomorrow-morning"]],
    ],
    "ఈ ఉదయం తరువాత వచ్చే వరుకు భారీవర్షం, మళ్ళీ ఈ సాయంత్రం నుండి మొదలుఅవుతుంది": [
        "sentence",
        ["until-starting-again", "heavy-rain", "later-today-morning", "today-evening"],
    ],
    "సాయంత్రం వచ్చే వరుకు మబ్బులతో, మళ్ళీ రాత్రిపూట వచ్చే అంత వరుకు కొనసాగుతుంది": [
        "sentence",
        ["starting-continuing-until", "heavy-clouds", "evening", "night"],
    ],
    "తేలికపాటి వడగండ్లవాన ఈ మధ్యాహ్నం తరువాత అప్పుడు మరియు పొగమంచు రేపు ప్రొద్దున అప్పుడు": [
        "sentence",
        [
            "and",
            ["during", "light-sleet", "later-today-afternoon"],
            ["during", "fog", "tomorrow-morning"],
        ],
    ],
    "ఈ ఉదయం వచ్చే వరుకు ప్రమాదకరమైన గాలులతో, మళ్ళీ ఈ మధ్యాహ్నం వచ్చే అంత వరుకు కొనసాగుతుంది మరియు వడగండ్లవాన రేపు ప్రొద్దున అప్పుడు": [
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
    "ఈ రాత్రి తరువాత మొదలయ్యే మబ్బులతో మరియు భారీ మంచు రేపు మధ్యాహ్నము అప్పుడు": [
        "sentence",
        [
            "and",
            ["starting", "heavy-clouds", "later-today-night"],
            ["during", "heavy-snow", "tomorrow-afternoon"],
        ],
    ],
    "పొడి ఈ రాత్రి అప్పుడు మరియు రేపు సాయంత్రం వచ్చే వరుకు తేలికపాటి వర్షపాతం, మళ్ళీ రేపు రాత్రి వచ్చే అంత వరుకు కొనసాగుతుంది": [
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
    "మంచు(5 ఇంచ్) రాత్రిపూట అప్పుడు": [
        "sentence",
        ["during", ["parenthetical", "medium-snow", ["inches", 5]], "night"],
    ],
    "తేలికపాటి మంచు(2 సెంటీమీటర్) ఈ ఉదయం తరువాత అప్పుడు": [
        "sentence",
        [
            "during",
            ["parenthetical", "light-snow", ["centimeters", 2]],
            "later-today-morning",
        ],
    ],
    "రోజు మొత్తం భారీ మంచు(8\u201312 ఇంచ్) గానే ఉంటుంది": [
        "sentence",
        ["for-day", ["parenthetical", "heavy-snow", ["inches", ["range", 8, 12]]]],
    ],
    "మంచు(< 1 సెంటీమీటర్) మధ్యాహ్నం అప్పుడు": [
        "sentence",
        [
            "during",
            ["parenthetical", "medium-snow", ["less-than", ["centimeters", 1]]],
            "afternoon",
        ],
    ],
    "వారమంతా వర్షపాతం లేదు తో అధిక ఉష్ణోగ్రతలు 85\u00b0F రేపు వద్ద పెరిగాయి": [
        "sentence",
        [
            "with",
            ["for-week", "no-precipitation"],
            ["temperatures-peaking", ["fahrenheit", 85], "tomorrow"],
        ],
    ],
    "వారాంతంలో మిశ్రమ వర్షపాతం తో అధిక ఉష్ణోగ్రతలు 32\u00b0C గురువారం నాడు కు పెరుగుతున్నాయి": [
        "sentence",
        [
            "with",
            ["over-weekend", "mixed-precipitation"],
            ["temperatures-rising", ["celsius", 32], "thursday"],
        ],
    ],
    "చినుకులు సోమవారం నాడు అప్పుడు తో అధిక ఉష్ణోగ్రతలు 15\u00b0F శుక్రవారం నాడు వద్ద నిలిచిపోయాయి": [
        "sentence",
        [
            "with",
            ["during", "very-light-rain", "monday"],
            ["temperatures-valleying", ["fahrenheit", 15], "friday"],
        ],
    ],
    "తేలికపాటి మంచు మంగళవారం నాడు మరియు వచ్చే బుధవారం అప్పుడు తో అధిక ఉష్ణోగ్రతలు 0\u00b0C ఆదివారం నాడు కు పడిపోతాయి": [
        "sentence",
        [
            "with",
            ["during", "light-snow", ["and", "tuesday", "next-wednesday"]],
            ["temperatures-falling", ["celsius", 0], "sunday"],
        ],
    ],
    "వర్షపాతం శనివారము నాడు ద్వారా నేడు అప్పుడు తో అధిక ఉష్ణోగ్రతలు 100\u00b0F సోమవారం నాడు వద్ద పెరిగాయి": [
        "sentence",
        [
            "with",
            ["during", "medium-precipitation", ["through", "today", "saturday"]],
            ["temperatures-peaking", ["fahrenheit", 100], "monday"],
        ],
    ],
    "రోజు మొత్తం మిశ్రమ వర్షపాతం(1\u20133 ఇంచ్) గానే ఉంటుంది": [
        "sentence",
        [
            "for-day",
            ["parenthetical", "mixed-precipitation", ["inches", ["range", 1, 3]]],
        ],
    ],
    "భారీ మంచు(1\u20133 ఇంచ్)": [
        "title",
        ["parenthetical", "heavy-snow", ["inches", ["range", 1, 3]]],
    ],
    "భారీ మంచు(3\u20135 సెంటీమీటర్)": [
        "title",
        ["parenthetical", "heavy-snow", ["centimeters", ["range", 3, 5]]],
    ],
    "రాబోయే ఉరుములతో కూడిన తుఫాను": ["title", "possible-thunderstorm"],
    "భారీవర్షం మరియు ఉరుములతో కూడిన తుఫాను": ["title", ["and", "heavy-rain", "thunderstorm"]],
    "< 1 నిమిషం లో మొదలయ్యే చినుకులు": [
        "sentence",
        ["starting-in", "very-light-rain", ["less-than", ["minutes", 1]]],
    ],
    "పొగ": ["title", "smoke"],
    "రోజు మొత్తం పొగ గానే ఉంటుంది": ["sentence", ["for-day", "smoke"]],
    "పొగ ఉదయం అప్పుడు": ["sentence", ["during", "smoke", "morning"]],
    "ఈ సాయంత్రం వచ్చే వరుకు పొగ": ["sentence", ["until", "smoke", "today-evening"]],
    "పొగ మరియు పాక్షికంగా మేఘావృతం": ["title", ["and", "smoke", "light-clouds"]],
    "పొగమంచు": ["title", "haze"],
    "రోజు మొత్తం పొగమంచు గానే ఉంటుంది": ["sentence", ["for-day", "haze"]],
    "పొగమంచు మధ్యాహ్నం అప్పుడు": ["sentence", ["during", "haze", "afternoon"]],
    "పొగమంచు మరియు ఆర్ద్ర": ["title", ["and", "haze", "high-humidity"]],
    "పొగమంచు రాత్రిపూట అప్పుడు": ["sentence", ["during", "mist", "night"]],
    "పొగమంచు మరియు మబ్బులతో": ["title", ["and", "mist", "heavy-clouds"]],
}
