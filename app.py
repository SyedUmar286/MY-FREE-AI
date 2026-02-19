import streamlit as st

st.set_page_config(page_title="My Free AI", page_icon="🎨")
st.title("🎨 My Own Free AI Logo Maker")

prompt = st.text_input("Kya banana hai?", placeholder="e.g. Modern lion logo gold style")

if st.button("Generate Logo"):
    if prompt:
        with st.spinner("AI Logo bana raha hai..."):
            # Naya aur behtar URL format
            clean_prompt = prompt.replace(" ", "%20")
            image_url = f"https://pollinations.ai/p/{clean_prompt}?width=1024&height=1024&nologo=true"
            
            # Image ko display karne ka sahi tareeqa
            st.image(image_url, caption="Tumhara Brand New Logo", use_container_width=True)
            st.success("Done!")
    else:
        st.warning("Pehle kuch likho toh sahi!")
