import matplotlib.pyplot as plt
from scipy.spatial import  Voronoi, voronoi_plot_2d
import numpy as np
import math
import pyclipper
import tripy
from shapely.geometry import Point,Polygon #used to chk pt in or out of poly
from math import sqrt
import time
#Start = time.time() #starting the time
#print("The start time is:",Start)
X = [];Y = [];Pi = [];PS = [];Xn = []; S = [];Yx = [];Yn = []; Yy = []; Pout = []
MP = []; Ym = [];Yp = [];Poly = []; YN = [];m = []; Pc = []; Pcc = []
#points = np.array([(1,8),(4,3),(6,0),(7,4),(8,2),(9,9),(7,6),(5,7),(5,5),(1,8)])
#points = np.array([(1,1),(2,2),(1,5),(4,3),(5,7),(5,5),(10,10)\
#          ,(10,-5),(6,-1),(3,-3),(1,1)])
Poly = [(24970,19250),(23600,19250),(20740,22110),(22790,24160),(19395,27554),\
     (17345,25504),(15560,27289),(15560,30215),(11165,30215),(11165,27915),\
     (12435,27915),(15220,24415),(12445,21630),(16865,17210),(19650,19995),\
     (23600,16045),(24970,16045)]
Poly = [(24970,19250),(23600,19250),(20740,22110),(22790,24160),(19395,27554)\
    ,(17345,25504),(15560,27289),(15560,30215),(16490,30215),(16490,31500)\
    ,(20670,31500),(20670,33700),(23370,33700),(23370,31150),(25785,31150)\
    ,(25785,41415),(16740,41416),(16740,39400),(10060,39400),(10060,41415)\
    ,(4315,41415),(4315,39400),(1300,39400),(1300,31300),(3545,31300)\
    ,(3545,34300),(6245,34300),(6245,29085),(4785,29085),(4785,26570)\
    ,(2085,26570),(2085,28615),(0,28615),(0,21110),(11925,21110),(12445,21630)\
    ,(16865,17210),(14600,14946),(16407,13139),(14498,11230),(12691,13036)\
    ,(9085,9430),(11430,7085),(11430,4800),(19590,4800),(19590,9250),(26255,9250)\
    ,(26255,7085),(32000,7085),(32000,9720),(36510,9720),(36510,15050)\
    ,(34330,15050),(34330,12850),(31430,12850),(31430,19250),(34330,19250)\
    ,(34330,17050),(37480,17050),(37480,23430),(34330,23430),(34330,26060)\
    ,(28385,26060),(28385,24260),(24970,24260)]

#Poly = [(8,8),(9,6),(11,8),(10,10),(9,12),(6,12),(5,16),(3,13),(0,13),(4,10)\
#        ,(0,0),(5,0),(8,2),(6,6),(7,7)]
'Poly = [(8000,8000),(9000,6000),(11000,8000),(9000,12000),(6000,12000)\
        ,(5000,16000),(3000,13000),(0,13000),(4000,10000),\
        (0,0),(5000,0),(8000,2000),(6000,5000),(7000,7000)]'
'Poly = [(12000,3000),(8000,8000),(14000,8000),(9000,11000),(4000,8000),\
        (6000,5000),(2000,8500),(4000,11000),(500,11000),(-2000,7500),(2000,6000),(-3000,6000),\
        (-2000,3000),(3000,0),(4000,2000),(8000,0),(14000,0),\
        (16000,2000),(15000,8000),(13000,7000)]'

#points = np.array([(0,0),(4,0),(4,4),(0,4),(0,0)])
#points = np.array([(10,10),(8,6),(7,8),(5,6),(4,7),(2,3)\
#        ,(0,4),(0,2),(1,1),(6,0),(8,0),(10,2),(9,4),(10,10)])
#points = np.array([(0,6),(1,1),(3,0),(7,2),(5,4),(7,5),(6,8),(4,7),(2,11),(0,6)])
#points = np.array([(1,1),(2,2),(1,5),(4,3),(5,7),(5,5),(10,10),(10,-5),(6,-1),(3,-3)])
#points = np.array([(0,0),(2,2),(0,4),(3,4),(3,0),(0,0)])
#Poly = [(1,2),(0,0),(2,-3),(5,-3),(7,-1),(6,2),(7,4),(4,6),(3,6),(-3,4)]
#points = np.array([(0,0),(10,0),(10,1),(10,5),(9,5),(8,1),(8,5),(7,5)\
#         ,(6,1),(6,5),(5,5),(4,1),(4,5),(3,5),(2,1),(2,5),(1,5),(0,1),(0,0)])
#points = np.array([(1,8),(4,3),(6,0),(7,4),(8,2),(9,9),(7,6),(5,7),(5,5)])
#Poly = [(3,16),(4,13),(5,11),(6,10),(8,9),(7,7),(5,4),(6,2),(7,4),(7,0),\
#        (4,0),(1,0),(1,1),(2,1),(3,3),(2,3),(2,6),(1,3),(0,3),(1,6)]
#Poly = [(20,10),(20,14),(16,14),(16,16),(10,16),(10,14),(6,14),(6,16),(2,16)\
#        ,(2,14),(0,14),(-5,7),(0,0),(2,-2),(4,0),(4,4),\
#        (4,4),(8,4),(8,0),(14,-5),(20,0),(20,6),(15,6),(15,10)]
#Poly = [(4000,4000),(8000,4000),(8000,0000),(14000,-5000),(20000,0),(20000,6000),(15000,6000),(15000,10000)\
#        ,(20000,10000),(20000,14000),(16000,14000),(16000,16000),(10000,16000),(10000,14000),(6000,14000),(6000,16000),(2000,16000)\
#       ,(2000,14000),(0,14000),(-5000,7000),(0,0),(2000,-2000),(4000,0)]
points = np.array(Poly)
P = points
#print(P)
vor = Voronoi(points)
#print("Vor point are:",vor)

def voronoi_finite_polygons_2d(vor, radius=None):
    """
    Reconstruct infinite voronoi regions in a 2D diagram to finite
    regions.

    Parameters
    ----------
    vor : Voronoi
        Input diagram
    radius : float, optional
        Distance to 'points at infinity'.

    Returns
    -------
    regions : list of tuples
        Indices of vertices in each revised Voronoi regions.
    vertices : list of tuples
        Coordinates for revised Voronoi vertices. Same as coordinates
        of input vertices, with 'points at infinity' appended to the
        end.

    """

    if vor.points.shape[1] != 2:
        raise ValueError("Requires 2D input")

    new_regions = []
    new_vertices = vor.vertices.tolist()

    center = vor.points.mean(axis=0)
    if radius is None:
        radius = vor.points.ptp().max()

    # Construct a map containing all ridges for a given point
    all_ridges = {}
    for (p1, p2), (v1, v2) in zip(vor.ridge_points, vor.ridge_vertices):
        all_ridges.setdefault(p1, []).append((p2, v1, v2))
        all_ridges.setdefault(p2, []).append((p1, v1, v2))

    # Reconstruct infinite regions
    for p1, region in enumerate(vor.point_region):
        vertices = vor.regions[region]

        if all(v >= 0 for v in vertices):
            # finite region
            new_regions.append(vertices)
            continue

        # reconstruct a non-finite region
        ridges = all_ridges[p1]
        new_region = [v for v in vertices if v >= 0]

        for p2, v1, v2 in ridges:
            if v2 < 0:
                v1, v2 = v2, v1
            if v1 >= 0:
                # finite ridge: already in the region
                continue

            # Compute the missing endpoint of an infinite ridge

            t = vor.points[p2] - vor.points[p1] # tangent
            t /= np.linalg.norm(t)
            n = np.array([-t[1], t[0]])  # normal

            midpoint = vor.points[[p1, p2]].mean(axis=0)
            direction = np.sign(np.dot(midpoint - center, n)) * n
            far_point = vor.vertices[v2] + direction * radius

            new_region.append(len(new_vertices))
            new_vertices.append(far_point.tolist())

        # sort region counterclockwise
        vs = np.asarray([new_vertices[v] for v in new_region])
        c = vs.mean(axis=0)
        angles = np.arctan2(vs[:,1] - c[1], vs[:,0] - c[0])
        new_region = np.array(new_region)[np.argsort(angles)]
        # finish
        new_regions.append(new_region.tolist())
    return new_regions, np.asarray(new_vertices)
regions, vertices = voronoi_finite_polygons_2d(vor)
polygons = []
#print("The vertices are:",vertices)
fig = voronoi_plot_2d(vor)
vert = []
for i in range(len(vertices)):
    Vx = [] ;Vy = []
    Vx = (vertices[i][0])
    Vy = (vertices[i][1])
    V = (Vx,Vy)
    vert.append(V)
#print("The vertices are aaaaaaa:",vert)
P = Poly
AP = P
P.append(P[0])
Pc = vert
#Pc.append(Pc[0])
AAP = Pc
Start = time.time() #starting the time
#print("The start time is:",Start)
def Sorting(lst): 
    lst2 = sorted(lst, key=len, reverse = True) 
    return lst2 
''' orientation function: To check the orientation on points (x1,y1),(x2,y2),(x3,y3)'''
def orientation(x1,y1,x2,y2,x3,y3):
        val = (float((y2-y1)*(x3-x2)))-(float((x2-x1)*(y3-y2)))
        if (val>0):
            return 1 #clockwise
        elif (val<0):
            return 2 #counterclockwise
        else:
            return 0 #collinear
''' point_in_seg_area function: To check if the point lies in segment area'''
def point_in_seg_area(x1,y1,x2,y2,x3,y3):  
        if ((x2<=max(x1,x3)) and (x2>=min(x1,x3))\
                and (y2<=max(y1,y3)) and (y2>=min(y1,y3))):
            return True
        return False
''' check_intersection function: To check if the line formed by points (x1,y1) and (x2,y2) intersects line
      formed by (x3,y3) and (x4,y4)'''
def check_intersection(x1,y1,x2,y2,x3,y3,x4,y4):
        o1 = orientation(x1,y1,x2,y2,x3,y3)
        o2 = orientation(x1,y1,x2,y2,x4,y4)
        o3 = orientation(x3,y3,x4,y4,x1,y1)
        o4 = orientation(x3,y3,x4,y4,x2,y2)
        if ((o1 == 0) and point_in_seg_area(x1,y1,x3,y3,x2,y2)): #both are neede to tell if the point is on the segment 
            return False
        if ((o2 == 0) and point_in_seg_area(x1,y1,x4,y4,x2,y2)):
            return False
        if ((o3 == 0) and point_in_seg_area(x3,y3,x1,y1,x4,y4)):
            return False
        if ((o4 == 0) and point_in_seg_area(x3,y3,x1,y1,x4,y4)):
            return False
        if ((o1!=o2) and (o3!=o4)):
            return True
        return  False
def create_point_pair(P):
    Pb = []
    for i in range(len(P)-1):
        Pa = []
        Pa.append(P[i])
        Pa.append(P[i+1])
        Pb.append(Pa)
    return Pb

Pb = create_point_pair(P)

Yx = []

def find_dist(A,B,C,D):
    d = ((C-A)^2 + (D-B)^2)^(1/2)
    return d
def non_intersecting_diag(Pc,P, Pb):
    for i in range(len(Pc)): #keep in mind len(Pc)-1
        S = []
        for j in range(len(P)-1):
            Pi = []
            Pi.append(Pc[i])
            Pi.append(P[j])
            S.append(Pi)
        PS.append(S)
    #print("Bhai PS:",PS)
    for n in range(len(PS)):
        for k in range(len(PS[n])):
            Xn = []
            for l in range(len(P)-1):
                if  (check_intersection(PS[n][k][0][0],PS[n][k][0][1],PS[n][k][1][0]\
                    ,PS[n][k][1][1],P[l][0],P[l][1],P[l+1][0],P[l+1][1])==True)\
                     : #check on this, error
                      continue
                else:
                      Xn.append(PS[n][k][0])
                      Xn.append(PS[n][k][1])
            Y = []
            if len(Xn) == 2*(len(P)-1): #no intersection with any polygon side
               Y.append(Xn[0])
               Y.append(Xn[1])
            if Y == []:
                continue
            else:
                Yx.append(Y)
    #print("Yx is:",Yx)
    for m in range(len(Yx)):
        px = float((Yx[m][0][0]+Yx[m][1][0])/2)
        py = float((Yx[m][0][1]+Yx[m][1][1])/2)
        mp = (px,py)
        if not (Point(mp).within(Polygon(AP))): #chk point in or out
               Pout.append(Yx[m])
        MP.append(mp)
    #print("The list of outer lines:",Pout)
    for n in range(len(Pout)):
            if Pout[n] in Yx:
                Yx.remove(Pout[n])
    return Yx

Yx = non_intersecting_diag(Pc,P,Pb)
Tx = Yx
print(Tx)

def find_length(A,B):
    D = sqrt(((A[0]-B[0])**2) + ((A[1]-B[1])**2))
    return D

def scan_range(Tx,Yx,SR): #Do not forget to define the scan range as SR
    for i in (Tx):
        A = i[0]
        B = i[1]
        if find_length(A,B) > SR:
           Yx.remove(i)
        else:
           continue
    return Yx
Yx = scan_range(Tx,Yx,10000)


Tx = Yx

def find_angle(P1,P2,P3):
    angle = math.degrees(math.atan2(P3[1]-P2[1],P3[0]-P2[0])- \
                         math.atan2(P1[1]-P2[1],P1[0]-P2[0]))
    if angle<0:
        return angle+360
    else:
        return angle

def scan_angle(Tx,Yx,P,Pc,Pb,r):
    for i in range(len(Pb)):
        for j in Tx:
            if (j[1] == Pb[i][0]):
              Ang = find_angle(j[0],j[1],Pb[i][1])
              if ((Ang > 180 and Ang < 180+r) or Ang > 360-r): 
                     if j in Yx:
                        Yx.remove(j)
              elif (Ang < 180 and(Ang < r or Ang > 180-r)):
                     if j in Yx:
                        Yx.remove(j)
               
            elif (j[1] == Pb[i][1]):
                Ang = find_angle(j[0],j[1],Pb[i][0])
                if ((Ang > 180 and Ang < 180+r) or Ang > 360-r):
                     if j in Yx:
                        Yx.remove(j)
                elif (Ang < 180 and (Ang < r or Ang > 180-r)):
                     if j in Yx:
                        Yx.remove(j)  
    return Yx
Yx = scan_angle(Tx,Yx,P,Pc,Pb,10)
print("The non intersecting diagonals are:",Yx)


def mini_chk_pts(Yf1,F,Yn):
    Yf2 = []
    while F != []:
        Yy = []; Ys = []; M = []
        for a in range(len(Yf1)):
            Yy = []
            for b in range(len(Yf1[a])):
                for c in range(len(F)):
                    if (F[c][0] in Yf1[a][b][0]) and (F[c][1] in Yf1[a][b][1])\
                       and (Yf1[a][b][0][1] in F[c]) and Yf1[a][b][1][1] in F[c]:
                        Yy.append(Yf1[a][b])
            Ys.append(Yy)
        Yf2 = Sorting(Ys)
        A2 = Yf2[0]
        for i in range(len(Yf2[0])):
            Yn.append(Yf2[0][i])
        Yf2.remove(Yf2[0])
        for j in range(len(F)):
            for k in range(len(A2)):
                if (F[j][0] == A2[k][0][1]) and (F[j][1] == A2[k][1][1]):
                        M.append(F[j])
                else:
                        continue
        F2 = []
        for l in range(len(F)):
                if not F[l] in M:
                        F2.append(F[l])
                else:
                        continue
        Yf1 = Yf2
        F = F2
    return Yn


def chk_pts(Pc,P,Yx,Pb):
    Yn=[];M=[];Ys1=[];Yk1=[];Yy1=[];Yf1 = [];Ye1 = []; R = []
    for r in range(len(Pc)):#this is important for arranging the diagonals.
        Yy1 = []
        for s in range(len(Yx)):
            if Pc[r] == Yx[s][0]:
               Yy1.append(Yx[s])
        if not Yy1 == []:
               Yy1.append(Yy1[0])
        Ys1.append(Yy1)
    Yk1 = Sorting(Ys1)  #sorting in descending order of  length of sub-list.
    #print("The list Yk1 is:",Yk1)
    for b in range(len(Yk1)):
            Yg = []
            for c in range(len(Yk1[b])-1):
                 for a in range(len(P)-1):
                     Yf = []
                     if ((P[a] == Yk1[b][c][1]) and (P[a+1] == Yk1[b][c+1][1])):
                         Yf.append(Yk1[b][c])
                         Yf.append(Yk1[b][c+1])
                         Yg.append(Yf)
            if not Yg == []:
                Ye1.append(Yg)
    Yf1 = Sorting(Ye1)
    #print("Yf1 pair is:",Yf1)
    A1 = Yf1[0]
    for d in range(len(Yf1[0])):
        Yn.append(Yf1[0][d])
    Yf1.remove(Yf1[0])
    for e in range(len(Pb)):
        for f in range(len(A1)):
            if ((Pb[e][0] == A1[f][0][1]) and (Pb[e][1] == A1[f][1][1])):
                m.append(Pb[e])
            else:
                continue
    F = []
    for g in range(len(Pb)):
         if not Pb[g] in m:
            F.append(Pb[g])
    #print("The Pb:",F)
    Pfinal = mini_chk_pts(Yf1,F,Yn)
    final = []
    for i in Pfinal:
         if not i in final:
                 final.append(i)
    r = []
    for p in range(len(final)): #solution for adjecent points
        for q in range(len(final)): #this is a big change!!!!!!!!!
            for r in range(len(Pc)-1):
                if (final[p][0][0] or final[p][1][0]) == Pc[r]:
                   if (Pc[r+1] or Pc[r-1])==(final[q][0][1] or final[q][1][1]):
                          R.append(final[q])
    #print("Bro R is:",R)
    for r in range(len(R)):#PREVENT REPITITION
        if R[r] in final:
            final.remove(R[r])
    return final   
# Code perfect................................................#
Yn = (chk_pts(Pc,P,Yx,Pb))
print("The co-ordinates are:",Yn)
# Code perfect................................................#
def plt_plot(P,Yn,vert):
    plot_lstx = list()
    plot_lsty = list()
    Px = [];Py = [];Dx = [];Dy = [];Sx = [];Sy = [];Tx = [];Ty = [];Pcx = [];Pcy = []
    for i in range(len(P)):
        Px.append(P[i][0])
        Py.append(P[i][1])
    for j in range(len(Yn)):    
        Dx=[];Dy=[]
        Dx.append(Yn[j][0][0][0])
        Dy.append(Yn[j][0][0][1])
        Dx.append(Yn[j][0][1][0])
        Dy.append(Yn[j][0][1][1])
        Dx.append(Yn[j][1][0][0])
        Dy.append(Yn[j][1][0][1])
        Dx.append(Yn[j][1][1][0])
        Dy.append(Yn[j][1][1][1])
        Sx.append(Yn[j][0][0][0])
        Sy.append(Yn[j][0][0][1])
        plt.plot(Dx,Dy, color = 'g')
    for k in range(len(vert)):
        Pcx.append(vert[k][0])
        Pcy.append(vert[k][1])
    #plt.scatter(Pcx,Pcy,s = 200, marker = '.', color = 'r')
    plt.plot(Px,Py,color = 'b')
    plt.scatter(Sx,Sy,s = 700,marker = '.',color = 'k')
    End = time.time()
    return plt.show(),print("The end time is:",End),print("The runtime is:",(End-Start)) 

plt_plot(P,Yn,vert)
