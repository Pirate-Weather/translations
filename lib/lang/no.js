

function join_with_shared_prefix(a, b, joiner) {
  let i = 0;

  while(i !== a.length &&
        i !== b.length &&
        a.charCodeAt(i) === b.charCodeAt(i))
    ++i;

  while(i && a.charCodeAt(i - 1) !== 32)
    --i;

  return a + joiner + b.slice(i);
}

function strip_prefix(period) {
  if(period.slice(0, 12) === "över natten ") {
    return period.slice(12);
  }
  if(period.slice(0, 6) === "under ") {
    return period.slice(6);
  }
  return period;
}

module.exports = {
  "clear": "klart",
  "no-precipitation": "ingen målbar nedbør",
  "mixed-precipitation": "blandet nedbør",
  "possible-very-light-precipitation": "sjanse for veldig lett nedbør",
  "very-light-precipitation": "veldig lett nedbør",
  "possible-light-precipitation": "sjanse for lett nedbør",
  "light-precipitation": "lett nedbør",
  "medium-precipitation": "nedbør",
  "heavy-precipitation": "kraftig regn",
  "possible-very-light-rain": "sjanse for lett duskregn",
  "very-light-rain": "duskregn",
  "possible-light-rain": "sjanse for lette regnbyger",
  "light-rain": "regnbyger",
  "medium-rain": "regn",
  "heavy-rain": "kraftige regnbyger",
  "possible-very-light-sleet": "sjanse for veldig lett sludd",
  "very-light-sleet": "veldig lett sludd",
  "possible-light-sleet": "sjanse for lett sludd",
  "light-sleet": "lett sludd",
  "medium-sleet": "sludd",
  "heavy-sleet": "kraftig sludd",
  "possible-very-light-snow": "sjanse for vedlig lett snø",
  "very-light-snow": "veldig lett snø",
  "possible-light-snow": "sjanse for lett snø",
  "light-snow": "lett snø",
  "medium-snow": "snø",
  "heavy-snow": "rikelig med snø",
  "possible-thunderstorm": "tordenvær kan forekomme",
  "thunderstorm": "tordenvær",
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
  "light-wind": "lett vind",
  "medium-wind": "sterk vind",
  "heavy-wind": "storm",
  "low-humidity": "tørke",
  "high-humidity": "fuktig",
  "fog": "tåke",
  "very-light-clouds": "stort sett klart",
  "light-clouds": "lettskyet",
  "medium-clouds": "skyet",
  "heavy-clouds": "overskyet",
  "today-morning": "i løpet av formiddagen",
  "later-today-morning": "senere på morgenen",
  "today-afternoon": "på ettermiddagen",
  "later-today-afternoon": "senere på ettermiddagen",
  "today-evening": "i løpet av kvelden",
  "later-today-evening": "senere på kvelden",
  "today-night": "i kveld",
  "later-today-night": "senere i kveld",
  "tomorrow-morning": "i morgen tidlig",
  "tomorrow-afternoon": "i morgen ettermiddag",
  "tomorrow-evening": "i morgen kveld",
  "tomorrow-night": "i morgen natt",
  "morning": "om morgenen",
  "afternoon": "på ettermiddagen",
  "evening": "om kvelden",
  "night": "om natten",
  "today": "i dag",
  "tomorrow": "i morgen",
  "sunday": "på søndag",
  "monday": "på mandag",
  "tuesday": "på tirsdag",
  "wednesday": "på onsdag",
  "thursday": "på torsdag",
  "friday": "på fredag",
  "saturday": "på lørdag",
  "next-sunday": "neste søndag",
  "next-monday": "neste mandag",
  "next-tuesday": "neste tirsdag",
  "next-wednesday": "neste onsdag",
  "next-thursday": "neste torsdag",
  "next-friday": "neste fredag",
  "next-saturday": "neste lørdag",
  "minutes": "$1 min.",
  "fahrenheit": "$1\u00B0F",
  "celsius": "$1\u00B0C",
  "inches": "$1 in.",
  "centimeters": "$1 cm.",
  "less-than": "under $1",
  "and": function(a, b) {
    return join_with_shared_prefix(
      a,
      b,
      a.indexOf(",") !== -1 ? " og " : " og ",
    );
  },
  "through": function(a, b) {
    return join_with_shared_prefix(a, b, " fram til ");
  },
  "with": "$1, med $2",
  "range": "$1\u2013$2",
  "parenthetical": "$1 ($2)",
  "for-hour": "$1 i løpet av de neste timene",
  "starting-in": "$1 som starter om $2",
  "stopping-in": "$1 som avtar om $2",
  "starting-then-stopping-later": "$1 som starter om $2, avtar $3 senere",
  "stopping-then-starting-later": "$1 avtar om $2, starter igjen $3 senere",
  "for-day": "$1 i løpet av dagen",
  "starting": "$1 som starter $2",
  "until": function(condition, period) {
    return condition + " fram til " + strip_prefix(period);
  },
  "until-starting-again": function(condition, a, b) {
    return condition + " fram til " + strip_prefix(a) + ", som starter igjen " + b;
  },
  "starting-continuing-until": function(condition, a, b) {
    return condition + " som starter " + a + ", fortsetter fram til " + strip_prefix(b);
  },
  "during": "$1 $2",
  "for-week": "$1 i løpet av uken",
  "over-weekend": "$1 over helgen",
  "temperatures-peaking": "temperaturer opptil $1 $2",
  "temperatures-rising": "temperaturer som stiger til $1 $2",
  "temperatures-valleying": "temperaturer som stopper på $1 $2",
  "temperatures-falling": "temperaturer som synker til $1 $2",
  /* Capitalize the sentence (but not each word). */
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
  "next-hour-forecast-status": "Værvarsel for neste time er $1 på grunn av $2.",
  "unavailable": "ikke tilgjengelig",
  "temporarily-unavailable": "midertidlig ikke tilgjengelig",
  "partially-unavailable": "delvis ikke tilgjengelig",
  "station-offline": "ingen kontakt med radarstasjoner i nærheten",
  "station-incomplete": "hull i dekningen fra radarstasjoner i nærheten",
};
