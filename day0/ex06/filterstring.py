import sys
from ft_filter import ft_filter


def main():
    try:
        assert len(sys.argv) == 3, "the arguments are bad"

        s = sys.argv[1]
        n = sys.argv[2]

        assert isinstance(s, str), "the arguments are bad"
        assert n.isdigit(), "the arguments are bad"
        n = int(n)

        words = s.split()

        result = ft_filter(lambda word: len(word) > n, words)
        print(list(result))

    except AssertionError as e:
        print("AssertionError:", e)


if __name__ == "__main__":
    main()
