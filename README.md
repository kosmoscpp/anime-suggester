# 🎬 Anime Suggestor

A simple ML/Data project built during **MLH Global Hack Week: Data Week**.  
This project recommends the **Top 5 anime** based on a chosen genre and minimum rating using the [Kaggle Anime Dataset](https://www.kaggle.com/datasets/CooperUnion/anime-recommendations-database).

---

## 🚀 Features
- Interactive **Gradio UI** with dropdown for genres and slider for ratings.  
- Recommends **Top 5 anime** with:
  - 🎭 Genre-based filtering  
  - ⭐ Ratings  
  - 👥 Popularity (number of members)  
- Visualization of top anime genres.  

---

## 📊 Dataset
The dataset used is from Kaggle:  
[Anime Recommendations Database](https://www.kaggle.com/datasets/CooperUnion/anime-recommendations-database)

Columns include:
- `anime_id` – unique ID  
- `name` – anime title  
- `genre` – list of genres  
- `type` – TV, Movie, OVA, etc.  
- `episodes` – number of episodes  
- `rating` – average user rating (1–10)  
- `members` – popularity score  

---

## 🛠️ How to Run

### 1. Run in Google Colab (Recommended)  
Click this badge to open in Colab:  

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YOUR_USERNAME/anime-suggestor/blob/main/anime_suggestor.ipynb)

- Upload `anime.csv` when prompted.  
- Enjoy your anime recommendations! 🎉  

---

### 2. Run Locally
Clone the repo and install requirements:
```bash
git clone https://github.com/YOUR_USERNAME/anime-suggestor.git
cd anime-suggestor
pip install -r requirements.txt
python anime_suggestor.py

For any query, ask me on my Instagram [https://www.instagram.com/kosmos.cpp/].
