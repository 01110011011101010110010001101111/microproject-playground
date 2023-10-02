# Robotics Manipulation

## Iterative Closest Point

Before deep learning became as powerful as it is today, a lot of robotics vision was based in known equations. One of the simpler and most popular algorithms is the Iterative Closest Point (ICP) algorithm that's still used as part of algorithms today! 

The general idea behind ICP is you are given a scene point cloud and you want to map these points to the model point cloud. To do so, it proposes an iterative algorithm following these steps:

1. Find the nearest neighbors of the scene to the model. This determines which scene points to use.
2. Calculate the average coordinate for both the model and the scene points
3. Subtract the average from the original point clouds (this is the "error" of the scene and the model)
4. Create a matrix W that is the product of the matrices from step #3
5. Use SVD to decompose $W = U \Sigma V^T$. The rotation matrix is $R = U V^T$
6. The new point is the average scene minus the product of the rotation matrix and the average model points
7. Repeat these steps several times or untill you don't change by a threshold

And with that, you've determined the pose for your robot! Some key limitations to this algorithm is that it is highly dependent on the initial pose. If the initial pose is far off, the solution may hit a local minimum. To counter this, algorithm such as RANSAC exist to help determine a pretty good starting guess.
