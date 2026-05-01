# AI-AGENT
# 📊 AI Real-Time Data Analyst

An advanced, AI-driven data exploration platform that transforms natural language into actionable insights. Upload CSVs and let the agent handle the SQL, logic, and visualization in real-time.

---

## 🌟 Key Features

*   **⚡ Ultra-Fast Inference**: Powered by **Groq (Llama-3.1-8b-instant)** for near-instant responses.
*   **🧠 Intelligent SQL Agent**: Automatically interprets complex schemas and handles joins, aggregations, and filtering.
*   **🎭 Adaptive UI**: Custom **Glassmorphism** design with a background animation that supports both Light and Dark modes.
*   **📈 Dynamic Visuals**: Auto-generates Plotly charts tailored to the specific query output.
*   **🛡️ Production Ready**: Features robust error handling for API rate limits (429 errors) and database constraints.

---

## 🛠️ Tech Stack

| Category | Technology |
| :--- | :--- |
| **Frontend** | [Streamlit](https://streamlit.io/) |
| **Orchestration** | [LangChain](https://www.langchain.com/) |
| **Model** | [Groq (Llama 3.1)](https://groq.com/) |
| **Database** | SQLite (In-Memory via SQLAlchemy) |
| **Visuals** | [Plotly Express](https://plotly.com/python/) |

---

## 📂 Featured Datasets

The application is optimized for specialized analysis in these domains:
*   **Healthcare (`heart.csv`)**: Identifying cardiovascular risk factors and patient demographics.
*   **Finance (`insurance.csv`)**: Analyzing cost drivers, BMI correlations, and regional insurance trends.

---

## 🚀 Installation & Setup


### 1. Set Up Environment
Create a `.env` file or enter your API key directly in the UI:
bash
GROQ_API_KEY=your_key_here

Install Dependencies

Bash
pip install -r requirements.txt
Launch the Dashboard

Bash
streamlit run app.py
💡 Example Prompts to Try
"Show a bar chart of heart disease cases grouped by ChestPainType."

"Compare the average insurance charges for smokers vs non-smokers."

"What is the average cholesterol level for each RestingECG category?"

---

## 👨‍💻 Developed By

**Yashawanth B R**  
*Cloud Data Analytics | Computer Science*

> **Reliability Note:** This system implements a custom **"Direct Route"** prompt structure. This architectural choice specifically minimizes "Failed to call function" errors and optimizes inference speed for real-time analysis.

**Author:**  
**Yashawanth B R**  
*Data Analytics & Data Science Specialist*
