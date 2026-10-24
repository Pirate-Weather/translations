Pirate Weather API Translation Module
===============================

Introduction
------------

The [Pirate Weather API][1] has, since version 2.5, included a module for
producing textual weather summaries from its weather data.  These summaries
have always been in English (since that's the only language we know) and have
always been procedurally generated (since there are so many possible weather
conditions). Procedural generation makes translating these summaries into other
languages especially difficult, because the naive approach—using a table
lookup to replace an English sentence with one of a different language—becomes
impractical, requiring a *very* large table to support!

[1]: https://pirateweather.net/en/latest/

This software module was developed in order to work around these issues. We are
modifying the Pirate Weather API text summary code to generate a machine-readable
format (described below) rather than its usual English; summaries in this new
format are then handed off to this module for translation into the desired
language. Since this module is open-source, anyone may contribute additional
language components to it, so that the desired language can be used in the
Pirate Weather API.

Appendix A: Pirate Weather Summary Format
-----------------------------------

Below is a listing of every possible machine-readable summary produced by
Pirate Weather. The listing is recursive so as to better describe how the various
structural components interact.

### Status Information

Instead of producing a summary of weather information, we may sometimes generate
a status message indicating an error of some sort. Such messages may take one of
the following forms:

*   `["sentence", [STATUS_MESSAGE, STATUS_TYPE, REASON]]`

`STATUS_MESSAGE` may be one of the following:

*   `"next-hour-forecast-status"`: we have information to convey about our
    hyperlocal next-hour forecasts

`STATUS_TYPE` may be one of the following:

*   `"unavailable"`: no forecast is available for this request
*   `"partially-unavailable"`: only a partial forecast is available for this request
*   `"temporarily-unavailable"`: no forecast is available for this request, but we
    expect it to be available again in the future

`REASON` may be one of the following:

*   `"station-offline"`: we cannot generate a forecast because all nearby weather
    stations are offline (e.g. for maintenance)
*   `"station-incomplete"`: we cannot generate a forecast because of gaps in the
    coverage of all nearby weather stations (e.g. radar beams are blocked by
    local terrain)

`"next-hour-forecast-status"`, `"unavailable"`, `"partially-unavailable"`, `"temporarily-unavailable"`, `"station-offline"`, and `"station-incomplete"` are not used in any other forms.

### Moment Summaries

When the API is producing a text summary for a single moment in time (that is,
`currently.summary` and `hourly.data[N].summary`), summaries of the following
structure are produced:

*   `["title", WEATHER_CONDITION]`
*   `["title", ["and", WEATHER_CONDITION, WEATHER_CONDITION]]`

The `"title"` component is never used in any other situation, and signifies
that (in English, anyway) these conditions represent phrases rather than
complete sentences; as such, they are capitalized like a *title* (that is, each
word is capitalized and there is no punctuation). For all below cases, the
`"sentence"` component wraps the construction (signifying that the summary
represents a full, English sentence, meaning that only the first word is
capitalized, and the sentence is to end with a period).

`"and"` is used all over the place. Sorry.

### Hour Summaries

For text summaries for the next hour (that is, `minutely.summary`), summaries
of the following formats are produced:

*   `["sentence", ["for-hour", WEATHER_CONDITION]]`
*   `["sentence", ["starting-in", PRECIPITATION_TYPE, DURATION]]`
*   `["sentence", ["stopping-in", PRECIPITATION_TYPE, DURATION]]`
*   `["sentence", ["starting-then-stopping-later", PRECIPITATION_TYPE, DURATION, DURATION]]`
*   `["sentence", ["stopping-then-starting-later", PRECIPITATION_TYPE, DURATION, DURATION]]`

Except for the first case, each such summary only takes precipitation into
account, and tells how the intensity of precipitation will vary over the next
hour or so.

The `DURATION`s listed above may be either of:

*   `["less-than", ["minutes", 1]]` ("less than a minute")
*   `["minutes", NUMBER]` ("X minutes")

`"for-hour"`, `"starting-in"`, `"stopping-in"`,
`"starting-then-stopping-later"`, `"stopping-then-starting-later"`, and
`"minutes"` are only used as above. `"less-than"` is also used for precipitation
accumulation (see below).

### Day Summaries

Day summaries are produced by the API when a duration of 24 hours is under
consideration (that is, `hourly.summary` and `daily.data[N].summary`). They are
the most complex summaries in the API, owing to the number of possible
combinations of the various terms. They are of the following formats:

*   `["sentence", DAY_CONDITION_SUMMARY]`
*   `["sentence", ["and", DAY_CONDITION_SUMMARY, DAY_CONDITION_SUMMARY]]`
*   `["sentence", ["accompanied-by", DAY_CONDITION_SUMMARY, DAY_CONDITION_SUMMARY]]`
*   `["multiple-sentences", ["sentence", DAY_CONDITION_SUMMARY], ["sentence", DAY_CONDITION_SUMMARY]]`

`"multiple-sentences"` splits a day summary into separate sentences instead of
joining every condition with `"and"`. For example, "Foggy in the morning and
windy starting in the afternoon." becomes "Foggy in the morning. Windy starting
in the afternoon.", and a precipitation summary can be followed by its expected
accumulation in its own sentence. Each half is already a complete sentence, so
the template only needs to join them; English puts a space in between.
Languages that don't put spaces between sentences, such as Japanese and
Chinese, should use `"$1$2"`.

`"accompanied-by"` joins a main condition with a secondary one that happens
alongside it, to avoid long chains of `"and"` (e.g. "Rain, with possible
thunderstorms starting this afternoon."). It is separate from `"with"`, which
is only used in weekly summaries. The condition strings are in the nominative
case, so languages where "with" requires a different case (e.g. Russian "с",
Polish "z", German "mit") should rephrase rather than use the preposition
directly, or use a function to inflect the second condition.

#### Day Condition Summaries

A "day condition" represents a specific weather condition at a specific time of
day. (Or a larger period of the day, as the case may be.)

*   `["for-day", WEATHER_CONDITION]`
*   `["for-night", WEATHER_CONDITION]`
*   `["during", WEATHER_CONDITION, TIME_OF_DAY]`
*   `["during", WEATHER_CONDITION, ["and", TIME_OF_DAY, TIME_OF_DAY]]`
*   `["during", WEATHER_CONDITION, ["list", TIME_OF_DAY, TIME_OF_DAY, ...]]`
*   `["starting", WEATHER_CONDITION, TIME_OF_DAY]`
*   `["until", WEATHER_CONDITION, TIME_OF_DAY]`
*   `["starting-continuing-until", WEATHER_CONDITION, TIME_OF_DAY, TIME_OF_DAY]`
*   `["until-starting-again", WEATHER_CONDITION, TIME_OF_DAY, TIME_OF_DAY]`

`"for-day"`, `"for-night"`, `"starting"`, `"until"`, `"starting-continuing-until"`, and
`"until-starting-again"` are only used in the above manner, and may be
considered analogous to the five similar cases in hourly summaries. `"during"`
is used both here and in weekly summaries, below. `"for-night"` is the
overnight counterpart of `"for-day"` (e.g. "rain throughout the night").

`WEATHER_CONDITION` may also be one of the precipitation or cloud cover
quantifiers described under [Quantifiers](#quantifiers) below.

#### Times of Day

Daily summaries covering a specific day use the following time periods:

*   `"morning"`
*   `"afternoon"`
*   `"evening"`
*   `"night"`

Daily summaries covering the next 24 hours (as in a forecast) use the following
time periods instead:

*   `"today-morning"`
*   `"today-afternoon"`
*   `"today-evening"`
*   `"today-night"`
*   `"later-today-morning"`
*   `"later-today-afternoon"`
*   `"later-today-evening"`
*   `"later-today-night"`
*   `"tomorrow-morning"`
*   `"tomorrow-afternoon"`
*   `"tomorrow-evening"`
*   `"tomorrow-night"`

In general, the most specific case is used.

The exact times that each duration begins or ends is not intended to be
critical, and nonprecise terminology should be used if possible. However, for
aid in translation, the time periods currently correspond to the following:

*   **morning:**   06:00  (6am) to 12:00 (12pm)
*   **afternoon:** 12:00 (12pm) to 18:00  (6pm)
*   **evening:**   18:00  (6pm) to 24:00 (12am)
*   **night:**     00:00 (12am) to 06:00  (6am)

### Week Summaries

For summaries spanning an entire week (`daily.summary`), the following format
is used:

*   `["sentence", ["with", WEEKLY_PRECIPITATION_SUMMARY, WEEKLY_TEMPERATURE_SUMMARY]]`

Since an entire week is a very broad span of time, we concern ourselves only
with the most broadly applicable information: which days will have rain, and
how the temperatures will fluctuate. The sentence is broken into two parts,
which each comprise one of the above.

`"with"` is not used in any other way.

#### Weekly Precipitation Summary

A "weekly precipitation summary" is used to describe which days of the week are
expected to have rain, as compactly as possible.

*   `["for-week", PRECIPITATION_TYPE]`
*   `["over-weekend", PRECIPITATION_TYPE]`
*   `["during", PRECIPITATION_TYPE, DAY_OF_WEEK]`
*   `["during", PRECIPITATION_TYPE, ["and", DAY_OF_WEEK, DAY_OF_WEEK]]`
*   `["during", PRECIPITATION_TYPE, ["list", DAY_OF_WEEK, DAY_OF_WEEK, ...]]`
*   `["during", PRECIPITATION_TYPE, ["through", DAY_OF_WEEK, DAY_OF_WEEK]]`

`"for-week"`, `"over-weekend"`, and `"through"` are all only used as above.
`"during"` is used both here and in daily summaries.

`"list"` is used instead of nested `"and"`s when there are three or more items
(e.g. "Rain today, Friday, Sunday and next Wednesday."); two items still use
`"and"`. It takes any number of arguments, so it must be a function with the
signature `def list_function(stack, *items)`. Each language chooses its own
separators (e.g. `、` in Japanese and Chinese, `،` in Arabic) and whether to
use a serial comma. If your `"and"` function rewrites days (as German does
with "am"), apply the same logic in `"list"`.

#### Weekly Temperature Summary

A "weekly temperature summary" describes the general pattern of temperatures
over the course of the next week: whether they'll get hotter, colder,
hotter-then-colder, colder-then-hotter or if temperatures are steady around a certain value.

*   `["temperatures-rising", TEMPERATURE, DAY_OF_WEEK]`
*   `["temperatures-falling", TEMPERATURE, DAY_OF_WEEK]`
*   `["temperatures-peaking", TEMPERATURE, DAY_OF_WEEK]`
*   `["temperatures-valleying", TEMPERATURE, DAY_OF_WEEK]`
*   `["temperatures-steady", TEMPERATURE]`

`"temperatures-peaking"`, `"temperatures-valleying"`, `"temperatures-rising"`,
`"temperatures-falling"` and `"temperatures-steady"` are all only used as above.

#### Temperatures

*   `["fahrenheit", NUMBER]`
*   `["celsius", NUMBER]`

Every language should support both temperature units, as the choice of language
and units are separate options in the API (and can be mixed-and-matched as
desired).

#### Days of the Week

*   `"today"`
*   `"tomorrow"`
*   `"sunday"`
*   `"monday"`
*   `"tuesday"`
*   `"wednesday"`
*   `"thursday"`
*   `"friday"`
*   `"saturday"`
*   `"next-sunday"`
*   `"next-monday"`
*   `"next-tuesday"`
*   `"next-wednesday"`
*   `"next-thursday"`
*   `"next-friday"`
*   `"next-saturday"`

`"today"` and `"tomorrow"` are used in preference to the other cases. The
`"next-*"` cases are used when the day in question is a week from today (e.g.
if today is Wednesday, and we expect rain a week from today, then the summary
would be `["during", "medium-rain", "next-wednesday"]`.)

### Weather Conditions

#### Precipitation Types

*   `"no-precipitation"`: Represents no precipitation. Only used in "weekly
    precipitation summary" blocks. (This condition is in contrast to `"clear"`,
    which represents no significant weather of any kind.)
*   `"mixed-precipitation"`: Represents multiple types of precipitation, such
    as both rain and snow. Only used in "weekly precipitation summary" blocks;
    in all other cases, the predominate type of precipitation is used.
*   `GENERIC_TYPE`
*   `RAIN_TYPE`
*   `SLEET_TYPE`
*   `FREEZING_RAIN_TYPE`
*   `SNOW_TYPE`
*   `["parenthetical", EXPECTED_PRECIP_TYPE, SNOW_ACCUMULATION]`: For daily or
    weekly summaries, if a significant amount of snow is expected, we will
    qualify it with the amount of expected snow accumulation. (For example,
    "snow (3–4 in) throughout the day".) PLEASE NOTE that it is possible for a
    chance of snow accumulation to be forecasted even if the expected
    precipitation type is rain or sleet: this may occur if the forecasted
    temperature is right around the freezing point. Translations should clarify
    that the parenthetical refers to a chance of snow in such circumstances.
    (For example, "sleet (with a chance of 3–4 in of snow) throughout the day".)
    `SNOW_ACCUMULATION` takes one of the forms listed under
    [Precipitation Accumulation](#precipitation-accumulation).
*   `["of-expected", PRECIP_ACCUMULATION, EXPECTED_PRECIP_TYPE]`: For daily
    summaries, if a significant amount of precipitation is expected, a separate
    sentence gives the expected accumulation (e.g. "Rain throughout the day.
    7–16 mm of rain expected."). Unlike `"parenthetical"`, which is only used
    for snow, this is used for every precipitation type. `PRECIP_ACCUMULATION`
    takes one of the forms listed under
    [Precipitation Accumulation](#precipitation-accumulation).

    When more than one type of precipitation is expected, the type shown is
    picked as follows:
    1. If more than 1 mm of ice (sleet or freezing rain) is expected, ice.
    2. Otherwise, if more than 5 cm of snow is expected, snow.
    3. Otherwise, if more than 10 mm of rain is expected, rain.
    4. Otherwise, the type with the most accumulation.

    The accumulation sentence is only added when the expected amount is
    significant. The thresholds are not final, but are currently planned to
    be 1 mm or more for sleet and freezing rain, 15 mm or more for rain, and
    1 cm or more for snow.

In each of the below precipitation types, the intensity of precipitation is
(very approximately) as follows:

*   `"very-light-X"`: 0.02–0.4 mm/hr
*   `"light-X"`: 0.4–2.5 mm/hr
*   `"medium-X"`: 2.5–10 mm/hr
*   `"heavy-X"`: 10 mm/hr

Snow intensities are (also very approximately) one-third of these. (That is,
`"heavy-snow"` is more like 3 mm/hr.) However, these are only intended as a
rough guide, as these values change over time as we fine-tune our system.

The `"possible-X"` text is added to the summary if the precipitation intensity is below 0.02 mm/h or if the hourly/daily possibility of precipitation is below 25% for the hour or the day.
Every intensity of every type has a `"possible-X"` form.

##### Generic Types

Generic precipitation forms are used when we don't have information regarding
the exact type of precipitation expected. (This is a rare occurrence.)

*   `"possible-very-light-precipitation"` (Usually called "possible light precipitation" in English.)
*   `"very-light-precipitation"` (Usually called "light precipitation" in English.)
*   `"possible-light-precipitation"` (Usually called "possible light precipitation" in English.)
*   `"light-precipitation"` (Usually called "light precipitation" in English.)
*   `"possible-medium-precipitation"` (Usually called "possible precipitation" in English.)
*   `"medium-precipitation"` (Usually called "precipitation" in English.)
*   `"possible-heavy-precipitation"` (Usually called "possible heavy precipitation" in English.)
*   `"heavy-precipitation"` (Usually called "heavy precipitation" in English.)

##### Rain Types

Rain precipitation forms represent liquid precipitation.

*   `"possible-very-light-rain"` (Usually called "possible drizzle" in English.)
*   `"very-light-rain"` (Usually called "drizzle" in English.)
*   `"possible-light-rain"` (Usually called "possible light rain" in English.)
*   `"light-rain"` (Usually called "light rain" in English.)
*   `"possible-medium-rain"` (Usually called "possible rain" in English.)
*   `"medium-rain"` (Usually called "rain" in English.)
*   `"possible-heavy-rain"` (Usually called "possible heavy rain" in English.)
*   `"heavy-rain"` (Usually called "heavy rain" in English.)

##### Sleet Types

Sleet precipitation forms represent sleet or ice pellets, of the sort that
generally occur in winter when temperatures are around freezing.

*   `"possible-very-light-sleet"` (Usually called "possible light sleet" in English.)
*   `"very-light-sleet"` (Usually called "light sleet" in English.)
*   `"possible-light-sleet"` (Usually called "possible light sleet" in English.)
*   `"light-sleet"` (Usually called "light sleet" in English.)
*   `"possible-medium-sleet"` (Usually called "possible sleet" in English.)
*   `"medium-sleet"` (Usually called "sleet" in English.)
*   `"possible-heavy-sleet"` (Usually called "possible heavy sleet" in English.)
*   `"heavy-sleet"` (Usually called "heavy sleet" in English.)

##### Freezing Rain Types

Freezing rain precipitation forms represent rain that falls as a liquid but
freezes on contact with the ground or other surfaces.

*   `"possible-very-light-freezing-rain"` (Usually called "possible freezing drizzle" in English.)
*   `"very-light-freezing-rain"` (Usually called "freezing drizzle" in English.)
*   `"possible-light-freezing-rain"` (Usually called "possible light freezing rain" in English.)
*   `"light-freezing-rain"` (Usually called "light freezing rain" in English.)
*   `"possible-medium-freezing-rain"` (Usually called "possible freezing rain" in English.)
*   `"medium-freezing-rain"` (Usually called "freezing rain" in English.)
*   `"possible-heavy-freezing-rain"` (Usually called "possible heavy freezing rain" in English.)
*   `"heavy-freezing-rain"` (Usually called "heavy freezing rain" in English.)

##### Snow Types

Snow precipitation forms represent solid precipitation in the form of
snowflakes.

*   `"possible-very-light-snow"` (Usually called "possible flurries" in English.)
*   `"very-light-snow"` (Usually called "flurries" in English.)
*   `"possible-light-snow"` (Usually called "possible light snow" in English.)
*   `"light-snow"` (Usually called "light snow" in English.)
*   `"possible-medium-snow"` (Usually called "possible snow" in English.)
*   `"medium-snow"` (Usually called "snow" in English.)
*   `"possible-heavy-snow"` (Usually called "possible heavy snow" in English.)
*   `"heavy-snow"` (Usually called "heavy snow" in English.)

##### Precipitation Accumulation

Represents a distance measurement indicating the amount of precipitation
accumulation that is expected. These take the form of "N in", "< N in", or
"M–N in" in English (and likewise for centimeters and millimeters).

*   `["inches", NUMBER]`
*   `["less-than", ["inches", 1]]`
*   `["inches", ["range", NUMBER, NUMBER]]`
*   `["centimeters", NUMBER]`
*   `["less-than", ["centimeters", 1]]`
*   `["centimeters", ["range", NUMBER, NUMBER]]`
*   `["millimeters", NUMBER]`
*   `["less-than", ["millimeters", 1]]`
*   `["millimeters", ["range", NUMBER, NUMBER]]`

#### Quantifiers

Quantifiers describe how a condition behaves over the course of the day. They
can be used anywhere a `WEATHER_CONDITION` is used in a day condition summary
(e.g. `["during", ["periods-of", "medium-rain"], "afternoon"]`). The wrapped
conditions are in the nominative case, so in languages where adjectives agree
with the noun, prefer an adverb or a phrase after the noun (e.g. Russian
"дождь с перерывами") over an adjective that would need to change with gender
or number.

##### Precipitation Quantifiers

*   `["intermittent", PRECIPITATION_TYPE]`: Precipitation that starts and
    stops. (e.g. "intermittent rain from afternoon until night")
*   `["occasional", PRECIPITATION_TYPE]`: Precipitation that only falls now and
    then. (e.g. "occasional rain starting in the morning")
*   `["periods-of", PRECIPITATION_TYPE]`: Precipitation that falls in distinct
    spells. (e.g. "periods of rain throughout the day")
*   `["tapering-off", PRECIPITATION_TYPE]`: Precipitation that gradually
    weakens and stops. (e.g. "rain tapering off in the afternoon")

##### Cloud Cover Quantifiers

*   `["generally", CLOUD_COVER]`: Cloud cover that mostly stays at one level.
    (e.g. "generally cloudy throughout the day")
*   `["to", CLOUD_COVER, CLOUD_COVER]`: Cloud cover that varies between two
    levels. (e.g. "partly cloudy to mostly cloudy")
*   `"increasing"`: Cloud cover that increases over the period. (e.g.
    "increasing clouds throughout the day")
*   `"clearing"`: Cloud cover that decreases over the period. (e.g. "clearing in
    the afternoon")

`CLOUD_COVER` is one of `"clear"`, `"very-light-clouds"`, `"light-clouds"`,
`"medium-clouds"` or `"heavy-clouds"`.

##### Transitions

*   `["becoming", WEATHER_CONDITION, WEATHER_CONDITION]`: One condition
    changing into another. Usually used for cloud cover (e.g. "partly cloudy
    becoming mostly cloudy in the afternoon"), but can also be used for one
    precipitation type changing into another (e.g. "rain becoming snow in the
    afternoon").

#### Other Weather Conditions

*   `"clear"`: Represents the lack of *any* significant weather occurring and cloud cover covering less than 11.5% of the sky.
*   `"possible-thunderstorm"`: Represents a chance of thunderstorms occurring.
*   `"thunderstorm"`: Represents thunderstorms occurring.
*   `"light-wind"`: Represents light wind at a location. (15 mph (~24.14 km/h) or greater)
    (Usually called "breezy" in English.)
*   `"medium-wind"`: Represents moderate wind at a location. (~22.37 mph (36 km/h) or greater)
    (Usually called "windy" in English.)
*   `"heavy-wind"`: Represents strong wind at a location. (40 mph (~64.37 km/h) or greater)
    (Usually called "very windy" in English.)
*   `"fog"`: Represents when there is less than approximately 0.62 miles (1 kilometer) of
    visibility and the dew point difference is less than or equal to 2.5C (4.5F).
*   `"smoke"`: Represents when it is not `fog`, and there is less than approximately 6.21 miles (10 kilometers) of
    visibility and surface smoke is greater than or equal to 25 µg/m<sup>3</sup>.
*   `"mist"`: Represents when it is not `fog` and not `smoke`, and there is less than approximately 6.21 miles (10 kilometers) of
    visibility and the dew point difference is less than or equal to 3C (5.4F).
*   `"haze"`: Represents when it is not `fog`, not `smoke`, and not `mist`, and there is less than approximately 6.21 miles (10 kilometers) of
    visibility, surface smoke is less than 25 µg/m<sup>3</sup> and the dew point difference is greater than 3C (5.4F).
*   `"very-light-clouds"`: Represents when clouds cover less than 37.5% of the sky.
    (Usually called "mostly clear" in English.)
*   `"light-clouds"`: Represents when clouds cover more than 37.5% but less than 62.5% of the sky.
    (Usually called "partly cloudy" in English.)
*   `"medium-clouds"`: Represents when clouds cover more than 62.5% (but not
    all) of the sky. (Usually called "mostly cloudy" in English.)
*   `"heavy-clouds"`: Represents complete (or nearly-complete) cloud cover.
    (Usually called "overcast" in English.)
