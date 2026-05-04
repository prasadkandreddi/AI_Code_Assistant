
import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
import time

# ---------- PAGE CONFIG ----------
st.set_page_config(page_title="AI Code Assistant", page_icon="🧩", layout="wide")

# ---------- UI ----------
st.markdown("""
<style>
.stApp { background-color: #0f172a; color: #e2e8f0; }
section[data-testid="stSidebar"] { background-color: #020617; }
.stTextArea textarea {
    background-color: #020617 !important;
    color: #e2e8f0 !important;
}
.stButton>button {
    background-color: #2563eb;
    color: white;
    border-radius: 8px;
}
</style>
""", unsafe_allow_html=True)

# ---------- LOAD API ----------
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

if not api_key:
    st.error("❌ Add GEMINI_API_KEY in Secrets or .env")
    st.stop()

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-2.5-flash")

# ---------- SESSION ----------
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------- SIDEBAR ----------
with st.sidebar:
    st.title("⚙️ Settings")

    temperature = st.slider("Temperature", 0.0, 1.0, 0.3)
    top_p = st.slider("Top P", 0.0, 1.0, 0.9)
    top_k = st.slider("Top K", 1, 100, 40)

    if st.button("🧹 Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# ---------- PROMPT ----------
def build_prompt(user_input):
    return f"""
You are a strict coding assistant.

STEP 1:
Check if input is coding-related.

IF NOT:
Reply ONLY:
❌ This assistant handles coding-related questions only.

---

IF YES:
Follow STRICT format:

💻 CODE:
(code only, no comments)

🧠 EXPLANATION:
(max 3 lines)

🎯 QUESTIONS:
(3 coding interview questions)

---

USER INPUT:
{user_input}
"""

# ---------- MAIN ----------
st.title("🧩 AI Code Assistant")
st.caption("Coding-only assistant 🚀")

# ---------- CHAT ----------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ---------- INPUT ----------
user_input = st.chat_input("Ask coding questions only...")

if user_input:

    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.markdown(user_input)

    prompt = build_prompt(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Thinking... ⏳"):
            try:
                time.sleep(1)  # prevent rapid requests

                response = model.generate_content(
                    prompt,
                    generation_config={
                        "temperature": temperature,
                        "top_p": top_p,
                        "top_k": top_k,
                        "max_output_tokens": 512,
                    }
                )

                output = response.text
                st.markdown(output)

                st.session_state.messages.append(
                    {"role": "assistant", "content": output}
                )

            except Exception as e:
                if "429" in str(e):
                    st.error("⚠️ API limit reached. Please wait and try again.")
                else:
                    st.error(f"❌ Error: {str(e)}")


