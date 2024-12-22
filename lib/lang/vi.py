def join_with_shared_prefix(a, b, joiner):
    """
    Joins two strings (`a` and `b`) using a shared prefix with a specified joiner.

    This function compares the characters of `a` and `b` from the start, finding the longest common prefix
    and then joins them with a specified joiner.

    Parameters:
    - a (str): The first string to join.
    - b (str): The second string to join.
    - joiner (str): The string used to join the two strings.

    Returns:
    - str: The two strings joined together using the common prefix and the joiner.
    """
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

    return a[:i] + a[i:] + joiner + b[i:]


def and_function(stack, a, b):
    return join_with_shared_prefix(a, b, ", và " if "," in a else " và ")


def through_function(stack, a, b):
    return join_with_shared_prefix(a, b, " cho tới ")


def parenthetical_function(stack, a, b):
    """
    Returns a string formatted as 'a (b)', with a conditional suffix if 'a' equals "mưa rải rác".

    If the input 'a' is "mưa rải rác", the function appends " tuyết)" to the string, otherwise it appends ")".

    Parameters:
    - a (str): The first part of the string.
    - b (str): The second part of the string to be enclosed in parentheses.

    Returns:
    - str: The formatted string with parentheses and a conditional suffix.
    """
    if a == "mưa rải rác":
        return f"{a} ({b} tuyết)"
    else:
        return f"{a} ({b})"


def sentence_function(stack, s):
    """
    Capitalize the first word of the sentence and end with a period.
    """
    s = s[0].upper() + s[1:]
    if not s.endswith("."):
        s += "."
    return s


template = {
    "clear": "quang mây",
    "no-precipitation": "không mưa",
    "mixed-precipitation": "mưa rải rác",
    "possible-very-light-precipitation": "có thể có mưa nhỏ",
    "very-light-precipitation": "mưa nhỏ",
    "possible-light-precipitation": "có thể có mưa nhẹ",
    "light-precipitation": "lượng mưa nhỏ",
    "medium-precipitation": "lượng mưa trung bình",
    "heavy-precipitation": "lượng mưa lớn",
    "possible-very-light-rain": "có thể có mưa phùn",
    "very-light-rain": "mưa phùn",
    "possible-light-rain": "có thể có mưa nhỏ",
    "light-rain": "mưa nhỏ",
    "medium-rain": "mưa vừa",
    "heavy-rain": "mưa to",
    "possible-very-light-sleet": "có thể tuyết rơi nhỏ",
    "very-light-sleet": "mưa tuyết nhỏ",
    "possible-light-sleet": "có thể có mưa tuyết nhỏ",
    "light-sleet": "mưa tuyết nhỏ",
    "medium-sleet": "mưa tuyết vừa",
    "heavy-sleet": "mưa tuyết to",
    "possible-very-light-snow": "có thể có tuyết rơi nhỏ",
    "very-light-snow": "tuyết rơi rất nhỏ",
    "possible-light-snow": "có thể có tuyết rơi nhỏ",
    "light-snow": "tuyết rơi nhỏ",
    "medium-snow": "tuyết rơi",
    "heavy-snow": "tuyết rơi nhiều",
    "possible-thunderstorm": "có thể có dông",
    "thunderstorm": "có dông",
    "possible-medium-precipitation": "possible precipitation",
    "possible-heavy-precipitation": "possible heavy precipitation",
    "possible-medium-rain": "possible rain",
    "possible-heavy-rain": "possible heavy rain",
    "possible-medium-sleet": "possible sleet",
    "possible-heavy-sleet": "possible heavy sleet",
    "possible-medium-snow": "possible snow",
    "possible-heavy-snow": "possible heavy snow",
    "possible-freezing-drizzle": "possible freezing drizzle",
    "freezing-drizzle": "freezing drizzle",
    "possible-light-freezing-rain": "possible light freezing rain",
    "light-freezing-rain": "light freezing rain",
    "possible-freezing-rain": "possible freezing rain",
    "freezing-rain": "freezing rain",
    "possible-heavy-freezing-rain": "possible heavy freezing rain",
    "heavy-freezing-rain": "heavy freezing rain",
    "possible-hail": "possible hail",
    "hail": "hail",
    "light-wind": "gió nhẹ",
    "medium-wind": "có gió",
    "heavy-wind": "gió to",
    "low-humidity": "trời hanh khô",
    "high-humidity": "độ ẩm cao",
    "fog": "có sương mù",
    "very-light-clouds": "có quang mây",
    "light-clouds": "ít mây",
    "medium-clouds": "có mây",
    "heavy-clouds": "trời âm u",
    "today-morning": "sáng nay",
    "later-today-morning": "cuối buổi sáng",
    "today-afternoon": "trưa nay",
    "later-today-afternoon": "chiều hôm nay",
    "today-evening": "chiều tối nay",
    "later-today-evening": "tối hôm nay",
    "today-night": "đêm nay",
    "later-today-night": "nửa đêm",
    "tomorrow-morning": "sáng mai",
    "tomorrow-afternoon": "trưa mai",
    "tomorrow-evening": "chiều tối mai",
    "tomorrow-night": "tối mai",
    "morning": "buổi sáng",
    "afternoon": "buổi chiều",
    "evening": "buổi tối",
    "night": "đêm",
    "today": "hôm nay",
    "tomorrow": "ngày mai",
    "sunday": "chủ nhật",
    "monday": "thứ hai",
    "tuesday": "thứ ba",
    "wednesday": "thứ tư",
    "thursday": "thứ năm",
    "friday": "thứ sáu",
    "saturday": "thứ bảy",
    "next-sunday": "chủ nhật tuần sau",
    "next-monday": "thứ hai tuần sau",
    "next-tuesday": "thứ ba tuần sau",
    "next-wednesday": "thứ tư tuần sau",
    "next-thursday": "thứ năm tuần sau",
    "next-friday": "thứ sáu tuần sau",
    "next-saturday": "thứ bảy tuần sau",
    "minutes": "$1 phút",
    "fahrenheit": "$1\u00b0F",
    "celsius": "$1\u00b0C",
    "inches": "$1 in",
    "centimeters": "$1 cm",
    "less-than": "dưới $1",
    "and": and_function,
    "through": through_function,
    "with": "$1, với $2",
    "range": "$1\u2013$2",
    "parenthetical": parenthetical_function,
    "for-hour": "$1 trong một giờ",
    "starting-in": "$1 bắt đầu sau $2",
    "stopping-in": "$1 dừng sau $2",
    "starting-then-stopping-later": "$1 bắt đầu sau $2, dừng lại $3 sau",
    "stopping-then-starting-later": "$1 dừng sau $2, tiếp tục $3 sau",
    "for-day": "$1 suốt cả ngày",
    "starting": "$1 bắt đầu lúc $2",
    "until": "$1 cho đến $2",
    "until-starting-again": "$1 cho đến $2, bắt đầu lại $3",
    "starting-continuing-until": "$1 bắt đầu lúc $2, tiếp tục tới $3",
    "during": "$1 vào $2",
    "for-week": "$1 cả tuần",
    "over-weekend": "$1 suốt cuốt tuần",
    "temperatures-peaking": "nhiệt độ đỉnh điểm $1 vào $2",
    "temperatures-rising": "nhiệt độ tăng tới $1 vào $2",
    "temperatures-valleying": "nhiệt độ thấp nhất $1 vào $2",
    "temperatures-falling": "nhiệt độ giảm tới $1 vào $2",
    "title": "$1",
    "sentence": sentence_function,
    "next-hour-forecast-status": "next hour forecasts are $1 due to $2",
    "unavailable": "unavailable",
    "temporarily-unavailable": "temporarily unavailable",
    "partially-unavailable": "partially unavailable",
    "station-offline": "all nearby radar stations being offline",
    "station-incomplete": "gaps in coverage from nearby radar stations",
}
