# Computational-Geometry-Research-on-the-Art-Gallery-Problem (AGP)

## Introduction to the Art Gallery Problem

The art gallery problem is a problem to determine the minimum number of guards that are required or are sufficient to cover or see every point in the interior of an art gallery. An art gallery can be viewed as a polygon with or without holes with a total of n vertices; and guards as points in polygon, or on vertex, or on the edge of the polygon. Any point P in the polygon is said to be visible from a guard G if the line segment joining P and G does not intersect the exterior of the polygon. If the stationary guards are placed anywhere inside the polygon, then they are referred as point guards. If the stationary guards are placed on vertex of the polygon, then those are called vertex guards. Whereas if the guards move inside the polygon, then they are referred as mobile guards and further if these mobile guards are restricted to edges of polygon, then they are called edge guards.

The image below shows an indoor environment (Art Gallery/Museum) and its polygon:

![Indoor Environment and Polygon](https://user-images.githubusercontent.com/79450753/166154443-0b71c4df-68f6-4a19-b088-17e3911bfdca.png)

Proposed (Simplified) Algorithm to solve the Art Gallery Problem (Diagonalisation Method):
1) Create a polygon
2) Find a vertex(Vi) in the polygon which guards maximum no. of edges of the polygon
3) Now search for edges that remain unguarded by the previous vertex (Vi)
4) Find another vertex (Vj) on the polygon which guards maximum of the remaining unguarded edges.
5) Continue step 3 and 4 until all the edges of the polygon are guarded

Results:
A) Solution to AGP with guards on the vertices of the polygon

![Guards on the vertices of the polygon](https://user-images.githubusercontent.com/79450753/166160319-7fe947e7-2698-43bc-9895-31c918019cbf.png)

B) Solution to AGP with guards on the vertices of the voronoi diagram of the polygon

![Guards on the vertices of the voronoi diagram of the polygon](https://user-images.githubusercontent.com/79450753/166160412-5f1c143c-5a1e-41a8-a811-36411b25c83f.png)


C) Solution to AGP with guards on the vertices of the polygon

D) Solution to AGP with guards on the vertices of the polygon
