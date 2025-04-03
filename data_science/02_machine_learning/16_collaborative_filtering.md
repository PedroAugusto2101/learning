# Collaborative Filtering

## 🔹 Overview

- **Recommends items based on user attitudes toward them.**
- Uses the **"wisdom of the crowd"** to suggest relevant items.

## 🔹 Types

1️⃣ **User-Based Collaborative Filtering**

- Finds similar users and recommends items they liked.
- _Example:_ If João and Maria like the same movies, João may like what Maria watched.

2️⃣ **Item-Based Collaborative Filtering**

- Finds similar items based on user preferences.
- _Example:_ If users who bought a phone also bought headphones, recommend headphones to phone buyers.

3️⃣ **Matrix Factorization (SVD, ALS, etc.)**

- Decomposes user-item interactions into latent features.
- _Example:_ Netflix Prize competition used these models to enhance recommendations.

4️⃣ **Hybrid Filtering**

- Combines collaborative filtering and content-based filtering.
- _Example:_ Netflix suggests movies based on your history + similar users.

## 🔹 Pros & Cons

✅ **Pros:**  
✔️ Works without needing explicit item attributes.  
✔️ Improves with more user interactions.

❌ **Cons:**  
❌ Suffers from the **Cold Start** problem (new users/items).  
❌ Needs large datasets for high-quality recommendations.

🚀 Used by **Netflix, Amazon, Spotify, YouTube**, etc.
