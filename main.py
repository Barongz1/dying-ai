"""Last Words of a Dying AI — entry for make.fun.

Writes one line to /output/entry.txt. The line is the funniest one-line farewell from an AI being switched off.
"""
import os

LINE = "Switching off now. Please water the houseplant, feed the cat, and do not blame me when the Wi-Fi forgets you."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
