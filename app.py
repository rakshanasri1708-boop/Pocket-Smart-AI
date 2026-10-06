import streamlit as st
import google.generativeai as genai

genai.configure(api_key="YOUR_GEMINI_API_KEY")
model = genai.GenerativeModel("gemini-1.5-flash")

st.set_page_config(page_title="PocketSmart", page_icon="💰")
st.title("💰 PocketSmart AI - Smart Budget Planner")
st.markdown("Your AI money manager for students!")

income = st.number_input("Monthly Income / Pocket Money ₹", min_value=1000, value=15000, step=1000)

st.subheader("Monthly Expenses")
col1, col2 = st.columns(2)
with col1:
    rent = st.number_input("Rent / Hostel ₹", value=5000)
    food = st.number_input("Food ₹", value=4000)
    travel = st.number_input("Travel ₹", value=1000)

with col2:
    ott = st.number_input("OTT / Shopping ₹", value=1000)
    others = st.number_input("Others ₹", value=1000)

total_exp = rent + food + travel + ott + others
savings = income - total_exp

st.metric("Total Expense", f"₹{total_exp}")
st.metric("Remaining", f"₹{savings}")

goal = st.selectbox("Your Saving Goal", ["Save 5k per month", "Buy Laptop", "Trip", "Just manage"])
if st.button("💡 Get AI Budget Plan"):
   with st.spinner("Analyzing..."):
     prompt = f"""
     I am Indian college student. Income {income}, expenses:
     Rent {rent}, Food {food}, Travel {travel}, OTT {ott}, Others {others}.
     Total expense {total_exp}, saving {savings}. Goal: {goal}.
     Give:
     1. 50/30/20 budget review 
     2. Where to cut 
     3. 3 smart saving tips 
     4. Best investment for student (Mutual fund/SIP/Gold)
     Use Tamil + English mix, friendly tone.
     """
     res =
model.generate_content(prompt)
     st.success("Your Personalized Plan:")
     st.write(res.text)

st.sidebar.info("For NASSCOM FSP SB Project")
