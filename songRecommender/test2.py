import os

# Read the generated playlist ID from new.txt
with open(r"C:\Users\Vivek Shekhawat\Desktop\final year project\Emotify-Arithemania\new.txt", "r") as f:
    playlist_id = f.read().strip()

# Create the HTML content with the embedded Spotify playlist using the playlist_id
html_content = f'''<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Spotify Playlist Embed</title>
  </head>
  <body style="background-image: url('file:///C:/Users/Vivek%20Shekhawat/Desktop/final%20year%20project/Emotify-Arithemania/songRecommender/data/bg.jpg');">
    <script src="index.js"></script>
    <iframe style="border-radius:12px" 
            src="https://open.spotify.com/embed/playlist/{playlist_id}?utm_source=generator" 
            width="75%" height="500" frameBorder="0" 
            allow="autoplay; clipboard-write; encrypted-media; picture-in-picture" 
            loading="lazy"></iframe>
  </body>
</html>'''

# Write the HTML content to new.html
with open(r"C:\Users\Vivek Shekhawat\Desktop\final year project\Emotify-Arithemania\new.html", "w") as fp:
    fp.write(html_content)

# Open the HTML file using the default browser (Windows)
os.startfile(r"C:\Users\Vivek Shekhawat\Desktop\final year project\Emotify-Arithemania\new.html")
