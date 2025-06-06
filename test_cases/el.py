# This would be one of your translations, as a Python dictionary
cases = {
    "Αίθριος": ["title", "clear"],
    "Πιθανός ασθενής υετός": ["title", "possible-very-light-precipitation"],
    "Ασθενής υετός": ["title", "very-light-precipitation"],
    "Πιθανός ελαφρύς υετός": ["title", "possible-light-precipitation"],
    "Ελαφρύς υετός": ["title", "light-precipitation"],
    "Υετός": ["title", "medium-precipitation"],
    "Ισχυρός υετός": ["title", "heavy-precipitation"],
    "Πιθανή ασθενής βροχή": ["title", "possible-very-light-rain"],
    "Ασθενής βροχή": ["title", "very-light-rain"],
    "Πιθανή ελαφριά βροχή": ["title", "possible-light-rain"],
    "Ελαφριά βροχή": ["title", "light-rain"],
    "Βροχή": ["title", "medium-rain"],
    "Ισχυρή βροχή": ["title", "heavy-rain"],
    "Πιθανό ασθενές χιονόνερο": ["title", "possible-very-light-sleet"],
    "Ασθενές χιονόνερο": ["title", "very-light-sleet"],
    "Πιθανό ελαφρύ χιονόνερο": ["title", "possible-light-sleet"],
    "Ελαφρύ χιονόνερο": ["title", "light-sleet"],
    "Χιονόνερο": ["title", "medium-sleet"],
    "Ισχυρό χιονόνερο": ["title", "heavy-sleet"],
    "Πιθανή ασθενής χιονόπτωση": ["title", "possible-very-light-snow"],
    "Ασθενής χιονόπτωση": ["title", "very-light-snow"],
    "Πιθανή ελαφρά χιονόπτωση": ["title", "possible-light-snow"],
    "Ελαφρά χιονόπτωση": ["title", "light-snow"],
    "Χιονόπτωση": ["title", "medium-snow"],
    "Ισχυρή χιονόπτωση": ["title", "heavy-snow"],
    "Μέτριος άνεμος": ["title", "medium-wind"],
    "Ισχυρός άνεμος": ["title", "heavy-wind"],
    "Ομίχλη": ["title", "fog"],
    "Kυρίως σαφής": ["title", "very-light-clouds"],
    "Αραιή νέφωση": ["title", "light-clouds"],
    "Μερική νέφωση": ["title", "medium-clouds"],
    "Συννεφιά": ["title", "heavy-clouds"],
    "Ξηρασία και ασθενής άνεμος": ["title", ["and", "low-humidity", "light-wind"]],
    "Ασθενής βροχή και ισχυρός άνεμος": [
        "title",
        ["and", "very-light-rain", "heavy-wind"],
    ],
    "Υγρασία και αραιή νέφωση": ["title", ["and", "high-humidity", "light-clouds"]],
    "Αίθριος για αυτή την ώρα.": ["sentence", ["for-hour", "clear"]],
    "Ασθενής χιονόπτωση που θα αρχίσει σε 35 λεπτά.": [
        "sentence",
        ["starting-in", "very-light-snow", ["minutes", 35]],
    ],
    "Ελαφριά βροχή που θα σταματήσει σε 15 λεπτά.": [
        "sentence",
        ["stopping-in", "light-rain", ["minutes", 15]],
    ],
    "Ισχυρό χιονόνερο που θα αρχίσει σε 20 λεπτά, και θα σταματήσει 30 λεπτά αργότερα.": [
        "sentence",
        [
            "starting-then-stopping-later",
            "heavy-sleet",
            ["minutes", 20],
            ["minutes", 30],
        ],
    ],
    "Βροχή που θα σταματήσει σε 25 λεπτά, και θα συνεχιστεί 8 λεπτά αργότερα.": [
        "sentence",
        [
            "stopping-then-starting-later",
            "medium-rain",
            ["minutes", 25],
            ["minutes", 8],
        ],
    ],
    "Μερική νέφωση κατά τη διάρκεια της ημέρας.": [
        "sentence",
        ["for-day", "medium-clouds"],
    ],
    "Ασθενές χιονόνερο που θα αρχίσει το πρωί.": [
        "sentence",
        ["starting", "very-light-sleet", "morning"],
    ],
    "Μέτριος άνεμος μέχρι σήμερα το βράδυ.": [
        "sentence",
        ["until", "medium-wind", "today-night"],
    ],
    "Ισχυρός υετός μέχρι το μεσημέρι.": [
        "sentence",
        ["until", "heavy-precipitation", "afternoon"],
    ],
    "Ασθενής άνεμος το μεσημέρι.": ["sentence", ["during", "light-wind", "afternoon"]],
    "Χιονόπτωση αργότερα σήμερα το απόγευμα και αύριο το πρωί.": [
        "sentence",
        ["during", "medium-snow", ["and", "later-today-evening", "tomorrow-morning"]],
    ],
    "Ισχυρή βροχή μέχρι αργότερα σήμερα το πρωί, που θα συνεχιστεί και σήμερα το απόγευμα.": [
        "sentence",
        ["until-starting-again", "heavy-rain", "later-today-morning", "today-evening"],
    ],
    "Συννεφιά που θα αρχίσει το απόγευμα, και θα συνεχιστεί μέχρι το βράδυ.": [
        "sentence",
        ["starting-continuing-until", "heavy-clouds", "evening", "night"],
    ],
    "Ελαφρύ χιονόνερο αργότερα σήμερα το μεσημέρι και ομίχλη αύριο το πρωί.": [
        "sentence",
        [
            "and",
            ["during", "light-sleet", "later-today-afternoon"],
            ["during", "fog", "tomorrow-morning"],
        ],
    ],
    "Ισχυρός άνεμος που θα αρχίσει σήμερα το πρωί, και θα συνεχιστεί μέχρι το μεσημέρι, και χιονόνερο αύριο το πρωί.": [
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
    "Συννεφιά που θα αρχίσει αργότερα το βράδυ και ισχυρή χιονόπτωση αύριο το μεσημέρι.": [
        "sentence",
        [
            "and",
            ["starting", "heavy-clouds", "later-today-night"],
            ["during", "heavy-snow", "tomorrow-afternoon"],
        ],
    ],
    "Ξηρασία απόψε και ελαφρύς υετός που θα αρχίσει αύριο το απόγευμα, και θα συνεχιστεί μέχρι αύριο το βράδυ.": [
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
    "Χιονόπτωση (5 ιν.) το βράδυ.": [
        "sentence",
        ["during", ["parenthetical", "medium-snow", ["inches", 5]], "night"],
    ],
    "Ελαφρά χιονόπτωση (2 εκ.) αργότερα σήμερα το πρωί.": [
        "sentence",
        [
            "during",
            ["parenthetical", "light-snow", ["centimeters", 2]],
            "later-today-morning",
        ],
    ],
    "Ισχυρή χιονόπτωση (8\u201312 ιν.) κατά τη διάρκεια της ημέρας.": [
        "sentence",
        ["for-day", ["parenthetical", "heavy-snow", ["inches", ["range", 8, 12]]]],
    ],
    "Χιονόπτωση (λιγότερο από 1 εκ.) το μεσημέρι.": [
        "sentence",
        [
            "during",
            ["parenthetical", "medium-snow", ["less-than", ["centimeters", 1]]],
            "afternoon",
        ],
    ],
    "Καθόλου υετός κατά τη διάρκεια της εβδομάδας, με τη θερμοκρασία να κορυφώνεται στους 85\u00b0F αύριο.": [
        "sentence",
        [
            "with",
            ["for-week", "no-precipitation"],
            ["temperatures-peaking", ["fahrenheit", 85], "tomorrow"],
        ],
    ],
    "Μικτός υετός το Σαββατοκύριακο, με τη θερμοκρασία να αυξάνεται έως τους 32\u00b0C την Πέμπτη.": [
        "sentence",
        [
            "with",
            ["over-weekend", "mixed-precipitation"],
            ["temperatures-rising", ["celsius", 32], "thursday"],
        ],
    ],
    "Ασθενής βροχή την Δευτέρα, με τη θερμοκρασία να πέφτει στους 15\u00b0F την Παρασκευή.": [
        "sentence",
        [
            "with",
            ["during", "very-light-rain", "monday"],
            ["temperatures-valleying", ["fahrenheit", 15], "friday"],
        ],
    ],
    "Ελαφρά χιονόπτωση την Τρίτη και την Τετάρτη, με τη θερμοκρασία να μειώνεται στους 0\u00b0C την Κυριακή.": [
        "sentence",
        [
            "with",
            ["during", "light-snow", ["and", "tuesday", "wednesday"]],
            ["temperatures-falling", ["celsius", 0], "sunday"],
        ],
    ],
    "Υετός σήμερα μέχρι το Σάββατο, με τη θερμοκρασία να κορυφώνεται στους 100\u00b0F την Δευτέρα.": [
        "sentence",
        [
            "with",
            ["during", "medium-precipitation", ["through", "today", "saturday"]],
            ["temperatures-peaking", ["fahrenheit", 100], "monday"],
        ],
    ],
    "Μικτός υετός (1\u20133 ιν. χιονιού) κατά τη διάρκεια της ημέρας.": [
        "sentence",
        [
            "for-day",
            ["parenthetical", "mixed-precipitation", ["inches", ["range", 1, 3]]],
        ],
    ],
    "Ισχυρή χιονόπτωση (1\u20133 ιν.)": [
        "title",
        ["parenthetical", "heavy-snow", ["inches", ["range", 1, 3]]],
    ],
    "Ισχυρή χιονόπτωση (3\u20135 εκ.)": [
        "title",
        ["parenthetical", "heavy-snow", ["centimeters", ["range", 3, 5]]],
    ],
    "Πιθανή καταιγίδα": ["title", "possible-thunderstorm"],
    "Ισχυρή βροχή και καταιγίδα": ["title", ["and", "heavy-rain", "thunderstorm"]],
    "Η ωριαία πρόγνωση καιρού είναι προσωρινά μη διαθέσιμη λόγω του ότι όλοι οι γύρω μετεωρολογικοί σταθμοί είναι εκτός λειτουργίας.": [
        "sentence",
        ["next-hour-forecast-status", "temporarily-unavailable", "station-offline"],
    ],
    "Η ωριαία πρόγνωση καιρού είναι μερικώς μη διαθέσιμη λόγω χαμηλής κάλυψης από κοντινούς μετεωρολογικούς σταθμούς.": [
        "sentence",
        ["next-hour-forecast-status", "partially-unavailable", "station-incomplete"],
    ],
    "Η ωριαία πρόγνωση καιρού δεν είναι διαθέσιμη λόγω του ότι όλοι οι γύρω μετεωρολογικοί σταθμοί είναι εκτός λειτουργίας.": [
        "sentence",
        ["next-hour-forecast-status", "unavailable", "station-offline"],
    ],
}
