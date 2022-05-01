import matplotlib.pyplot as plt
class point:
        def __init__(self,x,y):
                self.x = x
                self.y = y
def Left_point(points):
    minn = 0
    for i in range(1,len(points)):
        if points[i].x < points[minn].x:
            minn = i
        elif points[i].x == points[minn].x:
            if points[i].y > points[minn].y:
                minn = i
    return minn
def orientation(p,q,r):
    val = (q.y - p.y)*(r.x - q.x) - (q.x - p.x)*(r.y - q.y)
    if val == 0:
        return 0
    elif val > 0:
        return 1
    else:
        return 2
def convexHull(points,n):
    if n < 3:
        return 
    l = Left_point(points)
    hull = []
    p = l
    q = 0
    while(True):
        hull.append(p)
        q = (p + 1) % n
        for i in range(n):
            if (orientation(points[p],points[i],points[q]) == 2):
                q = i
        p = q
        if(p == l):
            break
    Ax = list() ;Ay = list()
    for each in hull:
        Ax.append(points[each].x)
        Ay.append(points[each].y)
    return (Ax,Ay)
points = []
points.append(point(0,3)) ; points.append(point(2,2))
points.append(point(1,1)) ; points.append(point(1,4))
points.append(point(0.5,-3)) ;points.append(point(3,-5))
points.append(point(3.5,-4)) ; points.append(point(3,4))
points.append(point(3,2)) ; points.append(point(1,2))
points.append(point(2,1)) ; points.append(point(3,0))
points.append(point(0,0)) ; points.append(point(3,3))
points.append(point(0,3)) ; points.append(point(0.5,-4))
points.append(point(1.5,-6)) ; points.append(point(2,-3))
points.append(point(2.5,-5)) ; points.append(point(3.5,2))
points.append(point(3.8,-3)) ; points.append(point(3.7,-1))
lstx = list() ; lsty = list()
for i in points:
    lstx.append(i.x)
    lsty.append(i.y)
plt.scatter(lstx,lsty,s = 100,marker = '.')
A = convexHull(points, len(points))
print("A is:",A)
Ax = list() ; Ay = list()
for i in A[0]:
    Ax.append(i)
Ax.append(Ax[0])
for j in A[1]:
    Ay.append(j)
Ay.append(Ay[0])
plt.plot(Ax ,Ay)
plt.show()
convexHull(points, len(points))
