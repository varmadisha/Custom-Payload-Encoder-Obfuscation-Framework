"""
obfuscator.py

Implements reversible string-level obfuscation techniques
used to study how static signatures can be bypassed.
These transformations preserve the logical content
while changing the raw byte patterns.
"""

from __future__ import annotations
import random
import string
from typing import List


class Obfuscator:
    """
    Obfuscator applies lightweight, reversible transformations
    that are commonly seen in real-world malware and red-team tooling.
    """

    @staticmethod
    def insert_noise(payload: str, probability: float = 0.25) -> str:
        """
        Randomly insert harmless characters between real characters.
        This breaks simple keyword-based signatures.
        """
        if not payload:
            return ""

        out: List[str] = []

        for ch in payload:
            out.append(ch)
            if random.random() < probability:
                out.append(random.choice(string.ascii_letters))

        return "".join(out)

    @staticmethod
    def split_and_join(payload: str, chunk_size: int = 3) -> str:
        """
        Split the payload into small chunks and rejoin them
        using a separator. Semantics stay the same, but
        pattern matching becomes harder.
        """
        if not payload:
            return ""

        parts = [payload[i:i + chunk_size] for i in range(0, len(payload), chunk_size)]
        return "+".join(parts)

    @staticmethod
    def escape_hex(payload: str) -> str:
        """
        Encode each character as a hex escape sequence.
        This simulates how scripts hide strings.
        """
        return "".join(f"\\x{ord(ch):02x}" for ch in payload)
