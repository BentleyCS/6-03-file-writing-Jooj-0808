from fileinput import filename
import os
import pytest

import CSP_6_03_Writing_to_files as HW
from CSP_6_03_Writing_to_files import sortNames
from CSP_6_03_Writing_to_files import highScore


def test_writeFile():
    targetname = "lol"
    HW.writeFile(["First", "Second", "Third"], "lol")
    assert open(targetname, 'r').read() == "First\nSecond\nThird\n"
    os.remove(targetname)

def test_sortNames(tmp_path):
    with open("names.txt", "w") as f:
        f.write("Zebra\nApple\nMonkey\n")

    sortNames("names.txt", "namesNew.txt")

    assert open("namesNew.txt").read().splitlines() == ["Apple", "Monkey", "Zebra"]

    os.remove("names.txt")
    os.remove("namesNew.txt")

def test_highScore():
    with open("scores.txt", "w") as f:
        f.write("10\n20\n")

    assert highScore(30) == pytest.approx(20.0)

    if os.path.exists("scores.txt"): os.remove("scores.txt")
