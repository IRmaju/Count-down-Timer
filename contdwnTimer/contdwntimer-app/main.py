# main.py

import streamlit as st
import time

st.set_page_config(page_title="⏱️ Countdown Timer", page_icon="⏰", layout="centered")

st.markdown("# ⏱️ Countdown Timer")
st.markdown("Enter the number of seconds and click **Start** to begin the countdown.")

# User input for seconds
seconds = st.number_input("⏬ Enter countdown time in seconds", min_value=1, value=10, step=1)

if st.button("▶️ Start Timer"):
    placeholder = st.empty()

    for i in range(seconds, 0, -1):
        mins, secs = divmod(i, 60)
        timer_text = f"⏳ **{mins:02d}:{secs:02d}** remaining..."
        placeholder.markdown(timer_text)
        time.sleep(1)

    placeholder.markdown("🎉 **Time's up!** ⏰")


