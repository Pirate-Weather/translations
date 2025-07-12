def join_with_shared_prefix(a, joiner1, b, joiner2):
    """
    Joins two strings a and b using shared prefix matching and specified joiners.

    This function compares two input strings `a` and `b` to find the longest shared prefix.
    After finding the common prefix, it slices `b` from the point where the common prefix ends
    and joins the strings `a` and the sliced `b` with `joiner1` and `joiner2`, respectively.

    Parameters:
    - a (str): The first string.
    - joiner1 (str): The string to be used to join `a` with the rest of `b`.
    - b (str): The second string.
    - joiner2 (str): The string to be used after appending the remainder of `b` to `a`.

    Returns:
    - str: The combined string of `a` and `b` with the specified joiners.
    """
    i = 0

    # Find the longest common prefix between a and b
    while i < len(a) and i < len(b) and ord(a[i]) == ord(b[i]):
        i += 1

    # Backtrack to the last space character before the common prefix ends
    while i > 0 and ord(a[i - 1]) != 32:  # 32 is the ASCII code for space
        i -= 1

    # Join `a` and `b` using the specified joiners
    return a + joiner1 + b[i:] + joiner2


def and_function(stack, a, b):
    return join_with_shared_prefix(a, " ve ", b, "")


def through_function(stack, a, b):
    return join_with_shared_prefix(a, " ile ", b, " arası")


def parenthetical_function(stack, a, b):
    """
    Adds a parenthetical expression to the string `a`.

    This function takes two strings `a` and `b`, and adds the string `b` in parentheses
    to `a`. If `a` is the string "karışık yağış", the function adds " kar" before the closing parenthesis.

    Parameters:
    - a (str): The main string.
    - b (str): The string to be added inside the parentheses.

    Returns:
    - str: The string `a` followed by `b` in parentheses, with special handling if `a` is "karışık yağış".
    """
    if a == "karışık yağış":
        return f"{a} ({b} kar)"
    else:
        return f"{a} ({b})"


def title_function(stack, s):
    """
    Capitalize the first letter of every word.
    """
    return s[0].upper() + s[1:]


def sentence_function(stack, s):
    """
    Capitalize the first word of the sentence and end with a period.
    """
    s = s[0].upper() + s[1:]
    if not s.endswith("."):
        s += "."
    return s


template = {
    "clear": "açık hava",
    "no-precipitation": "yağış yok",
    "mixed-precipitation": "karışık yağış",
    "possible-very-light-precipitation": "çok hafif yağış ihtimali",
    "very-light-precipitation": "çok hafif yağış",
    "possible-light-precipitation": "hafif yağış ihtimali",
    "light-precipitation": "hafif yağış",
    "medium-precipitation": "yağış",
    "heavy-precipitation": "yoğun yağış",
    "possible-very-light-rain": "çok hafif yağmur ihtimali",
    "very-light-rain": "çok hafif yağmur",
    "possible-light-rain": "hafif yağmur ihtimali",
    "light-rain": "hafif yağmur",
    "medium-rain": "yağmur",
    "heavy-rain": "yoğun yağmur",
    "possible-very-light-sleet": "çok hafif karla karışık yağmur ihtimali",
    "very-light-sleet": "çok hafif karla karışık yağmur",
    "possible-light-sleet": "hafif karla karışık yağmur ihtimali",
    "light-sleet": "hafif karla karışık yağmur",
    "medium-sleet": "karla karışık yağmur",
    "heavy-sleet": "yoğun karla karışık yağmur",
    "possible-very-light-snow": "çok hafif kar ihtimali",
    "very-light-snow": "çok hafif kar",
    "possible-light-snow": "hafif kar ihtimali",
    "light-snow": "hafif kar",
    "medium-snow": "kar",
    "heavy-snow": "yoğun kar",
    "possible-thunderstorm": "fırtına olasılığı",
    "thunderstorm": "fırtına",
    "possible-medium-precipitation": "yağış ihtimali",
    "possible-heavy-precipitation": "yoğun yağış ihtimali",
    "possible-medium-rain": "yağmur ihtimali",
    "possible-heavy-rain": "yoğun yağmur ihtimali",
    "possible-medium-sleet": "karla karışık yağmur ihtimali",
    "possible-heavy-sleet": "yoğun karla karışık yağmur ihtimali",
    "possible-medium-snow": "kar ihtimali",
    "possible-heavy-snow": "yoğun kar ihtimali",
    "possible-very-light-freezing-rain": "donan çok hafif ihtimali",
    "very-light-freezing-rain": "donan çok hafif",
    "possible-light-freezing-rain": "hafif donan yağmur ihtimali",
    "light-freezing-rain": "hafif donan yağmur",
    "possible-medium-freezing-rain": "donan yağmur ihtimali",
    "medium-freezing-rain": "donan yağmur",
    "possible-heavy-freezing-rain": "yoğun donan yağmur ihtimali",
    "heavy-freezing-rain": "yoğun donan yağmur",
    "possible-hail": "dolu ihtimali",
    "hail": "dolu",
    "light-wind": "hafif rüzgar",
    "medium-wind": "rüzgar",
    "heavy-wind": "yoğun rüzgar",
    "low-humidity": "düşük nem",
    "high-humidity": "yoğun nem",
    "fog": "sis",
    "very-light-clouds": "çoğunlukla net",
    "light-clouds": "hafif bulutlanma",
    "medium-clouds": "bulutlanma",
    "heavy-clouds": "yoğun bulutlanma",
    "today-morning": "bu sabah",
    "later-today-morning": "bu sabahtan itibaren",
    "today-afternoon": "bugün öğleden sonra",
    "later-today-afternoon": "bu öğleden sonradan itibaren",
    "today-evening": "bu akşam",
    "later-today-evening": "bu akşamdan itibaren",
    "today-night": "bu gece",
    "later-today-night": "bu geceden itibaren",
    "tomorrow-morning": "yarın sabah",
    "tomorrow-afternoon": "yarın öğleden sonra",
    "tomorrow-evening": "yarın akşam",
    "tomorrow-night": "yarın gece",
    "morning": "sabah",
    "afternoon": "öğleden sonra",
    "evening": "akşam",
    "night": "gece",
    "today": "bugün",
    "tomorrow": "yarın",
    "sunday": "Pazar",
    "monday": "Pazartesi",
    "tuesday": "Salı",
    "wednesday": "Çarşamba",
    "thursday": "Perşembe",
    "friday": "Cuma",
    "saturday": "Cumartesi",
    "next-sunday": "Haftaya Pazar'a kadar",
    "next-monday": "Haftaya Pazartesi'ye kadar",
    "next-tuesday": "Haftaya Salı'ya kadar",
    "next-wednesday": "Haftaya Çarşamba'ya kadar",
    "next-thursday": "Haftaya Perşembe'ye kadar",
    "next-friday": "Haftaya Cuma'ya kadar",
    "next-saturday": "Haftaya Cumartesi'ye kadar",
    "minutes": "$1 dk.",
    "fahrenheit": "$1\u00b0F",
    "celsius": "$1\u00b0C",
    "inches": "$1 in.",
    "centimeters": "$1 cm.",
    "less-than": "$1'nin altında",
    "and": and_function,
    "through": through_function,
    "with": "$1, $2",
    "range": "$1\u2013$2",
    "parenthetical": parenthetical_function,
    "for-hour": " saat boyunca $1",
    "starting-in": "$1 $2 içinde başlayacak",
    "stopping-in": "$1 $2 içinde duracak",
    "starting-then-stopping-later": "$1 $2 içinde başlayacak, $3 sonra duracak",
    "stopping-then-starting-later": "$1 $2 içinde duracak, $3 sonra tekrar başlayacak",
    "for-day": "$1 gün boyunca devam edecek",
    "starting": "$2 $1 başlayacak",
    "until": "$1 $2 sona erecek",
    "until-starting-again": "$1 $2 sona erecek, $3 tekrar başlayacak",
    "starting-continuing-until": "$1 $2 başlayacak, $3 sona erecek",
    "during": "$2 $1",
    "for-week": "hafta boyunca $1",
    "over-weekend": "hafta sonu $1",
    "temperatures-peaking": "$2 yüksek sıcaklık $1",
    "temperatures-rising": "$2 sıcaklık $1'ye yükseliyor",
    "temperatures-valleying": "$2 hava soğuyor ve sıcaklık $1'ye düşüyor",
    "temperatures-falling": "$2 sıcaklık $1'ye düşüyor",
    "title": title_function,
    "sentence": sentence_function,
    "next-hour-forecast-status": "$2 nedeniyle sonraki saat tahminleri $1",
    "unavailable": "kullanılamıyor",
    "temporarily-unavailable": "geçici olarak kullanılamıyor",
    "partially-unavailable": "kısmen kullanılamıyor",
    "station-offline": "yakındaki tüm radar istasyonlarının çevrimdışı olması",
    "station-incomplete": "yakındaki tüm radar istasyonlarının kapsama alanı dışında olması",
    "smoke": "duman",
    "haze": "pus",
    "mist": "sis",
}
