import streamlit as st

st.set_page_config(page_title="My Free AI", page_icon="🎨")
st.title("🎨 My Own Free AI Logo Maker")
st.write("Description likho aur Magic dekho!")

# Input Box
prompt = st.text_input("Kya banana hai?", placeholder="e.g. A cool gaming logo with a dragon")

if st.button("Generate Logo"):
    if prompt:
        with st.spinner("AI Logo bana raha hai..."):
            # Flux model use kar rahe hain jo sabse best aur free hai
            image_url = f"https://pollinations.ai/p/{prompt.replace(' ', '%20')}?width=1024&height=1024&seed=42&model=flux"
            st.image(image_url, caption="Tumhara Brand New Logo")
            st.success("Done!")
    else:
        st.warning("Pehle kuch likho toh sahi!")
