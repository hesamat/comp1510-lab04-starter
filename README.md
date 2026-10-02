# COMP 1510 - Lab 4: Functions and Debugging

Open a terminal in the folder where you keep your course projects, outside
any existing project. Run this command to clone the starter repository:

```sh
git clone https://github.com/hesamat/comp1510-lab04-starter.git
```

This creates a new folder named `comp1510-lab04-starter`. In PyCharm, choose
**File > Open** and select that folder. Follow the Lab 4 handout on Learning Hub
for the requirements and pytest setup.

Install `pytest` for the project's selected Python interpreter. Test run
configurations must use that same interpreter. If tests report
`No module named 'pytest'`, open **Run > Edit Configurations**, select your
test run, and set **Python Interpreter** to **Project Default** or the same
interpreter you chose for the project.

In your own code, use the course's basic variables, numbers, strings, indexing,
arithmetic, comparisons, Boolean operators, conditions, loops, built-in functions,
and string operations, plus functions, parameters, returned values, docstrings,
and assertions. Do not create lists, dictionaries, sets, or tuples. Do not use
`range()`, comprehensions, classes, additional imports, `try`/`except`, `global`,
or doctests.
These restrictions do not apply to the supplied formatting helper and tests:
leave them unchanged, and call the formatter as provided.

- Complete `decide_winner(player_one, player_two)` in `q1.py` to referee
  one round of rock, paper, scissors. Return `"Player 1"`, `"Player 2"`, or
  `"Tie"` and add a one-sentence docstring. Keep the supplied `main()` unchanged.
  Run the handout's four sample cases. Question 1 requires no assertions,
  pytest tests, or report section.
- Complete `time_to_seconds(hhmmss)` to return integer seconds since midnight,
  using indexing to read the time string. Complete
  `add_seconds_to_time(hhmmss, delta)` to return the adjusted `HH:MM:SS` string.
  Keep both supplied function names and parameters unchanged. Design and write
  at least one additional calculation helper with clear inputs and a returned
  result. Use your conversion function, the supplied formatter, and at least
  one of your additional helpers in `add_seconds_to_time()`.
  Keep the supplied `seconds_to_time()` and `main()` unchanged except for two
  assertions: one nonzero change within a day and one change crossing midnight,
  both checking `add_seconds_to_time()`. Document all functions you write.
  Run the `tests/` folder through pytest to run all supplied clock tests.
  Run `q2.py` with the handout's sample inputs to execute
  your assertions and check the keyboard input and printed result.
- Investigate and repair `longest_digit_streak()` in `digit_streak.py` using
  the three supplied tests in `test_digit_streak.py`.
- Complete the compact debugging record in `debugging.md`: keep your original
  prediction, record the failed test and expected/actual results, then record
  the statement changed (original and replacement), a brief explanation,
  and final pytest summary.
  No screenshots are required.

The `tests/` folder contains the supplied clock tests. Leave all
supplied tests unchanged. At the start of Question 2, run
`tests/test_seconds_to_time.py::test_zero_is_midnight`, which checks the supplied
formatter and passes before you implement the clock functions. Running all
clock tests with the unmodified starter gives **10 failed, 4 passed**. Tests for
unfinished functions will fail until you complete them.

For help, see the [Git cloning reference](https://git-scm.com/docs/git-clone)
and [PyCharm pytest guide](https://www.jetbrains.com/help/pycharm/pytest.html).
For terminal use, see the [official pytest getting-started guide](https://docs.pytest.org/en/stable/getting-started.html).

## Submit on Learning Hub

Upload these four files to the Lab 4 dropbox:

- `q1.py`
- `q2.py`
- `digit_streak.py` (with your repair)
- `debugging.md`

Check that all four files uploaded successfully. Git commits and pushes are not
required for this lab.
