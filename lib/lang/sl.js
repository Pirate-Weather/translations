

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

module.exports = {
  "clear": "jasno",
  "no-precipitation": "brez padavin",
  "mixed-precipitation": "možne padavine",
  "possible-very-light-precipitation": "možne so rahle padavine",
  "very-light-precipitation": "rahle padavine",
  "possible-light-precipitation": "možne so rahle padavine",
  "light-precipitation": "rahle padavine",
  "medium-precipitation": "padavine",
  "heavy-precipitation": "močne padavine",
  "possible-very-light-rain": "možen je rahel dež",
  "very-light-rain": "rosenje",
  "possible-light-rain": "možen je rahel dež",
  "light-rain": "rahel dež",
  "medium-rain": "dež",
  "heavy-rain": "močan dež",
  "possible-very-light-sleet": "možnost rahlega žleda",
  "very-light-sleet": "rahel žled",
  "possible-light-sleet": "možnost žleda",
  "light-sleet": "rahel žled",
  "medium-sleet": "dež s snegom",
  "heavy-sleet": "žled",
  "possible-very-light-snow": "možno je rahlo sneženje",
  "very-light-snow": "rahlo sneženje",
  "possible-light-snow": "možnost rahlega sneženja",
  "light-snow": "rahlo sneženje",
  "medium-snow": "sneg",
  "heavy-snow": "močno sneženje",
  "possible-thunderstorm": "possible thunderstorms",
  "thunderstorm": "thunderstorms",
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
  "light-wind": "vetrovno",
  "medium-wind": "vetrovno",
  "heavy-wind": "močni sunki vetra",
  "low-humidity": "suho",
  "high-humidity": "vlažno",
  "fog": "megleno",
  "very-light-clouds": "pretežno jasno",
  "light-clouds": "delno oblačno",
  "medium-clouds": "pretežno oblačno",
  "heavy-clouds": "oblačno",
  "today-morning": "danes zjutraj",
  "later-today-morning": "kasneje to jutro",
  "today-afternoon": "danes popoldan",
  "later-today-afternoon": "kasneje popoldan",
  "today-evening": "danes zvečer",
  "later-today-evening": "drevi",
  "today-night": "danes ponoči",
  "later-today-night": "danes čez noč",
  "tomorrow-morning": "jutri zjutraj",
  "tomorrow-afternoon": "jutri popoldne",
  "tomorrow-evening": "jutri zvečer",
  "tomorrow-night": "jutri zvečer",
  "morning": "zjutraj",
  "afternoon": "popoldan",
  "evening": "zvečer",
  "night": "zvečer",
  "today": "danes",
  "tomorrow": "jutri",
  "sunday": "v nedeljo",
  "monday": "v ponedeljek",
  "tuesday": "v torek",
  "wednesday": "v sredo",
  "thursday": "v četrtek",
  "friday": "v petek",
  "saturday": "v soboto",
  "next-sunday": "naslednjo nedeljo",
  "next-monday": "naslednji ponedeljek",
  "next-tuesday": "naslednji torek",
  "next-wednesday": "naslednjo sredo",
  "next-thursday": "naslednji četrtek",
  "next-friday": "naslednji petek",
  "next-saturday": "naslednjo soboto",
  "minutes": "$1 min.",
  "fahrenheit": "$1\u00B0F",
  "celsius": "$1\u00B0C",
  "inches": "$1 in.",
  "centimeters": "$1 cm.",
  "less-than": "manj kot $1",
  "and": function(a, b) {
    return join_with_shared_prefix(
      a,
      b,
      a.indexOf(",") !== -1 ? ", in " : " in ",
    );
  },
  "through": function(a, b) {
    return join_with_shared_prefix(a, b, " do ");
  },
  "with": "$1, s $2",
  "range": "$1\u2013$2",
  "parenthetical": "$1 ($2)",
  "for-hour": "$1 za uro",
  "starting-in": "$1 od $2",
  "stopping-in": "$1 do $2",
  "starting-then-stopping-later": "$1 od $2, do $3 kasneje",
  "stopping-then-starting-later": "$1 do $2, začelo bo zopet $3 kasneje",
  "for-day": "$1 čez dan",
  "starting": "$1 od $2",
  "until": "$1 do $2",
  "until-starting-again": "$1 do $2, začelo bo zopet $3",
  "starting-continuing-until": "$1 začel $2, do $3",
  "during": "$1 $2",
  "for-week": "$1 čez teden",
  "over-weekend": "$1 v soboto in nedeljo",
  "temperatures-peaking": "temperaturami do $1 $2",
  "temperatures-rising": "temperaturami do $1 $2",
  "temperatures-valleying": "najnižjimi temperaturami okoli $1 $2",
  "temperatures-falling": "temperaturami do $1 $2",
  /* Capitalize the first letter of every word. */
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
  "next-hour-forecast-status": "urne napovedi $1, ker $2",
  "unavailable": "niso na voljo",
  "temporarily-unavailable": "začasno niso na voljo",
  "partially-unavailable": "delno niso na voljo",
  "station-offline": "so vse bližnje radarske postaje brez povezave",
  "station-incomplete": "imajo bližnje radarske postaje pomanjkljivo pokritost",
};
