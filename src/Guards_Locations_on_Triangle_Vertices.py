import matplotlib.pyplot as plt
import tripy
import time
Start = time.time()
polygon = [(0, 0), (0, 101), (20, 100), (30, 60)\
    , (40, 100), (60, 100), (60, 0), (40, 10), (40, 40), (20, 40), (20, 10)]

# polygon = [(8,8),(9,6),(11,8),(10,10),(9,12),(6,12),(5,16),(3,13),(0,13),(4,10)\
#         ,(0,0),(5,0),(8,2),(6,5),(7,7)]
# polygon = [(-2,3),(3,0),(4,2),(8,0),(14,0),(16,2),(15,8),(13,7),(12,3),(8,8),(14,8)\
#      ,(9,11),(4,8),(6,5),(2,8.5),(4,11),(0.5,11),(-2,7.5),(2,6),(-3,6),(-2,3)]
# polygon = [(24970,19250),(23600,19250),(20740,22110),(22790,24160),(19395,27554)\
#     ,(17345,25504),(15560,27289),(15560,30215),(16490,30215),(16490,31500)\
#     ,(20670,31500),(20670,33700),(23370,33700),(23370,31150),(25785,31150)\
#     ,(25785,41415),(16740,41416),(16740,39400),(10060,39400),(10060,41415)\
#     ,(4315,41415),(4315,39400),(1300,39400),(1300,31300),(3545,31300)\
#     ,(3545,34300),(6245,34300),(6245,29085),(4785,29085),(4785,26570)\
#     ,(2085,26570),(2085,28615),(0,28615),(0,21110),(11925,21110),(12445,21630)\
#     ,(16865,17210),(14600,14946),(16407,13139),(14498,11230),(12691,13036)\
#     ,(9085,9430),(11430,7085),(11430,4800),(19590,4800),(19590,9250),(26255,9250)\
#     ,(26255,7085),(32000,7085),(32000,9720),(36510,9720),(36510,15050)\
#     ,(34330,15050),(34330,12850),(31430,12850),(31430,19250),(34330,19250)\
#     ,(34330,17050),(37480,17050),(37480,23430),(34330,23430),(34330,26060)\
#     ,(28385,26060),(28385,24260),(24970,24260)]
polygon = [(87,45), (63,44), (75,36), (68,25), (58,45), (49,36), (54, 29), (44,29), (44,22), (60, 22),(60,15), 
(36,15), (36, -8),(66,-22), (52, 4), (65, 4), (66,-1), (78, -4), (81,3), (78, 17), (89,15), (101, 20), (101, 31), (87, 35)]
polygon = [(72 ,-13), (90 ,-27) ,(122 ,-36),(126 ,-20),(109 ,-21),(97 ,-2),(116 ,-2),(116 ,13),(134 ,13),(128 ,-7),
        (150 ,-7),(150 ,6),(167 ,6),(167 ,20),(153 ,20),(132 ,30),(132 ,40),(153 ,40),(153 ,51),(140 ,51),(140 ,69),
        (109, 69),(99 ,55),(110 ,55),(110 ,30),(98 ,25),(98 ,36),(84 ,36),(84 ,23),(75 ,23),(75 ,6)]
A_triangles = []

'''We have to enter the first coordinate again at the end so as to perfectly 
   trianglate the polygon'''

def tri_poly_and_find_SG(polygon):
    triangles = tripy.earclip(polygon)
    #print(triangles)
    
    '''We introduces A_triangles to remove the last triangle from the
       triangulation because unnecessary coordinates are counted further'''
    
    A_triangles = []  
    for i in range(len(triangles)-1): 
        A_triangles.append(triangles[i])
        
    '''We introduce Plot_lstx and Plot_lsty to make list of X and Y coordinates
       of points of polygon to plot on the matplotlib'''
    
    Plot_lstx=[]; Plot_lsty=[];Diag_lstx=[];Diag_lsty=[];lst=[]
    for i in polygon:
        Plot_lstx.append(i[0])
        Plot_lsty.append(i[1])
        
    '''We append the first coordinate again in order to complete the polygon
       if in case we don't enter the first coordinate again in (polygon)'''
    
    Plot_lstx.append(Plot_lstx[0])   
    Plot_lsty.append(Plot_lsty[0])
    #print(Plot_lstx,Plot_lsty)
    
    '''We introduce Diag_lstx and Diag_lsty to make list of X and Y coordinates
       of points of triangles to plot on the matplotlib'''
    
    for i in triangles: 
        for j in i:
            Diag_lstx.append(j[0])
            Diag_lsty.append(j[1])
    A = final_security_guards(polygon,A_triangles)#check
    #print("The security guards are:",A)
    SGlstx = []; SGlsty = []
    
    '''we introduce SGlstx and SGlsty to make list of coordinates of security
       guards so as to plot them on matplotlib'''
    
    for i in range(len(A)):
        SGlstx.append(A[i][0])
        SGlsty.append(A[i][1])
    # plt.scatter(Diag_lstx,Diag_lsty,\
    # s = 200, marker = '.',color = 'r')
    plt.scatter(SGlstx,SGlsty,\
    marker = '.',s = 1000, color = 'k')
    plt.plot(Diag_lstx,Diag_lsty,color = 'g')
    plt.plot(Plot_lstx,Plot_lsty,color = 'b')
    End = time.time()
    return plt.show(), print("The running time is:",(End - Start)),print("The end time:",End)

''' the function def most_freq() gives us the most frequent coordinate in
    the triangles and then we assign this coordinate as a fan center.'''

def most_freq(List): 
    counter = 0;num = List[0] 
    for i in List: 
        curr_freq = List.count(i) 
        if(curr_freq> counter): 
            counter = curr_freq
            num = i
    return num

''' the function def fan_components gives us the list of coordinates of polygon
    and their occurances, so using most_freq function on this list gives us
    the fan centers.'''

def fan_components(polygon,triangles):# complexity o(n^3)
    lst = []
    for i in range(0,len(polygon)-1): 
         for j in range(0,len(triangles)):  
             for k in range(0,3):
                 if polygon[i]==triangles[j][k]:
                     lst.append(triangles[j][k])
                 else:
                    continue
    return lst

''' the function def chk_pts() gives us the update list of triangles after
    removing the processed most frequent element triangles from the list.'''

def chk_pts(triangles):
    X =[]
    for i in range(len(triangles)):
        if most_freq(fan_components(polygon,triangles))in triangles[i]:
            continue
        else:
            X.append(triangles[i])
    return X
Flst = []; lst = []; M = []; X = []

''' the function def final_security_guards() gives us the final list of the
    security guard which can cover the total boundary of the polygon and can be
    plotted on matplotlib'''

def final_security_guards(polygon,A_triangles): #check A_triangles
    while A_triangles != []:
        lst = fan_components(polygon,A_triangles) #complexity 3+1 = O(n^4)
        #print(lst)
        M  = most_freq(lst)
        Flst.append(M)
        X = chk_pts(A_triangles)
        A_triangles = X                 
    return Flst                         
#polygon = list();X = list();Y = list()  
'''while True:
    Vx = input("Enter the x coordinates:")
    if Vx == "done": break
    try: Vx = float(Vx)
    except: print("Invalid Input");continue
    X.append(Vx)
    Vy = input("Enter the y coordinates:")
    if Vy == "done": break
    try: Vy = float(Vy)
    except: print("Invalid Input");continue
    Y.append(Vy)
polygon = [(X[i],Y[i]) for i in range(0,len(X))]'''
tri_poly_and_find_SG(polygon)

