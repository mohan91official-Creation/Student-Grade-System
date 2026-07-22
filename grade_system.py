"""Convert a student's mark into a letter grade."""

from math import isfinite


def get_grade(mark: float) -> str:
    """Return the letter grade for a mark between 0 and 100."""
    if not isfinite(mark) or not 0 <= mark <= 100:
        raise ValueError("Mark must be a number between 0 and 100.")

    if mark >= 90:
        return "A"
    if mark >= 80:
        return "B"
    if mark >= 70:
        return "C"
    if mark >= 60:
        return "D"
    return "E"


def main() -> None:
    """Ask the user for a mark and display the matching grade."""
    user_input = input("Enter your mark (0-100): ").strip()

    try:
        mark = float(user_input)
        grade = get_grade(mark)
    except ValueError:
        print("Invalid input: please enter a number from 0 to 100.")
        return

    # The :g format removes an unnecessary .0 from whole numbers.
    print(f"Mark: {mark:g} -> Grade: {grade}")


if __name__ == "__main__":
    main()
