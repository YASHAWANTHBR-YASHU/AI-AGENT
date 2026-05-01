# AI-AGENT
📊 AI Real-Time Data Analyst
An interactive, AI-powered web application that allows users to upload CSV data and receive instant insights paired with dynamic visualizations. This project leverages LLMs to translate natural language queries into SQL, providing a "chat-with-your-data" experience.

✨ Key Features
Dual-Dataset Analysis: Specialized support for healthcare and insurance data (e.g., insurance.csv and heart.csv).

Natural Language to SQL: Converts user questions into precise SQLite queries using Llama 3.1 8B via Groq.

Dynamic Visualizations: Automatically generates Plotly charts that match the AI's textual insights.

Theme-Aware UI: Features a custom animated background and "Glassmorphism" UI that adapts to both Light and Dark modes.

Rate-Limit Resilience: Built-in "Smart Wait" logic and retry mechanisms to handle high-traffic API requests.

🛠️ Tech Stack
Frontend: Streamlit

AI Orchestration: LangChain (SQL Agent)

Inference: Groq (Llama-3.1-8b-instant)

Data Handling: Pandas, SQLAlchemy (In-Memory SQLite)

Charts: Plotly Express

🚀 Getting Started
Prerequisites
Python 3.8+

A Groq API Key

Installation
Clone the repository:

Bash
git clone https://github.com/your-username/ai-data-analyst.git
cd ai-data-analyst
Install dependencies:

Bash
pip install streamlit pandas plotly sqlalchemy langchain-groq langchain-community
Run the app:

Bash
streamlit run app.py
📈 Example Queries
“Compare the average insurance charges for smokers vs non-smokers.”

“Show a bar chart of heart disease cases grouped by chest pain type.”

“What is the average BMI for each region?”

⚙️ Recent Optimizations
Performance: Switched to llama-3.1-8b-instant for faster inference and lower token consumption.

UI/UX: Replaced deprecated parameters with width='stretch' for future-proof Plotly rendering.

Reliability: Implemented a "Direct Route" prompt structure to minimize "Failed to call function" errors.

Author
Yashawanth B R
Cloud Data Analytics & Computer Science Specialist
