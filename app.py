import streamlit as st
from paraphrase import generate_paraphrase

st.set_page_config(
    page_title="AI Paraphrasing Chat",
    page_icon="🧠",
    layout="wide"
)

# ---------- Custom CSS ----------
st.markdown("""
<style>

textarea {
    font-size:18px !important;
}

.stButton>button {
    width:100%;
    border-radius:8px;
}

.chat-user {
    background-color:#f1f1f1;
    padding:12px;
    border-radius:10px;
    margin-bottom:10px;
}

.chat-ai {
    background-color:#e6ffe6;
    padding:12px;
    border-radius:10px;
    margin-bottom:10px;
}

</style>
""", unsafe_allow_html=True)

# ---------- Session State ----------
if "messages" not in st.session_state:
    st.session_state.messages = []

if "mode" not in st.session_state:
    st.session_state.mode = "Standard"

# ---------- Sidebar ----------
with st.sidebar:

    st.title("🧠 Paraphrase AI")

    if st.button("➕ New Chat"):
        st.session_state.messages = []

    st.divider()

    st.subheader("Rewrite Modes")

    if st.button("Standard Mode"):
        st.session_state.mode = "Standard"

    if st.button("Fluency Mode"):
        st.session_state.mode = "Fluency"

    if st.button("Formal Mode"):
        st.session_state.mode = "Formal"

    if st.button("Creative Mode"):
        st.session_state.mode = "Creative"

    st.divider()

    st.success(f"Active Mode: {st.session_state.mode}")

    st.caption("Powered by Groq + Streamlit")

# ---------- Title ----------
st.title("💬 AI Paraphrasing Chat")

st.write("Rewrite sentences using AI")

# ---------- Chat History ----------
for message in st.session_state.messages:

    if message["role"] == "user":
        st.markdown(
            f"<div class='chat-user'><b>You:</b> {message['content']}</div>",
            unsafe_allow_html=True
        )

    else:
        st.markdown(
            f"<div class='chat-ai'><b>AI:</b> {message['content']}</div>",
            unsafe_allow_html=True
        )

# ---------- Chat Input ----------
user_input = st.chat_input("Type your sentence...")

if user_input:

    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.spinner("AI is rewriting..."):

        response = generate_paraphrase(
            user_input,
            st.session_state.mode
        )

    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })

    st.rerun()