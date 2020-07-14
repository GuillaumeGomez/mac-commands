#!/usr/bin/env python3

# Requires to first install `brightness`:
# `brew install brightness`

import subprocess
import sys

def get_brightness():
    r = subprocess.run(["brightness", "-l"], capture_output=True)
    for part in [t.strip() for t in r.stdout.decode('utf-8').split('\n')]:
        if not part.startswith("display 0:"):
            continue
        sub = part.split(":")[1].strip()
        if not sub.startswith("brightness "):
            continue
        return float(sub.split(" ")[1].strip())
    return None

def change_brightness(change):
    current_bri = get_brightness()
    if current_bri is None:
        print("Failed to get brightness...")
        return
    current_bri += change
    if current_bri < 0:
        current_bri = 0
    elif current_bri > 1:
        current_bri = 1
    subprocess.run(["brightness", str(current_bri)])
    print("brightness is now at {}".format(current_bri))


if __name__ == "__main__":
    argv = sys.argv[1:]
    if len(argv) > 0:
        if argv[0] == "up":
            change_brightness(0.1)
        elif argv[0] == "down":
            change_brightness(-0.1)
        else:
            print("Unknown command...")
    else:
        print("missing command (up or down)")
