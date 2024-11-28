import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import openai

# Set your OpenAI API Key (replace with your key)
openai.api_key = "your_openai_api_key"

# Streamlit UI
st.set_page_config(
    page_title="Interactive Data Visualizer",
    page_icon="📊",
    layout="wide",
)

# Generate random data
@st.cache_data
def generate_random_data():
    np.random.seed(42)
    data = pd.DataFrame({
        "Date": pd.date_range(start="2023-01-01", periods=20, freq="D"),
        "Category": [f"Category {i}" for i in range(1, 21)],
        "Value": np.random.uniform(10, 100, 20),
        "Temperature": np.random.uniform(15, 35, 20),
        "Humidity": np.random.uniform(20, 80, 20),
        "Rainfall": np.random.uniform(0, 20, 20),
    })
    return data

data = generate_random_data()

# Function to query OpenAI API
def query_llm(prompt, columns):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a data visualization assistant."},
            {"role": "user", "content": f"Columns available: {columns}. {prompt}"}
        ],
        temperature=0.5,
    )
    return response['choices'][0]['message']['content']

# Function to generate a graph based on LLM response
def generate_graph(llm_response):
    try:
        # Parse the LLM response (basic parsing based on keywords)
        if "line" in llm_response.lower():
            graph_type = "line"
        elif "scatter" in llm_response.lower():
            graph_type = "scatter"
        elif "bar" in llm_response.lower():
            graph_type = "bar"
        else:
            return None, "Error: Unsupported graph type!"

        # Identify the columns to use
        if "value" in llm_response.lower():
            y_col = "Value"
        elif "temperature" in llm_response.lower():
            y_col = "Temperature"
        elif "humidity" in llm_response.lower():
            y_col = "Humidity"
        elif "rainfall" in llm_response.lower():
            y_col = "Rainfall"
        else:
            return None, "Error: Unsupported column!"

        x_col = "Category" if "category" in llm_response.lower() else "Date"

        # Generate the graph using Plotly
        if graph_type == "line":
            fig = px.line(data, x=x_col, y=y_col, title=f"{graph_type.capitalize()} graph of {y_col} over {x_col}")
        elif graph_type == "scatter":
            fig = px.scatter(data, x=x_col, y=y_col, title=f"{graph_type.capitalize()} graph of {y_col} over {x_col}")
        elif graph_type == "bar":
            fig = px.bar(data, x=x_col, y=y_col, title=f"{graph_type.capitalize()} graph of {y_col} over {x_col}")
        return fig, None

    except Exception as e:
        return None, f"Error generating graph: {e}"



# Add custom CSS to hide header and toolbar
st.markdown(
    """
    <style>
    header {visibility: hidden;}
    [data-testid="stToolbar"] {visibility: hidden;}
    .viewerBadge_container__1QSob {visibility: hidden;}
    .main {padding-top: 0px;}
    </style>
    """,
    unsafe_allow_html=True,
)

# Sidebar for page navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Choose a Page", ["Home", "Line Chart", "Scatter Plot", "Bar Chart"])

# Page: Home
if page == "Home":
    st.title("📊 Interactive Data Visualizer")
    st.markdown(
        "Welcome to the **Interactive Data Visualizer**! Use the sidebar to navigate between different types of charts."
    )
    st.subheader("Random Data Preview")
    st.dataframe(data)

# Page: Line Chart
elif page == "Line Chart":
    st.title("📈 Line Chart")
    st.markdown("This page displays a **line chart** of the data.")
    fig = px.line(data, x="Date", y="Value", title="Line Chart of Value Over Time", markers=True)
    st.plotly_chart(fig, use_container_width=True)

# Page: Scatter Plot
elif page == "Scatter Plot":
    st.title("🔵 Scatter Plot")
    st.markdown("This page displays a **scatter plot** of the data.")
    fig = px.scatter(data, x="Temperature", y="Humidity", size="Value", color="Category", 
    title="Scatter Plot of Humidity vs. Temperature")
    st.plotly_chart(fig, use_container_width=True)

# Page: Bar Chart
elif page == "Bar Chart":
    st.title("📊 Bar Chart")
    st.markdown("This page displays a **bar chart** of the data.")
    fig = px.bar(data, x="Category", y="Value", title="Bar Chart of Values by Category", color="Value")
    st.plotly_chart(fig, use_container_width=True)
