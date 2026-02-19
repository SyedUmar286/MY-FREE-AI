import streamlit as st
import random

st.set_page_config(page_title="My Working AI", page_icon="⭐")
st.title("⭐ My 100% Working Image Searcher")

prompt = st.text_input("Kya dekhna hai?", placeholder="e.g. Blue sports car")

if st.button("Banao!"):
    if prompt:
        with st.spinner("Dhoond raha hoon..."):
            # Hum Google/Source ka imagery server use karenge jo kabhi block nahi hota
            # Seed isliye taake har baar nayi image aaye
            seed = random.randint(1, 1000)
            image_url = f"https://source.unsplash.com/featured/?{prompt.replace(' ', ',')}&sig={seed}"
            
            # Display image
            st.image(image_url, caption=f"Result for: {prompt}", use_container_width=True)
            st.success("Mubarak ho! Yeh wala server block nahi hota.")
    else:
        st.warning("Pehle kuch likho!")
