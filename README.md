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
format (described below) rather than it's usual English; summaries in this new
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
`"summary"` component wraps the construction (signifying that the summary
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
`"minutes"` are only used as above. `"less-than"` is also used for snow
accumulation (see below).

### Day Summaries

Day summaries are produced by the API when a duration of 24 hours is under
consideration (that is, `hourly.summary` and `daily.data[N].summary`). They are
the most complex summaries in the API, owing to the number of possible
combinations of the various terms. They are of the following formats:

*   `["sentence", DAY_CONDITION_SUMMARY]`
*   `["sentence", ["and", DAY_CONDITION_SUMMARY, DAY_CONDITION_SUMMARY]]`

#### Day Condition Summaries

A "day condition" represents a specific weather condition at a specific time of
day. (Or a larger period of the day, as the case may be.)

*   `["for-day", WEATHER_CONDITION]`
*   `["during", WEATHER_CONDITION, TIME_OF_DAY]`
*   `["during", WEATHER_CONDITION, ["and", TIME_OF_DAY, TIME_OF_DAY]]`
*   `["starting", WEATHER_CONDITION, TIME_OF_DAY]`
*   `["until", WEATHER_CONDITION, TIME_OF_DAY]`
*   `["starting-continuing-until", WEATHER_CONDITION, TIME_OF_DAY, TIME_OF_DAY]`
*   `["until-starting-again", WEATHER_CONDITION, TIME_OF_DAY, TIME_OF_DAY]`

`"for-day"`, `"starting"`, `"until"`, `"starting-continuing-until"`, and
`"until-starting-again"` are only used in the above manner, and may be
considered analagous to the five similar cases in hourly summaries. `"during"`
is used both here and in weekly summaries, below.

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

In general, the most specific case is used. (For example, if it is currently
afternoon and a weather condition would occur later in the afternoon,
`"later-today-afternoon"` would be used. If it was any other time of day,
`"today-afternoon"` would be used.)

The exact times that each duration begins or ends is not intended to be
critical, and nonprecise terminology should be used if possible. However, for
aid in translation, the time periods currently correspond to the following:

*   **morning:**   04:00  (4am) to 12:00 (12pm)
*   **afternoon:** 12:00 (12pm) to 17:00  (5pm)
*   **evening:**   17:00  (5pm) to 22:00 (10pm)
*   **night:**     22:00 (10pm) to 04:00  (4am)

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
*   `["during", PRECIPITATION_TYPE, ["through", DAY_OF_WEEK, DAY_OF_WEEK]]`

`"for-week"`, `"over-weekend"`, and `"through"` are both only used as above.
`"during"` is used both here and in daily summaries.

#### Weekly Temperature Summary

A "weekly temperature summary" describes the general pattern of temperatures
over the course of the next week: whether they'll get hotter, colder,
hotter-then-colder, or colder-then-hotter.

*   `["temperatures-rising", TEMPERATURE, DAY_OF_WEEK]`
*   `["temperatures-falling", TEMPERATURE, DAY_OF_WEEK]`
*   `["temperatures-peaking", TEMPERATURE, DAY_OF_WEEK]`
*   `["temperatures-valleying", TEMPERATURE, DAY_OF_WEEK]`

`"temperatures-peaking"`, `"temperatures-valleying"`, `"temperatures-rising"`,
and `"temperatures-falling"` are all only used as above.

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
would be `["during", "rain", "next-wednesday"]`.

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
*   `SNOW_TYPE`
*   `["parenthetical", EXPECTED_PRECIP_TYPE, SNOW_ACCUMULATION]`: For daily or
    weekly summaries, if a significant amount of snow is expected, we will
    qualify it with the amount of expected snow accumulation. (For example,
    "snow (3-4 in.) throughout the day".) PLEASE NOTE that it is possible for a
    chance of snow accumulation to be forecasted even if the expected
    precipitation type is rain or sleet: this may occur if the forecasted
    temperature is right around the freezing point. Translations should clarify
    that the parenthetical refers to a chance of snow in such circumstances.
    (For example, "sleet (chance of 3-4 in. of snow) throughout the day".)

In each of the below precipitation types, the intensity of precipitation is
(very approximately) as follows:

*   `"very-light-X"`: 0.02–0.4 mm/hr
*   `"light-X"`: 0.4–2.5 mm/hr
*   `"medium-X"`: 2.5–10 mm/hr
*   `"heavy-X"`: 10 mm/hr

Snow intensities are (also very approximately) one-third of these. (That is,
`"heavy-snow"` is more like 3 mm/hr.) However, these are only intended as a
rough guide, as these values change over time as we fine-tune our system.

##### Generic Types

Generic precipitation forms are used when we don't have information regarding
the exact type of precipitation expected. (This is a rare occurance.)

*   `"possible-very-light-precipitation"`
*   `"very-light-precipitation"`
*   `"possible-light-precipitation"`
*   `"light-precipitation"`
*   `"medium-precipitation"`
*   `"heavy-precipitation"`

##### Rain Types

Rain precipitation forms represent liquid precipitation.

*   `"possible-very-light-rain"`
*   `"very-light-rain"`
*   `"possible-light-rain"`
*   `"light-rain"`
*   `"medium-rain"`
*   `"heavy-rain"`

##### Sleet Types

Sleet precipitation forms represent sleet, freezing rain, or ice pellets, of
the sort that generally occur in winter when temperatures are around freezing.

*   `"possible-very-light-sleet"`
*   `"very-light-sleet"`
*   `"possible-light-sleet"`
*   `"light-sleet"`
*   `"medium-sleet"`
*   `"heavy-sleet"`

##### Snow Types

Snow precipitation forms represent solid precipitation in the form of
snowflakes.

*   `"possible-very-light-snow"`
*   `"very-light-snow"`
*   `"possible-light-snow"`
*   `"light-snow"`
*   `"medium-snow"`
*   `"heavy-snow"`

##### Snow Accumulation

Represents a distance measurement indicating the amount of snow accumulation is
expected. These take the form of "N inches", "< N inches", or "M-N inches"
in English, respectively.

*   `["inches", NUMBER]`
*   `["less-than", ["inches", 1]]`
*   `["inches", ["range", NUMBER, NUMBER]]`
*   `["centimeters", NUMBER]`
*   `["less-than", ["centimeters", 1]]`
*   `["centimeters", ["range", NUMBER, NUMBER]]`

#### Other Weather Conditions

*   `"clear"`: Represents the lack of *any* significant weather occurring and cloud cover covering less than 11.5% of the sky.
*   `"possible-thunderstorm"`: Represents a chance of thunderstorms occurring.
*   `"thunderstorm"`: Represents thunderstorms occurring.
*   `"light-wind"`: Represents light wind at a location. (15 mph (~24.14 km/h) or greater)
*   `"medium-wind"`: Represents moderate wind at a location. (~22.37 mph (36 km/h) or greater)
*   `"heavy-wind"`: Represents strong wind at a location. (40 mph (~64.37 km/h) or greater)
*   `"low-humidity"`: Represents when the humidity is below 15%
*   `"high-humidity"`: Represents when the humidity is above 95% and the air temperature is above 20C (68F).
*   `"fog"`: Represents when there is less than approximately 0.62 miles (1 kilometers) of
    visibility.
*   `"very-light-clouds"`: Represents when clouds cover more less than 37.5% of the sky.
    (Usually called "mostly clear" in English.)
*   `"light-clouds"`: Represents when clouds cover more than than 37.5% but less than 62.5% of the sky.
    (Usually called "partly cloudy" in English.)
*   `"medium-clouds"`: Represents when clouds cover more than 62.5% (but not
    all) of the sky. (Usually called "mostly cloudy" in English.)
*   `"heavy-clouds"`: Represents complete (or nearly-complete) cloud cover.
    (Usually called "overcast" in English.)
