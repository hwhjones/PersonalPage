import streamlit as st
import feedparser
import unicodedata
import re
import streamlit.components.v1 as components


def get_medium_feed(username):
    feed_url = f"https://medium.com/feed/{username}"
    return feedparser.parse(feed_url)

d = get_medium_feed("@freedomfromthemadness")

print(d.feed.title)

print(d.feed.link)

print(d.feed.description)

def remove_invisible_chars(text):
    return ''.join(ch for ch in text if not unicodedata.category(ch).startswith('C'))

def strip_html(text):
    return re.sub('<[^<]+?>', '', text)

def clean_text(text):
    text = remove_invisible_chars(text)
    text = strip_html(text)
    return text

for entry in d.entries:
    st.subheader(entry.title)
    st.write(f"Published on: {entry.published}")
    st.markdown(entry.summary, unsafe_allow_html=True)
    st.markdown(f"[Read more]({entry.link})")
    st.markdown("---")