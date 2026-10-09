import streamlit as st
from google import genai
from dotenv import load_dotenv
import time
load_dotenv()
client = genai.Client()
import time

st.set_page_config(page_title="AI Travel Assistant", page_icon="✈️", layout="centered")

TITLE = "AI Travel Assistant"
SUBTITLE = "Plan smarter. Travel farther. 🌍"


def static_header():
    st.markdown(f"# ✈️ :rainbow[{TITLE}]")
    st.caption(SUBTITLE)
    st.divider()


def animated_header():
    sky = st.empty()
    title = st.empty()
    subtitle = st.empty()

    # 1) Plane flies across the screen leaving a trail
    for i in range(28):
        sky.markdown(f"### {'☁️ ' if i % 7 == 0 else ''}{'—' * i}✈️")
        time.sleep(0.03)
    sky.markdown("### 🌍 ✈️ 🏝️ 🗼 🏔️ 🚆")

    # 2) Title types itself out in rainbow colours
    for k in range(1, len(TITLE) + 1):
        title.markdown(f"# :rainbow[{TITLE[:k]}] ▌")
        time.sleep(0.06)
    title.markdown(f"# :rainbow[{TITLE}]")

    # 3) Subtitle typewriter effect
    for k in range(1, len(SUBTITLE) + 1):
        subtitle.caption(SUBTITLE[:k] + "▌")
        time.sleep(0.03)
    subtitle.caption(SUBTITLE)

    st.divider()
    st.toast("Welcome aboard! Where to next?", icon="🧳")


# Play the intro animation only once per session
if "intro_done" not in st.session_state:
    animated_header()
    st.session_state.intro_done = True
else:
    static_header()
location=st.text_input("Where does your mind lead you today?")
days=st.number_input("May I know for how many days?", min_value=1, max_value=30)
budget=st.selectbox("Select Your Budget:moneybag:" , ["luxury","Moderate","Budget friendly"])
travel_type=st.radio("With whom are u travelling with?" , ['family','solo','friends'])
prompt=f"""You are a proffesional travel plan designer and the user has to go to {location} for {days}.
Plan a perfect plan and present the plan as main points in numbering and sub points as bullet points also plan according the budget of a {budget} type of plan
and Travel Type: {travel_type}"""
if st.button("Plan a Trip"):

    
  interaction = client.interactions.create(
         model="gemini-3.5-flash-lite",
         input=prompt,
         #stream=True,
         generation_config={
             "temperature":0.7,
             "top_k":20,
             "max_output_tokens":4000,
         }
         )
  st.success("Here Is Your Perfect Plan :100:")
  st.write(interaction.output_text)
  st.write("Thank You For Using Our Client 🙏")
   