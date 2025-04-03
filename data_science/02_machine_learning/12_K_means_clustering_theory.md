# K-Means Clustering

## Overview

- **K-Means** is an **unsupervised learning** algorithm.
- It groups **data points** into clusters based on **similar characteristics**.
- Common applications:

  - **Automatic document clustering**
  - **Customer segmentation**
  - **Market segmentation**
  - **Geostatistics**

- The goal is to **divide data into K distinct clusters** based on their features.

![image.png](../img/Screenshot%20from%202025-04-03%2015-11-46.png)

## How K-Means Works

1. **Choose a number K** (number of clusters).
2. **Randomly assign** each data point to a cluster.
3. **Repeat until clusters stop changing**:
   - Compute the **centroid** of each cluster (mean of all points in the cluster).
   - Reassign each point to the **nearest centroid**.

![image.png](../img/Screenshot%20from%202025-04-03%2015-12-46.png)

## Choosing the Right K

- Selecting **K** is a **challenging task** and requires **prior knowledge of the dataset**.
- A common approach is the **Elbow Method**.

![image.png](../img/Screenshot%20from%202025-04-03%2015-13-46.png)

### Elbow Method

1. Compute the **Sum of Squared Errors (SSE)** for multiple values of K (e.g., **2, 4, 6, ...**).
2. **SSE** is the **sum of squared distances** between each data point and its cluster centroid.
3. Plot **K vs. SSE**:
   - SSE **decreases as K increases**.
   - Look for the point where SSE **drops sharply** → This forms the "elbow".

![image.png](../img/Screenshot%20from%202025-04-03%2015-14-46.png)
