from fractions import Fraction
from collections import Counter


def encode(string: str) -> tuple[Counter, Fraction]:
    """Function to encode a string using arithmetic coding.

    Args:
        string (str): The input string to be encoded

    Returns:
        Fraction: Encoded string (common fraction).
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
        point = (left + right) / 2

    return freq_dict, point


def decode(code: Fraction, freq_dict: Counter) -> str:
    """A function to decode an encoded message using arithmetic coding.

    Args:
        code (Fraction): The code of the encoded message.
        freq_dict (Counter): dictionary with the frequencies of characters in
        the encoded string.

    Returns:
        [str]: decoded string
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
