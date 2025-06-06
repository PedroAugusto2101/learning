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

---

# Transformers

Transformers are a **neural network architecture** introduced in the paper _"Attention is All You Need"_, which revolutionized **natural language processing (NLP)** and other deep learning fields by replacing recurrent and convolutional networks with a **self-attention mechanism**.
![img](../img/Screenshot%20from%202025-04-21%2015-03-27.png)

## Key Features

- **Self-Attention**: Allows the model to evaluate the importance of each part of the input sequence in relation to the others.
- Processes sequences **in parallel**, unlike RNNs which are sequential.
- Enables capturing **long-range dependencies** in data.

## Architecture

![img](../img/Screenshot%20from%202025-04-21%2015-06-13.png)

- **Encoder**: Takes the input sequence and creates a contextual representation.
- **Decoder**: Generates the output sequence (e.g., translation or summary) based on the encoder's representation.
- **Multi-Head Attention**: Multiple attention mechanisms run in parallel, focusing on different parts of the sequence simultaneously.
- Highly **parallelizable**, making it efficient for **GPU training**.

## Impact

- Became the foundation of state-of-the-art models like:
  - **BERT**
  - **GPT**
  - **T5**
- Widely used in:
  - **NLP**
  - **Computer Vision** (e.g., Vision Transformer)
  - **Time Series Analysis** (e.g., Temporal Fusion Transformer)

> Transformers are the backbone of modern AI, offering flexibility, scalability, and superior performance across multiple domains.

---

# Large Language Models (LLMs)

LLMs (Large Language Models) are **generative AI models** capable of producing human-like text. ChatGPT, for example, is an interface that allows users to interact with such a model.
![img](../img/Screenshot%20from%202025-04-21%2016-40-53.png)

## Characteristics

- Based on **deep learning architectures**, typically using **billions or even trillions of parameters**.
- Trained on **large-scale text corpora** covering a wide range of topics, styles, and contexts.
- Can **understand and generate coherent, contextually relevant text**.
- Extremely versatile for a variety of **natural language processing (NLP)** tasks.

## Architecture

- Typically built on the **Transformer** architecture, introduced by the paper _"Attention is All You Need"_.
- Leverages **attention mechanisms** to process text **non-sequentially**, capturing long-term dependencies efficiently.

> LLMs represent a major leap in NLP, enabling tasks such as summarization, translation, question answering, and conversational AI.

## Training and Fine-Tuning of LLMs

LLMs operate in **three main stages**:

### 1. Pre-training

- The model is trained on a **large corpus of text** (books, articles, websites, etc.).
- It learns to **predict the next word** in a sentence or to **fill in missing words**, capturing **grammatical, semantic, and contextual patterns**.
- This phase is **unsupervised**, using massive amounts of data to develop general language understanding.

### 2. Fine-tuning

- After pre-training, the model is fine-tuned on **task-specific datasets** (e.g., translation, summarization, sentiment analysis, code generation).
- This phase is **supervised**, using labeled data to adapt the model for **specific use cases**.
- Fine-tuning is a form of **transfer learning**.

### 3. Inference (Text Generation and NLP Tasks)

- Once trained, the LLM can perform a variety of **natural language processing tasks**:
  - Text generation from prompts
  - Question answering
  - Translation
  - Sentiment classification
  - And more
- Due to their **size and complexity**, these models can generate **high-quality, human-like text**.

---

# Retrieval Augmented Generation (RAG) and GraphRAG

## Limitations of LLMs

- LLMs can only generate responses based on **the data they were trained on**.
- They lack knowledge of **external or updated content**, such as internal company documents, contracts, spreadsheets, databases, etc.

## What is RAG?

- **Retrieval Augmented Generation (RAG)** is a technique that combines:
  - **Language models** (like LLMs)
  - With **information retrieval systems**
- It allows LLMs to **access external knowledge bases** and generate more relevant and up-to-date responses.
- Useful when context is **dynamic** or **not included in the training data**.
  ![img](../img/Screenshot%20from%202025-04-21%2017-15-52.png)

## What is GraphRAG?

- **GraphRAG** extends RAG by incorporating **graph structures** for information retrieval.
- It organizes and accesses data **more efficiently** by capturing **relationships between entities**.
- Improves:
  - **Contextualization**
  - **Response quality**
  - **Interpretability**
- Instead of relying only on text documents or traditional databases, GraphRAG uses **knowledge graphs** for better semantic representation.

## Use Case Example:

- Internal documents (e.g., contracts, spreadsheets) → chunked and embedded → stored in a **graph or vector database**
- On user query: relevant chunks are retrieved → passed as context to LLM → LLM generates a **contextualized and accurate** answer

## Retrieval Augmented Generation (RAG) and Vector Databases

### RAG Architecture

RAG architecture can be understood in **two main components**:

#### 1. Information Retrieval

- Before generating a response, the model **consults an external database or document index**.
- Techniques used for retrieval include:
  - **TF-IDF**
  - **BM25**
  - **Embeddings** from neural networks
- The goal is to find the **most relevant texts** based on the prompt or query.

#### 2. Response Generation

- After retrieving relevant documents, the **language model (LLM)** uses them as **additional context**.
- This allows the LLM to generate **more accurate and informed responses**, even including:
  - Factual data
  - Citations
  - Information not seen during pre-training

### Role of Vector Databases

- In modern RAG systems, **vector databases** (like FAISS, Pinecone, Weaviate, Qdrant) are commonly used for efficient **similarity search**.
- Text is embedded into **high-dimensional vectors**, and user queries are matched against this vector space to retrieve the most relevant content.

![img](../img/Screenshot%20from%202025-04-22%2019-40-52.png)
