import streamlit as st

st.set_page_config(
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items=None
)
# Sidebar content
st.sidebar.title("")

# Add custom CSS for full-width header and chat container
st.markdown("""
    <style>
        .full-width-header {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 15%;
            background-color: #111111;
            padding-left: 4.5rem;
            text-align: left;
            z-index: 1000;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .content-padding {
            margin-top: 120px;
        }
    </style>
""", unsafe_allow_html=True)

# Add the header
st.markdown("""
    <div class="full-width-header">
        <h1 style="color: white; font-size: 2.5rem; padding-top: 25px;">Avaandmete visualiseerimine</h1>
    </div>
    <div class="content-padding"></div>
""", unsafe_allow_html=True)

st.header("Graafi kirjeldus")
st.write("tekst")

# Initialize chat history in session state if it doesn't exist
if "messages" not in st.session_state:
    st.session_state.messages = []

st.image("../data/image.png", width=800)  # Set fixed width instead of container width


# Chat container
with st.container():
    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Chat input
    if prompt := st.chat_input("Küsi minult graafi kohta midagi..."):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Add assistant response
        response = f"This is a sample response to: {prompt}"  # Replace with actual chatbot logic
        st.session_state.messages.append({"role": "assistant", "content": response})

# Remove header link
st.markdown("""
    <style>
        div[data-testid="stDecoration"] {display:none;}
    </style>
""", unsafe_allow_html=True)

# Hide default Streamlit elements
hide_streamlit_style = """
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .stDeployButton {display:none;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
