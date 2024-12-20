

function in_the(period) {
  if (period === "myttin" || period === "dohajydh" || period === "gorthugher" || period === "nos") {
    return " y'n " + period;
  }
  if (period === "an dohajydh ma" || period === "an nos ma") {
    return " y'n " + period.slice(3);
  }
  if ("123456789".indexOf(period.charAt(0)) !== -1) {
    return " yn " + period;
  }
  return " " + period;
}

function until_the(period) {
  if (period === "myttin" || period === "dohajydh" || period === "gorthugher" || period === "nos") {
    return " bys y'n " + period;
  }
  if (period === "an dohajydh ma" || period === "an nos ma") {
    return " bys y'n " + period.slice(3);
  }
  return " bys yn " + period;
}

module.exports = {
  "clear": "kler",
  "no-precipitation": "kodhans vyth",
  "mixed-precipitation": "kodhans kemyskys",
  "possible-very-light-precipitation": "kodhans skav possybyl",
  "very-light-precipitation": "kodhans pur skav",
  "possible-light-precipitation": "kodhans skav possybyl",
  "light-precipitation": "kodhans skav",
  "medium-precipitation": "kodhans",
  "heavy-precipitation": "kodhans poos",
  "possible-very-light-rain": "glaw skav possybyl",
  "very-light-rain": "glaw pur skav",
  "possible-light-rain": "glaw skav possybyl",
  "light-rain": "glaw skav",
  "medium-rain": "glaw",
  "heavy-rain": "glaw poos",
  "possible-very-light-sleet": "erghlaw skav possybyl",
  "very-light-sleet": "erghlaw pur skav",
  "possible-light-sleet": "erghlaw skav possybyl",
  "light-sleet": "erghlaw skav",
  "medium-sleet": "erghlaw",
  "heavy-sleet": "erghlaw poos",
  "possible-very-light-snow": "ergh skav possybyl",
  "very-light-snow": "ergh pur skav",
  "possible-light-snow": "ergh skav possybyl",
  "light-snow": "ergh skav",
  "medium-snow": "ergh",
  "heavy-snow": "ergh poos",
  "possible-thunderstorm": "tewedhow-taran possybyl",
  "thunderstorm": "tewedhow-taran",
  "possible-medium-precipitation": "kodhans possybyl",
  "possible-heavy-precipitation": "kodhans poos possybyl",
  "possible-medium-rain": "glaw possybyl",
  "possible-heavy-rain": "glaw poos possybyl",
  "possible-medium-sleet": "erghlaw possybyl",
  "possible-heavy-sleet": "erghlaw poos possybyl",
  "possible-medium-snow": "ergh possybyl",
  "possible-heavy-snow": "ergh poos possybyl",
  "possible-freezing-drizzle": "glaw rewl pur skav possybyl",
  "freezing-drizzle": "glaw rewl pur skav",
  "possible-light-freezing-rain": "glaw rewl skav possybyl",
  "light-freezing-rain": "glaw rewl skav",
  "possible-freezing-rain": "glaw rewl possybyl",
  "freezing-rain": "glaw rewl",
  "possible-heavy-freezing-rain": "glaw rewl poos possybyl",
  "heavy-freezing-rain": "glaw rewl poos",
  "possible-hail": "storm hael possybyl",
  "hail": "storm hael",
  "light-wind": "nebes gwynsek",
  "medium-wind": "gwynsek",
  "heavy-wind": "gwynsek bys yn peryl",
  "low-humidity": "sygh",
  "high-humidity": "glyb",
  "fog": "niwlek",
  "very-light-clouds": "soprattuttu chjaru",
  "light-clouds": "nebes komolek",
  "medium-clouds": "komolek",
  "heavy-clouds": "komolek poos",
  "today-morning": "hedhyw vyttin",
  "later-today-morning": "diwettha hedhyw vyttin",
  "today-afternoon": "an dohajydh ma",
  "later-today-afternoon": "diwettha an dohajydh ma",
  "today-evening": "haneth",
  "later-today-evening": "diwettha haneth",
  "today-night": "an nos ma",
  "later-today-night": "diwettha haneth",
  "tomorrow-morning": "ternos vyttin",
  "tomorrow-afternoon": "dohajydhweyth a-vorow",
  "tomorrow-evening": "gorthugherweyth a-vorow",
  "tomorrow-night": "nosweyth a-vorow",
  "morning": "myttin",
  "afternoon": "dohajydh",
  "evening": "gorthugher",
  "night": "nos",
  "today": "hedhyw",
  "tomorrow": "a-vorow",
  "sunday": "dy' Sul",
  "monday": "dy' Lun",
  "tuesday": "dy' Meurth",
  "wednesday": "dy' Mergher",
  "thursday": "dy' Yow",
  "friday": "dy' Gwener",
  "saturday": "dy' Sadorn",
  "next-sunday": "dy' Sul a dheu",
  "next-monday": "dy' Lun a dheu",
  "next-tuesday": "dy' Meurth a dheu",
  "next-wednesday": "dy' Mergher a dheu",
  "next-thursday": "dy' Yow a dheu",
  "next-friday": "dy' Gwener a dheu",
  "next-saturday": "dy' Sadorn a dheu",
  "minutes": "$1 myn.",
  "fahrenheit": "$1\u00B0F",
  "celsius": "$1\u00B0C",
  "inches": "$1 mv.",
  "centimeters": "$1 cm.",
  "less-than": "le ages $1",
  "and": function(a, b) {
    let andy = a.indexOf(",") !== -1 ? ", ha" : " ha";
    if (b.charAt(0) === "a" || b.charAt(0) === "e" || b.charAt(0) === "i" || b.charAt(0) === "o" || b.charAt(0) === "u") {
      andy = andy + "g";
    }

    return a + andy + " " + b;
  },
  "through": function(a, b) {
    return a + until_the(b);
  },
  "with": "$1, gans $2",
  "range": "$1\u2013$2",
  "parenthetical": function(a, b) {
    return a + " (" + b + (a === "kodhans kemyskys" ? " a ergh)" : ")");
  },
  "for-hour": "$1 rag an our",
  "starting-in": function(condition, period) {
    return condition + " ow talleth" + in_the(period);
  },
  "stopping-in": function(condition, period) {
    return condition + " ow hedhi" + in_the(period);
  },
  "starting-then-stopping-later": function(condition, period1, period2) {
    return condition + " ow talleth" + in_the(period1) + ", ow hedhi " + period2 + " diwettha";
  },
  "stopping-then-starting-later": function(condition, period1, period2) {
    return condition + " ow hedhi" + in_the(period1) + ", ow tastalleth " + period2 + " diwettha";
  },
  "for-day": "$1 dres oll an jydh",
  "starting": function(condition, period) {
    return condition + " ow talleth" + in_the(period);
  },
  "until": function(condition, period) {
    return condition + until_the(period);
  },
  "until-starting-again": function(condition, a, b) {
    return condition + until_the(a) + ", ow tastalleth" + in_the(b);
  },
  "starting-continuing-until": function(condition, a, b) {
    return condition + " ow talleth" + in_the(a) + ", ow pesya" + until_the(b);
  },
  "during": function(condition, period) {
    return condition + in_the(period);
  },
  "for-week": "$1 dres oll an seythun",
  "over-weekend": "$1 dres an bennseythun",
  "temperatures-peaking": "ughella tempredhow a $1 $2",
  "temperatures-rising": "tempredhow ow kressya dhe $1 $2",
  "temperatures-valleying": "tempredhow ow hedhi kodha dhe $1 $2",
  "temperatures-falling": "tempredhow ow kodha dhe $1 $2",
  // Capitalize the first letter of every word, except if that word is
  // "and". (This is a very crude bastardization of proper English titling
  // rules, but it is adequate for the purposes of this module.)
  "title": function(str) {
    return str.replace(
      /\b(?:a(?!nd\b)|c(?!m\.)|i(?!n\.)|[^\Waci])/g,
      function(letter) {
        return letter.toUpperCase();
      },
    );
  },
  /* Capitalize the first word of the sentence and end with a period. */
  "sentence": function(str) {
    /* Capitalize. */
    str = str.charAt(0).toUpperCase() + str.slice(1);

    /* Add a period if there isn't already one. */
    if (str.charAt(str.length - 1) !== ".")
      str += ".";

    return str;
  },
  "next-hour-forecast-status": "Darganow herwydh an our yw $1 drefen bos $2.",
  "unavailable": "ankavadow",
  "temporarily-unavailable": "ankavadow dres pols",
  "partially-unavailable": "ankavadow yn rann",
  "station-offline": "pub gorsav radar y'n ranndir dhywarlinen",
  "station-incomplete": "aswaow y'n gorherans dhyworth gorsavow radar y'n ranndir",
};
