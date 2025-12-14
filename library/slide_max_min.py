# 与えられた配列の窓（length = k）の中でmax,minをO(len(list))で求める
from collections import deque

# スライドmax
def slide_max(list, k):
    window = deque()
    max_num_in_window = []
    for i in range(len(list)):
        if window and window[0] < i - k + 1:
            window.popleft()
        while window and list[window[-1]] < list[i]:
            window.pop()
        window.append(i)
        if i >= k - 1:
            max_num_in_window.append(list[window[0]])
    return max_num_in_window

# スライドmin
def slide_min(list, k):
    window = deque()
    min_num_in_window = []
    for i in range(len(list)):
        if window and window[0] < i - k + 1:
            window.popleft()
        while window and list[window[-1]] > list[i]:
            window.pop()
        window.append(i)
        if i >= k - 1:
            min_num_in_window.append(list[window[0]])
    return min_num_in_window
