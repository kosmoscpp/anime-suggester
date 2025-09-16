# ==========================
# Anime Suggestor with AniList API 
# ==========================

import requests
import gradio as gr

#  Function to query AniList API
def fetch_anime(genre, min_score):
    query = """
    query ($genre: String, $min_score: Int) {
      Page(page: 1, perPage: 6) {
        media(genre_in: [$genre], sort: SCORE_DESC, averageScore_greater: $min_score, type: ANIME) {
          id
          title {
            romaji
            english
          }
          averageScore
          coverImage {
            large
          }
          siteUrl
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

    # Build gallery in 2 columns
    cards = "<div style='display:grid; grid-template-columns: repeat(2, 1fr); gap: 20px;'>"
    for anime in results:
        title = anime["title"]["english"] or anime["title"]["romaji"]
        score = f"⭐ {anime['averageScore']}/100"
        url = anime["siteUrl"]
        img = anime["coverImage"]["large"]

        cards += f"""
        <div style='text-align:center; padding:10px; border:1px solid #ddd; border-radius:10px; background:#fafafa;'>
            <a href='{url}' target='_blank'>
                <img src='{img}' style='width:180px; border-radius:10px;'><br>
                <b>{title}</b>
            </a><br>
            {score}
        </div>
        """
    cards += "</div>"
    return cards

#  Gradio UI
genres = [
    "Action", "Adventure", "Comedy", "Drama", "Fantasy",
    "Horror", "Mystery", "Psychological", "Romance", "Sci-Fi", 
    "Slice of Life", "Sports", "Supernatural", "Thriller"
]

demo = gr.Interface(
    fn=fetch_anime,
    inputs=[
        gr.Dropdown(choices=genres, label="Choose a Genre"),
        gr.Slider(1, 10, value=7, step=0.5, label="Minimum Rating (out of 10)")
    ],
    outputs=gr.HTML(label="Top Anime Recommendations"),
    title="🎬 Anime Suggestor",
    description="Find the top 6 anime with posters and clickable links to AniList pages."
)

# Footer
with gr.Blocks() as app:
    gr.Markdown("## 🎬 Anime Suggestor")
    demo.render()
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
