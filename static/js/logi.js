// script.js
document.getElementById('send-button').addEventListener('click', function() {
    const userInput = document.getElementById('user-input').value.trim();
    if (userInput !== '') {
      addMessage('user', userInput);  // Display user message
      getChatGPTResponse(userInput);   // Get response from ChatGPT
    }
    document.getElementById('user-input').value = '';  // Clear input box
  });
  
  function addMessage(sender, message) {
    const chatBox = document.getElementById('chat-box');
    const messageElement = document.createElement('div');
    messageElement.classList.add('message', sender === 'user' ? 'user-message' : 'bot-message');
    messageElement.textContent = message;
    chatBox.appendChild(messageElement);
    chatBox.scrollTop = chatBox.scrollHeight;  // Scroll to the bottom
  }
  
  function getChatGPTResponse(userMessage) {
    // Simulating an API call to ChatGPT (replace this with actual API request)
    setTimeout(() => {
      const botResponse = "This is a simulated ChatGPT response: " + userMessage;
      addMessage('bot', botResponse);  // Display bot message
    }, 1000);
  }
  