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
