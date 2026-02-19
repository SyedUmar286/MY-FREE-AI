import streamlit as st
import random

st.set_page_config(page_title="My VIP AI", page_icon="🔥")
st.title("🔥 My VIP Fast AI Generator")

prompt = st.text_input("Kya banana hai?", placeholder="e.g. A futuristic robot playing cricket")

if st.button("Generate Now"):
    if prompt:
        with st.spinner("AI photo bana raha hai, thoda sabar..."):
            # Is baar hum server aur seed badal kar try kar rahe hain
            seed = random.randint(1, 100000)
            # Alternative stable link
            image_url = f"https://pollinations.ai/p/{prompt.replace(' ', '%20')}?width=1024&height=1024&seed={seed}&model=flux&nologo=true"
            
            # Direct Image display
            st.image(image_url, caption="Mubarak ho! Picture tayyar hai.", use_container_width=True)
            
            # Agar image phir bhi na dikhe toh ye Link kaam karega
            st.write("---")
            st.write("📩 **Agar upar photo nazar nahi aa rahi, toh niche button dabao:**")
            st.link_button("Photo Dekho (Open in New Tab)", image_url)
    else:
        st.warning("Kuch likho toh sahi!")
