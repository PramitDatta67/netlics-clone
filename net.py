import streamlit as st

# Movie data with placeholder images
movies = {
    'The Matrix': {
        'genre': 'Sci-Fi', 
        'description': 'A hacker discovers the true nature of his reality and his role in the war against its controllers.', 
        'image': 'https://upload.wikimedia.org/wikipedia/en/9/94/The_Matrix.jpg',
        'trailer': 'https://www.youtube.com/watch?v=vKQi3bBA1y8'
    },
    'Inception': {
        'genre': 'Action', 
        'description': 'A thief who enters the dreams of others to steal secrets from their subconscious is given a chance to have his criminal record erased.', 
        'image': 'https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg',
        'trailer': 'https://www.youtube.com/watch?v=YoHD9XEInc0'
    },
    'The Dark Knight': {
        'genre': 'Action', 
        'description': 'Batman faces a new enemy, the Joker, who seeks to create chaos in Gotham City.', 
        'image': 'https://upload.wikimedia.org/wikipedia/en/1/1c/The_Dark_Knight_%282008_film%29.jpg',
        'trailer': 'https://www.youtube.com/watch?v=EXeTwQWrcwY'
    },
    'Avatar': {
        'genre': 'Adventure', 
        'description': 'A paraplegic Marine dispatched to the moon Pandora on a unique mission becomes torn between following his orders and protecting the world he feels is his home.', 
        'image': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcSvIXsBmZhSV4cYIHDIe8q131FicQ2u8VbRqcrNxdIj5J-VFHX0',
        'trailer': 'https://www.youtube.com/watch?v=5PSNL1qE6VY'
    },
    'The Lion King': {
        'genre': 'Animation', 
        'description': 'Lion prince Simba and his father are targeted by his bitter uncle, who wants to ascend the throne himself.', 
        'image': 'https://upload.wikimedia.org/wikipedia/en/3/3d/The_Lion_King_poster.jpg',
        'trailer': 'https://www.youtube.com/watch?v=4CbLXeGSDxg'
    }
}

# Set page configuration
st.set_page_config(page_title="Netflix Clone", layout="wide")

# Custom CSS for Netflix-like styling
st.markdown("""
<style>
    .stApp {
        background-color: #000;
        color: #fff;
    }
    .stButton>button {
        background-color: #E50914;
        color: white;
        border: none;
        padding: 8px 20px;
        border-radius: 4px;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #f40612;
    }
    .stTitle {
        color: #E50914;
    }
</style>
""", unsafe_allow_html=True)

# Title with Netflix-like styling
st.markdown("<h1 style='color: #E50914;'>Welcome to My Netflix Clone</h1>", unsafe_allow_html=True)

# Display movie posters in a grid
cols = st.columns(5)  # Creates 5 columns for our 5 movies

for i, (movie, details) in enumerate(movies.items()):
    with cols[i]:
        st.image(details['image'], use_column_width=True)
        st.subheader(movie)
        st.caption(f"Genre: {details['genre']}")
        
        # Movie detail button
        if st.button(f"Watch {movie}"):
            st.write(f"Now streaming {movie}...")
            st.video(details['trailer'])  # Play the trailer

# Horizontal line separator
st.markdown("---")

# Detailed view when a movie is selected
selected_movie = st.selectbox("Select a movie to learn more", list(movies.keys()))

if selected_movie:
    st.header(selected_movie)
    col1, col2 = st.columns([1, 3])
    
    with col1:
        st.image(movies[selected_movie]['image'], width=300)
    
    with col2:
        st.subheader(f"Genre: {movies[selected_movie]['genre']}")
        st.write(movies[selected_movie]['description'])
        if st.button(f"Play {selected_movie}", key=f"play_{selected_movie}"):
            st.video(movies[selected_movie]['trailer'])
            st.success(f"Enjoy watching {selected_movie}!")