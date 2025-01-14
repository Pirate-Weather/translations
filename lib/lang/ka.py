def parenthetical_function(stack, a, b):
    return f"{a} ({b}{' თოვლის გარეშე)' if a == 'ცვალებადი ნალექი' else ')'}"


def sentence_function(stack, s):
    if not s.endswith("."):
        s += "."
    return s


template = {
    "clear": "მოწმენდილი",
    "no-precipitation": "უნალექო",
    "mixed-precipitation": "ცვალებადი ნალექი",
    "possible-very-light-precipitation": "მოსალოდნელია სუსტი ნალექი",
    "very-light-precipitation": "სუსტი ნალექი",
    "possible-light-precipitation": "მოსალოდნელია მცირე ნალექი",
    "light-precipitation": "მცირე ნალექი",
    "medium-precipitation": "ნალექი",
    "heavy-precipitation": "ძლიერი ნალექი",
    "possible-very-light-rain": "მოსალოდნელია სუსტი წვიმა",
    "very-light-rain": "სუსტი წვიმა",
    "possible-light-rain": "მოსალოდნელია მცირე წვიმა",
    "light-rain": "მცირე წვიმა",
    "medium-rain": "წვიმა",
    "heavy-rain": "ძლიერი წვიმა",
    "possible-very-light-sleet": "მოსალოდნელია სუსტი თოვლჭყაპი",
    "very-light-sleet": "სუსტი თოვლჭყაპი",
    "possible-light-sleet": "მოსალოდნელია მცირე თოვლჭყაპი",
    "light-sleet": "მცირე თოვლჭყაპი",
    "medium-sleet": "თოვლჭყაპი",
    "heavy-sleet": "ძლიერი თოვლჭყაპი",
    "possible-very-light-snow": "მოსალოდნელია სუსტი თოვლი",
    "very-light-snow": "სუსტი თოვლი",
    "possible-light-snow": "მოსალოდნელია მცირე თოვლი",
    "light-snow": "მცირე თოვლი",
    "medium-snow": "თოვლი",
    "heavy-snow": "ძლიერი თოვლი",
    "possible-thunderstorm": "მოსალოდნელია ჭექა-ქუხილი",
    "thunderstorm": "ჭექა-ქუხილი",
    "possible-medium-precipitation": "მოსალოდნელია ნალექი",
    "possible-heavy-precipitation": "მოსალოდნელია ძლიერი ნალექი",
    "possible-medium-rain": "მოსალოდნელია წვიმა",
    "possible-heavy-rain": "მოსალოდნელია ძლიერი წვიმა",
    "possible-medium-sleet": "მოსალოდნელია თოვლჭყაპი",
    "possible-heavy-sleet": "მოსალოდნელია ძლიერი თოვლჭყაპი",
    "possible-medium-snow": "მოსალოდნელია თოვლი",
    "possible-heavy-snow": "მოსალოდნელია ძლიერი თოვლი",
    "possible-very-light-freezing-rain": "მოსალოდნელია გაყინული სუსტი წვიმა",
    "very-light-freezing-rain": "გაყინული სუსტი წვიმა",
    "possible-light-freezing-rain": "მოსალოდნელია მცირე გაყინული წვიმა",
    "light-freezing-rain": "მცირე გაყინული წვიმა",
    "possible-medium-freezing-rain": "მოსალოდნელია გაყინული წვიმა",
    "medium-freezing-rain": "გაყინული წვიმა",
    "possible-heavy-freezing-rain": "მოსალოდნელია ძლიერი გაყინული წვიმა",
    "heavy-freezing-rain": "ძლიერი გაყინული წვიმა",
    "possible-hail": "მოსალოდნელია სეტყვა",
    "hail": "სეტყვა",
    "light-wind": "სუსტი ქარი",
    "medium-wind": "ქარი",
    "heavy-wind": "ძლიერი ქარი",
    "low-humidity": "მშრალი",
    "high-humidity": "ტენიანი",
    "fog": "ნისლი",
    "very-light-clouds": "უმეტესად მოწმენდილი",
    "light-clouds": "ნაწილობრივ ღრუბლიანი",
    "medium-clouds": "უმეტესად ღრუბლიანი",
    "heavy-clouds": "მოღრუბლულობა",
    "today-morning": "დილით",
    "later-today-morning": "დღეს დილით",
    "today-afternoon": "შუადღეს",
    "later-today-afternoon": "ნაშუადღევს",
    "today-evening": "საღამოს",
    "later-today-evening": "ამ საღამოს",
    "today-night": "ღამე",
    "later-today-night": "გვიან ღამით",
    "tomorrow-morning": "ხვალ დილით",
    "tomorrow-afternoon": "ხვალ შუადღეს",
    "tomorrow-evening": "ხვალ საღამოს",
    "tomorrow-night": "ხვალ ღამით",
    "morning": "დილას",
    "afternoon": "შუადღეს",
    "evening": "საღამოს",
    "night": "ღამე",
    "today": "დღეს",
    "tomorrow": "ხვალ",
    "sunday": "კვირას",
    "monday": "ორშაბათს",
    "tuesday": "სამშაბათს",
    "wednesday": "ოთხშაბათს",
    "thursday": "ხუთშაბათს",
    "friday": "პარასკევს",
    "saturday": "შაბათს",
    "next-sunday": "შემდეგ კვირას",
    "next-monday": "შემდეგ ორშაბათს",
    "next-tuesday": "შემდეგ სამშაბათს",
    "next-wednesday": "შემდეგ ოთხშაბათს",
    "next-thursday": "შემდეგ ხუთშაბათს",
    "next-friday": "შემდეგ პარასკევს",
    "next-saturday": "შემდეგ შაბათს",
    "minutes": "$1 წთ.",
    "fahrenheit": "$1\u00b0F",
    "celsius": "$1\u00b0C",
    "inches": "$1 ინ.",
    "centimeters": "$1 სმ.",
    "less-than": "< $1",
    "and": "$1 და $2",
    "through": "$1 $2",
    "with": "$1, $2",
    "range": "$1\u2013$2",
    "parenthetical": parenthetical_function,
    "for-hour": "$1 ამ დროისთვის",
    "starting-in": "$1 დაიწყება $2",
    "stopping-in": "$1 შეწყდება $2",
    "starting-then-stopping-later": "$1 დაიწყება $2, შეწყდება $3 მოგვიანებით",
    "stopping-then-starting-later": "$1 შეწყდება $2, დაიწყება კვლავ $3 მოგვიანებით",
    "for-day": "$1 მთელი დღის განმავლობაში",
    "starting": "$1 დაიწყება $2",
    "until": "$1 გაგრძელდება $2",
    "until-starting-again": "$1 $2, დაიწყება კვლავ $3",
    "starting-continuing-until": "$1 დაიწყება $2, გაგრძელდება $3",
    "during": "$1 $2",
    "for-week": "$1 მთელი კვირის განმავლობაში",
    "over-weekend": "$1 შაბათ-კვირას",
    "temperatures-peaking": "ტემპერატურა პიკს აღწევს $1 $2",
    "temperatures-rising": "ტემპერატურა მოიმატებს $1 $2",
    "temperatures-valleying": "ტემპერატურა დაიწევს $1 $2",
    "temperatures-falling": "ტემპერატურა დაეცემა $1 $2",
    "title": "$1",
    "sentence": sentence_function,
    "next-hour-forecast-status": "next hour forecasts are $1 due to $2",
    "unavailable": "unavailable",
    "temporarily-unavailable": "temporarily unavailable",
    "partially-unavailable": "partially unavailable",
    "station-offline": "all nearby radar stations being offline",
    "station-incomplete": "gaps in coverage from nearby radar stations",
}
