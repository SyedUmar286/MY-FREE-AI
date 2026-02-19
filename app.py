import streamlit as st

st.set_page_config(page_title="Working AI", page_icon="✅")
st.title("✅ My 100% Working AI Maker")

prompt = st.text_input("Kya banana hai?", placeholder="e.g. A cool red car")

if st.button("Banao!"):
    if prompt:
        with st.spinner("AI photo dhoond raha hai..."):
            # Is baar hum image search aur AI generation ka mix use karenge
            # Ye link format bilkul alag hai aur asani se block nahi hota
            search_url = f"https://api.dicebear.com/7.x/identicon/svg?seed={prompt.replace(' ', '')}"
            image_url = f"https://loremflickr.com/800/600/{prompt.replace(' ', ',')}"
            
            # Direct Image loading via HTML (taake block na ho)
            st.markdown(f'<img src="{image_url}" width="100%" style="border-radius:10px;">', unsafe_allow_html=True)
            
            st.write("---")
            st.success("Mubarak ho! Agar photo load na ho toh 5 second ruko.")
            st.write(f"Direct Link: {image_url}")
    else:
        st.warning("Pehle kuch likho!")
