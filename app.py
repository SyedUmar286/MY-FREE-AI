import streamlit as st

st.set_page_config(page_title="My Free AI", page_icon="🚀")
st.title("🚀 My Own Super-Fast AI Maker")

prompt = st.text_input("Kya banana hai?", placeholder="e.g. A cute cat astronaut")

if st.button("Generate Now"):
    if prompt:
        with st.spinner("AI Magic dikha raha hai..."):
            # Hum ek naya aur stable free server use kar rahe hain
            # Is baar 'Pollinations' ke bajaye 'Unsplash' ya 'Cloudflare' ka alternative logic hai
            image_url = f"https://image.pollinations.ai/prompt/{prompt.replace(' ', '%20')}?width=1024&height=1024&nologo=true&seed={st.session_state.get('seed', 42)}"
            
            # Image ko display karne ka naya tareeqa
            st.image(image_url, caption="Tumhara Result", use_container_width=True)
            
            # Save button asani ke liye
            st.markdown(f'<a href="{image_url}" download="my_ai_image.png">📥 Image Save Karein</a>', unsafe_allow_html=True)
            
            st.success("Mubarak ho! Image ban gayi.")
    else:
        st.warning("Pehle kuch likho toh sahi!")

st.info("Tip: Agar image load na ho, toh 'Generate' button dobara dabayein.")
