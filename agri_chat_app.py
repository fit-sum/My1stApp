import streamlit as st
import openai
import os

# 🔐 Securely set your OpenAI API key (recommended via Streamlit secrets or environment variable)
# openai.api_key = st.secrets["openai_api_key"]  # preferred for deployment
openai.api_key = "sk-..."

# Page title and layout
st.set_page_config(page_title="AgriChat Assistant", layout="centered")
st.title("🌾 AgriChat Assistant")
st.write("Ask questions and get personalized farming advice powered by ChatGPT.")

# User inputs
crop = st.text_input("🌱 Crop Type", "Maize")
soil_properties = st.text_area("🧪 Soil Properties", "pH: 6.5, Organic Matter: Medium, Texture: Loam")
location = st.text_input("📍Location (optional)", "Ethiopia")
question = st.text_area("❓Your Farming Question", "What type of fertilizer should I use?")

# Button logic
if st.button("Get Recommendation"):
    with st.spinner("Analyzing and generating response..."):
        prompt = (
            f"You are an expert agricultural advisor.\n"
            f"Crop: {crop}\n"
            f"Soil Properties: {soil_properties}\n"
            f"Location: {location}\n"
            f"Question: {question}\n"
            f"Provide a concise, practical, and research-based recommendation."
        )

        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are an expert agronomist specializing in soil and crop management."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=500
            )
            reply = response['choices'][0]['message']['content']
            st.success("✅ Recommendation:")
            st.write(reply)

        except Exception as e:
            st.error(f"❌ Error: {str(e)}")