"""Lab 04, Question 2 -- 24-hour clock arithmetic.

YOUR NAME
Complete time_to_seconds() and add_seconds_to_time().
Design at least one additional calculation helper.
Document the functions you write.
Add two assertions in main(). Follow the lab handout.
"""


def time_to_seconds(hhmmss):
    """TODO: replace this placeholder with a complete docstring."""
    pass


def seconds_to_time(total):
    """Format a second count as a zero-padded HH:MM:SS string.

    :param total: an integer number of seconds in [0, 86399]
    :return: the time as a zero-padded "HH:MM:SS" string
    """
    hours = total // 3600
    minutes = (total // 60) % 60
    seconds = total % 60
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


def add_seconds_to_time(hhmmss, delta):
    """TODO: replace this placeholder with a complete docstring."""
    pass


def main():
    """Drive the program."""
    # Add two checks for add_seconds_to_time: ordinary and midnight boundary.
    assert seconds_to_time(5) == "00:00:05"

    time_string = input("Input time: ")
    delta = int(input("Delta seconds: "))
    print(add_seconds_to_time(time_string, delta))


if __name__ == "__main__":
    main()
