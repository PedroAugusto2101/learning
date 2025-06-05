# K-Nearest Neighbors (KNN)

- **KNN** is a **classification algorithm** that operates in a simple way.
- Example: Imagine we have **height** and **weight** data for **dogs** and **horses**.
  ![img](../img/Screenshot%20from%202025-04-02%2017-01-46.png)

## How It Works

- **Based on the relative distance** between data points.
- **Training Algorithm**:
  - Simply **stores** the data.
- **Testing (Prediction) Algorithm**:
  1. Calculate the **distance** between the new point **x** and all stored points.
  2. Sort the data by **increasing distance**.
  3. Assign the class based on the **majority vote** of the first **K** nearest neighbors.

## The Effect of "K"

- The **choice of K** affects classifications:

  - **Small K** → More sensitive to noise, leading to **overfitting**.
  - **Large K** → Can lead to **underfitting**, missing key patterns.

  ![img](../img/Screenshot%20from%202025-04-02%2017-02-46.png)

  ![img](../img/Screenshot%20from%202025-04-02%2017-03-46.png)

  ![img](../img/Screenshot%20from%202025-04-02%2017-04-46.png)

## Pros & Cons

### **Pros**

✔ **Very simple** algorithm.  
✔ **Trivial training process** (just storing data).  
✔ **Works well with many classes**.  
✔ **Easily handles new data**.  
✔ **Few parameters** (K and distance metric).

### **Cons**

❌ **High computational cost** for predictions (slow for large datasets).  
❌ **Struggles with high-dimensional data** (many features).  
❌ **Categorical variables** do not work well.
