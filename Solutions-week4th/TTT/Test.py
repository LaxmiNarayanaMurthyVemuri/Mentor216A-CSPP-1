
def cwin(n, c):
    g = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for i in range(8):
        if n[g[i][0]] == c and n[g[i][1]] == c and n[g[i][2]] == c:
            return True
    return False




n = []
for _ in range(3):
    n.append(input().split())
xcnt = n.count("x")
ocnt = n.count("o")
flag = 1
if((xcnt == ocnt + 1) and cwin(n,"x") and (not cwin(n, "o"))):
    print('x')
elif((xcnt==ocnt) and (not cwin(n,"x")) and cwin(n, "o")):
    print("o")
elif((xcnt == ocnt + 1) and (not cwin(n,"x")) and (not cwin(n, "o"))):
    print("draw")
else:
    print("invalid input")