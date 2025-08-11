def minutes_function(stack, value):
    """
    Returns the given value prefixed with the word "منٹ" (minute in Urdu).

    Parameters:
    - value (str): The value to be prefixed.

    Returns:
    - str: The prefixed value.
    """
    return f"منٹ {value}"


def fahrenheit_function(stack, value):
    """
    Returns the given value prefixed with the phrase "فارن ہائیٹ" (Fahrenheit in Urdu).

    Parameters:
    - value (str): The value to be prefixed.

    Returns:
    - str: The prefixed value.
    """
    return f"فارن ہائیٹ {value}"


def celsius_function(stack, value):
    """
    Returns the given value prefixed with the word "سیلشن" (Celsius in Urdu).

    Parameters:
    - value (str): The value to be prefixed.

    Returns:
    - str: The prefixed value.
    """
    return f"سیلشن {value}"


def inches_function(stack, value):
    """
    Returns the given value prefixed with the word "انچ" (inches in Urdu).

    Parameters:
    - value (str): The value to be prefixed.

    Returns:
    - str: The prefixed value.
    """
    return f"انچ {value}"


def centimeters_function(stack, value):
    """
    Returns the given value prefixed with the word "سینٹی میٹرس" (centimeters in Urdu).

    Parameters:
    - value (str): The value to be prefixed.

    Returns:
    - str: The prefixed value.
    """
    return f"سینٹی میٹرس {value}"


def less_than_function(stack, value):
    """
    Returns the given value prefixed with the phrase "سے کم" (less than in Urdu).

    Parameters:
    - value (str): The value to be prefixed.

    Returns:
    - str: The prefixed value.
    """
    return f"سے کم {value}"


def starting_in_function(stack, first, second):
    """
    Returns a string indicating the start of an event in a specific time frame.

    Parameters:
    - first (str): The first part of the string, typically the time or event.
    - second (str): The second part of the string, typically the unit of time.

    Returns:
    - str: The formatted string.
    """
    return f"شروع ہو رہا {first} میں {second}"


def stopping_in_function(stack, first, second):
    """
    Returns a string indicating the stopping of an event in a specific time frame.

    Parameters:
    - first (str): The first part of the string, typically the time or event.
    - second (str): The second part of the string, typically the unit of time.

    Returns:
    - str: The formatted string.
    """
    return f"رک رہا {first} میں {second}"


def starting_then_stopping_later_function(stack, first, second, third):
    """
    Returns a string indicating that an event starts, then stops later.

    Parameters:
    - first (str): The first part of the string, typically the time or event.
    - second (str): The second part of the string, typically the time.
    - third (str): The third part of the string, typically the event or time.

    Returns:
    - str: The formatted string.
    """
    return f"رک رہا ہے {third} شروع ہو رہا، بعد میں {first} میں {second}"


def stopping_then_starting_later_function(stack, first, second, third):
    """
    Returns a string indicating that an event stops, then starts later.

    Parameters:
    - first (str): The first part of the string, typically the time or event.
    - second (str): The second part of the string, typically the time.
    - third (str): The third part of the string, typically the event or time.

    Returns:
    - str: The formatted string.
    """
    return f"شروع ہو رہا ہے {third} رک رہا، بعد میں {first} میں {second}"


def for_day_function(stack, first):
    """
    Returns a string indicating the event lasts for the entire day.

    Parameters:
    - first (str): The first part of the string, typically the event or activity.

    Returns:
    - str: The formatted string.
    """
    return f"پورے دن {first}"


def starting_function(stack, first, second):
    """
    Returns a string indicating the start of an event in a specific time.

    Parameters:
    - first (str): The first part of the string, typically the event or activity.
    - second (str): The second part of the string, typically the time or unit.

    Returns:
    - str: The formatted string.
    """
    return f"{second} میں {first}"


def until_function(stack, first, second):
    """
    Returns a string indicating that an event continues until a specific time.

    Parameters:
    - first (str): The first part of the string, typically the time.
    - second (str): The second part of the string, typically the event or activity.

    Returns:
    - str: The formatted string.
    """
    return f"{first} تک {second}"


def until_starting_again_function(stack, first, second, third):
    """
    Returns a string indicating that an event will start again after a specific time.

    Parameters:
    - first (str): The first part of the string, typically the time.
    - second (str): The second part of the string, typically the event or activity.
    - third (str): The third part of the string, typically the event or activity starting again.

    Returns:
    - str: The formatted string.
    """
    return f"{third} دوبارہ شروع کر رہا ہے ،{first} تک {second}"


def starting_continuing_until_function(stack, first, second, third):
    """
    Returns a string indicating that an event is continuing until a specific time.

    Parameters:
    - first (str): The first part of the string, typically the time or event.
    - second (str): The second part of the string, typically the time or activity.
    - third (str): The third part of the string, typically the event or activity.

    Returns:
    - str: The formatted string.
    """
    return f"{third} جاری رہا ہے جب تک ،{first} تک {second}"


def during_function(stack, first, second):
    """
    Returns a string indicating that an event is happening during a specific time.

    Parameters:
    - first (str): The first part of the string, typically the time or event.
    - second (str): The second part of the string, typically the event or activity.

    Returns:
    - str: The formatted string.
    """
    return f"کے دوران {second} {first}"


def for_week_function(stack, first):
    """
    Returns a string indicating the event lasts for the entire week.

    Parameters:
    - first (str): The first part of the string, typically the event or activity.

    Returns:
    - str: The formatted string.
    """
    return f"پورے ہفتے {first}"


def over_weekend_function(stack, first):
    """
    Returns a string indicating the event happens over the weekend.

    Parameters:
    - first (str): The first part of the string, typically the event or activity.

    Returns:
    - str: The formatted string.
    """
    return f"ہفتے کے دن پر {first}"


def temperatures_peaking_function(stack, first, second):
    """
    Returns a string indicating that temperatures are peaking during the week.

    Parameters:
    - first (str): The first part of the string, typically the time or event.
    - second (str): The second part of the string, typically the temperature.

    Returns:
    - str: The formatted string.
    """
    return f"ہفتے کے دن پر {second} {first}"


def temperatures_rising_function(stack, first, second):
    """
    Returns a string indicating that temperatures are rising.

    Parameters:
    - first (str): The first part of the string, typically the time or event.
    - second (str): The second part of the string, typically the temperature.

    Returns:
    - str: The formatted string.
    """
    return f"کی طرف تیز درجہ حرارت بڑھ رہا ہے {second} {first}"


def temperatures_valleying_function(stack, first, second):
    """
    Returns a string indicating that temperatures are decreasing.

    Parameters:
    - first (str): The first part of the string, typically the time or event.
    - second (str): The second part of the string, typically the temperature.

    Returns:
    - str: The formatted string.
    """
    return f"کے نیچے تیز درجہ حرارت بن رہا ہے {second} {first}"


def temperatures_falling_function(stack, first, second):
    """
    Returns a string indicating that temperatures are falling.

    Parameters:
    - first (str): The first part of the string, typically the time or event.
    - second (str): The second part of the string, typically the temperature.

    Returns:
    - str: The formatted string.
    """
    return f"کی جانب تیز درجہ حرارت بن رہا ہے {second} {first}"


def and_function(stack, first, second):
    """
    Returns a string joining two parts with the word "اور" (and in Urdu).

    Parameters:
    - first (str): The first part of the string.
    - second (str): The second part of the string.

    Returns:
    - str: The formatted string.
    """
    return f"{second} اور {first}"


def through_function(stack, first, second):
    """
    Returns a string indicating that something happens through a specific event or time.

    Parameters:
    - first (str): The first part of the string, typically the event or time.
    - second (str): The second part of the string, typically the event or activity.

    Returns:
    - str: The formatted string.
    """
    return f"بھر {second}، {first}"


def with_function(stack, first, second):
    """
    Returns a string indicating that something happens with another event or activity.

    Parameters:
    - first (str): The first part of the string, typically the event or activity.
    - second (str): The second part of the string, typically the event or activity.

    Returns:
    - str: The formatted string.
    """
    return f"کے ساتھ {second}، {first}"


template = {
    "clear": "صاف کریں",
    "mostly-clear": "زیادہ تر صاف",
    "no-precipitation": "کوئی ورن نہیں",
    "mixed-precipitation": "مخلوط ورن",
    "possible-very-light-precipitation": "ممکنہ ورن",
    "very-light-precipitation": "ہلکی ورن",
    "possible-light-precipitation": "ممکنہ ہلکی ورن",
    "light-precipitation": "ہلکی ورن",
    "medium-precipitation": "ورن",
    "heavy-precipitation": "بھاری ورن",
    "possible-very-light-rain": "ممکنہ بوندا باندی",
    "very-light-rain": "بوندا باندی",
    "possible-light-rain": "ممکنہ ہلکی بارش",
    "light-rain": "ہلکی بارش",
    "medium-rain": "بارش",
    "heavy-rain": "بھاری بارش",
    "possible-very-light-sleet": "ممکنہ اولے والی بارش",
    "very-light-sleet": "ہلکی اولے والی بارش",
    "possible-light-sleet": "ممکنہ ہلکی اولے والی بارش",
    "light-sleet": "ہلکی اولے والی بارش",
    "medium-sleet": "اولے والی بارش",
    "heavy-sleet": "بھاری اولے والی بارش",
    "possible-very-light-snow": "ممکنہ برف",
    "very-light-snow": "برف",
    "possible-light-snow": "ممکنہ ہلکی برف",
    "light-snow": "ہلکی برف",
    "medium-snow": "برف باری",
    "heavy-snow": "بھاری برف باری",
    "possible-thunderstorm": "ممکنہ برق و باراں",
    "thunderstorm": "برق و باراں",
    "possible-medium-precipitation": "ممکنہ بارش",
    "possible-heavy-precipitation": "ممکنہ بھاری بارش",
    "possible-medium-rain": "ممکنہ بارش",
    "possible-heavy-rain": "ممکنہ شدید بارش",
    "possible-medium-sleet": "ممکنہ اولے",
    "possible-heavy-sleet": "ممکنہ بھاری اولے",
    "possible-medium-snow": "ممکنہ برفباری",
    "possible-heavy-snow": "شدید برفباری کا امکان",
    "possible-very-light-freezing-rain": "ممکنہ منجمد بوندا باندی",
    "very-light-freezing-rain": "جمنے والی بوندا باندی",
    "possible-light-freezing-rain": "ممکنہ ہلکی منجمد بارش",
    "light-freezing-rain": "ہلکی منجمد بارش",
    "possible-medium-freezing-rain": "ممکنہ منجمد بارش",
    "medium-freezing-rain": "منجمد بارش",
    "possible-heavy-freezing-rain": "ممکنہ شدید منجمد بارش",
    "heavy-freezing-rain": "شدید منجمد بارش",
    "possible-hail": "ممکنہ ژالہ باری",
    "hail": "اولے",
    "light-wind": "ہوائی",
    "medium-wind": "طوفانی ہوا",
    "heavy-wind": "خطرناک ہوائی",
    "low-humidity": "روکھا",
    "high-humidity": "نمی",
    "fog": "دھندلا",
    "very-light-clouds": "زیادہ تر واضح",
    "light-clouds": "جزوی طور پر ابر آلود",
    "medium-clouds": "زیادہ تر ابر آلود",
    "heavy-clouds": "ابر آلود",
    "today-morning": "اس صبح",
    "later-today-morning": "بعد میں آج صبح",
    "today-afternoon": "اس دوپہر",
    "later-today-afternoon": "بعد میں اس دوپہر",
    "today-evening": "اس شام",
    "later-today-evening": "بعد میں اس شام",
    "today-night": "اس رات",
    "later-today-night": "بعد میں اس رات",
    "tomorrow-morning": "کل صبح",
    "tomorrow-afternoon": "کل دوپہر",
    "tomorrow-evening": "کل شام",
    "tomorrow-night": "کل رات",
    "morning": "صبح",
    "afternoon": "دوپہر",
    "evening": "شام",
    "night": "رات بھر",
    "today": "آج کے دن",
    "tomorrow": "کل",
    "sunday": "اتوار کو",
    "monday": "پیر کو",
    "tuesday": "منگل کو",
    "wednesday": "بدھ کو",
    "thursday": "جمعرات کو",
    "friday": "جمعہ کو",
    "saturday": "ہفتے کو",
    "next-sunday": "اگلے اتوار",
    "next-monday": "اگلے پیر",
    "next-tuesday": "اگلے منگل",
    "next-wednesday": "اگلے بدھ",
    "next-thursday": "اگلی جمعرات",
    "next-friday": "اگلی جمعہ",
    "next-saturday": "اگلے ہفتے کے دن",
    "minutes": minutes_function,
    "fahrenheit": fahrenheit_function,
    "celsius": celsius_function,
    "inches": inches_function,
    "centimeters": centimeters_function,
    "less-than": less_than_function,
    "and": and_function,
    "through": through_function,
    "with": with_function,
    "for-hour": "$1 ایک گھنٹے کے لئے",
    "starting-in": starting_in_function,
    "stopping-in": stopping_in_function,
    "starting-then-stopping-later": starting_then_stopping_later_function,
    "stopping-then-starting-later": stopping_then_starting_later_function,
    "for-day": for_day_function,
    "starting": starting_function,
    "until": until_function,
    "until-starting-again": until_starting_again_function,
    "starting-continuing-until": starting_continuing_until_function,
    "during": during_function,
    "for-week": for_week_function,
    "over-weekend": over_weekend_function,
    "temperatures-peaking": temperatures_peaking_function,
    "temperatures-rising": temperatures_rising_function,
    "temperatures-valleying": temperatures_valleying_function,
    "temperatures-falling": temperatures_falling_function,
    "range": "$1\u2013$2",
    "title": "$1",
    "sentence": "$1",
    "parenthetical": "$1 ($2)",
    "next-hour-forecast-status": "اگلے گھنٹے کی پیشن گوئی 2$ کی وجہ سے 1$ ہے۔",
    "unavailable": "دستیاب نہیں",
    "temporarily-unavailable": "عارضی طور پر دستیاب نہیں",
    "partially-unavailable": "جزوی طور پر دستیاب نہیں",
    "station-offline": "تمام قریبی ریڈار اسٹیشن آف لائن ہیں۔",
    "station-incomplete": "قریبی ریڈار اسٹیشنوں سے کوریج میں فرق",
    "smoke": "دھواں",
    "haze": "دھند",
    "mist": "دھند",
}
