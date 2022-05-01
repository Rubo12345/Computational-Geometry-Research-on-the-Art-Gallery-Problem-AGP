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

(Instructions to run the code are given in the code itself)

Results:

A) Solution to AGP with guards on the vertices of the polygon 

`
Guard_Locations_on_Shrink_Polygon.py
`

![Guards on the vertices of the polygon](https://user-images.githubusercontent.com/79450753/166160319-7fe947e7-2698-43bc-9895-31c918019cbf.png)

B) Solution to AGP with guards on the vertices of the voronoi diagram of the polygon

`
Guard_Locations_on_Voronoi_Diagram.py
`

![Guards on the vertices of the voronoi diagram of the polygon](https://user-images.githubusercontent.com/79450753/166160462-63d5eb58-2dd5-4c7c-853a-d725979e9ec4.png)

C) Solution to AGP with guards on the dual tree of the polygon

`
Guard_Locations_on_the_Dual_Tree.py
`

![Guards on the dual tree of the polygon](https://user-images.githubusercontent.com/79450753/166160612-5a3509ab-8785-4601-a541-d5cced1cd3e0.png)

D) Solution to AGP with guards on the vertices of the triangles

`
Guards_Locations_on_Triangle_Vertices.py
`

![Guards on the vertices of the triangles](https://user-images.githubusercontent.com/79450753/166160732-1457917d-371d-410f-b997-7ace0f8f7701.png)

### Methods for guard placement, from best to worst, based on the minimum number of guards:

(Vertices of the polygon / Shrink Polygon) > (Vertices of the voronoi diagram) >> (Vertices of the dual tree) > (Vertices of the triangles)

E) Solution to AGP with guards on the vertices of the polygon with holes

`
Guard_Locations_on_Shrink_Polygon_with_Holes.py
`

![Guards on the vertices of the polygon with holes](https://user-images.githubusercontent.com/79450753/166161641-a0c02780-5476-4ead-8236-4351831a9a53.png)

