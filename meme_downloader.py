import praw
import requests
import os

# Function to sanitize a string for use as a filename
def sanitize_filename(filename):
    # Replace characters that are not allowed in filenames with underscores
    return "".join(c if c.isalnum() or c in "._-" else "_" for c in filename)

# Create a Reddit instance and authenticate with your credentials
reddit = praw.Reddit(
    client_id='g64ckSTpYAj6cPhaHzrFeA',
    client_secret='mJlFpORfzmrpNRqGGnxy77sQe1cMsg',
    username="Sarabroop",
    password="121103sarab",
    user_agent="WarHammer"
)

# Fetch the top posts from r/memes
subreddit = reddit.subreddit("bookmemes")
top_posts = subreddit.top(limit=40)

# Create a directory to save the downloaded memes
if not os.path.exists("automated videos"):
    os.makedirs("automated videos")

# Download the images from the top posts and save them with sanitized titles
for post in top_posts:
    if post.url.endswith(".jpg") or post.url.endswith(".png"):
        response = requests.get(post.url)
        extension = post.url.split(".")[-1]
        sanitized_title = sanitize_filename(post.title)
        sanitized_title = sanitized_title.replace("?", "")  # Remove question marks
        filename = f"automated videos/{sanitized_title}.{extension}"
        with open(filename, "wb") as f:
            f.write(response.content)
