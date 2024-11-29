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
            background-color: #111111;
            padding: 1rem;
            text-align: center;
            z-index: 1000;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .full-width-header p {
            font-size: 2.5rem;  /* Increased font size */
            font-weight: bold;  /* Made text bold */
            margin: 0;
        }
        .content-padding {
            margin-top: 120px; /* Adjust based on header height */
        }
        .chat-container {
            position: fixed;
            bottom: 0;
            right: 0;
            width: 400px;
            background-color: transparent;  # Changed from 'white' to 'transparent'
            padding: 1rem;
            border-radius: 10px 0 0 0;
            box-shadow: -2px -2px 5px rgba(0,0,0,0.1);
            z-index: 1000;
    </style>
""", unsafe_allow_html=True)

# Add the header
st.markdown("""
    <div class="full-width-header">
        <p>Pealkiri</p>
    </div>
    <div class="content-padding"></div>
""", unsafe_allow_html=True)

# Made the main content title bigger using header level 1
st.header("Pealkiri")
# Display image in main container
st.image("../data/image.png", width=800)  # Set fixed width instead of container width

# Initialize chat history in session state if it doesn't exist
if "messages" not in st.session_state:
    st.session_state.messages = []

# Chat container
with st.container():
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)
    
    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Chat input
    if prompt := st.chat_input("Ask me anything..."):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Add assistant response
        response = f"This is a sample response to: {prompt}"  # Replace with actual chatbot logic
        st.session_state.messages.append({"role": "assistant", "content": response})
    
    st.markdown('</div>', unsafe_allow_html=True)

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
