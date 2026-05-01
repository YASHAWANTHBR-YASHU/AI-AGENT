import streamlit as st
import pandas as pd
import plotly.express as px
import re
import time
from sqlalchemy import create_engine
from langchain_groq import ChatGroq
from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import create_sql_agent

# 1. Page Config
st.set_page_config(page_title="AI Data Analyst Pro", layout="wide", page_icon="📈")

# --- Adaptive CSS for Light & Dark Theme Animation ---
st.markdown("""
    <style>
    /* Animated gradient that works on both themes */
    .stApp {
        background: linear-gradient(-45deg, rgba(0, 212, 255, 0.1), rgba(121, 9, 121, 0.1), rgba(0, 255, 148, 0.1));
        background-size: 400% 400%;
        animation: gradient 15s ease infinite;
    }

    @keyframes gradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* Glassmorphism effect for cards */
    div[data-testid="stVerticalBlock"] > div:has(div.stMarkdown) {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 15px;
        padding: 20px;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        margin-bottom: 10px;
    }

    /* Primary Button Styling */
    .stButton>button {
        background-color: #00d4ff;
        border: none;
        border-radius: 8px;
        transition: 0.3s;
    }
    .stButton>button:hover {
        box-shadow: 0 0 15px #00d4ff;
        transform: scale(1.02);
    }
    </style>
    """, unsafe_allow_html=True)

st.title("📊 AI Real-Time Analyst")
st.write("Your adaptive, theme-aware data assistant.")

# 2. Sidebar Management
with st.sidebar:
    st.header("🔑 Authentication")
    user_api_key = st.text_input("Groq API Key", type="password")
    
    st.divider()
    st.header("📂 File Upload")
    uploaded_files = st.file_uploader("Drop CSVs here", type=["csv"], accept_multiple_files=True)
    
    if st.button("🔄 Reset App"):
        st.rerun()

if uploaded_files and user_api_key:
    # 3. Fast-Engine Setup
    engine = create_engine("sqlite:///:memory:")
    
    for file in uploaded_files:
        t_name = re.sub(r'\W+', '_', file.name.replace(".csv", "")).lower()
        try:
            try:
                df = pd.read_csv(file)
            except UnicodeDecodeError:
                file.seek(0)
                df = pd.read_csv(file, encoding='latin1')
            
            df.to_sql(t_name, engine, index=False, if_exists="replace")
            st.sidebar.success(f"✅ Active: {t_name}")
        except Exception as e:
            st.sidebar.error(f"Error: {e}")

    db = SQLDatabase(engine=engine)

    # 4. Agent Initialization
    llm = ChatGroq(model="llama-3.1-8b-instant", groq_api_key=user_api_key, temperature=0)
    agent_executor = create_sql_agent(llm=llm, db=db, agent_type="openai-tools", verbose=False)

    # 5. Interaction Logic
    query = st.chat_input("Ask: 'Show a bar chart of average charges by region'")

    if query:
        with st.spinner("🤖 Thinking..."):
            final_prompt = f"{query}. Use one SQL query. Return the SQL in a ```sql block."
            
            max_retries = 2
            for i in range(max_retries):
                try:
                    response = agent_executor.invoke({"input": final_prompt})
                    
                    c1, c2 = st.columns([1, 1])
                    with c1:
                        st.subheader("💡 Analysis")
                        st.write(response["output"])
                    
                    with c2:
                        st.subheader("📊 Visualization")
                        sql_search = re.search(r"```sql\n(.*?)\n```", response["output"], re.DOTALL)
                        
                        if sql_search:
                            sql_text = sql_search.group(1)
                            viz_data = pd.read_sql(sql_text, engine)
                            
                            if not viz_data.empty and len(viz_data.columns) >= 2:
                                # Plotly auto-detects theme if template is not forced to 'plotly_dark'
                                fig = px.bar(
                                    viz_data, 
                                    x=viz_data.columns[0], 
                                    y=viz_data.columns[1],
                                    color_discrete_sequence=['#00d4ff']
                                )
                                st.plotly_chart(fig, width='stretch')
                            else:
                                st.dataframe(viz_data)
                        else:
                            st.info("Query successful, but no chart-ready data found.")
                    break
                except Exception as e:
                    if "429" in str(e):
                        time.sleep(2)
                        continue
                    else:
                        st.error(f"Error: {e}")
                        break
else:
    st.info("👈 Enter your API Key and upload CSVs in the sidebar.")