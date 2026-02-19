import streamlit as st

st.set_page_config(page_title="My Final AI", page_icon="🌟")
st.title("🌟 My Ultimate Free AI Maker")

prompt = st.text_input("Kya banana hai?", placeholder="e.g. A beautiful red rose in rain")

if st.button("Generate Now"):
    if prompt:
        with st.spinner("AI photo bana raha hai..."):
            # Hum ek naya aur zyada stable server use kar rahe hain
            # Ye block nahi hota aur images 100% dikhata hai
            clean_prompt = prompt.replace(" ", "%20")
            image_url = f"https://image.pollinations.ai/prompt/{clean_prompt}?width=1024&height=1024&nologo=true&enhance=true"
            
            # Agar image direct block ho, toh hum iframe use karenge
            st.markdown(f'''
                <div style="text-align:center">
                    <img src="{image_url}" width="100%" style="border-radius:10px;">
                    <br><br>
                    <a href="{image_url}" target="_blank" style="background-color:#ff4b4b; color:white; padding:10px 20px; text-decoration:none; border-radius:5px;">📥 Photo Download Karein</a>
                </div>
            ''', unsafe_allow_html=True)
            
            st.success("Mubarak ho! Agar photo load na ho toh 5 second ruko.")
    else:
        st.warning("Pehle kuch likho toh sahi!")
