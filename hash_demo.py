import hashlib

def sha256_hash(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()

# Dummy example only; no real account or password hashes.
test_candidates = ["hello123", "CyberDemo123!", "student2026"]

# Create a sample target hash from our own test data.
target_hash = sha256_hash("CyberDemo123!")

print("OFFLINE HASH-MATCHING DEMO")
print("-" * 30)

for candidate in test_candidates:
    candidate_hash = sha256_hash(candidate)
    print(f"Testing candidate: {candidate}")

    if candidate_hash == target_hash:
        print("Result: Match found in the demo dataset.")
        break
else:
    print("No match found in the demo dataset.")
