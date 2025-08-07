import sys
import os

TEMPLATE = '''\
import sys
sys.setrecursionlimit(10**7)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
from collections import Counter
from collections import deque
from collections import defaultdict
import bisect
import math
import itertools
import copy

#----------------------------------------#
'''

def create_abc_folder(contest_number):
    base_path = os.path.join(os.path.expanduser("~"), "Desktop", "python","AtCoder", "contest")
    contest_dir = os.path.join(base_path, f"ABC{contest_number}")
    os.makedirs(contest_dir, exist_ok=True)

    for ch in "abcdefg":
        file_path = os.path.join(contest_dir, f"{ch}.py")
        if not os.path.exists(file_path):
            with open(file_path, "w") as f:
                f.write(TEMPLATE)

    input_txt_path = os.path.join(contest_dir, "input.txt")
    if not os.path.exists(input_txt_path):
        with open(input_txt_path, "w") as f:
            f.write("")

    print(f"Created contest folder: {contest_dir}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python abcsetup.py <contest_number>")
    else:
        create_abc_folder(sys.argv[1])
