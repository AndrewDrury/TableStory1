<template>
  <div class="interaction">
		<b-container fluid class="">
			<b-row>
				<b-col md=4>
					<video ref="video" id="webcam" width="640" height="480" autoplay></video>
					<canvas ref="canvas" id="canvas" width="640" height="480"></canvas>
					<b-btn id="snap" v-on:click="capture()">Snap Photo</b-btn>
					<ul>
							<li v-for="c in captures">
									<img v-bind:src="c" height="50" />
							</li>
					</ul>
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
		</b-container>
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
		transcription: [],
		captures: []
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
		},
		capture() {
			this.canvas = this.$refs.canvas;
			var context = this.canvas.getContext("2d").drawImage(document.getElementById("webcam"), 0, 0, document.getElementById("webcam").width, document.getElementById("webcam").height);
			this.captures.push(canvas.toDataURL("image/png"));
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
            'c5f9e26a7872c93b123bfa7023baecee3984356658c573d6c7e24f4e07e8b3c0'
        )[0]
        let mic = devices.filter(
          v =>
            v.deviceId ==
            'a54f598b6bedb363b459c7158a4563025f11910198f2456bb4f9fe72537ce601'
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
            width: { ideal: window.innerWidth },
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
