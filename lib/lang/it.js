

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
  if(period === "in serata") return "sera";
  if(period === "in mattinata") return "mattina";
  if(period.slice(0, 6) === "nella ") return period.slice(6);
  if(period.slice(0, 4) === "nel ") return period.slice(4);
  return period;
}

module.exports = {
  "clear": "sereno",
  "no-precipitation": "nessuna precipitazione",
  "mixed-precipitation": "precipitazioni miste",
  "possible-very-light-precipitation": "possibilità di precipitazioni molto leggere",
  "very-light-precipitation": "precipitazioni molto leggere",
  "possible-light-precipitation": "possibilità di precipitazioni leggere",
  "light-precipitation": "precipitazioni leggere",
  "medium-precipitation": "precipitazioni",
  "heavy-precipitation": "forti precipitazioni",
  "possible-very-light-rain": "possibilità di pioggia molto leggera",
  "very-light-rain": "pioggia molto leggera",
  "possible-light-rain": "possibilità di pioggia leggera",
  "light-rain": "pioggia leggera",
  "medium-rain": "pioggia",
  "heavy-rain": "temporali",
  "possible-very-light-sleet": "possibilità di nevischio molto leggero",
  "very-light-sleet": "nevischio molto leggero",
  "possible-light-sleet": "possibilità di nevischio leggero",
  "light-sleet": "nevischio leggero",
  "medium-sleet": "nevischio",
  "heavy-sleet": "forte nevischio",
  "possible-very-light-snow": "possibilità di nevicate molto leggere",
  "very-light-snow": "nevicate molto leggere",
  "possible-light-snow": "possibilità di neve leggera",
  "light-snow": "neve leggera",
  "medium-snow": "nevicate",
  "heavy-snow": "forti nevicate",
  "possible-thunderstorm": "possibili nubifragi",
  "thunderstorm": "nubifragi",
  "possible-medium-precipitation": "possibilità di precipitazioni",
  "possible-heavy-precipitation": "possibilità di forti precipitazioni",
  "possible-medium-rain": "possibilità di pioggia",
  "possible-heavy-rain": "possibilità di temporali",
  "possible-medium-sleet": "possibilità di nevischio",
  "possible-heavy-sleet": "possibilità di forte nevischio",
  "possible-medium-snow": "possibilità di nevicate",
  "possible-heavy-snow": "possibilità di forti nevicate",
  "possible-freezing-drizzle": "possibilità di pioggia leggera molto gelata",
  "freezing-drizzle": "pioggia leggera molto gelata",
  "possible-light-freezing-rain": "possibilità di pioggia gelata leggera",
  "light-freezing-rain": "freezing pioggia leggera",
  "possible-freezing-rain": "possibilità di pioggia gelata",
  "freezing-rain": "pioggia gelata",
  "possible-heavy-freezing-rain": "possibilità di forte pioggia gelata",
  "heavy-freezing-rain": "forte pioggia gelata",
  "possible-hail": "possibilità di grandine",
  "hail": "grandine",
  "light-wind": "venticello",
  "medium-wind": "vento",
  "heavy-wind": "forte vento",
  "low-humidity": "bassa umidità",
  "high-humidity": "umido",
  "fog": "nebbia",
  "very-light-clouds": "prevalentemente sereno",
  "light-clouds": "poco nuvoloso",
  "medium-clouds": "nubi sparse",
  "heavy-clouds": "nuvoloso",
  "today-morning": "stamattina",
  "later-today-morning": "a mattina inoltrata",
  "today-afternoon": "questo pomeriggio",
  "later-today-afternoon": "a pomeriggio inoltrato",
  "today-evening": "stasera",
  "later-today-evening": "a sera inoltrata",
  "today-night": "stanotte",
  "later-today-night": "notte inoltrata",
  "tomorrow-morning": "domani mattina",
  "tomorrow-afternoon": "domani pomeriggio",
  "tomorrow-evening": "domani sera",
  "tomorrow-night": "domani notte",
  "morning": "in mattinata",
  "afternoon": "nel pomeriggio",
  "evening": "in serata",
  "night": "nella notte",
  "today": "oggi",
  "tomorrow": "domani",
  "sunday": "Domenica",
  "monday": "Lunedì",
  "tuesday": "Martedì",
  "wednesday": "Mercoledì",
  "thursday": "Giovedì",
  "friday": "Venerdì",
  "saturday": "Sabato",
  "next-sunday": "prossima Domenica",
  "next-monday": "prossimo Lunedì",
  "next-tuesday": "prossimo Martedì",
  "next-wednesday": "prossimo Mercoledì",
  "next-thursday": "prossimo Giovedì",
  "next-friday": "prossimo Venerdì",
  "next-saturday": "prossimo Sabato",
  "minutes": "$1 min.",
  "fahrenheit": "$1\u00B0F",
  "celsius": "$1\u00B0C",
  "inches": "$1 in.",
  "centimeters": "$1 cm.",
  "less-than": "meno di $1",
  "and": function(a, b) {
    let joiner = b.length > 8 && b.slice(0,8) === "prossimo" ? " e il " :
      b.length > 8 && b.slice(0,8) === "prossima" ? " e la " :
        " e ";
    if (a.indexOf(",") !== -1) joiner = "," + joiner;
    return join_with_shared_prefix(a,b,joiner);
  },
  "through": function(a, b) {
    const joiner = b.length > 8 && b.slice(0,8) === "prossimo" ? " fino al " :
      b.length > 8 && b.slice(0,8) === "prossima" ? " fino alla " :
        " fino a ";
    return join_with_shared_prefix(a, b, joiner);
  },
  "with": "$1, con $2",
  "range": "$1\u2013$2",
  "parenthetical": function(a, b) {
    return a + " (" + b + (a === "precipitazioni miste" ? " di neve)" : ")");
  },
  "for-hour": "$1 per un ora",
  "starting-in": "$1 tra $2",
  "stopping-in": "$1 per $2",
  "starting-then-stopping-later": "$1 a partire tra $2 per $3",
  "stopping-then-starting-later": "$1 per altri $2, per ricominciare $3 più tardi",
  "for-day": "$1 durante il giorno",
  "starting": function(condition, period) {
    return condition + " a partire da " + strip_prefix(period);
  },
  "until": function(condition, period) {
    return condition + " fino a " + strip_prefix(period);
  },
  "until-starting-again": function(condition, a, b) {
    return condition + " fino a " + strip_prefix(a) + ", ricominciando da " + b;
  },
  "starting-continuing-until": function(condition, a, b) {
    return condition + " a partire da " + strip_prefix(a) + ", fino a " + strip_prefix(b);
  },
  "during": "$1 $2",
  "for-week": "$1 durante la settimana",
  "over-weekend": "$1 tutto il week end",
  "temperatures-peaking": "temperatura massima di $1 $2",
  "temperatures-rising": "temperature in aumento fino a $1 $2",
  "temperatures-valleying": "temperatura minima di $1 $2",
  "temperatures-falling": "temperature in diminuzione fino a $1 $2",
  /* Capitalize the first letter of every word, except if that word is "e". */
  "title": function(str) {
    return str.replace(/\S+/g, function(word) {
      return word === "e" ?
        word :
        word.charAt(0).toUpperCase() + word.slice(1);
    });
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
