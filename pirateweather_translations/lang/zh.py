def and_function(stack, a, b):
    """
    Returns a string that concatenates `a` and `b` with a comma, unless `a` ends with a full stop (。).

    If the string `a` ends with a full stop (。), the function concatenates `a` and `b` without a comma.
    Otherwise, it concatenates them with a comma.

    Parameters:
    - a (str): The first string.
    - b (str): The second string to be concatenated with `a`.

    Returns:
    - str: The concatenated string, with or without a comma depending on the condition.
    """
    return a + b if a.endswith("。") else a + "，" + b


def sentence_function(stack, s):
    """
    Ensures that the string `s` ends with a full stop (。).

    If the string `s` already ends with a full stop (。), it returns `s` unchanged.
    Otherwise, it appends a full stop (。) to the end of `s`.

    Parameters:
    - s (str): The input string.

    Returns:
    - str: The input string with a full stop (。) at the end.
    """
    return s if s.endswith("。") else s + "。"


template = {
    "clear": "晴朗",
    "no-precipitation": "无降水",
    "mixed-precipitation": "多云转雨",
    "possible-very-light-precipitation": "可能有少量降水",
    "very-light-precipitation": "少量降水",
    "possible-light-precipitation": "可能有少量降水",
    "light-precipitation": "少量降水",
    "medium-precipitation": "中度降水",
    "heavy-precipitation": "大量降水",
    "possible-very-light-rain": "可能有毛毛雨",
    "very-light-rain": "毛毛雨",
    "possible-light-rain": "可能有小雨",
    "light-rain": "小雨",
    "medium-rain": "降雨",
    "heavy-rain": "倾盆大雨",
    "possible-very-light-sleet": "可能有较小的雨夹雪",
    "very-light-sleet": "轻微的雨夹雪",
    "possible-light-sleet": "可能有轻微雨夹雪",
    "light-sleet": "轻微的雨夹雪",
    "medium-sleet": "雨夹雪",
    "heavy-sleet": "较强的雨夹雪",
    "possible-very-light-snow": "可能有轻微降雪",
    "very-light-snow": "轻微降雪",
    "possible-light-snow": "可能有小雪",
    "light-snow": "小雪",
    "medium-snow": "降雪",
    "heavy-snow": "鹅毛大雪",
    "light-wind": "微风",
    "medium-wind": "有风",
    "heavy-wind": "推人大风",
    "low-humidity": "干燥",
    "high-humidity": "潮湿",
    "fog": "有雾",
    "very-light-clouds": "大部分時間晴朗",
    "light-clouds": "局部多云",
    "medium-clouds": "多云",
    "heavy-clouds": "多云转阴",
    "possible-thunderstorm": "可能有雷暴",
    "thunderstorm": "雷暴",
    "possible-medium-precipitation": "可能有中度降水",
    "possible-heavy-precipitation": "可能有大量降水",
    "possible-medium-rain": "可能有降雨",
    "possible-heavy-rain": "可能有倾盆大雨",
    "possible-medium-sleet": "可能有雨夹雪",
    "possible-heavy-sleet": "可能有较强的雨夹雪",
    "possible-medium-snow": "可能有降雪",
    "possible-heavy-snow": "可能有鹅毛大雪",
    "possible-very-light-freezing-rain": "可能有冻毛毛雨",
    "very-light-freezing-rain": "冻毛毛雨",
    "possible-light-freezing-rain": "可能有小冻雨",
    "light-freezing-rain": "小冻雨",
    "possible-medium-freezing-rain": "可能有冻雨",
    "medium-freezing-rain": "冻雨",
    "possible-heavy-freezing-rain": "可能有大冻雨",
    "heavy-freezing-rain": "大冻雨",
    "possible-hail": "可能有冰雹",
    "hail": "冰雹",
    "today-morning": "今天早上",
    "later-today-morning": "今天上午晚些时候",
    "today-afternoon": "今天下午",
    "later-today-afternoon": "午后",
    "today-evening": "今晚",
    "later-today-evening": "今天夜里",
    "today-night": "明晚",
    "later-today-night": "今天夜里",
    "tomorrow-morning": "明天上午",
    "tomorrow-afternoon": "明天下午",
    "tomorrow-evening": "明晚",
    "tomorrow-night": "明晚",
    "morning": "早上",
    "afternoon": "下午",
    "evening": "晚上",
    "night": "当晚",
    "today": "今天",
    "tomorrow": "明天",
    "sunday": "周日",
    "monday": "周一",
    "tuesday": "周二",
    "wednesday": "周三",
    "thursday": "周四",
    "friday": "周五",
    "saturday": "周六",
    "minutes": "$1分钟",
    "next-sunday": "下周日",
    "next-monday": "下周一",
    "next-tuesday": "下周二",
    "next-wednesday": "下周三",
    "next-thursday": "下周四",
    "next-friday": "下周五",
    "next-saturday": "下周六",
    "fahrenheit": "$1\u00b0F",
    "celsius": "$1\u00b0C",
    "inches": "$1英寸",
    "centimeters": "$1厘米",
    "less-than": "低于$1",
    "and": and_function,
    "through": "$1直至$2",
    "through": "$1直至$2",
    "with": "$1，且$2",
    "range": "$1\u2013$2",
    "parenthetical": "$1($2)",
    "for-hour": "在接下来一个小时内$1。",
    "starting-in": "$1将于$2后开始。",
    "stopping-in": "$1将于$2后结束。",
    "starting-then-stopping-later": "$1将于$2后开始，并在之后的$3结束。",
    "stopping-then-starting-later": "$1将于$2后结束，而在之后的$3又将继续。",
    "for-day": "$1将持续一整天。",
    "starting": "$1开始于$2。",
    "until": "$1将持续至$2",
    "until-starting-again": "$1直到$2，将于$3再次出现",
    "starting-continuing-until": "$1开始于$2，将持续至$3",
    "during": "$1持续至$2",
    "for-week": "$1持续一整周",
    "over-weekend": "$1持续一整周",
    "temperatures-peaking": "$2温度剧增到$1",
    "temperatures-rising": "$2升温到$1",
    "temperatures-valleying": "$2温度骤降到$1",
    "temperatures-falling": "$2温度下降到$1",
    "title": "$1",
    "sentence": sentence_function,
    "next-hour-forecast-status": "下一小時的預測是$1，因為$2",
    "unavailable": "不可用",
    "temporarily-unavailable": "暫時無法使用",
    "partially-unavailable": "部分不可用",
    "station-offline": "附近所有雷達站均處於離線狀態",
    "station-incomplete": "附近雷達站覆蓋範圍的缺口",
}
