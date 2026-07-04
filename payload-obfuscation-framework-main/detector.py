"""
detector.py

Implements a simple static signature-based detection engine.
This simulates how traditional antivirus and IDS systems
match known malicious patterns in payloads.
"""

from __future__ import annotations
from typing import List


class Detector:
    """
    A minimal signature-based scanner.
    Used to demonstrate how obfuscation defeats naive detection.
    """

    SIGNATURES: List[str] = [
        "powershell",
        "cmd",
        "malware",
        "invoke",
        "download",
        "shell"
    ]

    @staticmethod
    def scan(payload: str) -> bool:
        """
        Returns True if any malicious signature is found
        in the payload, otherwise False.
        """
        if not payload:
            return False

        data = payload.lower()

        for sig in Detector.SIGNATURES:
            if sig in data:
                return True

        return False
