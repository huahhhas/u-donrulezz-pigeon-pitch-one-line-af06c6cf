#!/usr/bin/env python3
"""Pigeon Pitch, One Line - entry program (Python stdlib only).

Writes the one-line elevator pitch to /output/entry.txt and prints it.
"""

ENTRY = "Investors, for seed money - literally, seed - my flock turns every rooftop into a last-mile delivery hub, staffed by birds who already work for crumbs."


def main():
    print(ENTRY)
    try:
        with open("/output/entry.txt", "w", encoding="utf-8") as f:
            f.write(ENTRY)
    except OSError:
        pass


if __name__ == "__main__":
    main()
