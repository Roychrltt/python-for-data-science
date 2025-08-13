import sys

def count(s):
    p = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    return {
        'upper': sum(1 for c in s if c.isupper()),
        'lower': sum(1 for c in s if c.islower()),
        'punctuation': sum(1 for c in s if c in p),
        'spaces': sum(1 for c in s if c == ' '),
        'digits': sum(1 for c in s if c.isdigit()),
        'length': len(s)
    }

def get_text_from_args():
    try:
        if len(sys.argv) == 1:
            return input("Enter a string:\n")
        elif len(sys.argv) > 2:
            raise AssertionError("AssertionError: more than one argument provided")
        else:
            return sys.argv[1]
    except Exception as e:
        print(e)
        sys.exit()

def display_counts(counts):
    print(f"The text contains {counts['length']} characters:")
    print(f"{counts['upper']} upper letters")
    print(f"{counts['lower']} lower letters")
    print(f"{counts['punctuation']} punctuation marks")
    print(f"{counts['spaces']} spaces")
    print(f"{counts['digits']} digits")

def main():
    text = get_text_from_args()
    counts = count(text)
    display_counts(counts)

if __name__ == "__main__":
    main()

