import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="IPL & Movie Recommendation App",
    page_icon="🎬",
    layout="wide"
)

# Header Title
st.title("🌟 Streamlit Cloud & Hugging Face Spaces App")
st.markdown("---")

# Navigation Tabs
tab1, tab2 = st.tabs(["🏏 Favorite IPL Team", "🎬 Trending Bollywood Movies"])

# ==============================================================================
# TASK 1: IPL TEAM SECTION
# ==============================================================================
with tab1:
    st.header("🏆 Favorite IPL Team: Mumbai Indians (MI)")
    
    col_logo, col_info = st.columns([1, 2])
    
    with col_logo:
        # Mumbai Indians Official Logo URL
        mi_logo_url = "https://upload.wikimedia.org/wikipedia/en/c/cd/Mumbai_Indians_Logo.svg"
        st.image(mi_logo_url, width=250, caption="Mumbai Indians Logo")
        
    with col_info:
        st.subheader("Team Overview")
        st.write("""
        - **Captain:** Hardik Pandya
        - **Home Ground:** Wankhede Stadium, Mumbai
        - **IPL Titles Won:** 5 (2013, 2015, 2017, 2019, 2020)
        - **Team Motto:** *Duniya Hila Denge Hum*
        """)
        st.info("💙 One of the most successful franchises in IPL history!")

# ==============================================================================
# TASK 2: MINI MOVIE RECOMMENDATION APP
# ==============================================================================
with tab2:
    st.header("🎬 5 Trending Bollywood Movies")
    st.write("Explore top recommended Bollywood movies with ratings, genre, and storylines:")
    
    # 5 Hardcoded Trending Bollywood Movies Data
    movies = [
        {
            "title": "1. Jawan (2023)",
            "genre": "Action / Thriller",
            "rating": "⭐ 8.4/10",
            "poster": "https://upload.wikimedia.org/wikipedia/en/3/39/Jawan_film_poster.jpg",
            "description": "A high-octane action thriller highlighting a man's emotional journey to rectify the wrongs in society and fight systemic corruption."
        },
        {
            "title": "2. Pathaan (2023)",
            "genre": "Action / Spy Thriller",
            "rating": "⭐ 7.8/10",
            "poster": "https://upload.wikimedia.org/wikipedia/en/c/c3/Pathaan_film_poster.jpg",
            "description": "An exiled RAW agent teams up with a fellow spy to bring down a mercenary group planning a deadly biological attack against India."
        },
        {
            "title": "3. Stree 2 (2024)",
            "genre": "Horror / Comedy",
            "rating": "⭐ 8.1/10",
            "poster": "https://upload.wikimedia.org/wikipedia/en/e/e0/Stree_2.jpg",
            "description": "The town of Chanderi is haunted by a headless demon 'Sarkata'. Vicky and his friends must seek help from Stree to save the town."
        },
        {
            "title": "4. 3 Idiots (2009)",
            "genre": "Comedy / Drama",
            "rating": "⭐ 8.5/10",
            "poster": "https://upload.wikimedia.org/wikipedia/en/d/df/3_idiots_poster.jpg",
            "description": "Two friends search for their long-lost college roommate while recalling their student days and life lessons under an eccentric engineering professor."
        },
        {
            "title": "5. Dangal (2016)",
            "genre": "Biography / Sports Drama",
            "rating": "⭐ 8.4/10",
            "poster": "https://upload.wikimedia.org/wikipedia/en/9/99/Dangal_Poster.jpg",
            "description": "Former wrestler Mahavir Singh Phogat trains his daughters Geeta and Babita to become world-class wrestlers and win India's first gold medal."
        }
    ]
    
    # Display each movie with st.image() and st.write()
    for movie in movies:
        st.markdown("---")
        m_col1, m_col2 = st.columns([1, 3])
        
        with m_col1:
            st.image(movie["poster"], width=180, caption=movie["title"])
            
        with m_col2:
            st.subheader(movie["title"])
            st.markdown(f"**Genre:** `{movie['genre']}` | **Rating:** {movie['rating']}")
            st.write(movie["description"])

st.markdown("---")
st.caption("Powered by Streamlit | Machine Learning Deployment Assignment")
