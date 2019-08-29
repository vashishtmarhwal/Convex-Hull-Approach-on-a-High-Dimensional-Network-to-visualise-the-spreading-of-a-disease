# Convex Hull Approach on a High-Dimensional Network to visualise the spreading of a disease
Used the Gift Wrapping algorithm from the Convex Hull approach to visualize the spread of chronic disease based on its latitude and longitude.

### Gift Wrapping Algorithm 
The gift wrapping algorithm begins with i=0 and a point p0 known to be on the convex hull, e.g., the leftmost point, and selects the point pi+1 such that all points are to the right of the line pi pi+1. This point may be found in O(n) time by comparing polar angles of all points with respect to point pi taken for the center of polar coordinates. Letting i=i+1, and repeating with until one reaches ph=p0 again yields the convex hull in h steps.

### Output 
![Output](https://i.ibb.co/dm44qZx/Screenshot-2019-08-29-at-2-20-43-PM.png)
