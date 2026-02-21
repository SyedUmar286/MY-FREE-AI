import streamlit as st
import random

st.set_page_config(page_title="Working AI", page_icon="✅")
st.title("✅ My 100% Working AI Maker")

prompt = st.text_input("Kya banana hai?", placeholder="e.g. A cool red car")

if st.button("Banao!"):
    if prompt:
        with st.spinner("AI photo dhoond raha hai..."):
            # Yahan humne 'random number' add kiya hai 
            # Is se har baar 'Billi' nahi balkay nayi photo aayegi
            seed = random.randint(1, 5000)
            
            # Humne link mein 'all' aur 'seed' add kiya hai taake results zyada milien
            image_url = f"https://loremflickr.com/800/600/{prompt.replace(' ', ',')}/all?lock={seed}"
            
            # Direct Image loading via HTML
            st.markdown(f'<img src="{image_url}" width="100%" style="border-radius:10px; border: 2px solid #eee;">', unsafe_allow_html=True)
            
            st.write("---")
            st.success("Mubarak ho! Agar photo pasand na aaye toh dobara 'Banao!' dabayein.")
            st.write(f"🔗 [Direct Image Link]({image_url})")
    else:
        st.warning("Pehle kuch likho!")
