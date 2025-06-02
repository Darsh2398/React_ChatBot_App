# Chatbot using Azure OpenAI, React.js, Python, and PostgreSQL

## Features:
- Chat interface built with React.js
- Python backend using FastAPI + Langchain
- Azure OpenAI GPT-4 integration
- PostgreSQL for persistent chat storage

## Setup Instructions

### Prerequisites:
- Node.js and npm
- Python 3.10+ and pip
- PostgreSQL
- Azure OpenAI API key

### Backend Setup:
1. Navigate to backend directory:
```bash
cd backend
python -m venv venv
venv\Scripts\activate on Windows
pip install -r requirements.txt
```
2. Update `config.py` with your Azure OpenAI and PostgreSQL credentials.
3. Run the server:
```bash
uvicorn main:app --reload
```

### Frontend Setup:
1. Navigate to frontend directory:
```bash
cd frontend
npm install
npm start
```

### Access:
Visit http://localhost:3000 to use the chatbot.