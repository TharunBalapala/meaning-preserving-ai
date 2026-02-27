const chatBox = document.getElementById("chat-box");

function addMessage(text, sender) {
    const messageDiv = document.createElement("div");
    messageDiv.classList.add("message", sender);
    messageDiv.innerText = text;
    chatBox.appendChild(messageDiv);
    chatBox.scrollTop = chatBox.scrollHeight;
}

async function sendMessage() {
    const input = document.getElementById("user-input");
    const text = input.value.trim();

    if (!text) return;

    addMessage(text, "user");
    input.value = "";

    addMessage("Processing...", "bot");

    try {
        const response = await fetch("http://127.0.0.1:8000/rewrite", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ text: text })
        });

        const data = await response.json();

        // Remove "Processing..."
        chatBox.removeChild(chatBox.lastChild);

        addMessage(data.rewritten_text, "bot");

    } catch (error) {
        chatBox.removeChild(chatBox.lastChild);
        addMessage("Error connecting to backend.", "bot");
        console.error(error);
    }
}