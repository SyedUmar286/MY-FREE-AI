import streamlit as st

st.set_page_config(page_title="My Free AI", page_icon="🎨")
st.title("🎨 My Own Free AI Logo Maker")

prompt = st.text_input("Kya banana hai?", placeholder="e.g. Modern lion logo gold style")

if st.button("Generate Logo"):
    if prompt:
        with st.spinner("AI Logo bana raha hai..."):
            # Sabse behtar aur naya tareeqa
            image_url = f"https://image.pollinations.ai/prompt/{prompt.replace(' ', '%20')}?width=1024&height=1024&nologo=true"
            
            # HTML ke zariye image dikhana taake error na aaye
            st.markdown(f'<img src="{image_url}" width="100%">', unsafe_allow_html=True)
            
            st.success("Ye lo tumhara logo!")
            st.write(f"[Direct Link Pe Click Karo Agar Image Nazar Na Aaye]({image_url})")
    else:
        st.warning("Pehle kuch likho toh sahi!")
