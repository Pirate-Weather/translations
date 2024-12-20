

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

const grammar = {
  "tänään": [null, null],
  "huomenna": ["huomisesta", "huomiseen asti"],
  "yöllä": ["yöstä", "yöhön asti"],
  "ilta": ["illasta", "iltaan asti"],
  "aamulla": ["aamusta", "aamuun asti"],
  "illalla": ["illasta", "iltaan asti"],
  "iltapäivällä": ["iltapäivästä", "iltapäivään asti"],
  "huomisaamu": ["huomisaamusta", "huomisaamuun asti"],
  "myöhemmin illalla": ["myöhemmästä illasta alkaen", "myöhempään iltaan asti"],
  "myöhemmin yöllä": ["myöhemmästä yöstä alkaen", "myöhempään yöhön asti"],
  "huomenna iltapäivällä": ["huomisesta iltapäivästä", "huomiseen iltapäivään asti"],
  "huomenna illalla": ["huomisesta illasta", "huomiseen iltaan asti"],
  "huomenna yöllä": ["huomisesta yöstä", "huomiseen yöhön asti"],
  "maanantaina": ["maanantaista", "maanantaihin"],
  "tiistaina": ["tiistaista", "tiistaihin"],
  "keskiviikkona": ["keskiviikosta", "keskiviikkoon"],
  "torstaina": ["torstaista", "torstaihin"],
  "perjantaina": ["perjantaista", "perjantaihin"],
  "lauantaina": ["lauantaista", "lauantaihin"],
  "sunnuntaina": ["sunnuntaista", "sunnuntaihin"],
};

function elative(word) {
  return Object.prototype.hasOwnProperty.call(grammar, word)? grammar[word][0]: word;
}

function illative(word){
  return Object.prototype.hasOwnProperty.call(grammar, word)? grammar[word][1]: word;
}

module.exports = {
  "clear": "selkeää",
  "no-precipitation": "poutaa",
  "mixed-precipitation": "räntäsadetta",
  "possible-very-light-precipitation": "heikon sateen mahdollisuus",
  "very-light-precipitation": "heikkoa sadetta",
  "possible-light-precipitation": "sadekuurojen mahdollisuus",
  "light-precipitation": "sadekuuroja",
  "medium-precipitation": "sadetta",
  "heavy-precipitation": "rankkasadetta",
  "possible-very-light-rain": "heikon sateen mahdollisuus",
  "very-light-rain": "heikkoa sadetta",
  "possible-light-rain": "sadekuurojen mahdollisuus",
  "light-rain": "sadekuuroja",
  "medium-rain": "sadetta",
  "heavy-rain": "rankkasadetta",
  "possible-very-light-sleet": "heikon räntäsateen mahdollisuus",
  "very-light-sleet": "heikkoa räntäsadetta",
  "possible-light-sleet": "räntäkuurojen mahdollisuus",
  "light-sleet": "räntäkuuroja",
  "medium-sleet": "räntäsadetta",
  "heavy-sleet": "voimakasta räntäsadetta",
  "possible-very-light-snow": "heikon lumisateen mahdollisuus",
  "very-light-snow": "heikkoa lumisadetta",
  "possible-light-snow": "lumikuurojen mahdollisuus",
  "light-snow": "lumikuuroja",
  "medium-snow": "lumisadetta",
  "heavy-snow": "rankkaa lumisadetta",
  "possible-thunderstorm": "ukkosmyrskyjä mahdollisuus",
  "thunderstorm": "ukkosmyrskyjä",
  "possible-medium-precipitation": "sadetta mahdollisuus",
  "possible-heavy-precipitation": "rankkasadetta mahdollisuus",
  "possible-medium-rain": "sadetta mahdollisuus",
  "possible-heavy-rain": "rankkasadetta mahdollisuus",
  "possible-medium-sleet": "räntäsadetta mahdollisuus",
  "possible-heavy-sleet": "voimakasta räntäsadetta mahdollisuus",
  "possible-medium-snow": "lumisadetta mahdollisuus",
  "possible-heavy-snow": "rankkaa lumisadetta mahdollisuus",
  "possible-freezing-drizzle": "jäätävää tihkusadetta mahdollisuus",
  "freezing-drizzle": "jäätävää tihkusadetta",
  "possible-light-freezing-rain": "kevyttä jäätävää sadetta mahdollisuus",
  "light-freezing-rain": "kevyttä jäätävää sadetta",
  "possible-freezing-rain": "jäätävää sadetta mahdollisuus",
  "freezing-rain": "jäätävää sadetta",
  "possible-heavy-freezing-rain": "rankkaa jäätävää sadetta mahdollisuus",
  "heavy-freezing-rain": "rankkaa jäätävää sadetta",
  "possible-hail": "hail mahdollisuus",
  "hail": "hail",
  "light-wind": "heikkoa tuulta",
  "medium-wind": "tuulista",
  "heavy-wind": "myrskyisää",
  "low-humidity": "kuivaa",
  "high-humidity": "kosteaa",
  "fog": "sumua",
  "very-light-clouds": "enimmäkseen selkeää",
  "light-clouds": "puolipilvistä",
  "medium-clouds": "enimmäkseen pilvistä",
  "heavy-clouds": "pilvistä",
  "today-morning": "aamulla",
  "later-today-morning": "myöhemmin aamulla",
  "today-afternoon": "iltapäivällä",
  "later-today-afternoon": "myöhemmin iltapäivällä",
  "today-evening": "illalla",
  "later-today-evening": "myöhemmin illalla",
  "today-night": "yöllä",
  "later-today-night": "myöhemmin yöllä",
  "tomorrow-morning": "huomisaamuna",
  "tomorrow-afternoon": "huomenna iltapäivällä",
  "tomorrow-evening": "huomenna illalla",
  "tomorrow-night": "huomenna yöllä",
  "morning": "aamulla",
  "afternoon": "iltapäivällä",
  "evening": "illalla",
  "night": "yöllä",
  "today": "tänään",
  "tomorrow": "huomenna",
  "sunday": "sunnuntaina",
  "monday": "maanantaina",
  "tuesday": "tiistaina",
  "wednesday": "keskiviikkona",
  "thursday": "torstaina",
  "friday": "perjantaina",
  "saturday": "lauantaina",
  "next-sunday": "sunnuntaina", // FIXME
  "next-monday": "maanantaina", // FIXME
  "next-tuesday": "tiistaina", // FIXME
  "next-wednesday": "keskiviikkona", // FIXME
  "next-thursday": "torstaina", // FIXME
  "next-friday": "perjantaina", // FIXME
  "next-saturday": "lauantaina", // FIXME
  "minutes": "$1 min.",
  "fahrenheit": "$1\u00B0F",
  "celsius": "$1\u00B0C",
  "inches": "$1 tuumaa",
  "centimeters": "$1 cm",
  "less-than": "alle $1",
  "and": function(a, b) {
    return join_with_shared_prefix(a, b, " ja ");
  },
  "through": function(a, b) {
    a = elative(a);
    b = illative(b);
    return (a && b)? a + " " + b + " asti":
      (a || b)? (a || b) + " asti":
        "asti";
  },
  "with": "$1, $2",
  "range": "$1\u2013$2",
  "parenthetical": "$1 ($2)",
  "for-hour": "$1 seuraavan tunnin ajan",
  "starting-in": "$1 odotettavissa $2 kuluessa",
  "stopping-in": "$1 vielä $2",
  "starting-then-stopping-later": "$1 $2 kuluessa, päättyen $3 myöhemmin",
  "stopping-then-starting-later": "$1 vielä $2, alkaen uudestaan $3 myöhemmin",
  "for-day": "$1 päivän aikana",
  "starting": function(condition, period){
    return condition + " " + elative(period);
  },
  "until": function(condition, period) {
    return condition + " " + illative(period);
  },
  "until-starting-again": function(condition, a, b) {
    return condition + " " + illative(a) + ", ja jälleen " + b;
  },
  "starting-continuing-until": function(condition, a, b) {
    return condition + " " + elative(a) + " " + illative(b);
  },
  "during": "$1 $2",
  "for-week": "$1 viikon ajan",
  "over-weekend": "$1 viikonloppuna",
  "temperatures-peaking": "lämpötilan noustessa lukemaan $1 $2",
  "temperatures-rising": "lämpötilan noustessa lukemaan $1 $2",
  "temperatures-valleying": "lämpötilan käydessä lukemassa $1 $2",
  "temperatures-falling": "lämpötilan laskiessa lukemaan $1 $2",
  /* Capitalize the first character in the word.*/
  "title": function(str) {
    str = str.charAt(0).toUpperCase() + str.slice(1);
    return str;
  },
  /* Capitalize the first word of the sentence and end with a period. */
  "sentence": function(str) {
    str = str.charAt(0).toUpperCase() + str.slice(1);

    if(str.charAt(str.length - 1) !== ".")
      str += ".";

    return str;
  },
};
