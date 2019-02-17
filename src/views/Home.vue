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

<script lang="ts">
import Vue from 'vue'
import HelloWorld from '@/components/HelloWorld.vue'

export default Vue.extend({
  name: 'home',
  components: {
    HelloWorld
  }

});


</script>

