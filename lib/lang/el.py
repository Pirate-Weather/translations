def singular_or_plural(n, singular, plural):
    return singular if abs(int(n)) == 1 else plural


def strip_prefix(period):
    if period == "απόψε":
        return "σήμερα το βράδυ"
    elif period.startswith("σήμερα "):
        return period[7:]
    return period


def and_function(stack, a, b):
    return a + (", και " if "," in a else " και ") + b


def through_function(stack, a, b):
    return a + " μέχρι " + b


def parenthetical_function(stack, a, b):
    return f"{a} ({b}{' χιονιού)' if a == 'μικτός υετός' else ')'}"


def until_function(stack, condition, period):
    return condition + " μέχρι " + strip_prefix(period)


def until_starting_again_function(stack, condition, a, b):
    return condition + " μέχρι " + strip_prefix(a) + ", που θα συνεχιστεί και " + b


def starting_continuing_until_function(stack, condition, a, b):
    return (
        condition
        + " που θα αρχίσει "
        + a
        + ", και θα συνεχιστεί μέχρι "
        + strip_prefix(b)
    )


def title_function(stack, s):
    # Apply custom_capitalize to every word
    return s[0].upper() + s[1:]


def sentence_function(stack, s):
    s = s[0].upper() + s[1:]
    if not s.endswith("."):
        s += "."
    return s


def temperatures_peaking_function(stack, a, b):
    sop = singular_or_plural(a.split("°")[0], "στον", "στους")
    return f"τη θερμοκρασία να κορυφώνεται {sop} {a} {b}"


def temperatures_rising_function(stack, a, b):
    sop = singular_or_plural(a.split("°")[0], "τον", "τους")
    return f"τη θερμοκρασία να αυξάνεται έως {sop} {a} {b}"


def temperatures_valleying_function(stack, a, b):
    sop = singular_or_plural(a.split("°")[0], "στον", "στους")
    return f"τη θερμοκρασία να πέφτει {sop} {a} {b}"


def temperatures_falling_function(stack, a, b):
    sop = singular_or_plural(a.split("°")[0], "στον", "στους")
    return f"τη θερμοκρασία να μειώνεται {sop} {a} {b}"


template = {
    "clear": "αίθριος",
    "no-precipitation": "καθόλου υετός",
    "mixed-precipitation": "μικτός υετός",
    "possible-very-light-precipitation": "πιθανός ασθενής υετός",
    "very-light-precipitation": "ασθενής υετός",
    "possible-light-precipitation": "πιθανός ελαφρύς υετός",
    "light-precipitation": "ελαφρύς υετός",
    "medium-precipitation": "υετός",
    "heavy-precipitation": "ισχυρός υετός",
    "possible-very-light-rain": "πιθανή ασθενής βροχή",
    "very-light-rain": "ασθενής βροχή",
    "possible-light-rain": "πιθανή ελαφριά βροχή",
    "light-rain": "ελαφριά βροχή",
    "medium-rain": "βροχή",
    "heavy-rain": "ισχυρή βροχή",
    "possible-very-light-sleet": "πιθανό ασθενές χιονόνερο",
    "very-light-sleet": "ασθενές χιονόνερο",
    "possible-light-sleet": "πιθανό ελαφρύ χιονόνερο",
    "light-sleet": "ελαφρύ χιονόνερο",
    "medium-sleet": "χιονόνερο",
    "heavy-sleet": "ισχυρό χιονόνερο",
    "possible-very-light-snow": "πιθανή ασθενής χιονόπτωση",
    "very-light-snow": "ασθενής χιονόπτωση",
    "possible-light-snow": "πιθανή ελαφρά χιονόπτωση",
    "light-snow": "ελαφρά χιονόπτωση",
    "medium-snow": "χιονόπτωση",
    "heavy-snow": "ισχυρή χιονόπτωση",
    "possible-thunderstorm": "πιθανή καταιγίδα",
    "thunderstorm": "καταιγίδα",
    "possible-medium-precipitation": "πιθανός υετός",
    "possible-heavy-precipitation": "πιθανός ισχυρός υετός",
    "possible-medium-rain": "πιθανή βροχή",
    "possible-heavy-rain": "πιθανή ισχυρή βροχή",
    "possible-medium-sleet": "πιθανή χιονόνερο",
    "possible-heavy-sleet": "πιθανή ισχυρό χιονόνερο",
    "possible-medium-snow": "πιθανή χιονόπτωση",
    "possible-heavy-snow": "πιθανή ισχυρή χιονόπτωση",
    "possible-freezing-drizzle": "πιθανή παγερό ψιλόβροχο",
    "freezing-drizzle": "παγερό ψιλόβροχο",
    "possible-light-freezing-rain": "πιθανή ελαφριά παγωμένη βροχή",
    "light-freezing-rain": "ελαφριά παγωμένη βροχή",
    "possible-freezing-rain": "πιθανή παγωμένη βροχή",
    "freezing-rain": "freezing βροχή",
    "possible-heavy-freezing-rain": "πιθανή ισχυρή παγωμένη βροχή",
    "heavy-freezing-rain": "ισχυρή παγωμένη βροχή",
    "possible-hail": "πιθανή χαλάζι",
    "hail": "χαλάζι",
    "light-wind": "ασθενής άνεμος",
    "medium-wind": "μέτριος άνεμος",
    "heavy-wind": "ισχυρός άνεμος",
    "low-humidity": "ξηρασία",
    "high-humidity": "υγρασία",
    "fog": "ομίχλη",
    "very-light-clouds": "kυρίως σαφής",
    "light-clouds": "αραιή νέφωση",
    "medium-clouds": "μερική νέφωση",
    "heavy-clouds": "συννεφιά",
    "today-morning": "σήμερα το πρωί",
    "later-today-morning": "αργότερα σήμερα το πρωί",
    "today-afternoon": "σήμερα το μεσημέρι",
    "later-today-afternoon": "αργότερα σήμερα το μεσημέρι",
    "today-evening": "σήμερα το απόγευμα",
    "later-today-evening": "αργότερα σήμερα το απόγευμα",
    "today-night": "απόψε",
    "later-today-night": "αργότερα το βράδυ",
    "tomorrow-morning": "αύριο το πρωί",
    "tomorrow-afternoon": "αύριο το μεσημέρι",
    "tomorrow-evening": "αύριο το απόγευμα",
    "tomorrow-night": "αύριο το βράδυ",
    "morning": "το πρωί",
    "afternoon": "το μεσημέρι",
    "evening": "το απόγευμα",
    "night": "το βράδυ",
    "today": "σήμερα",
    "tomorrow": "αύριο",
    "sunday": "την Κυριακή",
    "monday": "την Δευτέρα",
    "tuesday": "την Τρίτη",
    "wednesday": "την Τετάρτη",
    "thursday": "την Πέμπτη",
    "friday": "την Παρασκευή",
    "saturday": "το Σάββατο",
    "next-sunday": "την επόμενη Κυριακή",
    "next-monday": "την επόμενη Δευτέρα",
    "next-tuesday": "την επόμενη Τρίτη",
    "next-wednesday": "την επόμενη Τετάρτη",
    "next-thursday": "την επόμενη Πέμπτη",
    "next-friday": "την επόμενη Παρασκευή",
    "next-saturday": "το επόμενο Σάββατο",
    "minutes": "$1 λεπτά",
    "fahrenheit": "$1\u00b0F",
    "celsius": "$1\u00b0C",
    "inches": "$1 ιν.",
    "centimeters": "$1 εκ.",
    "less-than": "λιγότερο από $1",
    "and": and_function,
    "through": through_function,
    "with": "$1, με $2",
    "range": "$1\u2013$2",
    "parenthetical": parenthetical_function,
    "for-hour": "$1 για αυτή την ώρα",
    "starting-in": "$1 που θα αρχίσει σε $2",
    "stopping-in": "$1 που θα σταματήσει σε $2",
    "starting-then-stopping-later": "$1 που θα αρχίσει σε $2, και θα σταματήσει $3 αργότερα",
    "stopping-then-starting-later": "$1 που θα σταματήσει σε $2, και θα συνεχιστεί $3 αργότερα",
    "for-day": "$1 κατά τη διάρκεια της ημέρας",
    "starting": "$1 που θα αρχίσει $2",
    "until": until_function,
    "until-starting-again": until_starting_again_function,
    "starting-continuing-until": starting_continuing_until_function,
    "during": "$1 $2",
    "for-week": "$1 κατά τη διάρκεια της εβδομάδας",
    "over-weekend": "$1 το Σαββατοκύριακο",
    "temperatures-peaking": temperatures_peaking_function,
    "temperatures-rising": temperatures_rising_function,
    "temperatures-valleying": temperatures_valleying_function,
    "temperatures-falling": temperatures_falling_function,
    "title": title_function,
    "sentence": sentence_function,
    "next-hour-forecast-status": "η ωριαία πρόγνωση καιρού $1 λόγω $2",
    "unavailable": "δεν είναι διαθέσιμη",
    "temporarily-unavailable": "είναι προσωρινά μη διαθέσιμη",
    "partially-unavailable": "είναι μερικώς μη διαθέσιμη",
    "station-offline": "του ότι όλοι οι γύρω μετεωρολογικοί σταθμοί είναι εκτός λειτουργίας",
    "station-incomplete": "χαμηλής κάλυψης από κοντινούς μετεωρολογικούς σταθμούς",
}
