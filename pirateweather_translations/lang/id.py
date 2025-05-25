import re


def join_with_shared_prefix(a, b, joiner):
    m = a
    i = 0

    # Skip the prefix of b that is shared with a.
    min_len = min(len(m), len(b))
    while i < min_len and ord(m[i]) == ord(b[i]):
        i += 1

    # ...except whitespace! We need that whitespace!
    # Move back until we hit a space or start of string
    while i > 0 and (i > len(b) or (i <= len(b) and b[i - 1] != " ")):
        i -= 1

    return a + joiner + b[i:]


def and_function(stack, a, b):
    return join_with_shared_prefix(a, b, ", dan " if "," in a else " dan ")


def through_function(stack, a, b):
    return join_with_shared_prefix(a, b, " melalui ")


def parenthetical_function(stack, a, b):
    return f"{a} ({b}{' oleh salju)' if a == 'hujan ringan' else ')'}"


def title_function(stack, s):
    def replace_letter(match):
        return match.group(0).upper()

    return re.sub(r"\b(?:a(?!nd\b)|c(?!m\.)|i(?!n\.)|[^\Waci])", replace_letter, s)


def sentence_function(stack, s):
    s = s[0].upper() + s[1:]
    if not s.endswith("."):
        s += "."
    return s


template = {
    "clear": "cerah",
    "no-precipitation": "tidak hujan",
    "mixed-precipitation": "hujan ringan",
    "possible-very-light-precipitation": "kemungkinan hujan ringan",
    "very-light-precipitation": "hujan ringan",
    "possible-light-precipitation": "kemungkinan hujan ringan",
    "light-precipitation": "hujan ringan",
    "medium-precipitation": "hujan",
    "heavy-precipitation": "hujan lebat",
    "possible-very-light-rain": "kemungkinan hujan ringan",
    "very-light-rain": "hujan ringan",
    "possible-light-rain": "kemungkinan hujan ringan",
    "light-rain": "hujan ringan",
    "medium-rain": "hujan",
    "heavy-rain": "hujan lebat",
    "possible-very-light-sleet": "kemungkinan hujan salju",
    "very-light-sleet": "hujan salju ringan",
    "possible-light-sleet": "kemungkinan hujan salju ringan",
    "light-sleet": "hujan salju ringan",
    "medium-sleet": "hujan salju",
    "heavy-sleet": "hujan salju lebat",
    "possible-very-light-snow": "kemungkinan saju ringan",
    "very-light-snow": "salju ringan",
    "possible-light-snow": "kemungkinan salju ringan",
    "light-snow": "salju ringan",
    "medium-snow": "salju",
    "heavy-snow": "salju besar",
    "possible-thunderstorm": "kemungkinan badai",
    "thunderstorm": "badai",
    "possible-medium-precipitation": "kemungkinan precipitation",
    "possible-heavy-precipitation": "kemungkinan heavy precipitation",
    "possible-medium-rain": "kemungkinan hujan",
    "possible-heavy-rain": "kemungkinan hujan lebat",
    "possible-medium-sleet": "kemungkinan hujan salju",
    "possible-heavy-sleet": "kemungkinan hujan salju lebat",
    "possible-medium-snow": "kemungkinan salju",
    "possible-heavy-snow": "kemungkinan salju besar",
    "possible-very-light-freezing-rain": "kemungkinan hujan yang membekukan ringan",
    "very-light-freezing-rain": "hujan yang membekukan ringan",
    "possible-light-freezing-rain": "kemungkinan hujan yang membekukan ringan",
    "light-freezing-rain": "hujan yang membekukan ringan",
    "possible-medium-freezing-rain": "kemungkinan hujan yang membekukan",
    "medium-freezing-rain": "hujan yang membekukan",
    "possible-heavy-freezing-rain": "kemungkinan hujan yang membekukan lebat",
    "heavy-freezing-rain": "hujan yang membekukan lebat",
    "possible-hail": "kemungkinan hujan es",
    "hail": "hujan es",
    "light-wind": "berangin ringan",
    "medium-wind": "berangin",
    "heavy-wind": "berangin besar",
    "low-humidity": "kering",
    "high-humidity": "lembab",
    "fog": "berkabut",
    "very-light-clouds": "sebagian besar cerah",
    "light-clouds": "sedikit berawan",
    "medium-clouds": "berawan",
    "heavy-clouds": "berawan besar",
    "today-morning": "pagi ini",
    "later-today-morning": "nanti pagi ini",
    "today-afternoon": "sore ini",
    "later-today-afternoon": "nanti sore ini",
    "today-evening": "malam ini",
    "later-today-evening": "nanti malam ini",
    "today-night": "malam ini",
    "later-today-night": "nanti malam ini",
    "tomorrow-morning": "besok pagi",
    "tomorrow-afternoon": "besok sore",
    "tomorrow-evening": "besok malam",
    "tomorrow-night": "besok tengah malam",
    "morning": "pada pagi hari",
    "afternoon": "pada sore hari",
    "evening": "pada malam hari",
    "night": "tengah malam",
    "today": "hari ini",
    "tomorrow": "besok",
    "sunday": "pada hari Minggu",
    "monday": "pada hari Senin",
    "tuesday": "pada hari Selasa",
    "wednesday": "pada hari Rabu",
    "thursday": "pada hari Kamis",
    "friday": "pada hari Jum'at",
    "saturday": "pada hari Sabtu",
    "next-sunday": "Minggu minggu depan",
    "next-monday": "Senin minggu depan",
    "next-tuesday": "Selasa minggu depan",
    "next-wednesday": "Rabu minggu depan",
    "next-thursday": "Kamis minggu depan",
    "next-friday": "Jumat minggu depan",
    "next-saturday": "Sabtu minggu depan",
    "minutes": "$1 min.",
    "fahrenheit": "$1\u00b0F",
    "celsius": "$1\u00b0C",
    "inches": "$1 in.",
    "centimeters": "$1 cm.",
    "less-than": "dibawah $1",
    "and": and_function,
    "through": through_function,
    "with": "$1, dengan $2",
    "range": "$1\u2013$2",
    "parenthetical": parenthetical_function,
    "for-hour": "$1 pada jam",
    "starting-in": "$1 mulai pada $2",
    "stopping-in": "$1 berhenti pada $2",
    "starting-then-stopping-later": "$1 mulai pada $2, berhenti $3 nanti",
    "stopping-then-starting-later": "$1 berhenti pada $2, berhenti lagi $3 nanti",
    "for-day": "$1 selama sehari",
    "starting": "$1 mulai $2",
    "until": "$1 sampai $2",
    "until-starting-again": "$1 sampai $2, mulai kembali $3",
    "starting-continuing-until": "$1 mulai $2, berlanjut sampai $3",
    "during": "$1 $2",
    "for-week": "$1 selama seminggu",
    "over-weekend": "$1 selama akhir minggu",
    "temperatures-peaking": "suhu memuncak pada $1 $2",
    "temperatures-rising": "suhu naik ke $1 $2",
    "temperatures-valleying": "suhu menurun pada $1 $2",
    "temperatures-falling": "suhu turun pada $1 $2",
    "title": title_function,
    "sentence": sentence_function,
    "next-hour-forecast-status": "perkiraan jam berikutnya adalah $1 karena $2",
    "unavailable": "tidak tersedia",
    "temporarily-unavailable": "sementara tidak tersedia",
    "partially-unavailable": "sebagian tidak tersedia",
    "station-offline": "semua stasiun radar terdekat sedang offline",
    "station-incomplete": "kesenjangan dalam jangkauan dari stasiun radar terdekat",
}
