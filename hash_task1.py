#!/usr/bin/env python3
"""
hash_task1.py - Hash Type Detector & MD5 Generator
Author: Mahmoud Hazaimeh
Student ID: 202220421
Course: Field Training / Cybersecurity
"""

import hashlib
import re
import sys


HASH_LENGTHS = {
    32:  ["MD5"],
    40:  ["SHA1"],
    64:  ["SHA256"],
    96:  ["SHA384"],
    128: ["SHA512"],
}


def is_hex(s):
    return bool(re.fullmatch(r'[0-9a-fA-F]+', s))


def detect_hash(hash_str):
    hash_str = hash_str.strip()

    if not hash_str:
        return None, "[-] Error: Empty input. Please enter a hash string."

    if not is_hex(hash_str):
        return None, (
            "[-] Unrecognized format.\n"
            "    The input contains non-hexadecimal characters.\n"
            "    A valid hash must only contain: 0-9 and a-f (or A-F)."
        )

    length = len(hash_str)

    if length not in HASH_LENGTHS:
        supported = ", ".join(
            f"{l} chars ({'/'.join(t)})" for l, t in sorted(HASH_LENGTHS.items())
        )
        return None, (
            f"[-] Unrecognized hash length: {length} characters.\n"
            f"    Supported lengths: {supported}\n"
            f"    This hash does not match any known algorithm."
        )

    matches = HASH_LENGTHS[length]
    return matches, None


def generate_md5(plaintext):
    plaintext = plaintext.strip()
    if not plaintext:
        return None, "[-] Error: Empty input. Please enter a plaintext string."
    digest = hashlib.md5(plaintext.encode("utf-8")).hexdigest()
    return digest, None


def print_banner():
    banner = r"""
  _  _         _      ___       _            _
 | || |__ _ __| |_   |   \ ___| |_ ___ __  | |_ ___ _ _
 | __ / _` (_-< ' \  | |) / -_)  _/ -_) _| |  _/ _ \ '_|
 |_||_\__,_/__/_||_| |___/\___|\__\___\__|  \__\___/_|

        Hash Type Detector & MD5 Generator
        Author : Mahmoud Hazaimeh | ID: 202220421
        Course : Field Training / Cybersecurity
        Use    : For educational and ethical purposes only
    """
    print(banner)
    print("-" * 60)


def interactive_menu():
    print_banner()

    while True:
        print("\n[*] Main Menu")
        print("    [1] Detect hash type")
        print("    [2] Generate MD5 from plaintext")
        print("    [0] Exit")
        print()

        choice = input("[?] Select an option: ").strip()

        if choice == "1":
            hash_input = input("\n[?] Enter hash string: ").strip()
            matches, error = detect_hash(hash_input)

            if error:
                print(f"\n{error}")
            else:
                print(f"\n[+] Input       : {hash_input.lower()}")
                print(f"[+] Length      : {len(hash_input.strip())} characters")
                print(f"[+] Possible type(s): {', '.join(matches)}")

        elif choice == "2":
            plaintext = input("\n[?] Enter plaintext: ").strip()
            digest, error = generate_md5(plaintext)

            if error:
                print(f"\n{error}")
            else:
                print(f"\n[+] Plaintext   : {plaintext}")
                print(f"[+] MD5 Hash    : {digest}")

        elif choice == "0":
            print("\n[*] Exiting. Goodbye!\n")
            sys.exit(0)

        else:
            print("\n[-] Invalid option. Please choose 1, 2, or 0.")


def cli_mode(hash_str):
    print_banner()
    matches, error = detect_hash(hash_str)

    if error:
        print(f"\n{error}\n")
        sys.exit(1)
    else:
        print(f"\n[+] Input       : {hash_str.strip().lower()}")
        print(f"[+] Length      : {len(hash_str.strip())} characters")
        print(f"[+] Possible type(s): {', '.join(matches)}\n")
        sys.exit(0)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        cli_mode(sys.argv[1])
    elif len(sys.argv) == 1:
        interactive_menu()
    else:
        print("Usage:")
        print("  Interactive mode : python3 hash_task1.py")
        print("  CLI mode         : python3 hash_task1.py <hash_string>")
        sys.exit(1)
