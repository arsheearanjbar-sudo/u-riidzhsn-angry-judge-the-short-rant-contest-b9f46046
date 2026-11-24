"""Angry Judge: The Short Rant Contest -- entry writer.

Writes one short, funny rant about an everyday annoyance to
/output/entry.txt. Deterministic: the same text on every run.
"""

import os

RANT = (
    "The self-checkout machine watched me scan the same bag of apples "
    "twelve times, then asked if I need assistance, like a cashier who "
    "quit but stayed to judge me. It flagged the bag it told me to use "
    "as an unexpected item. I came for apples and left with a performance "
    "review from a toaster."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(RANT)


if __name__ == "__main__":
    main()
