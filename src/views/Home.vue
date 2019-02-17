<template>
  <div class="home">
    <b-container fluid class="p-0 verticalCenter">
      <b-row>
        <b-col>
          <h1 class="pb-4">Hi! I am --------.</h1>
          <h2>I am an ASL interpreter.</h2>
          <h2>I can help create seamless interactions!</h2>
          <h5 class="pt-4">Say or sign <strong>'Start Conversation'</strong> to begin your experience.</h5>
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

