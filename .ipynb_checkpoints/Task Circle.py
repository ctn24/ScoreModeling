import numpy as np
import pandas as pd


def Convert(string):
    list1 = []
    list1[:0] = string
    return list1


X = [2, -1, -4, -3, 3, 3, 6]
Y = [2, -2, 4, 1, -3, 5, 1]
S = "ABDCPEP"
S = Convert(S)
R = np.sqrt(np.power(X, 2) + np.power(Y, 2))
R = np.around(R, 2)
df = pd.DataFrame([X, Y, S, R])
df = df.sort_values(by=3, axis=1)
df = df.transpose()
print(df)
good_points = df.duplicated(subset=2, keep='first')
ans = 0
for i in good_points:
    if not i:
        ans = ans + 1
    else:
        break
print(ans)

