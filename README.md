# Password Cracking and Hashing Algorithms

## Project Overview
This project demonstrates basic password security concepts using Python. It includes a password strength checker, SHA-256 hash generation, and an offline hash-matching demonstration using dummy test data.

## Objectives
- Understand password strength and common improvement suggestions.
- Learn how SHA-256 hashing works.
- Demonstrate how candidate text can be compared against a known hash.
- Understand the limitations of general-purpose hashing for password storage.

## Features
1. **Password Strength Checker** — evaluates password length and character variety.
2. **SHA-256 Hash Generator** — generates a hexadecimal hash for test input.
3. **Offline Hash-Matching Demo** — compares candidate strings against a hash created from controlled test data.

## Technologies Used
- Python 3
- `hashlib`
- `getpass`
- `string`

## Project Files
- `password_security.py` — password strength checking and SHA-256 hashing.
- `hash_demo.py` — offline hash-matching demonstration.
- `evidence/` — screenshots of actual program tests.

## How to Run
Run these commands from the project directory:

```bash
python3 password_security.py
python3 hash_demo.py
```

Use dummy test passwords only. Do not enter personal or reused passwords during demonstrations.

## Testing
The program was tested in Kali Linux with Python 3.13.12. The recorded tests include a weak password example, a strong password example, and a successful match in the offline demonstration dataset.

## Security Notes and Limitations
- This is an educational prototype, not a full password-cracking engine.
- SHA-256 is a general-purpose hash and is not recommended by itself for password storage.
- Production applications should use a password-hashing scheme such as Argon2id, scrypt, or appropriately configured bcrypt/PBKDF2.
- Only dummy test data is used in the hash-matching demonstration.

## Conclusion
This project helped demonstrate password-strength checks, hash generation, and basic hash matching. It also highlights why secure password storage requires algorithms designed specifically for passwords.


