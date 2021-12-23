import numpy as np
import pandas as pd

N = 5

Allocation = np.array([[0, 1, 0], [2, 0, 0], [3, 0, 2], [2, 1, 1], [0, 0, 2]])
Max = np.array([[7, 5, 3], [3, 2, 2], [13, 0, 2], [2, 2, 2], [4, 3, 3]])
Available = np.array([3, 3, 2])
# Need = np.array([[7, 4, 3], [1, 2, 2], [10, 0, 0], [0, 1, 1], [4, 3, 1]])
Need = np.array(Max - Allocation)

data = {
    "Allocation": list(map(str, Allocation)),
    "Max": list(map(str, Max)),
    "Need": list(map(str, Need)),
}
print(pd.DataFrame(data, index=["P0", "P1", "P2", "P3", "P4"]))
print("Available", Available)
print()

# print("Allocation")
# print(*Allocation, sep="\n")
# print("Max")
# print(*Max, sep="\n")
# print("Available")
# print(Available)
# print("Need")
# print(*Need, sep="\n")


def safe_check():
    print("safe_check() start")

    # 1
    Work = Available.copy()
    print("Work : ", Work)
    Finish = [False] * N

    while True:
        # 2
        for i in range(N):
            if Finish[i] == False and np.all(Need[i] <= Work):
                # 3
                Work = Work + Allocation[i]
                Finish[i] = True  # finish i, 리소스 해제
                print(f"P{i} : True, Work : {Work}")
                break
        # 2.1
        else:
            break
    # 4
    for i in range(N):
        if Finish[i] == False:
            return False
    return True


print(f"safe_check() : {safe_check()}")
