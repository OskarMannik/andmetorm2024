<template>
  <div class="chat-container">
    <div class="chat-window">
      <div class="chat-messages" ref="messageContainer">
        <div v-for="(message, index) in messages" 
             :key="index" 
             :class="['message', message.sender]">
          {{ message.text }}
        </div>
      </div>

      <div class="chat-input">
        <input 
          type="text" 
          v-model="userInput" 
          @keyup.enter="sendMessage"
          placeholder="Kirjuta oma küsimus..."
          class="input-placeholder"
        >
        <button @click="sendMessage">
          <span>➤</span>
        </button>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, watch } from 'vue'

// User input is stored in this reactive ref
const userInput = ref('')

// Chat history is stored in this reactive ref array
const messages = ref([
  { text: 'Tere! Kuidas saan teid aidata?', sender: 'bot' }
])

// Ref for auto-scrolling
const messageContainer = ref<HTMLElement | null>(null)

const getBotResponse = (userMessage: string) => {
  const lowerMessage = userMessage.toLowerCase()
  
  if (lowerMessage.includes('tere') || lowerMessage.includes('hello')) {
    return 'Tere! Kuidas saan teid aidata?'
  }
  else if (lowerMessage.includes('abi') || lowerMessage.includes('help')) {
    return 'Mida soovite teada?'
  }
  else if (lowerMessage.includes('veekasutus')) {
    return 'Veekasutuse kohta leiate infot veekasutuse lehelt.'
  }
  else if (lowerMessage.includes('pinnavesi')) {
    return 'Pinnavee võtu kohta leiate infot pinnavee võtu lehelt.'
  }
  else {
    return 'Vabandust, ei saanud teie küsimusest aru. Palun proovige teisiti küsida.'
  }
}

const sendMessage = () => {
  if (!userInput.value.trim()) return

  // Add user message to messages array in memory
  messages.value.push({
    text: userInput.value,
    sender: 'user'
  })

  // Get and add bot response to messages array
  setTimeout(() => {
    const botResponse = getBotResponse(userInput.value)
    messages.value.push({
      text: botResponse,
      sender: 'bot'
    })
  }, 500)

  // Clear input after sending
  userInput.value = ''
}

// Auto-scroll to bottom when new messages arrive
watch(() => messages.value.length, () => {
  setTimeout(() => {
    if (messageContainer.value) {
      messageContainer.value.scrollTop = messageContainer.value.scrollHeight
    }
  }, 100)
})
</script>

<style scoped>
.chat-container {
  font-family: 'Poppins', sans-serif;
  height: 50%;
  width: 100%; /* Changed from fixed 500px to 100% */
  max-width: 650px; /* Added max-width to maintain size on larger screens */
  margin: 20px auto;
  background-color: #1A2D42;
  color: #C0C8CA;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0,0,0,0.1);
}

.chat-window {
  width: 100%;
  height: 100%;
  background-color: #2E4156;
  color: #C0C8CA;
  display: flex;
  flex-direction: column;
  border-radius: 8px;
}


.chat-messages {
  flex: 1;
  padding: 20px;
  overflow-y: auto;
  display: flex;
  flex-direction: column;
  gap: 12px;
  color: #C0C8CA;
  background-color: #2E4156;
  border-radius: 15px;
}

.message {
  padding: 10px 15px;
  border-radius: 15px;
  max-width: 85%;
  word-wrap: break-word;
  font-size: 0.95rem;
  color: #C0C8CA;
  line-height: 1.4;
}

.message.user {
  background-color: #1A2D42;
  color: #C0C8CA;
  align-self: flex-end;
  border-bottom-right-radius: 5px;
}

.message.bot {
  background-color: #1A2D42;
  color: #C0C8CA;
  align-self: flex-start;
  border-bottom-left-radius: 5px;
  box-shadow: 0 1px 2px rgba(0,0,0,0.1);
}

.chat-input {
  padding: 15px;
  display: flex;
  gap: 10px;
  color: #C0C8CA;
  background-color: #2E4156;
  border-radius: 0 0 8px 8px;
}

.chat-input input {
  font-family: 'Poppins', sans-serif;
  flex: 1;
  padding: 10px;
  color: #C0C8CA;
  background-color: #1A2D42;
  border-radius: 20px;
  outline: none;
  font-size: 0.95rem;
}

.chat-input input::placeholder {
  font-family: 'Poppins', sans-serif;
  color: #C0C8CA;
  opacity: 0.7;
}

.chat-input button {
  width: 40px;
  height: 40px;
  border-radius: 20px;
  background-color: #1A2D42;
  box-shadow: 0 2px 10px rgba(0,0,0,0.1);
  color: #C0C8CA;
  border: 2px solid #1e2a38;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: background-color 0.3s ease;
}

.chat-input button:hover {
  background-color: #415c7a;
}

.chat-input button span {
  font-size: 1.2rem;
}
</style> 