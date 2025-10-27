import sys


def main():
    NESTED_MORSE = {
            "A": ".- ", "B": "-... ", "C": "-.-. ", "D": "-.. ", "E": ". ",
            "F": "..-. ", "G": "--. ", "H": ".... ", "I": ".. ", "J": ".--- ",
            "K": "-.- ", "L": ".-.. ", "M": "-- ", "N": "-. ", "O": "--- ",
            "P": ".--. ", "Q": "--.- ", "R": ".-. ", "S": "... ", "T": "- ",
            "U": "..- ", "V": "...- ", "W": ".-- ", "X": "-..- ", "Y": "-.-- ",
            "Z": "--.. ", "0": "----- ", "1": ".---- ", "2": "..--- ",
            "3": "...-- ", "4": "....- ", "5": "..... ", "6": "-.... ",
            "7": "--... ", "8": "---.. ", "9": "----. ", " ": "/ "
            }
    try:
        assert len(sys.argv) == 2, "the arguments are bad"
        text = sys.argv[1]
        assert isinstance(text, str), "the arguments are bad"

        morse = ""
        for c in text.upper():
            assert c in NESTED_MORSE, "the arguments are bad"
            morse += NESTED_MORSE[c]

        print(morse.strip())

    except AssertionError as e:
        print("AssertionError:", e)


if __name__ == "__main__":
    main()
