#!/usr/bin/env python3

import subprocess
import sys

def get_volume():
    r = subprocess.run(["osascript", "-e", "get volume settings"], capture_output=True)
    for part in [t.strip() for t in r.stdout.decode('utf-8').split(',')]:
        if not part.startswith("output volume:"):
            continue
        return int(part.split(":")[1].strip())
    return None


def is_muted():
    r = subprocess.run(["osascript", "-e", "get volume settings"], capture_output=True)
    for part in [t.strip() for t in r.stdout.decode("utf-8").split(',')]:
        if not part.startswith("output muted:"):
            continue
        return part.split(":")[1].strip() == "true"
    return None


def set_muted(mute = None):
    if mute is None:
        mute = is_muted() is False # used to switch the state
    subprocess.run(["osascript", "-e", "set volume output muted {}".format("true" if mute else "false")])


def change_volume(change):
    current_vol = get_volume()
    if current_vol is None:
        print("Failed to get volume...")
        return
    if is_muted():
        set_muted(False)
    current_vol += change
    if current_vol < 0:
        current_vol = 0
    elif current_vol > 100:
        current_vol = 100
    subprocess.run(["osascript", "-e", "set volume output volume {}".format(current_vol)])
    print("Volume is now at {}".format(current_vol))


if __name__ == "__main__":
    argv = sys.argv[1:]
    if len(argv) > 0:
        if argv[0] == "up":
            change_volume(10)
        elif argv[0] == "down":
            change_volume(-10)
        elif argv[0] == "mute":
            set_muted()
        else:
            print("Unknown command...")
    else:
        print("missing command (up, down or mute)")
