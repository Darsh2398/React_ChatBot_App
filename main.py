from fastapi import FastAPI, Request
from database import init_db, SessionLocal, User, DateSession, Prompt, Response
from config import AZURE_OPENAI_API_KEY, AZURE_OPENAI_ENDPOINT, AZURE_DEPLOYMENT_NAME
from openai import AzureOpenAI
from datetime import datetime
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

init_db()

client = AzureOpenAI(
    api_key=AZURE_OPENAI_API_KEY,
    api_version="2024-02-15-preview",
    azure_endpoint=AZURE_OPENAI_ENDPOINT
)

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    prompt_text = data.get("message", "").strip()
    
    if not prompt_text:
        return {"reply": "Please enter a message."}

    db = SessionLocal()
    user = User()
    session = DateSession()
    db.add(user)
    db.add(session)
    db.commit()

    prompt = Prompt(text=prompt_text, user_id=user.id, date_id=session.id)
    db.add(prompt)
    db.commit()

    completion = client.chat.completions.create(
        model=AZURE_DEPLOYMENT_NAME,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt_text}
        ],
        temperature=0.7
    )

    reply = completion.choices[0].message.content
    response = Response(prompt_id=prompt.id, text=reply)
    db.add(response)
    db.commit()

    return {"reply": reply}
