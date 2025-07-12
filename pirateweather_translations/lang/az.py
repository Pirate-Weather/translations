import re


def custom_capitalize(s):
    return s[0].upper() + s[1:] if s else s


def and_function(stack, a, b):
    return a + " və " + b


def through_function(stack, a, b):
    return a + " ilə " + b + " arası"


def parenthetical_function(stack, a, b):
    return f"{a} ({b}{' qar)' if a == 'qarışıq yağış' else ')'}"


def until_function(stack, condition, period):
    return condition + " " + period + " dayanacaq"


def until_starting_again_function(stack, condition, a, b):
    return condition + " " + a + " dayanıb, " + b + " yenidən başlayacaq"


def starting_continuing_until_function(stack, condition, a, b):
    return a + " " + condition + " başlayıb, " + b + " dayanacaq"


def title_function(stack, s):
    # Apply custom_capitalize to every word
    def replace_func(txt: str) -> str:
        if txt in {"və", "düym", "sm."}:
            return txt
        return txt[0].upper() + txt[1:].lower()

    # Use regex to find all words with the specified letters
    return re.sub(r"([a-zA-ZÇçŞşIıƏəÖöĞğÜü.]+)", lambda m: replace_func(m.group(0)), s)


def sentence_function(stack, s):
    s = custom_capitalize(s)
    if not s.endswith("."):
        s += "."
    return s


template = {
    "clear": "buludsuz",
    "no-precipitation": "yağmursuz",
    "mixed-precipitation": "qarışıq yağış",
    "possible-very-light-precipitation": "yüngül yağış ehtimalı",
    "very-light-precipitation": "yüngül yağış",
    "possible-light-precipitation": "yüngül yağış ehtimalı",
    "light-precipitation": "yüngül yağış",
    "medium-precipitation": "yağış",
    "heavy-precipitation": "güclü yağış",
    "possible-very-light-rain": "çiskin yağış ehtimalı",
    "very-light-rain": "çiskin",
    "possible-light-rain": "yüngül yağış ehtimalı",
    "light-rain": "yüngül yağış",
    "medium-rain": "yağış",
    "heavy-rain": "güclü yağış",
    "possible-very-light-sleet": "yüngül sulu qar ehtimalı",
    "very-light-sleet": "yüngül sulu qar",
    "possible-light-sleet": "yüngül sulu qar ehtimalı",
    "light-sleet": "yüngül sulu qar",
    "medium-sleet": "sulu qar",
    "heavy-sleet": "güclü sulu qar",
    "possible-very-light-snow": "sulu qar ehtimalı",
    "very-light-snow": "sulu qar",
    "possible-light-snow": "yüngül qar ehtimalı",
    "light-snow": "yüngül qar",
    "medium-snow": "qar",
    "heavy-snow": "güclü qar",
    "possible-thunderstorm": "mümkün tufanlar",
    "thunderstorm": "tufanlar",
    "possible-medium-precipitation": "mümkün yağıntı",
    "possible-heavy-precipitation": "mümkün ağır yağış",
    "possible-medium-rain": "mümkün yağış",
    "possible-heavy-rain": "mümkün güclü yağış",
    "possible-medium-sleet": "mümkün sulu qar",
    "possible-heavy-sleet": "mümkün ağır sulu qar",
    "possible-medium-snow": "mümkün qar",
    "possible-heavy-snow": "mümkün güclü qar",
    "possible-very-light-freezing-rain": "mümkün donma çiskin",
    "very-light-freezing-rain": "donmaq çiskin",
    "possible-light-freezing-rain": "mümkün işıq donması yağış",
    "light-freezing-rain": "yüngül donmuş yağış",
    "possible-medium-freezing-rain": "mümkün donma yağışı",
    "medium-freezing-rain": "donmuş yağış",
    "possible-heavy-freezing-rain": "mümkün güclü donmuş yağış",
    "heavy-freezing-rain": "güclü donmuş yağış",
    "possible-hail": "mümkün dolu",
    "hail": "dolu",
    "light-wind": "sərin",
    "medium-wind": "külək",
    "heavy-wind": "güclü külək",
    "low-humidity": "rütubətsiz",
    "high-humidity": "rütubətli",
    "fog": "dumanlı",
    "very-light-clouds": "əsasən buludsuz",
    "light-clouds": "qismən buludlu",
    "medium-clouds": "əsasən buludlu",
    "heavy-clouds": "tutqun hava",
    "today-morning": "bu gün səhər",
    "later-today-morning": "bu gün səhərdən sonra",
    "today-afternoon": "bu gün günortadan sonra",
    "later-today-afternoon": "bu gün günortadan sonra",
    "today-evening": "bu gün axşam",
    "later-today-evening": "bu gün axşam",
    "today-night": "bu gün gecə",
    "later-today-night": "bu gün gecə",
    "tomorrow-morning": "sabah səhər",
    "tomorrow-afternoon": "sabah günortadan sonra",
    "tomorrow-evening": "sabah axşam",
    "tomorrow-night": "sabah gecə",
    "morning": "səhər",
    "afternoon": "günortadan sonra",
    "evening": "axşam",
    "night": "gecə",
    "today": "bu gün",
    "tomorrow": "sabah",
    "sunday": "bazar günü",
    "monday": "bazar ertəsi",
    "tuesday": "çərşənbə axşamı",
    "wednesday": "çərşənbə günü",
    "thursday": "cümə axşamı",
    "friday": "cümə günü",
    "saturday": "şənbə günü",
    "next-sunday": "bazar günü",
    "next-monday": "bazar ertəsi",
    "next-tuesday": "çərşənbə axşamı",
    "next-wednesday": "çərşənbə günü",
    "next-thursday": "cümə axşamı",
    "next-friday": "cümə günü",
    "next-saturday": "şənbə günü",
    "minutes": "$1 dəq.",
    "fahrenheit": "$1\u00b0F",
    "celsius": "$1\u00b0C",
    "inches": "$1 düym",
    "centimeters": "$1 sm.",
    "less-than": "$1-dən aşağı",
    "and": and_function,
    "through": through_function,
    "with": "$1, $2",
    "range": "$1\u2013$2",
    "parenthetical": parenthetical_function,
    "for-hour": "1 saat boyunca $1 olacaq",
    "starting-in": "$2 sonra $1 başlayacaq",
    "stopping-in": "$1 $2 sonra dayanacaq",
    "starting-then-stopping-later": "$1 $2 sonra başlayacaq, $3 davam edib dayanacaq",
    "stopping-then-starting-later": "$1 $2 sonra dayanacaq, $3 sonra yenidən başlayacaq",
    "for-day": "gün boyu $1 olacaq",
    "starting": "$2 $1 başlayacaq",
    "until": until_function,
    "until-starting-again": until_starting_again_function,
    "starting-continuing-until": starting_continuing_until_function,
    "during": "$2 $1 olacaq",
    "for-week": "həftə boyunca $1 olacaq",
    "over-weekend": "həftə sonu $1 olacaq",
    "temperatures-peaking": "$2 hava kəskin istiləşəcək və temperatur $1-yə qalxacaq",
    "temperatures-rising": "$2 temperatur $1-yə qalxacaq",
    "temperatures-valleying": "$2 hava kəskin soyuyacaq və temperatur $1-yə düşəcək",
    "temperatures-falling": "$2 temperatur $1-yə düşəcək",
    "title": title_function,
    "sentence": sentence_function,
    "next-hour-forecast-status": "növbəti saat proqnozları var $1 səbəbiylə $2",
    "unavailable": "mövcud deyil",
    "temporarily-unavailable": "müvəqqəti olaraq mövcud deyil",
    "partially-unavailable": "qismən əlçatmazdır",
    "station-offline": "bütün yaxınlıqdakı radar stansiyaları oflayndır",
    "station-incomplete": "yaxınlıqdakı radar stansiyalarından əhatə dairəsində boşluqlar",
    "smoke": "tüstü",
    "haze": "çiskin",
    "mist": "duman",
}
