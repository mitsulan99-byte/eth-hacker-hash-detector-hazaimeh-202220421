```
 _  _         _      ___       _            _
| || |__ _ __| |_   |   \ ___| |_ ___ __  | |_ ___ _ _
| __ / _` (_-< ' \  | |) / -_)  _/ -_) _| |  _/ _ \ '_|
|_||_\__,_/__/_||_| |___/\___|\__\___\__|  \__\___/_|
```

# eth-hacker-hash-detector

> A command-line Python tool that identifies common cryptographic hash types and generates MD5 digests — built for security students and ethical hackers.

![Python](https://img.shields.io/badge/Python-3.x-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Use](https://img.shields.io/badge/Use-Educational%20%2F%20Ethical-orange)

---

## Features

- Detect hash type from input string: **MD5, SHA1, SHA256, SHA384, SHA512**
- Generate **MD5** hash from any plaintext input
- Validates hexadecimal format before attempting detection
- Clear error messages for invalid or unrecognized input
- Two modes: **interactive menu** and **one-shot CLI**
- No external dependencies — uses Python standard library only

---

## Quick Usage

### Interactive mode
```bash
python3 hash_task1.py
```

### CLI mode (direct detection)
```bash
python3 hash_task1.py <hash_string>
```

**Examples:**
```bash
# Detect an MD5 hash
python3 hash_task1.py 5f4dcc3b5aa765d61d8327deb882cf99

# Detect a SHA256 hash
python3 hash_task1.py e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855

# Interactive menu
python3 hash_task1.py
```

---

## Design

Detection works in three steps:

1. **Hex validation** — the input is checked against a regular expression that allows only hex characters (`0-9`, `a-f`, `A-F`). Any other character immediately marks the input as invalid.
2. **Length mapping** — the length of the hex string is compared against a fixed table:
   | Length | Algorithm |
   |--------|-----------|
   | 32     | MD5       |
   | 40     | SHA1      |
   | 64     | SHA256    |
   | 96     | SHA384    |
   | 128    | SHA512    |
3. **Result output** — if a match is found, the tool reports the algorithm(s). If not, a descriptive error message is shown.

MD5 generation uses Python's `hashlib.md5()` with UTF-8 encoding to ensure consistent, deterministic output.

---

## Installation

No installation required. Only Python 3 standard library modules are used:

```
hashlib   re   sys
```

**Clone and run:**
```bash
git clone https://github.com/<yourusername>/eth-hacker-hash-detector-hazaimeh-202220421.git
cd eth-hacker-hash-detector-hazaimeh-202220421
python3 hash_task1.py
```

---

## Screenshots

| Action | Screenshot |
|--------|------------|
| Detecting MD5 | `screenshots/detect_md5.png` |
| Detecting SHA256 | `screenshots/detect_sha256.png` |
| Generating MD5 | `screenshots/generate_md5.png` |
| Invalid input | `screenshots/invalid_input.png` |

---

## Ethical Use

This tool is developed strictly for **educational and ethical purposes**.
It is intended to support learning in cybersecurity courses and should not be used for any unauthorized or malicious activity.

---

## How to Cite / Contact

**Author:** Mahmoud Hazaimeh  
**Student ID:** 202220421  
**University:** Faculty of Science and Technology — Cybersecurity  
**Course:** Field Training / Cybersecurity  
**Supervisor:** Abdulrahman Al-Faqih  
