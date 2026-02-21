import streamlit as st
import requests
import random

st.set_page_config(page_title="AI Logo Maker", page_icon="✨")
st.title("✨ My Professional AI Logo Maker")

# User se prompt lena
prompt = st.text_input("Apne logo ka idea likho:", placeholder="e.g. A roaring lion logo, minimalist, gold and black")

if st.button("Generate Logo"):
    if prompt:
        with st.spinner("AI tumhara logo bana raha hai..."):
            # Hugging Face API ka naya aur stable endpoint
            # Ye server Pollinations se alag hai aur block nahi hota!
            # Hum ek specific model use kar rahe hain jo logo ke liye best hai.
            # Dhyan rahe, ye API kabhi kabhi slow ho sakta hai (free tier ki wajah se)
            
            # API endpoint for Stable Diffusion XL Turbo (community model)
            API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
            headers = {"Authorization": "Bearer hf_YOUR_API_TOKEN_HERE"} # VERY IMPORTANT: Neeche explain kiya hai!

            # Input data for the model
            payload = {
                "inputs": f"{prompt}, high quality, professional logo, vector art, brand identity, white background",
                "options": {"wait_for_model": True}
            }

            try:
                response = requests.post(API_URL, headers=headers, json=payload)
                response.raise_for_status() # Check for HTTP errors
                
                image_bytes = response.content
                
                if image_bytes:
                    st.image(image_bytes, caption=f"Tumhara AI Logo: {prompt}", use_container_width=True)
                    st.success("Mubarak ho! Logo ban gaya.")
                    
                    # Download button
                    st.download_button(
                        label="Logo Download Karo",
                        data=image_bytes,
                        file_name=f"ai_logo_{random.randint(1,10000)}.png",
                        mime="image/png"
                    )
                else:
                    st.error("AI koi image nahi bana saka. Dobara try karein ya prompt badlein.")

            except requests.exceptions.RequestException as e:
                st.error(f"Error: Server se connect nahi ho paya ya API key ghalat hai. {e}")
                st.info("Agar error baar baar aaye, toh prompt thoda simple likhein.")

    else:
        st.warning("Pehle kuch likho toh sahi!")
