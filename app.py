# ==========================
# Anime Suggestor with AniList API 
# =========================

import requests
import gradio as gr

# 🔹 Function: Search by Genre + Rating
def fetch_anime(genre, min_score):
    query = """
    query ($genre: String, $min_score: Int) {
      Page(page: 1, perPage: 6) {
        media(
          genre_in: [$genre], 
          sort: SCORE_DESC, 
          averageScore_greater: $min_score, 
          type: ANIME
        ) {
          title {
            romaji
            english
          }
          averageScore
          description(asHtml: false)
          coverImage {
            large
          }
          siteUrl
          trailer {
            site
            id
          }
        }
      }
    }
    """
    variables = {"genre": genre, "min_score": int(min_score * 10)}

    response = requests.post("https://graphql.anilist.co", json={"query": query, "variables": variables})
    if response.status_code != 200:
        return "<p>❌ API Error</p>"

    results = response.json()["data"]["Page"]["media"]
    if not results:
        return "<p>❌ No results found</p>"

    cards = "<div style='display:grid; grid-template-columns: repeat(2, 1fr); gap: 20px;'>"
    for anime in results:
        title = anime["title"]["english"] or anime["title"]["romaji"]
        score = f"⭐ {anime['averageScore']}/100" if anime["averageScore"] else "⭐ N/A"
        url = anime["siteUrl"]
        img = anime["coverImage"]["large"]
        desc = (anime["description"][:200] + "...") if anime["description"] else "No description available."

        # Trailer
        trailer = ""
        if anime["trailer"] and anime["trailer"]["site"] == "youtube":
            trailer_url = f"https://www.youtube.com/watch?v={anime['trailer']['id']}"
            trailer = f"<br><a href='{trailer_url}' target='_blank'>▶ Watch Trailer</a>"

        cards += f"""
        <div style='text-align:center; padding:10px; border:1px solid #ddd; border-radius:10px; background:#fafafa;'>
            <a href='{url}' target='_blank'>
                <img src='{img}' style='width:180px; border-radius:10px;'><br>
                <b>{title}</b>
            </a><br>
            {score}<br>
            <p style='font-size:14px; color:#333;'>{desc}</p>
            {trailer}
        </div>
        """
    cards += "</div>"
    return cards


# 🔹 Function: Search by Name
def search_anime(name):
    query = """
    query ($name: String) {
      Media(search: $name, type: ANIME) {
        title {
          romaji
          english
        }
        averageScore
        description(asHtml: false)
        coverImage {
          large
        }
        siteUrl
        trailer {
          site
          id
        }
      }
    }
    """
    variables = {"name": name}

    response = requests.post("https://graphql.anilist.co", json={"query": query, "variables": variables})
    if response.status_code != 200:
        return "<p>❌ API Error</p>"

    anime = response.json()["data"]["Media"]
    if not anime:
        return "<p>❌ No results found</p>"

    title = anime["title"]["english"] or anime["title"]["romaji"]
    score = f"⭐ {anime['averageScore']}/100" if anime["averageScore"] else "⭐ N/A"
    url = anime["siteUrl"]
    img = anime["coverImage"]["large"]
    desc = (anime["description"][:300] + "...") if anime["description"] else "No description available."

    trailer = ""
    if anime["trailer"] and anime["trailer"]["site"] == "youtube":
        trailer_url = f"https://www.youtube.com/watch?v={anime['trailer']['id']}"
        trailer = f"<br><a href='{trailer_url}' target='_blank'>▶ Watch Trailer</a>"

    card = f"""
    <div style='text-align:center; padding:20px; border:1px solid #ddd; border-radius:10px; background:#fafafa;'>
        <a href='{url}' target='_blank'>
            <img src='{img}' style='width:200px; border-radius:10px;'><br>
            <h3>{title}</h3>
        </a><br>
        {score}<br>
        <p style='font-size:14px; color:#333;'>{desc}</p>
        {trailer}
    </div>
    """
    return card


# 🔹 Genres
genres = [
    "Action", "Adventure", "Comedy", "Drama", "Fantasy",
    "Horror", "Mystery", "Psychological", "Romance", "Sci-Fi", 
    "Slice of Life", "Sports", "Supernatural", "Thriller"
]


# 🔹 Gradio UI
with gr.Blocks() as app:
    gr.Markdown("## 🎬 Anime Suggestor")

    with gr.Tabs():
        # Tab 1: Genre
        with gr.Tab("🎭 Search by Genre"):
            genre_input = gr.Dropdown(choices=genres, label="Choose a Genre")
            rating_input = gr.Slider(1, 10, value=7, step=0.1, label="Minimum Rating")
            genre_output = gr.HTML()
            gr.Button("Suggest").click(fn=fetch_anime, inputs=[genre_input, rating_input], outputs=genre_output)

        # Tab 2: Name
        with gr.Tab("🔎 Search by Name"):
            name_input = gr.Textbox(label="Enter Anime Name")
            name_output = gr.HTML()
            name_input.submit(fn=search_anime, inputs=name_input, outputs=name_output)

    # Footer
    gr.HTML(
        """
        <div style='margin-top:30px; padding:20px; 
             background: linear-gradient(90deg, #1e3c72, #2a5298); 
             border-radius: 12px; text-align:center;'>
            <h2 style='color:white; margin:0;'>Made by <span style="font-size:28px; font-weight:bold;">Krishna Jha</span></h2>
            <p style='margin:5px 0;'>
                <a href='https://instagram.com/kosmos.cpp' target='_blank' 
                   style='color:#a0c4ff; font-size:18px; text-decoration:none;'>@kosmos.cpp</a>
            </p>
        </div>
        """
    )

app.launch()
