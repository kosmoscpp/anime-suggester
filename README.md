# 🎬 Anime Suggester

Anime Suggester is a simple yet fun **Anime Recommendation App** built during **MLH Global Hack Week: Data Week 2025**.  
It uses **Python, Pandas, and Gradio** to provide quick recommendations based on your **preferred genre** and a **minimum rating threshold**.  

🔗 **Live Demo (temporary link):** generated via Gradio (expires weekly)  
👤 Created by [Krishna Jha](https://github.com/kosmoscpp) • [@kosmos.cpp](https://instagram.com/kosmos.cpp)  

---

## ⚡ Features
- 🎯 Select your favorite **Anime Genre** from a dropdown  
- ⭐ Filter results by **Minimum Rating (1–10)**  
- 📊 Get **Top 5 Anime Recommendations** ranked by rating and popularity (members)  
- 🖥️ Clean and interactive **Gradio User Interface**  
- ✨ Footer signature with author name + Instagram handle  

---

## 📊 Dataset
This project uses the **Anime Recommendations Database** from Kaggle:  
[👉 Kaggle Dataset](https://www.kaggle.com/datasets/CooperUnion/anime-recommendations-database)  

Dataset fields used:
- **Anime ID** – unique identifier  
- **Name** – anime title  
- **Genre** – list of genres  
- **Type** – TV, Movie, OVA, etc.  
- **Episodes** – number of episodes  
- **Rating** – average user rating  
- **Members** – number of users who added it to their list  

---

## 🚀 How to Run

### 🔹 Option 1: Run in Google Colab (Recommended)
1. Open [Google Colab](https://colab.research.google.com/).  
2. Upload:
   - `anime_suggestor.ipynb` (the notebook)  
   - `anime.csv` (dataset)  
3. Run all cells.  
4. You’ll get a **public Gradio link** (active for ~1 week).  

### 🔹 Option 2: Run Locally
```bash
# Clone this repository
git clone https://github.com/kosmoscpp/anime-suggester.git
cd anime-suggester

# Install dependencies
pip install -r requirements.txt

# Run the notebook
jupyter notebook anime_suggestor.ipynb
````

Create a `requirements.txt` with:

```
pandas
gradio
```

---

## 📸 Screenshots
![Capture](https://github.com/user-attachments/assets/bd6eb06e-7ac4-4eb2-a263-4bb7195ba1da)


---

## 🌍 Why This Project?

* Built for **MLH Global Hack Week: Data Week 2025**
* Designed to be **beginner-friendly** yet functional
* A showcase of **data preprocessing, filtering, and UI building** with Gradio

---

## 👤 Author

**Krishna Jha**

* GitHub: [kosmoscpp](https://github.com/kosmoscpp)
* Instagram: [@kosmos.cpp](https://instagram.com/kosmos.cpp)

---

## ⭐ Contribute

This is a simple hackathon project, but feel free to fork it and:

* Add new filters (e.g., type of anime, number of episodes)
* Improve UI with more styling
* Try building a **recommendation model** (collaborative filtering, embeddings, etc.)

---

## 📜 License

This project is open-source and free to use under the MIT License.
