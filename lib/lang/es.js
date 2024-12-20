

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
  "clear": "despejado",
  "no-precipitation": "sin precipitaciones",
  "mixed-precipitation": "precipitación mixta",
  "possible-very-light-precipitation": "posibles lluvias ligeras",
  "very-light-precipitation": "lluvias ligeras",
  "possible-light-precipitation": "posibles lluvias ligeras",
  "light-precipitation": "precipitación ligera",
  "medium-precipitation": "precipitación",
  "heavy-precipitation": "fuerte precipitación",
  "possible-very-light-rain": "posible llovizna",
  "very-light-rain": "llovizna",
  "possible-light-rain": "posible lluvia ligera",
  "light-rain": "lluvia ligera",
  "medium-rain": "lluvia",
  "heavy-rain": "fuertes lluvias",
  "possible-very-light-sleet": "posible aguanieve ligera",
  "very-light-sleet": "aguanieve ligera",
  "possible-light-sleet": "posible aguanieve ligera",
  "light-sleet": "aguanieve ligera",
  "medium-sleet": "aguanieve",
  "heavy-sleet": "fuertes aguanieves",
  "possible-very-light-snow": "posible nevada ligera",
  "very-light-snow": "nevadas ligeras",
  "possible-light-snow": "posible nevada ligera",
  "light-snow": "nevadas ligeras",
  "medium-snow": "nevadas",
  "heavy-snow": "fuertes nevadas",
  "possible-thunderstorm": "tormentas posibles",
  "thunderstorm": "tormenta",
  "possible-medium-precipitation": "posibles precipitation",
  "possible-heavy-precipitation": "posibles fuertes precipitation",
  "possible-medium-rain": "posible lluvia",
  "possible-heavy-rain": "posible heavy lluvia",
  "possible-medium-sleet": "posible aguanieve",
  "possible-heavy-sleet": "posible fuertes aguanieve",
  "possible-medium-snow": "posible nevadas",
  "possible-heavy-snow": "posible fuertes nevadas",
  "possible-freezing-drizzle": "posible llovizna helada",
  "freezing-drizzle": "llovizna helada",
  "possible-light-freezing-rain": "posible nevadas lluvia helada",
  "light-freezing-rain": "nevadas lluvia helada",
  "possible-freezing-rain": "posible lluvia helada",
  "freezing-rain": "lluvia helada",
  "possible-heavy-freezing-rain": "posible fuertes lluvia helada",
  "heavy-freezing-rain": "fuertes lluvia helada",
  "possible-hail": "posible granizo",
  "hail": "granizo",
  "light-wind": "vientos suaves",
  "medium-wind": "ventoso",
  "heavy-wind": "peligrosamente ventoso",
  "low-humidity": "seco",
  "high-humidity": "húmedo",
  "fog": "niebla",
  "very-light-clouds": "mayormente despejado",
  "light-clouds": "parcialmente nublado",
  "medium-clouds": "mayormente nublado",
  "heavy-clouds": "nublado",
  "today-morning": "esta mañana",
  "later-today-morning": "después esta mañana",
  "today-afternoon": "esta tarde",
  "later-today-afternoon": "después esta tarde",
  "today-evening": "esta noche",
  "later-today-evening": "después esta noche",
  "today-night": "esta noche",
  "later-today-night": "después esta noche",
  "tomorrow-morning": "mañana por la mañana",
  "tomorrow-afternoon": "mañana por la tarde",
  "tomorrow-evening": "mañana por la noche",
  "tomorrow-night": "mañana por la noche",
  "morning": "por la mañana",
  "afternoon": "por la tarde",
  "evening": "por la noche",
  "night": "por la noche",
  "today": "hoy",
  "tomorrow": "mañana",
  "sunday": "el Domingo",
  "monday": "el Lunes",
  "tuesday": "el Martes",
  "wednesday": "el Miércoles",
  "thursday": "el Jueves",
  "friday": "el Viernes",
  "saturday": "el Sábado",
  "next-sunday": "el próximo Domingo",
  "next-monday": "el próximo Lunes",
  "next-tuesday": "el próximo Martes",
  "next-wednesday": "el próximo Miércoles",
  "next-thursday": "el próximo Jueves",
  "next-friday": "el próximo Viernes",
  "next-saturday": "el próximo Sábado",
  "minutes": "$1 min.",
  "fahrenheit": "$1\u00B0F",
  "celsius": "$1\u00B0C",
  "inches": "$1 in.",
  "centimeters": "$1 cm.",
  "less-than": "bajo $1",
  "and": function(a, b) {
    return join_with_shared_prefix(
      a,
      b,
      a.indexOf(",") !== -1 ? ", y " : " y ",
    );
  },
  "through": function(a, b) {
    return join_with_shared_prefix(a, b, " hasta ");
  },
  "with": "$1, con $2",
  "range": "$1\u2013$2",
  "parenthetical": "$1 ($2)",
  "for-hour": "$1 por la hora",
  "starting-in": "$1 comenzando en $2",
  "stopping-in": "$1 parando en $2",
  "starting-then-stopping-later": "$1 comenzando en $2, después parando en $3",
  "stopping-then-starting-later": "$1 parando en $2, comenzando de nuevo $3 después",
  "for-day": "$1 durante el día",
  "starting": "$1 comenzando $2",
  "until": "$1 hasta $2",
  "until-starting-again": "$1 hasta $2, comenzando otra vez $3",
  "starting-continuing-until": "$1 comenzando $2, continuando hasta $3",
  "during": "$1 $2",
  "for-week": "$1 durante la semana",
  "over-weekend": "$1 sobre el fin de semana",
  "temperatures-peaking": "temperaturas alcanzando un máximo de $1 $2",
  "temperatures-rising": "temperaturas llegando a $1 $2",
  "temperatures-valleying": "temperaturas alcanzando un mínimo de $1 $2",
  "temperatures-falling": "temperaturas cayendo a $1 $2",
  /* Capitalize the first letter of every word, except if that word is "y". */
  "title": function(str) {
    return str.replace(/\S+/g, function(word) {
      return word === "y" ?
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
