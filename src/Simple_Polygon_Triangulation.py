import matplotlib.pyplot as plt
import tripy
polygon = [(1,1),(2,2),(1,5),(4,3),\
    (5,7),(5,5),(10,10),(10,-5),(6,-1),(3,-3),(1,1),(4,0),(8,0),(6,2),(4,0)]
polygon = [(8,8),(9,6),(11,8),(10,10),(9,12),(6,12),(5,16),(3,13),(0,13),(4,10)\
       ,(0,0),(5,0),(8,2),(6,5),(7,7)]
triangles = tripy.earclip(polygon)
print (triangles)
plot_lstx = list()
plot_lsty = list()
for i in triangles:
    for j in i:
        plot_lstx.append(j[0])
        plot_lsty.append(j[1])
print(plot_lstx)
print(plot_lsty)
plt.plot(plot_lstx,plot_lsty)
plt.scatter(plot_lstx,plot_lsty,s = 200,marker = '.', color = 'r')
plt.show()
