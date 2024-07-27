<template>
  <p
    class="Message mb-10 text-zinc-200 rounded-3xl py-3 px-6"
    :class="classes"
  >
    <VueMarkdown
      :source="text"
      :options="markdownItOptions"
      class="flex flex-col gap-4"
    />
  </p>
</template>

<script setup>
import VueMarkdown from 'vue-markdown-render'

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

<style>
.Message-Sent {
  width: 80%;
  float: right;
  background-color: #3d3b35;
  border: solid 0.1rem #584f00;
}

.Message-Received p > code,
.Message-Received li > code {
  background-color: #353535;
  color: #e3dfa6;
  padding: 0.25rem 0.75rem;
  border-radius: 0.35rem;
}

.Message-Received > div > pre {
  background-color: #000110;
  padding: 1rem;
  border: solid 1px #3c3c3c;
  border-radius: 0.75rem;
}
</style>