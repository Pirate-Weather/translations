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
    joiner = ", agus " if "," in a else " agus "
    return join_with_shared_prefix(a, b, joiner)


def through_function(stack, a, b):
    return join_with_shared_prefix(a, b, " tro ")


def title_function(stack, s):
    def capitalize_word(word):
        if word == "Agus":
            return word
        return word[0].upper() + word[1:]

    # Split the input string into words and apply the capitalize_word function
    words = re.findall(r"\S+", s)  # Find all non-whitespace words
    return " ".join([capitalize_word(word) for word in words])


def sentence_function(stack, s):
    s = s[0].upper() + s[1:]
    if not s.endswith("."):
        s += "."
    return s


template = {
    "clear": "soilleir",
    "no-precipitation": "gun sileadh",
    "mixed-precipitation": "sileadh measgaichte",
    "possible-very-light-precipitation": "ma dh'fhaoidte gu sil i beagan",
    "very-light-precipitation": "sileadh glè aotrom",
    "possible-light-precipitation": "ma dh'fhaoidte gu sil i",
    "light-precipitation": "sileadh aotrom",
    "medium-precipitation": "sileadh",
    "heavy-precipitation": "sileadh trom",
    "possible-very-light-rain": "ma dh'fhaoidte gum bi uisge glè aotrom",
    "very-light-rain": "uisge glè aotrom",
    "possible-light-rain": "ma dh'fhaoidte gum bi uisge aotrom",
    "light-rain": "uisge aotrom",
    "medium-rain": "uisge",
    "heavy-rain": "uisge trom",
    "possible-very-light-sleet": "ma dh'fhaoidte gum bi frasan flin",
    "very-light-sleet": "frasan flin",
    "possible-light-sleet": "ma dh'fhaoidte gum bi flin aotrom",
    "light-sleet": "flin aotrom",
    "medium-sleet": "flin",
    "heavy-sleet": "flin trom",
    "possible-very-light-snow": "ma dh'fhaoidte gum bi frasan sneachda",
    "very-light-snow": "frasan sneachda",
    "possible-light-snow": "ma dh'fhaoidte gun cur i sneachda",
    "light-snow": "sneachd aotrom",
    "medium-snow": "sneachd",
    "heavy-snow": "sneachda trom",
    "possible-thunderstorm": "ma dh'fhaoidte gum bi stoirmean tàirneanaich",
    "thunderstorm": "stoirmean tàirneanaich",
    "possible-medium-precipitation": "ma dh'fhaoidte gum sileadh",
    "possible-heavy-precipitation": "ma dh'fhaoidte gum sileadh trom",
    "possible-medium-rain": "ma dh'fhaoidte gum bi uisge",
    "possible-heavy-rain": "ma dh'fhaoidte gum bi uisge",
    "possible-medium-sleet": "ma dh'fhaoidte gum bi flin",
    "possible-heavy-sleet": "ma dh'fhaoidte gum bi flin trom",
    "possible-medium-snow": "ma dh'fhaoidte gum bi sneachd",
    "possible-heavy-snow": "ma dh'fhaoidte gum bi sneachd trom",
    "possible-freezing-drizzle": "ma dh'fhaoidte gum bi glè reòta aotrom",
    "freezing-drizzle": "glè aotrom reòta",
    "possible-light-freezing-rain": "ma dh'fhaoidte gum bi light uisge reòta aotrom",
    "light-freezing-rain": "uisge reòta aotrom",
    "possible-freezing-rain": "ma dh'fhaoidte gum bi uisge reòta",
    "freezing-rain": "uisge reòta",
    "possible-heavy-freezing-rain": "ma dh'fhaoidte gum bi uisge reòta trom",
    "heavy-freezing-rain": "uisge reòta trom",
    "possible-hail": "possma dh'fhaoidte gum biible fàilinn",
    "hail": "fàilinn",
    "light-wind": "oiteag shocair",
    "medium-wind": "gaoth",
    "heavy-wind": "gaoth làidir",
    "low-humidity": "tioram",
    "high-humidity": "tais",
    "fog": "ceòthach",
    "very-light-clouds": "soilleir sa mhòr-chuid",
    "light-clouds": "sgothan aotruime",
    "medium-clouds": "sgothach",
    "heavy-clouds": "sgothan truime",
    "today-morning": "madainn an-diugh",
    "later-today-morning": "nas anmoiche madainn an-diugh",
    "today-afternoon": "tràth feasgar an-diugh",
    "later-today-afternoon": "nas anmoiche feasgar an-diugh",
    "today-evening": "anmoch feasgar an-diugh",
    "later-today-evening": "nas anmoiche feasgar an-diugh",
    "today-night": "a-nochd",
    "later-today-night": "nas anmoiche a-nochd",
    "tomorrow-morning": "madainn a-màireach",
    "tomorrow-afternoon": "tràth feasgar a-màireach",
    "tomorrow-evening": "anmoch feasgar a-màireach",
    "tomorrow-night": "an ath oidhche",
    "morning": "anns a' mhadainn",
    "afternoon": "tràth san fheasgar",
    "evening": "anmoch san fheasgar",
    "night": "a-nochd",
    "today": "an-diugh",
    "tomorrow": "a-màireach",
    "sunday": "Didòmhnaich",
    "monday": "Diluain",
    "tuesday": "Dimàirt",
    "wednesday": "Diciadain",
    "thursday": "Diardaoin",
    "friday": "Dihaoine",
    "saturday": "Disathairne",
    "next-sunday": "Didòmhnaich an ath sheachdain",
    "next-monday": "Diluain an ath sheachdain",
    "next-tuesday": "Dimàirt an ath sheachdain",
    "next-wednesday": "Diciadain an ath sheachdain",
    "next-thursday": "Diardaoin an ath sheachdain",
    "next-friday": "Dihaoine an ath sheachdain",
    "next-saturday": "Disathairne an ath sheachdain",
    "minutes": "$1 mion.",
    "fahrenheit": "$1\u00b0F",
    "celsius": "$1\u00b0C",
    "inches": "$1 òir.",
    "centimeters": "$1 cm.",
    "less-than": "< $1",
    "and": and_function,
    "through": through_function,
    "with": "$1, le $2",
    "range": "$1\u2013$2",
    "parenthetical": "$1 ($2)",
    "for-hour": "$1 fad uair a thìde",
    "starting-in": "$1 a' tòiseachadh ann an $2",
    "stopping-in": "$1 a' stad ann an $2",
    "starting-then-stopping-later": "$1 a' tòiseachadh ann an $2, a' stad as dèidh $3",
    "stopping-then-starting-later": "$1 a' stad ann an $2, a' tòiseachadh a-rithist as dèidh $3",
    "for-day": "$1 fad an latha",
    "starting": "$1 a' tòiseachadh $2",
    "until": "$1 a' stad $2",
    "until-starting-again": "$1 a' stad $2, a' tòiseachadh a-rithist $3",
    "starting-continuing-until": "$1 a' tòiseachadh $2, a' stad $3",
    "during": "$1 $2",
    "for-week": "$1 fad na seachdain",
    "over-weekend": "$1 thairis air an deireadh-sheachdain",
    "temperatures-peaking": "an teòthachd as àirde a' ruigsinn $1 $2",
    "temperatures-rising": "an teòthachd as àirde a' ruigsinn $1 $2",
    "temperatures-valleying": "an teòthachd as àirde a' tuiteam gu $1 $2",
    "temperatures-falling": "an teòthachd as àirde a' tuiteam gu $1 $2",
    "title": title_function,
    "sentence": sentence_function,
    "next-hour-forecast-status": "chan eil ro-aithrisean an ath uair $1 air sgàth 's gu bheil $2",
    "unavailable": "ri fhaoitinn",
    "temporarily-unavailable": "ri fhaoitinn airson grèis",
    "partially-unavailable": "ri fhaoitinn gu h-iomlan",
    "station-offline": "gu bheil a h-uile stèisean-radar a tha faisg air làimh far loidhne",
    "station-incomplete": "beàrnan anns an fhiosrachadh bho na stèisean-radar a tha faisg air làimh",
}
