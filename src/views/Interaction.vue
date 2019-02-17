<template>
  <!-- <div class="interaction verticalCenter">
    <video autoplay id="webcam" class="d-flex align-items-start"></video>
		<b-btn v-on:click="capture">Screencap</b-btn>
  </div> -->

	<div id="interaction">
        <div><video ref="video" id="webcam" width="640" height="480" autoplay></video></div>
        <div><b-btn id="snap" v-on:click="capture()">Snap Photo</b-btn></div>
        <canvas ref="canvas" id="canvas" width="640" height="480"></canvas>
        <ul>
            <li v-for="c in captures">
                <img v-bind:src="c" height="50" />
            </li>
        </ul>
				<label>End of capture</label>
    </div>
	
</template>


<style lang="scss">
@import url("/src/assets/main.scss");
.verticalCenter {
  height: 100vh;
}
</style>

<script>
export default {
  data() {
		return {
			video: {},
			canvas: {},
			captures: []
		}
	},
	
  mounted: () => {
    navigator.mediaDevices.enumerateDevices().then( devices =>
		{
      console.log(devices)
      // this is the device id of webcam. WILL NEED TO CHANGE THIS FOR THE LOGITECH WEBCAM
			devices= devices.filter( v => (v.deviceId == "c5f9e26a7872c93b123bfa7023baecee3984356658c573d6c7e24f4e07e8b3c0")); 
			let device= devices[0];
			if( !device )
			{
				console.log("No devices!");
				return;
			} else {
        console.log(device)
      }
			
			let constraints =
			{
				audio: false, 
				video: {
					deviceId: { ideal: device.deviceId },
					width: { ideal: window.innerWidth },
					height: { ideal: window.innerHeight }
				}
			};
			navigator.mediaDevices.getUserMedia(constraints)
			.then( stream =>
			{
        const video = document.getElementById("webcam")
				video.srcObject = stream
				console.log("DONE");
			})
			.catch( err =>
			{
				console.log(err.name + ": " + err.message);
			});	
		})
		.catch( err =>
		{
			console.log(err.name + ": " + err.message);
		});
	},

	created() {
	},

	methods: {
		capture() {
			this.canvas = this.$refs.canvas;
			var context = this.canvas.getContext("2d").drawImage(document.getElementById("webcam"), 0, 0, document.getElementById("webcam").width, document.getElementById("webcam").height);
			this.captures.push(canvas.toDataURL("image/png"));
		}
	}
}
</script>
