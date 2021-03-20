from fractions import Fraction
from collections import Counter
import sys


def arithmetic_encode(string: str) -> Fraction:
    """
    Function to encode a string using arithmetic coding.

    :param string: the input string to be encoded
    :return: object of class Fraction (common fraction)
    """
    freq_dict = Counter(string)
    segments = {}
    counter = Fraction()
    str_len = len(string)

    for char, freq in list(freq_dict.items()):
        probability = Fraction(freq, str_len)
        segments[char] = (counter, counter + probability)
        counter += probability

    left = Fraction()
    right = Fraction(1, 1)

    point = Fraction()

    for char in string:
        new_right = left + (right - left) * segments[char][1]
        new_left = left + (right - left) * segments[char][0]
        right = new_right
        left = new_left
        point = (left)

    return point


def arithmetic_decode(code: Fraction, freq_dict: dict) -> str:
    """
    A function to decode an encoded message using arithmetic coding.

    :param code: the code of the encoded message.
    :param freq_dict: dictionary with the frequencies of characters in the encoded string
    :return: decoded string
    """

    str_len = sum(freq_dict.values())
    segments = []
    decoded_string = ""

    counter = Fraction()
    for char, freq in list(freq_dict.items()):
        prob = Fraction(freq, str_len)
        segments.append((counter, counter + prob, char))
        counter += prob

    for _ in range(str_len):
        for left, right, char in segments:
            if left <= code < right:
                decoded_string += char
                code = (code - left) / (right - left)
                break

    return decoded_string


def main() -> None:
    string = sys.argv[1]
    print(f"Input string: {string}")

    freq_dict = Counter(string)
    encode = arithmetic_encode(string)
    print(f"\nEncoded message:")
    print(f"(common) {encode.numerator} / {encode.denominator}")
    print(f"(decimal) {float(encode):.30e}\n")

    decode = arithmetic_decode(encode, freq_dict)
    print(f"Decoded message is '{decode}'")


if __name__ == "__main__":
    main()
