def join_with_shared_prefix(a, b, joiner):
    if a[:4] == "يوم " and b[:4] == "يوم " and joiner == " و ":
        return "يومي " + a[4:] + joiner + b[4:]
    else:
        return a + joiner + b


def strip_prefix(period):
    if period[:10] == "خلال الليل":
        return period[5:]
    elif period[:3] == "في ":
        return period[3:]
    else:
        return period


def and_function(stack, a, b):
    return join_with_shared_prefix(a, b, " و ")


def through_function(stack, a, b):
    return join_with_shared_prefix(a, b, " حتى ")


def parenthetical_function(stack, a, b):
    return a + " (" + b + (" من الثلج)" if a == "هطول أمطار وثلوج" else ")")


def until_function(stack, condition, period):
    return condition + " حتى " + strip_prefix(period)


def until_starting_again_function(stack, condition, a, b):
    return condition + " حتى " + strip_prefix(a) + " وتبدأ مجدداً في " + strip_prefix(b)


def starting_continuing_until_function(stack, condition, a, b):
    return condition + " تبدأ في " + strip_prefix(a) + " وتستمر حتى " + strip_prefix(b)


template = {
    "clear": "صافِ",
    "mostly-clear": "صافٍ في الغالب",
    "no-precipitation": "لا أمطار",
    "mixed-precipitation": "هطول أمطار وثلوج",
    "possible-very-light-precipitation": "إحتمالية هطول أمطار خفيفة",
    "very-light-precipitation": "أمطار خفيفة",
    "possible-light-precipitation": "إحتمالية هطول أمطار خفيفة",
    "light-precipitation": "أمطار خفيفة",
    "medium-precipitation": "أمطار متوسطة",
    "heavy-precipitation": "أمطار غزيرة",
    "possible-very-light-rain": "إحتمالية هطول أمطار خفيفة",
    "very-light-rain": "أمطار خفيفة",
    "possible-light-rain": "إحتمالية أمطار خفيفة",
    "light-rain": "أمطار خفيفة",
    "medium-rain": "أمطار متوسطة",
    "heavy-rain": "أمطار غزيرة",
    "possible-very-light-sleet": "إحتمالية موجة صقيع خفيفة",
    "very-light-sleet": "موجة صقيع خفيفة",
    "possible-light-sleet": "إحتمالية موجة صقيع خفيفة",
    "light-sleet": "موجة صقيع خفيفة",
    "medium-sleet": "صقيع",
    "heavy-sleet": "موجة صقيع شديدة",
    "possible-very-light-snow": "احتمالية تساقط ثلوج خفيفة",
    "very-light-snow": "رياح خفيفة",
    "possible-light-snow": "احتمالية تساقط ثلوج خفيفة",
    "light-snow": "ثلوج خفيفة",
    "medium-snow": "ثلوج",
    "heavy-snow": "ثلوج كثيفة",
    "possible-thunderstorm": "عواصف محتملة",
    "thunderstorm": "عواصف",
    "possible-medium-precipitation": "هطول الأمطار المحتمل",
    "possible-heavy-precipitation": "هطول الأمطار الغزيرة المحتملة",
    "possible-medium-rain": "أمطار محتملة",
    "possible-heavy-rain": "أمطار غزيرة محتملة",
    "possible-medium-sleet": "صقيع محتمل",
    "possible-heavy-sleet": "أمطار ثلجية غزيرة محتملة",
    "possible-medium-snow": "ثلوج محتملة",
    "possible-heavy-snow": "ثلوج كثيفة محتملة",
    "possible-very-light-freezing-rain": "رذاذ متجمد محتمل",
    "very-light-freezing-rain": "رذاذ متجمد",
    "possible-light-freezing-rain": "أمطار خفيفة متجمدة خفيفة محتملة",
    "light-freezing-rain": "أمطار متجمدة خفيفة",
    "possible-medium-freezing-rain": "أمطار متجمدة محتملة",
    "medium-freezing-rain": "أمطار متجمدة",
    "possible-heavy-freezing-rain": "أمطار متجمدة غزيرة محتملة",
    "heavy-freezing-rain": "أمطار متجمدة غزيرة",
    "possible-hail": "بَرَد محتمل",
    "hail": "البَرَد",
    "light-wind": "رياح خفيفة",
    "medium-wind": "رياح متوسطة",
    "heavy-wind": "عواصف",
    "low-humidity": "اجواء جافة",
    "high-humidity": "اجواء رطبة",
    "fog": "اجواء غائمة",
    "very-light-clouds": "واضح في الغالب",
    "light-clouds": "غائم جزئياً",
    "medium-clouds": "اجواء غائمة",
    "heavy-clouds": "اجواء غائمة",
    "today-morning": "هذا الصباح",
    "later-today-morning": "لاحقاً هذا الصباح",
    "today-afternoon": "بعد الظهر",
    "later-today-afternoon": "لاحقاً بعد الظهر",
    "today-evening": "هذا المساء",
    "later-today-evening": "لاحقاً هذا المساء",
    "today-night": "الليلة",
    "later-today-night": "لاحقاً الليلة",
    "tomorrow-morning": "الغد صباحاً",
    "tomorrow-afternoon": "غداً بعد الظهر",
    "tomorrow-evening": "الغد مساءً",
    "tomorrow-night": "الغد ليلاً",
    "morning": "في الصباح",
    "afternoon": "بعد الظهيرة",
    "evening": "في المساء",
    "night": "خلال الليل",
    "today": "اليوم",
    "tomorrow": "غداً",
    "sunday": "يوم الأحد",
    "monday": "يوم الإثنين",
    "tuesday": "يوم الثلاثاء",
    "wednesday": "يوم الأربعاء",
    "thursday": "يوم الخميس",
    "friday": "يوم الجمعة",
    "saturday": "يوم السبت",
    "next-sunday": "الأحد القادم",
    "next-monday": "الإثنين القادم",
    "next-tuesday": "الثلاثاء القادم",
    "next-wednesday": "الأربعاء القادم",
    "next-thursday": "الخميس القادم",
    "next-friday": "الجمعة القادمة",
    "next-saturday": "السبت القادم",
    "minutes": "$1 دقيقة",
    "fahrenheit": "$1\u00b0F",
    "celsius": "$1\u00b0C",
    "inches": "$1 انش",
    "centimeters": "$1 سم",
    "less-than": "أقل من $1",
    "and": and_function,
    "through": through_function,
    "with": "$1 مع $2",
    "range": "$1\u2013$2",
    "parenthetical": parenthetical_function,
    "for-hour": "$1 لهذه الساعة",
    "starting-in": "$1 تبدأ خلال $2",
    "stopping-in": "$1 تتوقف خلال $2",
    "starting-then-stopping-later": "$1 تبدأ خلال $2 وتتوقف لاحقاً خلال $3",
    "stopping-then-starting-later": "$1 تتوقف خلال $2 وتبدأ لاحقاً خلال $3",
    "for-day": "$1 خلال اليوم",
    "starting": "$1 تبدأ $2",
    "until": until_function,
    "until-starting-again": until_starting_again_function,
    "starting-continuing-until": starting_continuing_until_function,
    "during": "$1 $2",
    "for-week": "$1 خلال الأسبوع",
    "over-weekend": "$1 خلال نهاية الأسبوع",
    "temperatures-peaking": "درجات حرارة تبلغ ذروتها عند $1 $2",
    "temperatures-rising": "درجات حرارة ترتفع حتى $1 $2",
    "temperatures-valleying": "انخفاض درجات الحرارة لأدنى مستوى لها عند $1 $2",
    "temperatures-falling": "درجات حرارة تنخفض حتى $1 $2",
    "title": "$1",
    "sentence": "$1",
    "next-hour-forecast-status": "التوقعات للساعة القادمة هي $1 بسبب $2",
    "unavailable": "غير متاح",
    "temporarily-unavailable": "غير متاح مؤقتًا",
    "partially-unavailable": "غير متوفر جزئيًا",
    "station-offline": "جميع محطات الرادار القريبة غير متصلة بالإنترنت",
    "station-incomplete": "فجوات في التغطية من محطات الرادار القريبة",
    "smoke": "دخان",
    "haze": "ضباب",
    "mist": "شبورة",
}
