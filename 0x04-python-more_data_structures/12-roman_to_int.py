#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string and isinstance(roman_string, str):
        roman =
        {"X": 10, "V": 5, "I": 1, "L": 50, "D": 500, "C": 100, "M": 1000}
        total = 0
        prev_value = 0

        """Iterates through the characters of the
        roman_string in reverse order.
        Reversing the string allows the function to easily compare
        the current
        numeral with the one before it."""
        for char in reversed(roman_string):
            current_value = roman.get(char, 0)
            if current_value >= prev_value:
                total += current_value
            else:
                total -= current_value
            prev_value = current_value

        return (total)
    else:
        return (0)
