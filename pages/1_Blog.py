import streamlit as st
import feedparser
from pathlib import Path
from PIL import Image

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()

## Go up one level to the parent directory (personalpage)
parent_dir = current_dir.parent

# Now locate the CSS file in the styles folder
css_file = parent_dir / "styles" / "main.css"

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

def get_medium_feed(username):
    feed_url = f"https://medium.com/feed/{username}"
    return feedparser.parse(feed_url)

d = get_medium_feed("@hwhjones")

# print(d.feed.title)

# print(d.feed.link)

# print(d.feed.description)

# def remove_invisible_chars(text):
#     return ''.join(ch for ch in text if not unicodedata.category(ch).startswith('C'))

# def strip_html(text):
#     return re.sub('<[^<]+?>', '', text)

# def clean_text(text):
#     text = remove_invisible_chars(text)
#     text = strip_html(text)
#     return text

for entry in d.entries:
    st.subheader(entry.title)
    st.write(f"Published on: {entry.published}")
    st.markdown(entry.summary, unsafe_allow_html=True)
    st.markdown(f"[Read more]({entry.link})")
    st.markdown("---")