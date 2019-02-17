<template>
  <div class="home">
    <b-container fluid class="verticalCenter">
      <b-row>
        <b-col>
          <h1 class="line-1 anim-typewriter">Hi! I am <strong>sli.ai</strong></h1>
          <transition
          <h2>I am a sign language interpreter.</h2>
          <h2>I use AI to help create seamless interactions!</h2>
          <h5 class="pt-4"><i>Sign or say <em>Start Conversation</em> to begin your experience.</i></h5>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<style lang="scss">
@import url("/src/assets/main.scss");
.verticalCenter {
  height: 100vh;

}
.row {
  padding-top: 25vh;
  align-self: center;
  margin: 0 auto;
}
h2{
  line-height: 4em;
}

em {
  color: #303030;
}

.line-1{
    position: relative;
    margin: 0 auto;
    border-right: 2px solid rgba(255,255,255,.75);
    font-size: 180%;
    text-align: center;
    white-space: nowrap;
    overflow: hidden;
    transform: translateY(-50%);
}

/* Animation */
.anim-typewriter{
  animation: typewriter 4s steps(20) 1s 1 normal both,
             blinkTextCursor 500ms steps(20) infinite normal;
}
@keyframes typewriter{
  from{width: 0;}
  to{width: 6em;}
}
@keyframes blinkTextCursor{
  from{border-right-color: rgba(255,255,255,.75);}
  to{border-right-color: transparent;}
}

</style>

<script>
import Vue from 'vue'
import HelloWorld from '@/components/HelloWorld.vue'

var recognition

export default Vue.extend({
  name: 'home',
  components: {
    HelloWorld
  },
  props: {
    lang: {
      type: String,
      default: 'en-US'
    }
  },
  data: () => ({
    runtimeTranscription: '',
    transcription: []
  }),
  methods: {
    onRec (event) {
      const text = Array.from(event.results)
        .map(result => result[0])
        .map(result => result.transcript)
        .join('')
      this.runtimeTranscription = text
    },
    onRecEnd () {
      if (this.runtimeTranscription !== '') {
        console.log(this.runtimeTranscription)
        if (this.runtimeTranscription.includes('start conversation')) {
          recognition.removeEventListener('result', this.onRec)
          recognition.removeEventListener('end', this.onRecEnd)
          this.$router.push('interaction')
        }
        this.transcription.push(this.runtimeTranscription)
        this.$emit('onTranscriptionEnd', {
          transcription: this.transcription,
          lastSentence: this.runtimeTranscription
        })
      }
      this.runtimeTranscription = ''
      recognition.start()
    },
    checkApi: function () {
      window.SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition
      if (!SpeechRecognition && process.env.NODE_ENV !== 'production') {
        throw new Error('Speech Recognition does not exist on this browser. Use Chrome or Firefox')
      }
      if (!SpeechRecognition) {
        return
      }
      recognition = new SpeechRecognition()
      recognition.lang = this.lang
      recognition.interimResults = true
      recognition.addEventListener('result', this.onRec)
      recognition.addEventListener('end', this.onRecEnd)
      recognition.start()
    }
  },
  mounted () {
    this.checkApi()
  }

})

</script>
