# This would be one of your translations, as a Python dictionary
cases = {
    "വ്യക്തമായ": ["title", "clear"],
    "സാധ്യമായ നേരിയ വര്‍ഷപാതം": ["title", "possible-very-light-precipitation"],
    "നേരിയ വര്‍ഷപാതം": ["title", "very-light-precipitation"],
    "സാധ്യമായ നേരിയ വര്‍ഷപാതം": ["title", "possible-light-precipitation"],
    "നേരിയ വര്‍ഷപാതം": ["title", "light-precipitation"],
    "വര്‍ഷപാതം": ["title", "medium-precipitation"],
    "ശക്തിയേറിയ വര്‍ഷപാതം": ["title", "heavy-precipitation"],
    "സാധ്യമായ ചാറ്റല്‍മഴ": ["title", "possible-very-light-rain"],
    "ചാറ്റല്‍മഴ": ["title", "very-light-rain"],
    "സാധ്യമായ നേരിയ മഴ": ["title", "possible-light-rain"],
    "നേരിയ മഴ": ["title", "light-rain"],
    "മഴ": ["title", "medium-rain"],
    "ശക്തിയേറിയ മഴ": ["title", "heavy-rain"],
    "സാധ്യമായ നേരിയ ഹിമവര്‍ഷം": ["title", "possible-very-light-sleet"],
    "നേരിയ ഹിമവര്‍ഷം": ["title", "very-light-sleet"],
    "സാധ്യമായ നേരിയ ഹിമവര്‍ഷം": ["title", "possible-light-sleet"],
    "നേരിയ ഹിമവര്‍ഷം": ["title", "light-sleet"],
    "ഹിമവര്‍ഷം": ["title", "medium-sleet"],
    "ശക്തിയേറിയ ഹിമവര്‍ഷം": ["title", "heavy-sleet"],
    "സാധ്യമായ കാറ്റും മഴയും": ["title", "possible-very-light-snow"],
    "കാറ്റും മഴയും": ["title", "very-light-snow"],
    "സാധ്യമായ നേരിയ മഞ്ഞ്": ["title", "possible-light-snow"],
    "നേരിയ മഞ്ഞ്": ["title", "light-snow"],
    "മഞ്ഞ്": ["title", "medium-snow"],
    "കനത്ത മഞ്ഞ്": ["title", "heavy-snow"],
    "ശീതളമായ": ["title", "medium-wind"],
    "അപകടകരമായ കാറ്റ്": ["title", "heavy-wind"],
    "മൂടല്‍മഞ്ഞ്(മൂടിക്കെട്ടിയ)": ["title", "fog"],
    "മിക്കവാറും വ്യക്തമാണ്": ["title", "very-light-clouds"],
    "ഭാഗീകമായി മേഘാവൃതം": ["title", "light-clouds"],
    "മിക്കപ്പോഴും മേഘാവൃതമായ": ["title", "medium-clouds"],
    "മഴക്കാര്‍ മൂടിയ": ["title", "heavy-clouds"],
    "വരണ്ട ഉം കാറ്റ് ഉം": ["title", ["and", "low-humidity", "light-wind"]],
    "ചാറ്റല്‍മഴ ഉം അപകടകരമായ കാറ്റ് ഉം": ["title", ["and", "very-light-rain", "heavy-wind"]],
    "ഈര്‍പ്പം ഉം ഭാഗീകമായി മേഘാവൃതം ഉം": ["title", ["and", "high-humidity", "light-clouds"]],
    "മണിക്കൂറിനു വ്യക്തമായ": ["sentence", ["for-hour", "clear"]],
    "കാറ്റും മഴയും 35 മിനിട്ടു ഇല്‍ ആരംഭിക്കുന്നു": [
        "sentence",
        ["starting-in", "very-light-snow", ["minutes", 35]],
    ],
    "നേരിയ മഴ 15 മിനിട്ടു ഇല്‍ അവസാനിക്കുന്നു": [
        "sentence",
        ["stopping-in", "light-rain", ["minutes", 15]],
    ],
    "ശക്തിയേറിയ ഹിമവര്‍ഷം 20 മിനിട്ടു ഇല്‍ ആരംഭിക്കുന്നു, പിന്നീട് 30 മിനിട്ടു ഇല്‍ അവസാനിക്കുന്നു": [
        "sentence",
        [
            "starting-then-stopping-later",
            "heavy-sleet",
            ["minutes", 20],
            ["minutes", 30],
        ],
    ],
    "മഴ 25 മിനിട്ടു ഇല്‍ അവസാനിക്കുന്നു, പിന്നീട് 8 മിനിട്ടു ഇല്‍ വീണ്ടും ആരംഭിക്കുന്നു": [
        "sentence",
        [
            "stopping-then-starting-later",
            "medium-rain",
            ["minutes", 25],
            ["minutes", 8],
        ],
    ],
    "മിക്കപ്പോഴും മേഘാവൃതമായ ദിവസം മുഴുവന്‍": ["sentence", ["for-day", "medium-clouds"]],
    "നേരിയ ഹിമവര്‍ഷം പ്രാഭാതം ആരംഭിക്കുന്നു": [
        "sentence",
        ["starting", "very-light-sleet", "morning"],
    ],
    "ശീതളമായ ഇന്നു രാത്രി വരെ": ["sentence", ["until", "medium-wind", "today-night"]],
    "ശക്തിയേറിയ വര്‍ഷപാതം അപരാഹ്നം വരെ": [
        "sentence",
        ["until", "heavy-precipitation", "afternoon"],
    ],
    "കാറ്റ് അപരാഹ്നം കാലത്തില്‍": ["sentence", ["during", "light-wind", "afternoon"]],
    "മഞ്ഞ് പൂര്‍വ്വാധികം താമസിച്ച ഇന്നത്തെ സായാഹ്നം ഉം നാളത്തെ പ്രഭാതം ഉം കാലത്തില്‍": [
        "sentence",
        ["during", "medium-snow", ["and", "later-today-evening", "tomorrow-morning"]],
    ],
    "ശക്തിയേറിയ മഴ പൂര്‍വ്വാധികം താമസിച്ച ഇന്നത്തെ പ്രഭാതം വരെ, ഇന്നത്തെ സായാഹ്നം വീണ്ടും ആരംഭിക്കുന്നു": [
        "sentence",
        ["until-starting-again", "heavy-rain", "later-today-morning", "today-evening"],
    ],
    "മഴക്കാര്‍ മൂടിയ സായാഹ്നം വരെ, രാത്രി വരെ തുടരുന്നു": [
        "sentence",
        ["starting-continuing-until", "heavy-clouds", "evening", "night"],
    ],
    "നേരിയ ഹിമവര്‍ഷം പൂര്‍വ്വാധികം താമസിച്ച ഇന്നത്തെ അപരാഹ്നം കാലത്തില്‍ ഉം മൂടല്‍മഞ്ഞ്(മൂടിക്കെട്ടിയ) നാളത്തെ പ്രഭാതം കാലത്തില്‍ ഉം": [
        "sentence",
        [
            "and",
            ["during", "light-sleet", "later-today-afternoon"],
            ["during", "fog", "tomorrow-morning"],
        ],
    ],
    "അപകടകരമായ കാറ്റ് ഇന്നത്തെ പ്രഭാതം വരെ, ഇന്നത്തെ അപരാഹ്നം (ഉച്ച കഴിഞ്ഞുള്ള സമയം ) വരെ തുടരുന്നു ഉം ഹിമവര്‍ഷം നാളത്തെ പ്രഭാതം കാലത്തില്‍ ഉം": [
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
    "മഴക്കാര്‍ മൂടിയ പൂര്‍വ്വാധികം താമസിച്ച ഇന്നത്തെ രാത്രി ആരംഭിക്കുന്നു ഉം കനത്ത മഞ്ഞ് നാളത്തെ അപരാഹ്നം കാലത്തില്‍ ഉം": [
        "sentence",
        [
            "and",
            ["starting", "heavy-clouds", "later-today-night"],
            ["during", "heavy-snow", "tomorrow-afternoon"],
        ],
    ],
    "വരണ്ട ഇന്നു രാത്രി കാലത്തില്‍ ഉം നേരിയ വര്‍ഷപാതം നാളത്തെ സായാഹ്നം വരെ, നാളത്തെ രാത്രി വരെ തുടരുന്നു ഉം": [
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
    "മഞ്ഞ് (5 ഇഞ്ച്‌) രാത്രി കാലത്തില്‍": [
        "sentence",
        ["during", ["parenthetical", "medium-snow", ["inches", 5]], "night"],
    ],
    "നേരിയ മഞ്ഞ് (2 സെന്‍റിമീറ്റര്‍) പൂര്‍വ്വാധികം താമസിച്ച ഇന്നത്തെ പ്രഭാതം കാലത്തില്‍": [
        "sentence",
        [
            "during",
            ["parenthetical", "light-snow", ["centimeters", 2]],
            "later-today-morning",
        ],
    ],
    "കനത്ത മഞ്ഞ് (8\u201312 ഇഞ്ച്‌) ദിവസം മുഴുവന്‍": [
        "sentence",
        ["for-day", ["parenthetical", "heavy-snow", ["inches", ["range", 8, 12]]]],
    ],
    "മഞ്ഞ് (1 സെന്‍റിമീറ്റര്‍ ഇല്‍ കുറവ്) അപരാഹ്നം കാലത്തില്‍": [
        "sentence",
        [
            "during",
            ["parenthetical", "medium-snow", ["less-than", ["centimeters", 1]]],
            "afternoon",
        ],
    ],
    "വര്‍ഷപാതം ഇല്ല ആഴ്ചയിലുടനീളം, 85\u00b0F നാളെ ഇല്‍ എത്തുന്ന ഉയര്‍ന്ന താപനില നു ഒപ്പം": [
        "sentence",
        [
            "with",
            ["for-week", "no-precipitation"],
            ["temperatures-peaking", ["fahrenheit", 85], "tomorrow"],
        ],
    ],
    "സമ്മിശ്രമായ വര്‍ഷപാതം ആഴ്ചാവസാനത്തില്‍, 32\u00b0C വ്യാഴാഴ്ച ആയി വര്‍ദ്ധിക്കുന്ന ഉയര്‍ന്ന താപനില നു ഒപ്പം": [
        "sentence",
        [
            "with",
            ["over-weekend", "mixed-precipitation"],
            ["temperatures-rising", ["celsius", 32], "thursday"],
        ],
    ],
    "ചാറ്റല്‍മഴ തിങ്കളാഴ്ച കാലത്തില്‍, 15\u00b0F വെള്ളിയാഴ്ച ഇല്‍ ആയി താഴുന്ന ഉയര്‍ന്ന താപനില നു ഒപ്പം": [
        "sentence",
        [
            "with",
            ["during", "very-light-rain", "monday"],
            ["temperatures-valleying", ["fahrenheit", 15], "friday"],
        ],
    ],
    "നേരിയ മഞ്ഞ് ചൊവ്വാഴ്ച ഉം അടുത്ത ബുധനാഴ്ച ഉം കാലത്തില്‍, 0\u00b0C ഞായറാഴ്ച ആയി കുറയുന്ന ഉയര്‍ന്ന താപനില നു ഒപ്പം": [
        "sentence",
        [
            "with",
            ["during", "light-snow", ["and", "tuesday", "next-wednesday"]],
            ["temperatures-falling", ["celsius", 0], "sunday"],
        ],
    ],
    "വര്‍ഷപാതം ഇന്ന്, ശനിയാഴ്ച വില്‍ ഉടനീളം കാലത്തില്‍, 100\u00b0F തിങ്കളാഴ്ച ഇല്‍ എത്തുന്ന ഉയര്‍ന്ന താപനില നു ഒപ്പം": [
        "sentence",
        [
            "with",
            ["during", "medium-precipitation", ["through", "today", "saturday"]],
            ["temperatures-peaking", ["fahrenheit", 100], "monday"],
        ],
    ],
    "സമ്മിശ്രമായ വര്‍ഷപാതം (1\u20133 ഇഞ്ച്‌) ദിവസം മുഴുവന്‍": [
        "sentence",
        [
            "for-day",
            ["parenthetical", "mixed-precipitation", ["inches", ["range", 1, 3]]],
        ],
    ],
    "കനത്ത മഞ്ഞ് (1\u20133 ഇഞ്ച്‌)": [
        "title",
        ["parenthetical", "heavy-snow", ["inches", ["range", 1, 3]]],
    ],
    "കനത്ത മഞ്ഞ് (3\u20135 സെന്‍റിമീറ്റര്‍)": [
        "title",
        ["parenthetical", "heavy-snow", ["centimeters", ["range", 3, 5]]],
    ],
    "സാധ്യമായ ഇടിമിന്നല്‍": ["title", "possible-thunderstorm"],
    "ശക്തിയേറിയ മഴ ഉം ഇടിമിന്നല്‍ ഉം": ["title", ["and", "heavy-rain", "thunderstorm"]],
    "ചാറ്റല്‍മഴ 1 മിനിട്ടു ഇല്‍ കുറവ് ഇല്‍ ആരംഭിക്കുന്നു": [
        "sentence",
        ["starting-in", "very-light-rain", ["less-than", ["minutes", 1]]],
    ],
}
