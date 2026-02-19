import streamlit as st
import random

st.set_page_config(page_title="My Working AI", page_icon="🎨")
st.title("🎨 My Final Working AI Maker")

prompt = st.text_input("Kya banana hai?", placeholder="e.g. A cool gaming logo")

if st.button("Banao!"):
    if prompt:
        with st.spinner("AI Nayi Photo bana raha hai..."):
            # Har baar naya number (seed) generate hoga taake purani pic na aaye
            seed = random.randint(1, 99999)
            
            # Ye naya stable link hai jo block nahi hota
            image_url = f"https://pollinations.ai/p/{prompt.replace(' ', '%20')}?width=1024&height=1024&seed={seed}&nologo=true"
            
            # Image dikhana
            st.image(image_url, caption=f"Result for: {prompt}", use_container_width=True)
            st.success("Mubarak ho! Nayi image tayyar hai.")
    else:
        st.warning("Pehle kuch likho!")
