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
            placeholder="Write your message..."
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

  const emit = defineEmits(['firstMessage', 'newImage'])
  const userInput = ref('')
  const messages = ref([
    { text: 'Hello! What do you want to know about the graph?', sender: 'bot' }
  ])
  const messageContainer = ref<HTMLElement | null>(null)
  const hasUserSentMessage = ref(false)

  const getBotResponse = async (userMessage: string) => {
    try {
      const response = await fetch('http://127.0.0.1:5001/send-image', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ message: userMessage })
      })

      if (!response.ok) {
        throw new Error('Network response was not ok')
      }

      const imageBlob = await response.blob()
      const imageUrl = URL.createObjectURL(imageBlob)
      emit('newImage', imageUrl)

      return 'I have generated a new visualization based on your request.'

    } catch (error) {
      console.error('Error:', error)
      return 'Sorry, there was an error generating the visualization.'
    }
  }

  const sendMessage = async () => {
    if (!userInput.value.trim()) return

    messages.value.push({
      text: userInput.value,
      sender: 'user'
    })

    if (!hasUserSentMessage.value) {
      hasUserSentMessage.value = true
      emit('firstMessage')
    }

    const userMessageText = userInput.value
    userInput.value = ''

    messages.value.push({
      text: 'Generating visualization...',
      sender: 'bot'
    })

    const botResponse = await getBotResponse(userMessageText)
    messages.value[messages.value.length - 1].text = botResponse
  }

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
    width: 100%;
    max-width: 650px;
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