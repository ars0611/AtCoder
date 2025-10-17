import sys
import os

TEMPLATE = '''\
import sys
sys.setrecursionlimit(10**7)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
input = sys.stdin.readline
from collections import Counter, deque, defaultdict
from sortedcontainers import SortedSet, SortedList, SortedDict
from more_itertools import distinct_permutations
import heapq, bisect, math, itertools

#----------------------------------------#
'''

def create_abc_folder(contest_number):
    # スクリプトのあるフォルダから一つ上（= c:\python\AtCoder）をルートとする
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    base_path = os.path.join(repo_root, "contest")
    contest_dir = os.path.join(base_path, f"ABC{contest_number}")
    os.makedirs(contest_dir, exist_ok=True)

    for ch in "abcdefg":
        file_path = os.path.join(contest_dir, f"{ch}.py")
        if not os.path.exists(file_path):
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(TEMPLATE)

    input_txt_path = os.path.join(contest_dir, "input.txt")
    if not os.path.exists(input_txt_path):
        with open(input_txt_path, "w", encoding="utf-8") as f:
            f.write("")

    print(f"Created contest folder: {contest_dir}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python abcsetup.py <contest_number>")
    else:
        create_abc_folder(sys.argv[1])
