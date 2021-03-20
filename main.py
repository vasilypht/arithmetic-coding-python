import arithmetic as arith


def main() -> None:
    """Main function"""
    string = input("Enter the string: ")

    freq_dict, code = arith.encode(string)
    print(f"\nEncoded message:")
    print(f"(common) {code.numerator} / {code.denominator}")
    print(f"(decimal) {float(code):.30e}\n")

    decoded_string = arith.decode(code, freq_dict)
    print(f"Decoded message is '{decoded_string}'")


if __name__ == "__main__":
    main()
