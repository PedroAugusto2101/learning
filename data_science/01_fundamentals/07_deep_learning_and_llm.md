# Fundamentals of Artificial Neural Networks (ANNs)

Artificial Neural Networks (ANNs) are a machine learning architecture inspired by the **human brain**, designed to **recognize patterns** and **learn from data**.

## Key Concepts

- **Neurons**: Basic computational units.
- **Layers**:
  - **Input Layer**: Receives the input features.
  - **Hidden Layers**: Perform complex transformations.
  - **Output Layer**: Produces the final prediction.
- **Deep Learning**: When a model has multiple hidden layers.

## Biological Inspiration

- ANNs are inspired by the structure of the human brain.
- Like biological neurons connected by synapses, ANNs have **neurons connected by weights**.
  ![img](../img/Screenshot%20from%202025-04-21%2012-32-12.png)
  ![img](../img/Screenshot%20from%202025-04-21%2012-33-12.png)

## Mathematical Neuron

![img](../img/Screenshot%20from%202025-04-21%2012-34-12.png)
A simplified structure of a mathematical neuron involves:
![img](../img/Screenshot%20from%202025-04-21%2012-35-12.png)

- **Inputs (x₁, x₂, ..., xₙ)**
- **Weights (w₁, w₂, ..., wₙ)**
- **Linear Combination**: \( z = \sum (x_i \cdot w_i) + b \)
- **Activation Function**: Applies non-linearity (e.g., ReLU, sigmoid).
- **Output (ŷ)**

> The model learns by **adjusting the weights** to reduce the error between the prediction and the true value.

## Key Notes

- The performance depends on **data quality**, **model architecture**, and **training process**.
- **Training**: Uses labeled data to learn optimal weights.
- **Evaluation**: Measures performance on unseen data.
- **Scalability**: Larger models (e.g., LLMs) have billions or even trillions of parameters.

## LLMs (Large Language Models)

- A type of **deep learning model** trained on **massive datasets**.
- Uses **probabilistic reasoning** to generate outputs.
- Delivers **human-like responses** due to the scale and richness of training data.

> AI does not exist without data — a data strategy is essential before building an AI strategy.

---

# Deep Learning and the AI Revolution

Deep Learning is a **subfield of Machine Learning** that uses **artificial neural networks** inspired by the human brain to process and interpret large volumes of data.

## Key Points

- **Deep Learning requires a large amount of data**, which demands proper infrastructure: data pipelines, storage, architecture, etc.
- Networks are composed of **multiple layers of artificial neurons**, organized hierarchically.
- As data flows through these layers, the model learns increasingly **complex representations**.
- Ideal for **data with complex relationships**, such as **text**, **images**, and **audio**.

## The AI Revolution

The Deep Learning revolution began around **2012**, when neural networks started to outperform traditional methods in pattern recognition tasks.

### This breakthrough was driven by:

1. **Increased computational power** (e.g., GPUs)
2. **Availability of large datasets**
3. **Advances in algorithms and architectures**

> The most advanced AI models today are based on **deep learning**.

---

# Transfer Learning

Transfer learning is a technique in **machine learning**, especially popular in **deep learning**, where a model trained on one task is **reused** as the starting point for a different but related task.

## Key Points

- Uses **pre-trained models** that are adapted to a **new task**.
- Especially useful when the **new dataset is limited**.
- Leverages knowledge learned from a **large dataset** to improve performance on a smaller one.
- Common in tasks like **image classification**, **NLP**, and **speech recognition**.

## Advantages

- **Reduces training time**.
- **Requires less data**.
- Improves performance when there's **limited computational resources**.
  ![img](../img/Screenshot%20from%202025-04-21%2014-55-54.png)
  ![img](../img/Screenshot%20from%202025-04-21%2014-56-48.png)

> Transfer learning enables faster and more efficient development of ML models by reusing what has already been learned.
