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

    If the string `a` already ends with a full stop (。), it returns `s` unchanged.
    Otherwise, it appends a full stop (。) to the end of `s`.

    Parameters:
    - s (str): The input string.

    Returns:
    - str: The input string with a full stop (。) at the end.
    """
    return s if s.endswith("。") else s + "。"


template = {
    "clear": "晴朗",
    "mostly-clear": "大部分晴朗",
    "no-precipitation": "無降水",
    "mixed-precipitation": "多雲轉雨",
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
    "heavy-rain": "傾盆大雨",
    "possible-very-light-sleet": "可能有較小的雨夾雪",
    "very-light-sleet": "輕微的雨夾雪",
    "possible-light-sleet": "可能有輕微雨夾雪",
    "light-sleet": "輕微的雨夾雪",
    "medium-sleet": "雨夾雪",
    "heavy-sleet": "較強的雨夾雪",
    "possible-very-light-snow": "可能有輕微降雪",
    "very-light-snow": "輕微降雪",
    "possible-light-snow": "可能有小雪",
    "light-snow": "小雪",
    "medium-snow": "降雪",
    "heavy-snow": "鵝毛大雪",
    "possible-thunderstorm": "可能有雷暴",
    "thunderstorm": "雷暴",
    "possible-medium-precipitation": "可能有中度降水",
    "possible-heavy-precipitation": "可能有大量降水",
    "possible-medium-rain": "可能有降雨",
    "possible-heavy-rain": "可能有傾盆大雨",
    "possible-medium-sleet": "可能有雨夾雪",
    "possible-heavy-sleet": "可能有較強的雨夾雪",
    "possible-medium-snow": "可能有降雪",
    "possible-heavy-snow": "可能有鵝毛大雪",
    "possible-very-light-freezing-rain": "可能有凍毛毛雨",
    "very-light-freezing-rain": "凍毛毛雨",
    "possible-light-freezing-rain": "可能有小凍雨",
    "light-freezing-rain": "小凍雨",
    "possible-medium-freezing-rain": "可能有凍雨",
    "medium-freezing-rain": "凍雨",
    "possible-heavy-freezing-rain": "可能有大凍雨",
    "heavy-freezing-rain": "大凍雨",
    "possible-hail": "可能有冰雹",
    "hail": "冰雹",
    "light-wind": "微風",
    "medium-wind": "有風",
    "heavy-wind": "推人大風",
    "low-humidity": "乾燥",
    "high-humidity": "潮濕",
    "fog": "有霧",
    "very-light-clouds": "基本晴朗",
    "light-clouds": "局部多雲",
    "medium-clouds": "多雲",
    "heavy-clouds": "多雲轉陰",
    "today-morning": "今天早上",
    "later-today-morning": "今天上午晚些時候",
    "today-afternoon": "今天下午",
    "later-today-afternoon": "午後",
    "today-evening": "今晚",
    "later-today-evening": "今天夜裡",
    "today-night": "明晚",
    "later-today-night": "今天夜裡",
    "tomorrow-morning": "明天上午",
    "tomorrow-afternoon": "明天下午",
    "tomorrow-evening": "明晚",
    "tomorrow-night": "明晚",
    "morning": "早上",
    "afternoon": "下午",
    "evening": "晚上",
    "night": "當晚",
    "today": "今天",
    "tomorrow": "明天",
    "sunday": "周日",
    "monday": "周一",
    "tuesday": "周二",
    "wednesday": "周三",
    "thursday": "周四",
    "friday": "周五",
    "saturday": "周六",
    "next-sunday": "下周日",
    "next-monday": "下周一",
    "next-tuesday": "下周二",
    "next-wednesday": "下周三",
    "next-thursday": "下周四",
    "next-friday": "下周五",
    "next-saturday": "下周六",
    "minutes": "$1分鐘",
    "fahrenheit": "$1\u00b0F",
    "celsius": "$1\u00b0C",
    "inches": "$1英寸",
    "centimeters": "$1釐米",
    "less-than": "低於$1",
    "and": and_function,
    "through": "$1直至$2",
    "with": "$1，且$2",
    "range": "$1\u2013$2",
    "parenthetical": "$1($2)",
    "for-hour": "在接下來一個小時內$1。",
    "starting-in": "$1將於$2後開始。",
    "stopping-in": "$1將於$2後結束。",
    "starting-then-stopping-later": "$1將於$2後開始，並在之後的$3結束。",
    "stopping-then-starting-later": "$1將於$2後結束，而在之後的$3又將繼續。",
    "for-day": "$1將持續一整天。",
    "starting": "$1開始於$2。",
    "until": "$1將持續至$2",
    "until-starting-again": "$1直到$2，將於$3再次出現",
    "starting-continuing-until": "$1開始於$2，將持續至$3",
    "during": "$1持續至$2",
    "for-week": "$1持續一整周",
    "over-weekend": "$1持續一整周",
    "temperatures-peaking": "$2溫度劇增到$1",
    "temperatures-rising": "$2升溫到$1",
    "temperatures-valleying": "$2溫度驟降到$1",
    "temperatures-falling": "$2溫度下降到$1",
    "title": "$1",
    "sentence": sentence_function,
    "next-hour-forecast-status": "下一小时的预测是$1，因为$2",
    "unavailable": "不可用",
    "temporarily-unavailable": "暂时不可用",
    "partially-unavailable": "部分不可用",
    "station-offline": "附近所有雷达站均处于离线状态",
    "station-incomplete": "附近雷达站覆盖范围的缺口",
    "smoke": "煙",
    "haze": "霾",
    "mist": "薄霧",
}
