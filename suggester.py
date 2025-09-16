import pandas as pd
data = pd.read_csv("/anime.csv")
print(data.head())

!pip install gradio

# ==========================
# Anime Suggestor with Gradio UI (Table Output)
# ==========================

import pandas as pd
import gradio as gr


from google.colab import files
uploaded = files.upload()  # Upload your anime.csv here
data = pd.read_csv(list(uploaded.keys())[0])


data['genre'] = data['genre'].fillna('').apply(lambda x: x.split(','))
data['genre'] = data['genre'].apply(lambda x: [g.strip() for g in x])


def suggest_anime(preferred_genre, min_rating):
    filtered = data[data['genre'].apply(lambda x: preferred_genre.lower() in [g.lower() for g in x])]
    filtered = filtered[filtered['rating'] >= min_rating]

    if filtered.empty:
        return pd.DataFrame({"Message": ["❌ No anime found matching your preferences."]})

    # Sort by rating and members (popularity)
    filtered = filtered.sort_values(by=['rating', 'members'], ascending=False)

    # Return top 5 as a table
    return filtered[['name', 'rating', 'members']].head(5).rename(
        columns={"name": "Anime Name", "rating": "Rating", "members": "Members"}
    )


genres = sorted({g for sublist in data['genre'] for g in sublist if g})  # unique genres

with gr.Blocks() as demo:
    gr.Markdown("# 🎬 Anime Suggestor")
    gr.Markdown("Get Top 5 anime recommendations based on genre and rating.")

    genre_input = gr.Dropdown(choices=genres, label="Choose a Genre")
    rating_input = gr.Slider(1, 10, value=7, step=0.5, label="Minimum Rating")

    output = gr.Dataframe(label="Top 5 Anime Recommendations")

    btn = gr.Button("Suggest Anime")
    btn.click(suggest_anime, inputs=[genre_input, rating_input], outputs=output)

    # 👇 Footer with blue name + clickable insta handle
    gr.Markdown("---")
    gr.Markdown(
        "<div style='text-align: center; color: blue; font-size: 16px;'>"
        "Made by <b>Krishna Jha</b> • "
        "<a href='https://instagram.com/kosmos.cpp' target='_blank' style='color: blue;'>@kosmos.cpp</a>"
        "</div>"
    )


demo.launch()
