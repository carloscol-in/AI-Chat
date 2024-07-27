<!-- <template>
  <p
    class="Message mb-10 text-zinc-200 rounded-3xl py-3 px-6"
    :class="classes"
  >
    <VueMarkdown
      :source="text"
    ></VueMarkdown>
  </p>
</template>

<script setup>
import VueMarkdown from 'vue-markdown'

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
</style> -->