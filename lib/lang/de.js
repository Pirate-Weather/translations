

function join_with_shared_prefix(a, b, joiner) {
  let i = 0;

  while(i !== a.length &&
        i !== b.length &&
        a.charCodeAt(i) === b.charCodeAt(i))
    ++i;

  while(i && a.charCodeAt(i - 1) !== 32)
    --i;

  return a.slice(0, i) + a.slice(i) + joiner + b.slice(i);
}

function until_time(time) {
  return time === "Abend" ? "bis abends" :
    time === "Nacht" ? "die ganze Nacht" :
      "bis " + time;
}

module.exports = {
  "clear": "Klar",
  "no-precipitation": "kein Niederschlag",
  "mixed-precipitation": "wechselnder Niederschlag",
  "possible-very-light-precipitation": "leichter Niederschlag möglich",
  "very-light-precipitation": "leichter Niederschlag",
  "possible-light-precipitation": "leichter Niederschlag möglich",
  "light-precipitation": "leichter Niederschlag",
  "medium-precipitation": "Niederschlag",
  "heavy-precipitation": "schwerer Niederschlag",
  "possible-very-light-rain": "Nieselregen möglich",
  "very-light-rain": "Nieselregen",
  "possible-light-rain": "leichter Regen möglich",
  "light-rain": "leichter Regen",
  "medium-rain": "Regen",
  "heavy-rain": "Regenschauer",
  "possible-very-light-sleet": "leichter Graupelregen möglich",
  "very-light-sleet": "leichter Graupelregen",
  "possible-light-sleet": "leichter Graupelregen möglich",
  "light-sleet": "leichter Graupelregen",
  "medium-sleet": "Graupelregen",
  "heavy-sleet": "Graupelschauer",
  "possible-very-light-snow": "leichter Schneefall möglich",
  "very-light-snow": "leichter Schneefall",
  "possible-light-snow": "leichter Schneefall möglich",
  "light-snow": "leichter Schneefall",
  "medium-snow": "Schneefall",
  "heavy-snow": "starker Schneefall",
  "possible-thunderstorm": "Gewitter möglich",
  "thunderstorm": "Gewitter",
  "possible-medium-precipitation": "Niederschlag möglich",
  "possible-heavy-precipitation": "schwerer Niederschlag möglich",
  "possible-medium-rain": "Regen möglich",
  "possible-heavy-rain": "Regenschauer möglich",
  "possible-medium-sleet": "Graupelregen möglich",
  "possible-heavy-sleet": "Graupelschauer möglich",
  "possible-medium-snow": "Schneefall möglich",
  "possible-heavy-snow": "starker Schneefall möglich",
  "possible-freezing-drizzle": "gefrierender Nieselregen möglich",
  "freezing-drizzle": "gefrierender Nieselregen",
  "possible-light-freezing-rain": "leichter gefrierender Regen möglich",
  "light-freezing-rain": "leichter gefrierender Regen",
  "possible-freezing-rain": "gefrierender Regen möglich",
  "freezing-rain": "freezing Regen",
  "possible-heavy-freezing-rain": "starker gefrierender Regen möglich",
  "heavy-freezing-rain": "starker gefrierender Regen",
  "possible-hail": "Hagel möglich",
  "hail": "Hagel",
  "light-wind": "leichter Wind",
  "medium-wind": "frische Brise",
  "heavy-wind": "Sturm",
  "low-humidity": "niedrige Luftfeuchtigkeit",
  "high-humidity": "hohe Luftfeuchtigkeit",
  "fog": "Nebel",
  "very-light-clouds": "überwiegend Klar",
  "light-clouds": "leicht bewölkt",
  "medium-clouds": "überwiegend bewölkt",
  "heavy-clouds": "stark bewölkt",
  "today-morning":  "heute Vormittag",
  "later-today-morning": "späteren Vormittag",
  "today-afternoon": "heute Nachmittag",
  "later-today-afternoon": "am späteren Nachmittag",
  "today-evening": "heute Abend",
  "later-today-evening": "späteren Abend",
  "today-night": "heute Nacht",
  "later-today-night": "heute in der späteren Nacht",
  "tomorrow-morning": "morgen Vormittag",
  "tomorrow-afternoon": "morgen Nachmittag",
  "tomorrow-evening": "morgen Abend",
  "tomorrow-night": "morgen Nacht",
  "morning": "Vormittag",
  "afternoon": "Nachmittag",
  "evening": "Abend",
  "night": "Nacht",
  "today": "heute",
  "tomorrow": "morgen",
  "sunday": "am Sonntag",
  "monday": "am Montag",
  "tuesday": "am Dienstag",
  "wednesday": "am Mittwoch",
  "thursday": "am Donnerstag",
  "friday": "am Freitag",
  "saturday": "am Samstag",
  "next-sunday": "am nächsten Sonntag",
  "next-monday": "am nächsten Montag",
  "next-tuesday": "am nächsten Dienstag",
  "next-wednesday": "am nächsten Mittwoch",
  "next-thursday": "am nächsten Donnerstag",
  "next-friday": "am nächsten Freitag",
  "next-saturday": "am nächsten Samstag",
  "minutes": "$1 Min.",
  "fahrenheit": "$1\u00B0F",
  "celsius": "$1\u00B0C",
  "inches": "$1 Zoll",
  "centimeters": "$1 cm",
  "less-than": "weniger als $1",
  "and": function(a, b) {
    return join_with_shared_prefix(
      a,
      b,
      a.indexOf("bis") !== -1 || b.indexOf("bis") !== -1 ? " sowie " : (a.indexOf(",") !== -1 ? ", und " : " und "),
    );
  },
  "through": function(a, b) {
    return join_with_shared_prefix(a.replace("am ", "von "), b.replace("am ", ""), " bis ");
  },
  "with": "$1 mit $2",
  "range": "$1 bis $2",
  "parenthetical": "$1 ($2)",
  "for-hour": "in der kommenden Stunde $1",
  "starting-in": "in $2 $1",
  "stopping-in": "$1, endet in $2",
  "starting-then-stopping-later": "$1 in $2 für $3",
  "stopping-then-starting-later": "$1 endet in $2 und beginnt $3 danach erneut",
  "for-day": "den ganzen Tag lang $1",
  "starting":  function(condition, time) {
    if(this[1] === "starting")
      return time + ((time === "Vormittag" || time === "Nachmittag" || time === "Abend" || time === "Nacht") ? "s" : "") + " " + condition;

    if(this[1] === "and")
      return time + " " + condition;

    return condition + " " + time;
  },
  "until": function(condition, time) {
    return condition + " " + until_time(time);
  },
  "until-starting-again": function(condition, a, b) {
    return condition + " bis zum " + a + (b === "Nacht" ? " und Nacht" : " und " + b + " wieder");
  },
  "starting-continuing-until": function(condition, a, b) {
    if(a === "Abend" && b === "Nacht") {
      return condition + " abends und nächtlich";
    }

    if(a === "Abend") {
      a = "abends ";
    }
    else if(a === "Vormittag") {
      a = "vormittags";
    }
    else if (a === "Mittag") {
      a = "mittags";
    }
    else if (a === "Nachmittag") {
      a = "nachmittags";
    }
    return condition + " von " + a + " " + until_time(b);
  },
  "during": function(condition, time) {
    if(this[1] === "and") {
      return time + " " + condition;
    }

    if(this[1] === "with") {
      return condition + " " + time;
    }

    if(time === "Nacht") {
      return condition + " in der " + time;
    }

    if(time === "heute" || time === "morgen") {
      return condition + " " + time;
    }

    return condition + " am " + time;
  },
  "for-week": "die ganze Woche $1",
  "over-weekend": "$1 am Wochenende",
  "temperatures-peaking": "einem Temperaturmaximum von $1 $2",
  "temperatures-rising": "steigender Temperatur von $1 $2",
  "temperatures-valleying": "einem Temperaturminimum von $1 $2",
  "temperatures-falling": "fallender Temperatur von $1 $2",
  "title": function(str) {
    return str.charAt(0).toUpperCase() + str.slice(1);
  },
  /* Capitalize the first word of the sentence and end with a period. */
  "sentence": function(str) {
    /* Capitalize. */
    str = str.charAt(0).toUpperCase() + str.slice(1);

    /* Add a period if there isn't already one. */
    if(str.charAt(str.length - 1) !== ".")
      str += ".";

    return str;
  },
};
