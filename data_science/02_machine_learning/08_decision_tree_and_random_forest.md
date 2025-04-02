# Decision Tree

- Imagine that I **play tennis** every Saturday and invite a friend to join me.
- Sometimes he **comes**, sometimes he **doesn't**.
- His decision depends on **several factors**: weather, temperature, humidity, wind, etc.
- I start **recording** the conditions for each day to predict when he will join.
  ![img](../img/Screenshot%20from%202025-04-02%2019-07-46.png)

## Intuitive Approach: Decision Trees

- The **best way** to analyze this is by using a **decision tree**.
- The goal is to **predict** whether my friend **will play or not** based on past data.
  ![img](../img/Screenshot%20from%202025-04-02%2019-08-46.png)

## Components of a Decision Tree

- **Nodes**: Split the tree based on a value of a specific attribute.
- **Branches**: Represent the outcome of a decision at a node.
- **Root**: The initial node that starts the division.
- **Leaves**: The final nodes that make the classification decision.

## How It Works

1. Imagine a dataset with **3 features (X, Y, Z)** and **2 possible classes**.
2. A **split** in variable **Y** could perfectly separate the data:
   - **Y = 1?** → Yes → **Class A**, No → **Class B**.
3. **Entropy** and **Information Gain** are the mathematical foundations used to determine the best split.
   ![img](../img/Screenshot%20from%202025-04-02%2019-09-46.png)

### **Key Concepts**

- The algorithm always **splits** based on the attribute that provides the **highest information gain**.
- The **goal** is to divide the data in a way that minimizes uncertainty.
- **Formulas**:
  - **Entropy**:  
    $$ H(S) = -\sum p_i \log_2 p_i $$
  - **Information Gain**:  
    $$ IG(T, X) = H(T) - H(T | X) $$

## Drawbacks

- **Decision trees are highly susceptible to overfitting**, meaning they learn specific data characteristics **too well**.
- They **struggle with generalization**, making them unreliable for **new data**.

---

# Random Forests

- A **Random Forest** is an **ensemble** of multiple **Decision Trees**.
- Instead of using a **single tree**, we create multiple trees using **different data splits**.

## How It Works

- We create **trees** using **randomized subsets** of the data.
- To **improve performance**, we introduce **random sampling** when selecting parameters for splitting:
  - A new **random subset** of parameters is chosen for each tree **at each split**.
  - The algorithm selects **1 out of "m" parameters**.
  - In classification, **"m" is typically set as the square root of the total features "p"**.

## Why Does It Work?

- If a **single parameter dominates**, most trees will use it as the root, making them **highly correlated**.
- By introducing **stochasticity** in node selection, **random forests reduce correlation**, which helps in **reducing model variance**.

## Advantages of Random Forests

✔ **Less overfitting** compared to a single decision tree.  
✔ **Handles large datasets** with higher accuracy.  
✔ **Works well with both classification and regression tasks**.  
✔ **More stable predictions** due to averaging multiple trees.

## Disadvantages

❌ **Computationally expensive** due to multiple trees.  
❌ **Harder to interpret** than a single decision tree.
