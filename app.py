import streamlit as st
import random

st.set_page_config(page_title="My Final AI", page_icon="⚡")
st.title("⚡ My Real AI Image Maker")

prompt = st.text_input("Kya banana hai?", placeholder="e.g. A cool gaming logo")

if st.button("Banao!"):
    if prompt:
        with st.spinner("AI Nayi Photo bana raha hai..."):
            # Har baar naya number (seed) taake same pic na aaye
            seed = random.randint(1, 999999)
            
            # Ye link sabse stable hai aur images change karta hai
            image_url = f"https://image.pollinations.ai/prompt/{prompt.replace(' ', '%20')}?width=1024&height=1024&seed={seed}&nologo=true"
            
            # Hum image ko container mein dalenge taake error na aaye
            st.image(image_url, caption=f"Result for: {prompt}", use_container_width=True)
            
            # Agar image load na ho toh backup link
            st.write("---")
            st.write("📩 **Agar photo nazar nahi aa rahi, toh niche click karein:**")
            st.write(f"[Direct Photo Link]({image_url})")
            
            st.success("Done! Nayi image check karein.")
    else:
        st.warning("Pehle kuch likho!")
