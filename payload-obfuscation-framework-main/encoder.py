"""
encoder.py

High-quality encoding primitives used in payload obfuscation
and evasion research. This module implements common transformation
techniques observed in real-world malware and red-team tooling,
but is intended strictly for defensive and educational use.
"""

from __future__ import annotations
import base64
from typing import List


class Encoder:
    """
    Encoder implements multiple reversible transformations that
    alter the raw byte patterns of a payload while preserving
    its semantic meaning.
    """

    @staticmethod
    def base64_encode(payload: str) -> str:
        """
        Encode a payload using Base64.

        Base64 is commonly used to transport or hide payloads
        inside scripts, documents, or network traffic.
        """
        if not isinstance(payload, str):
            raise TypeError("payload must be a string")

        data = payload.encode("utf-8")
        encoded = base64.b64encode(data)
        return encoded.decode("utf-8")

    @staticmethod
    def xor_encode(payload: str, key: str) -> str:
        """
        XOR-encode a payload using a repeating key.

        XOR is widely used by malware because it is fast,
        reversible, and breaks simple static signatures.
        """
        if not payload:
            return ""
        if not key:
            raise ValueError("XOR key must not be empty")

        out: List[str] = []

        for i, ch in enumerate(payload):
            key_char = key[i % len(key)]
            out.append(chr(ord(ch) ^ ord(key_char)))

        return "".join(out)

    @staticmethod
    def rot13(payload: str) -> str:
        """
        Apply the ROT13 substitution cipher.

        ROT13 is a classic lightweight obfuscation technique
        that shifts alphabetical characters by 13 positions.
        """
        result: List[str] = []

        for ch in payload:
            o = ord(ch)

            if 65 <= o <= 90:       # A–Z
                result.append(chr((o - 65 + 13) % 26 + 65))
            elif 97 <= o <= 122:    # a–z
                result.append(chr((o - 97 + 13) % 26 + 97))
            else:
                result.append(ch)

        return "".join(result)
