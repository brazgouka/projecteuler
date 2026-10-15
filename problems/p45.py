
def fx(x):
    return int(x*(x+1)/2)

def fy(y):
    return int(y*(3*y-1)/2)

def fz(z):
    return int(z*(2*z-1))

skip = 1
x, y, z = 2, 2, 2
vx, vy, vz = fx(x), fy(y), fz(z)
while skip != -1:
    while not (vx == vy and vy == vz):
        min_v = min(min(vx, vy), vz)
        if min_v == vx:
            x += 1
            vx = fx(x)
        if min_v == vy:
            y += 1
            vy = fy(y)
        if min_v == vz:
            z += 1
            vz = fz(z)
    skip -= 1
    x += 1
    vx = fx(x)
print(vy)
