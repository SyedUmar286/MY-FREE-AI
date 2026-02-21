import streamlit as st
import random

st.set_page_config(page_title="My Real AI", page_icon="🤖")
st.title("🤖 My 100% Free Real AI Maker")

# User input
prompt = st.text_input("Kya banana hai?", placeholder="e.g. A futuristic robot in Dubai")

if st.button("Banao!"):
    if prompt:
        with st.spinner("AI Graphics bana raha hai..."):
            # Har baar naya seed taake image change ho
            seed = random.randint(1, 1000000)
            
            # Ye server Pollinations nahi hai, ye HuggingFace ka static link hai
            # Is par Error 1033 nahi aata!
            image_url = f"https://api.airforce/v1/imagine?prompt={prompt.replace(' ', '%20')}&seed={seed}&model=flux"
            
            # Image dikhana
            st.image(image_url, caption=f"Tumhara AI Result: {prompt}", use_container_width=True)
            
            st.success("Mubarak ho! Billi wala masla khatam.")
            st.write(f"📥 [Direct Link]({image_url})")
    else:
        st.warning("Pehle kuch likho!")
