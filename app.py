import streamlit as st
import google.generativeai as genai

# Configure Gemini API
genai.configure(api_key=st.secrets["G_API_KEY"])
model = genai.GenerativeModel("gemini-2.5-flash")

st.title("🥘♻️ Food Waste Optimizer")
st.write("Reduce your food wastage and help feed people in need! 💚")

# Inputs
food_type = st.text_input("Type of food (e.g., rice, curry, bread)")
quantity = st.number_input("Approximate surplus (in kg or servings)", min_value=0.0, value=1.0)
action = st.selectbox("What would you like to do?", ["Reuse creatively", "Donate to NGO", "Both"])

if st.button("Get Suggestions"):
    prompt = f"""
You are a helpful food waste reduction assistant. Suggest creative reuse or repurposing tips for {quantity} kg of {food_type}.
If the user also wants to donate, provide a gentle message encouraging them to contact local NGOs to distribute surplus food.
Mention practical steps they can take today.
"""

    response = model.generate_content(prompt)
    st.subheader("🍽️ Suggestions")
    st.write(response.text)

if action in ["Donate to NGO", "Both"]:
    st.subheader("🤝 Local NGOs for food donation")
    st.write("""
- **Robin Hood Army**: [Visit](https://robinhoodarmy.com)
- **Feeding America**: [Visit](https://www.feedingamerica.org/)
- **Food Rescue**: [Visit](https://foodrescue.us/)
- **World Food Program USA**: [Visit](https://www.wfpusa.org/)
""")

st.markdown("---")
st.markdown("✅ Thank you for making a difference! 💚")
