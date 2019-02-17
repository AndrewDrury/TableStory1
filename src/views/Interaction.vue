<template>
  <div class="interaction">
    <b-row>
      <b-col md=4>
        <video autoplay id="webcam"></video>
      </b-col>
      <b-col md=8 class="text-right">
        <div>
          <span>
            <p v-for="word in transcription">{{ word }}</p>
            <p>{{ runtimeTranscription }}</p>
          </span>
        </div>
      </b-col>
    </b-row>
  </div>
</template>

<style lang="scss">
@import url("/src/assets/main.scss");
</style>

<script>
export default {
  name: 'vue-speech',
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
    checkApi: function () {
      window.SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition
      if (!SpeechRecognition && process.env.NODE_ENV !== 'production') {
        throw new Error('Speech Recognition does not exist on this browser. Use Chrome or Firefox')
      }
      if (!SpeechRecognition) {
        return
      }
      const recognition = new SpeechRecognition()
      recognition.lang = this.lang
      recognition.interimResults = true
      recognition.addEventListener('result', event => {
        const text = Array.from(event.results)
          .map(result => result[0])
          .map(result => result.transcript)
          .join('')
        this.runtimeTranscription = text
      })
      recognition.addEventListener('end', () => {
        if (this.runtimeTranscription !== '') {
          this.transcription.push(this.runtimeTranscription)
          this.$emit('onTranscriptionEnd', {
            transcription: this.transcription,
            lastSentence: this.runtimeTranscription
          })
        }
        this.runtimeTranscription = ''
        recognition.start()
      })
      recognition.start()
    }
  },
  mounted () {
    this.checkApi()

    navigator.mediaDevices
      .enumerateDevices()
      .then(devices => {
        console.log(devices)
        // this is the webcam id of webcam. WILL NEED TO CHANGE THIS FOR THE LOGITECH WEBCAM
        let webcam = devices.filter(
          v =>
            v.deviceId ==
            'e475244503d345de8725c3dfab14230363442b16143e7da6212a68dd6640e04b'
        )[0]
        let mic = devices.filter(
          v =>
            v.deviceId ==
            'a11891fa0ad40f76ef3b21896c9afb54ce502971348678ad87cd554317c42d55'
        )[0]
        if (!webcam) {
          console.log('No web!')
          return
        } else {
          console.log(webcam)
        }

        let constraints = {
          audio: false,
          video: {
            deviceId: { ideal: webcam.deviceId },
            width: { ideal: window.innerWidth / 3 },
            height: { ideal: window.innerHeight }
          }
        }
        navigator.mediaDevices
          .getUserMedia(constraints)
          .then(stream => {
            const video = document.getElementById('webcam')
            video.srcObject = stream
            console.log('DONE')
          })
          .catch(err => {
            console.log(err.name + ': ' + err.message)
          })
      })
      .catch(err => {
        console.log(err.name + ': ' + err.message)
      })
  }
}
</script>
