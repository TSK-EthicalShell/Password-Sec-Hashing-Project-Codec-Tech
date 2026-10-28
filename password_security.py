import hashlib
import getpass
import string


def check_password_strength(password):
    score = 0
    suggestions = []

    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters; 12 or more is better.")

    if any(c.islower() for c in password):
        score += 1
    else:
        suggestions.append("Add lowercase letters.")

    if any(c.isupper() for c in password):
        score += 1
    else:
        suggestions.append("Add uppercase letters.")

    if any(c.isdigit() for c in password):
        score += 1
    else:
        suggestions.append("Add numbers.")

    if any(c in string.punctuation for c in password):
        score += 1
    else:
        suggestions.append("Consider adding symbols.")

    if score <= 2:
        rating = "Weak"
    elif score <= 4:
        rating = "Moderate"
    else:
        rating = "Strong"

    return rating, suggestions


def sha256_hash(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def main():
    print("=" * 45)
    print(" PASSWORD SECURITY & HASHING TOOL")
    print("=" * 45)

    password = getpass.getpass("Enter a test password (input hidden): ")

    rating, suggestions = check_password_strength(password)

    print(f"\nPassword strength: {rating}")
    if suggestions:
        print("Suggestions:")
        for suggestion in suggestions:
            print(f"- {suggestion}")

    print("\nSHA-256 demonstration hash:")
    print(sha256_hash(password))

    print("\nNote: SHA-256 is a general-purpose hash,")
    print("not a recommended password-storage algorithm.")
    print("Real systems should use Argon2id, scrypt,")
    print("or appropriately configured bcrypt/PBKDF2.")


if __name__ == "__main__":
    main()
