<template>
  <p
    class="Message mb-10 text-zinc-200 rounded-3xl py-3 px-6"
    :class="classes"
  >
    <MDC
      :value="text"
    >
    </MDC>
  </p>
</template>

<script setup>
const props = defineProps({
  text: {
    type: String,
    default: '',
  },
  from: {
    type: String,
    default: 'model'
  }
})

const {
  text,
} = toRefs(props)
const markdownItOptions = {
  // Enable HTML tags in source
  html: true,

  // Use '/' to close single tags (<br />).
  // This is only for full CommonMark compatibility.
  xhtmlOut: false,

  // Convert '\n' in paragraphs into <br>
  breaks: true,

  // CSS language prefix for fenced blocks. Can be
  // useful for external highlighters.
  langPrefix: 'language-',

  // Autoconvert URL-like text to links
  linkify: false,
}

const classes = ref('Message-Sent')

onMounted(() => {
  classes.value = props.from === 'user' ? 'Message-Sent' : 'Message-Received'
})
</script>

<style scoped>
.Message-Sent {
  width: 80%;
  float: right;
  background-color: #101320;
  border: solid 0.1rem #000000;
}
</style>