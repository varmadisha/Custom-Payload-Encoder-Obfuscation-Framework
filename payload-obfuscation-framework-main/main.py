"""
main.py

Runs the full payload encoding, obfuscation, and detection pipeline.
This is the entry point for the Payload Obfuscation & Evasion Framework.
"""

from encoder import Encoder
from obfuscator import Obfuscator
from detector import Detector


def print_result(name: str, payload: str):
    detected = Detector.scan(payload)
    status = "DETECTED" if detected else "BYPASSED"

    print(f"\n{name}")
    print("-" * len(name))
    print(payload)
    print(f"Detection Result: {status}")


def main():
    print("\nPayload Obfuscation & Signature Evasion Framework\n")

    payload = input("Enter test payload: ").strip()

    if not payload:
        print("No payload provided. Exiting.")
        return

    print_result("Original Payload", payload)

    # Encoding layer
    b64 = Encoder.base64_encode(payload)
    print_result("Base64 Encoded", b64)

    xor = Encoder.xor_encode(payload, "researchkey")
    print_result("XOR Encoded", xor)

    rot = Encoder.rot13(payload)
    print_result("ROT13 Encoded", rot)

    # Obfuscation layer
    noise = Obfuscator.insert_noise(payload)
    print_result("Noise Obfuscated", noise)

    split = Obfuscator.split_and_join(payload)
    print_result("Split & Join Obfuscated", split)

    escaped = Obfuscator.escape_hex(payload)
    print_result("Hex Escaped", escaped)


if __name__ == "__main__":
    main()
