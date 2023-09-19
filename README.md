# Snowflake

Create snowflake pattern in Python

1. Start with 6 corners of a uniform hexagon
2. Pick 2 points A and B by random among all the points
3. Draw another point C at 3/5 the distance from A to B (e.g. if A: (0,6) and B: (1,3) then C: (0.6, 4.8))
4. Repeat steps 2 and 3 until you have enough points

The file also contains sample outputs with number of points and the distance ratio used to draw new points.

For example, if 3000 points are drawn with 3/5 ratio AKA 60%, the file is named "n3000prc60.png".
