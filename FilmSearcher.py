import tkinter as tk
import os
from imdb_scraper import fetch_top_10_movies
from VertexImageGenerator import generate_dialogue, generateImage

root = tk.Tk()
root.title("🎬 AI Movie Scene Generator")
root.geometry("1200x720")

# SOL FRAME
left_frame = tk.Frame(root, width=300)
left_frame.pack(side="left", fill="y")

# SAĞ FRAME
right_frame = tk.Frame(root)
right_frame.pack(side="right", fill="both", expand=True)

# Film listesi
movie_listbox = tk.Listbox(left_frame, width=50, height=25)
movie_listbox.pack(padx=10, pady=(10, 5))

# Select film button
select_button = tk.Button(left_frame, text="🎥 Select Film", command=lambda: show_movie_info())
select_button.pack(pady=(0, 10))

# Sağda bilgi metni
info_text = tk.Text(right_frame, wrap="word", height=10, font=("Helvetica", 11))
info_text.pack(padx=10, pady=(10, 5), fill="x")

# Görseli göstermek için alan
image_label = tk.Label(right_frame)
image_label.pack(padx=10, pady=(5, 10), expand=True)

# Film verisi
movies = []

def load_dialogue(title):
    filename = f"{title.replace(' ', '_')}_dialogue.txt"
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            return f.read()
    return ""

def show_movie_info():
    selection = movie_listbox.curselection()
    if not selection:
        return
    movie = movies[selection[0]]
    info_text.delete("1.0", tk.END)
    info_text.insert(tk.END, f"🎬 Title: {movie['title']}\n🔗 IMDb: {movie['imdb_link']}\n\n📄 Description:\n{movie['description']}\n\n📖 Storyline:\n{movie['storyline']}")
    dialogue = load_dialogue(movie['title'])
    if dialogue:
        info_text.insert(tk.END, f"\n\n💬 Previous Dialogue:\n{dialogue}")

def generate_scene():
    selection = movie_listbox.curselection()
    if not selection:
        info_text.insert(tk.END, "\n⚠️ Please select a movie first.")
        return

    movie = movies[selection[0]]
    title = movie['title']
    prompt = prompt_entry.get().strip()
    num_characters = character_entry.get().strip()
    max_length = max_length_entry.get().strip()
    location = location_entry.get().strip()
    style = style_entry.get().strip()

    try:
        num_characters = int(num_characters)
        max_length = int(max_length)
    except ValueError:
        info_text.insert(tk.END, "\n⚠️ Number of characters and max dialogue length must be integers.")
        return

    try:
        # Diyalog üretimi
        full_text, scene = generate_dialogue(prompt, num_characters, max_length)
        info_text.insert(tk.END, f"\n\n🧠 Generated Dialogue:\n{full_text}\n\n🎬 Scene: {scene}")

        filename = f"{title.replace(' ', '_')}_dialogue.txt"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(full_text)

        # Görsel üretimi
        image_path = generateImage(num_characters, max_length, location, style, title, full_text)
        image = tk.PhotoImage(file=image_path)
        image_label.configure(image=image)
        image_label.image = image

    except Exception as e:
        info_text.insert(tk.END, f"\n[ERROR] {str(e)}")

def load_movies():
    global movies
    movies = fetch_top_10_movies()
    for movie in movies:
        movie_listbox.insert(tk.END, movie['title'])

# ALTTAKİ SORU GİRİŞ VE PARAMETRELER
bottom_frame = tk.Frame(left_frame)
bottom_frame.pack(side="bottom", anchor="w", padx=10, pady=10)

tk.Label(bottom_frame, text="Prompt:").pack(anchor="w")
prompt_entry = tk.Entry(bottom_frame, width=40)
prompt_entry.pack()

tk.Label(bottom_frame, text="Number of Characters:").pack(anchor="w")
character_entry = tk.Entry(bottom_frame, width=40)
character_entry.pack()

tk.Label(bottom_frame, text="Max Dialogue Length:").pack(anchor="w")
max_length_entry = tk.Entry(bottom_frame, width=40)
max_length_entry.pack()

tk.Label(bottom_frame, text="Scene Location:").pack(anchor="w")
location_entry = tk.Entry(bottom_frame, width=40)
location_entry.pack()

tk.Label(bottom_frame, text="Style (e.g. noir, cartoon):").pack(anchor="w")
style_entry = tk.Entry(bottom_frame, width=40)
style_entry.pack()

generate_button = tk.Button(bottom_frame, text="🪄 Generate Scene", command=generate_scene)
generate_button.pack(pady=(10, 5))

# Başlat
load_movies()
root.mainloop()