f = open('24.7.txt').readline()
mx = 0
for i in range(len(f) - 1):
    if f[i] in '-*0': continue
    r = i
    while  r < len(f) and f[r:r+2] not in ['--', '**', '-*', '*-', '-0', '*0']:
        r += 1
    mx = max(mx, r-i)
print(mx)