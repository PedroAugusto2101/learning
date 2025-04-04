# Natural Language Processing (NLP)

## 🔹 Overview

- **Goal:** process and analyze large amounts of natural language data.
- **Use cases:**
  - Group news by topic (e.g. Google News).
  - Search legal documents for relevant content.

## 🔹 Main Steps

1. **Compile** documents
2. **Categorize** them
3. **Compare** parameters

## 🔹 Bag of Words (BoW)

- Represents text as a **vector of word counts**.
- Example:

  - "casa azul" → (vermelha, azul, casa) → (0, 1, 1)
  - "casa vermelha" → (vermelha, azul, casa) → (1, 0, 1)

- Use **Cosine Similarity** to measure similarity between document vectors.

## 🔹 TF-IDF (Term Frequency – Inverse Document Frequency)

- Improves BoW by weighting important words.

### 📌 Term Frequency (TF)

- Importance of term _t_ in document _d_
- `TF(d, t) = number of times t appears in d`

### 📌 Inverse Document Frequency (IDF)

- Importance of term _t_ in the **entire corpus**
- `IDF(t) = log(D / T)`
  - D = total number of documents
  - T = number of documents containing term _t_

### ✅ Final Formula:

```math
TF-IDF(d, t) = TF(d, t) * log(D / T)
```
