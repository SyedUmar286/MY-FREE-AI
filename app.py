import streamlit as st
import random

st.set_page_config(page_title="Pro AI Maker", page_icon="🎨")
st.title("🎨 My Professional AI Image Maker")

# User se input lena
prompt = st.text_input("Kya banana hai?", placeholder="e.g. A futuristic city, high detail")

if st.button("Generate Image"):
    if prompt:
        with st.spinner("AI Graphics bana raha hai..."):
            # Random seed taake har baar bilkul nayi pic aaye
            seed = random.randint(1, 999999)
            
            # Hum image.pollinations.ai ka naya stable endpoint use karenge
            # Ismein humne 'nologo=true' aur 'model=flux' add kiya hai behtar results ke liye
            image_url = f"https://image.pollinations.ai/prompt/{prompt.replace(' ', '%20')}?seed={seed}&width=1024&height=1024&nologo=true&model=flux"
            
            # Image dikhane ka sabse behtar tareeqa
            st.image(image_url, caption=f"AI Result: {prompt}", use_container_width=True)
            
            # Download link
            st.write(f"🔗 [Direct Image Link]({image_url})")
            st.success("Tayyar hai!")
    else:
        st.warning("Kuch likho toh sahi!")
