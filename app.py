import streamlit as st
import pandas as pd
from chatbot import load_agent

# Load product data for display
data = pd.read_json("products.json")

st.title("📱 Retail Phone Store")
st.write("Welcome! Browse available phones below:")

for _, row in data.iterrows():
    st.subheader(f"{row['brand']} - {row['name']}")
    st.write(row['description'])
    st.write(f"💵 Price: ${row['price']} | ⭐ Reviews: {row['reviews']}")
    stock_status = "✅ In Stock" if row['stock'] else "❌ Out of Stock"
    st.write(stock_status)
    st.markdown("---")

# Sidebar for AI chat
st.sidebar.title("💬 Ask our AI Assistant")
query = st.sidebar.text_input("Type your question here...")

# You'll need to set your Groq API key here or via env variable for security
API_KEY = st.secrets.get("GROQ_API_KEY") or ""
if query:
    with st.spinner("Thinking..."):
        try:
            agent = load_agent(API_KEY)
            response = agent.ask(query)
            st.sidebar.success(response)
        except Exception as e:
            st.sidebar.error(f"Error: {str(e)}")
