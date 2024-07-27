<template>
  <div class="Background">
    <div class="AppContainer mx-auto h-screen w-full flex flex-col justify-between">
      <div class="flex flex-col overflow-scroll mt-16">
        <div v-for="message in messages">
          <Message :key="message.id" :text="message.text" :from="message.from" />
        </div>

        <Message :text="response" from="model" />
      </div>
  
      <div class="PromptContainer mx-auto mb-6 backdrop-blur-md bg-blue-900/40 border border-2 border-blue-800 h-fit w-full p-1 rounded-full flex justify-between">
        <div class="flex justify-between h-full w-full">
          <input
            placeholder="Write your prompt"
            class="bg-transparent appearance-none outline-none h-full w-full box-border ml-4 mr-2 text-zinc-200"
            type="text"
            v-model="prompt"
          >
        </div>
  
        <button
          class="bg-blue-600 rounded-full"
          @click="sendMessage"
        >
          <div class="w-12 h-12 items-center content-center">
            <font-awesome
              icon="paper-plane"
              class="text-white"
            ></font-awesome>
          </div>
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
const messages = ref([])
const messagesLength = ref(messages.value.length)
const socket = ref(null)
const prompt = ref('')
// const prompt = ref('Implement a hello world function in Python.')
// const prompt = ref('Why does the sky look blue?')
const response = ref('')

const sendMessage = (e) => {
  e.preventDefault()

  socket.value.send(prompt.value)

  if (response.value !== '') {
    messages.value.push({ text: response.value, from: 'model', id: messagesLength.value + 1 })
    messagesLength.value += 1
  }

  messages.value.push({ text: prompt.value, from: 'user', id: messagesLength.value + 1 })
  messagesLength.value += 1

  prompt.value = ''
  response.value = ''
}

onMounted(() => {
  socket.value = new WebSocket('ws://localhost:8000/ws')

  socket.value.addEventListener("open", (event) => {})

  socket.value.onmessage = (msg) => {
    response.value += msg.data
  }
})
</script>

<style scoped>
.Background {
  background-color: #181818;
}
.AppContainer {
  object-fit: cover;
  background-size: cover;
  width: min(1000px, 95%);
}
.PromptContainer {
  width: min(600px, 95%);
}
</style>