import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");

const sendMessage = async () => {
  if (!input.trim()) return;

  const userMessage = { sender: "user", text: input };
  setMessages(prev => [...prev, userMessage]);
  setInput("");

  try {
    const res = await axios.post("http://localhost:8000/chat", { message: input });
    const botMessage = { sender: "bot", text: res.data.reply };
    setMessages(prev => [...prev, botMessage]);
  } catch (error) {
    setMessages(prev => [...prev, { sender: "bot", text: "❌ Error: Failed to get response" }]);
    console.error("Axios Error:", error);
  }
};


  return (
    <div className="chat-container">
      <h2>Futuristic Chatbot</h2>
      <div className="chat-box">
        {messages.map((msg, idx) => (
          <div key={idx} className={`message ${msg.sender}`}>
            {msg.text}
          </div>
        ))}
      </div>
      <div className="input-container">
        <input value={input} onChange={e => setInput(e.target.value)} />
        <button onClick={sendMessage}>Send</button>
      </div>
    </div>
  );
}

export default App;