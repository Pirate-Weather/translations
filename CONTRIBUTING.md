Contributing Translations
---------------

The API (and therefore this module as well) is written in [Python][1]. Knowledge of that environment is
required in order to contribute to this software, but this document will do its
best to provide a crash-course for developers that are not familiar with Python.

[1]: https://www.python.org/

Getting Started
---------------

### Install Python

You will need to have [Python][1] installed. You can check to see whether it is installed by running:

    $ python -V or python3 -V
    v3.10.12

If the command gives an error message, you should re-install Python and try again.

### Install Dependencies

While this package requires no dependencies to run in production, if you want
to develop against it you will need the testing library [Pytest][2]. Installing
it is simple:

    $ python3 -m pip install  -r requirements.txt

[pip][3] is the Python Package Manager, and is part of the Python software
distribution. The above command will install the modules used for testing. After this, you can verify that everything is
working by running the tests:

    ======================================================================================== test session starts ========================================================================================
    platform linux -- Python 3.10.12, pytest-8.3.4, pluggy-1.5.0
    plugins: anyio-4.6.0, cov-6.0.0, subtests-0.14.1
    collected 18 items                                                                                                                                                                                  

    test.py .................,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,. [100%]

    ============================================================================= 18 passed, 3634 subtests passed in 7.33s ==============================================================================


[2]: https://docs.pytest.org/en/stable/
[3]: https://pip.pypa.io/en/stable/

Input Format
------------

The data passed from the Pirate Weather API to this translation module is a simple,
structured format reminiscent of [s-expressions][7], consisting only of
numbers, strings, and arrays. Some examples produced by the API are below:

*   `"heavy-rain"`
*   `["and", "light-wind", "light-clouds"]`
*   `["starting-in", "very-light-rain", ["minutes", 15]]`

Each of these expressions corresponds to a text summary in English:

*   "heavy rain"
*   "breezy and partly cloudy"
*   "drizzle starting in 15 minutes"

Generally speaking, numbers and strings represent specific terms, while arrays
represent templates dependent upon some number of arguments (with the first
element in that array representing the form of the template). For example, in
the sentence above, `"light-wind"` represents the English term "breezy",
`"light-clouds"` represents the English term "partly cloudy", and the array
`["and", X, Y]` represents the English phrase "X and Y".

In this way, the meaning (in English) of any given (machine-readable)
expression is intended to be fairly intuitive. However, a complete description
of the input format is given in [Appendix A](https://github.com/Pirate-Weather/translations?tab=readme-ov-file#appendix-a-pirate-weather-summary-format) anyway.

[7]: https://en.wikipedia.org/wiki/S-expression

Adding a Translation
--------------------

### Translation Submodules

There is one translation submodule per language, all found in the `/lib/lang`
directory. (Any source files in that directory are automatically loaded by the
library at run-time, so nothing further needs to be done once the file is
created.) Each submodule is a Python object, representing a collection
of *translation templates*. An expression (as described above) will get looked
up in the object and translated as the object's value dictates, recursively as
necessary.

For example, suppose we have the following object:

      template = {
          "very-light-rain": "drizzle",
      }
      
      def minutes_function(stack, n):
          return n + " minutes"

      def starting_in_function(stack, rain, time):
          return rain + " starting in " + time

And the expression noted above:

    ["starting-in", "very-light-rain", ["minutes", 15]]

The following algorithm will be applied:

1.  The function will first look at the expression `["starting-in", X, Y]` and
    find that there is a corresponding function in the associative array with
    two arguments. It will then recursively apply the procedure on these two
    arguments.

2.  The function will then look at the expression `"very-light-rain"`. There is
    also a match in the associative array, so this expression will be replaced
    with `"drizzle"`.

3.  The function will then look at the expression `["minutes", 15]`. There is
    once again a match in the associative array, for a function with a single
    argument. The function will once again recursively apply the procedure on
    the argument.

4.  The function will look at the expression `15`. Being a number, it will
    simply return it verbatim.

5.  Having it's single argument collected, `["minutes", 15]` is now replaced
    with the expression `"15 minutes"`, as per the code of the function for
    `"minutes"`.

6.  Finally, with the two arguments of `["starting-in", X, Y]` collected, they
    are substituted into the function and a final expression is returned:
    `"drizzle starting in 15 minutes"`.

Any arbitrary Python code may be used in a function, but in many templating
scenarios, only simple string concatenation is necessary. In these cases, a
shortcut syntax is also allowed:

    template = {
      "very-light-rain": "drizzle",
      "minutes": "$1 minutes",
      "starting-in": "$1 starting in $2"
    }

The [sigiled][8] expressions are replaced with the numbered argument to the
function (`$1` with the first argument, `$2` with the second, and so on).

Finally, if you need the extra power, each function's `stack` parameter is set
to an array representing the called function's position in the expression tree.
For example, in the example above, the `"minutes"` function is passed `stack`
with a value of `["starting-in", "minutes"]` since `"minutes"` is a child of
the `"starting-in"` template. (This is handy for languages like Dutch or German
where, I hear, that the ordering of words are important.)

Please see `/lib/lang/en.js` for an example of this in action.

[8]: http://en.wikipedia.org/wiki/Sigil_(computer_programming)

### Writing Tests

Once a new translation module has been created, it is advisable to write tests
for it to ensure its correctness. (In fact, it may be advisable to write the
tests beforehand!) Much of the work of this has been done for you; simply
create the file `/test-cases/<language>.py`. This file should contain an
associative array of translated sentences to the expression used to generate
them:

    {
      "drizzle starting in 15 minutes":
        ["starting-in", "very-light-rain", ["minutes", 15]]
    }

The English test cases (`/test-cases/en.py`) may be used as an example
and starting place. As noted above, you can verify your tests by running
`pytest test.py`. Pull requests without a full suite of passing tests will not
be accepted. Please make every effort to ensure that your tests provide
as full code coverage as possible.

General Considerations
----------------------

When translating text summaries, please keep the following in mind:

*   Text summaries are often used by API consumers in headings: **be as brief
    as possible,** and use abbreviations where appropriate.
*   It is simpler to maintain one version of a language than two: **avoid
    dialectal or regional variations** if at all possible. (For example, we try
    to maintain one version of English, despite the several major, distinct
    English variants—American English, British English, etc. We have had to
    alter terminology a few times to avoid generating insulting summaries!)
*   **Try to keep the text as natural as possible,** so that it is easily
    intelligible to an average reader. (Yes, we know this conflicts with
    brevity, but try your best!)
