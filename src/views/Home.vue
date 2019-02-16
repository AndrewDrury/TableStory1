<template>
  <div class="home">
    <b-container fluid class="p-0">
      <b-row>
        <b-col>
          <h2>Welcome to my site</h2>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<style lang="scss">
@import url("/src/assets/main.scss");
</style>


<script lang="ts">
import Vue from "vue";
import HelloWorld from "@/components/HelloWorld.vue";

export default Vue.extend({
  name: "home",
  components: {
    HelloWorld
  }
});
</script>
`