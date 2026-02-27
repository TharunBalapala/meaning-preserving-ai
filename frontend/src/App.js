import React, { useState } from "react";
import axios from "axios";

function App() {
  const [message, setMessage] = useState("");
  const [chat, setChat] = useState([]);

  const sendMessage = async () => {
    if (!message.trim()) return;

    const userMessage = { sender: "user", text: message };
    setChat([...chat, userMessage]);

    try {
      const res = await axios.post("http://127.0.0.1:8000/chat", {
        message: message,
      });

      const botMessage = { sender: "bot", text: res.data.reply };
      setChat(prev => [...prev, botMessage]);
    } catch (error) {
      console.error(error);
    }

    setMessage("");
  };

  return (
    <div style={styles.container}>
      <h2>Meaning Preserving AI</h2>

      <div style={styles.chatBox}>
        {chat.map((msg, index) => (
          <div
            key={index}
            style={
              msg.sender === "user"
                ? styles.userMessage
                : styles.botMessage
            }
          >
            {msg.text}
          </div>
        ))}
      </div>

      <div style={styles.inputContainer}>
        <input
          style={styles.input}
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          placeholder="Type your message..."
        />
        <button style={styles.button} onClick={sendMessage}>
          Send
        </button>
      </div>
    </div>
  );
}

const styles = {
  container: {
    width: "600px",
    margin: "50px auto",
    fontFamily: "Arial",
  },
  chatBox: {
    border: "1px solid #ddd",
    padding: "10px",
    height: "400px",
    overflowY: "scroll",
    marginBottom: "10px",
  },
  userMessage: {
    textAlign: "right",
    margin: "5px",
    background: "#d1e7dd",
    padding: "8px",
    borderRadius: "10px",
  },
  botMessage: {
    textAlign: "left",
    margin: "5px",
    background: "#f8d7da",
    padding: "8px",
    borderRadius: "10px",
  },
  inputContainer: {
    display: "flex",
  },
  input: {
    flex: 1,
    padding: "10px",
  },
  button: {
    padding: "10px 15px",
  },
};

export default App;