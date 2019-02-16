<template>
  <div class="home">
    <b-container fluid class="p-0">
      <b-row class="height-50">
        <b-col
          sm=12
          md=6
        >
          <h2>
            Welcome to my site
          </h2>
        </b-col>
        <b-col
          sm=12
          md=6
        >
          <div
            style=" backgroundImage:url('/img/Portrait.jpeg') "
            class="h-100 w-100 d-block background-image"
          >
a
          </div>
          <!-- <img alt="Vue logo" src="../assets/General/Portrait.jpeg"> -->
          <!-- <HelloWorld msg="Welcome to Your Vue.js + TypeScript App"/> -->
        </b-col>
      </b-row>
      <b-row
        class="height-50"
        v-for="(page, key) in json"
        :key="page.id"
      >
        <b-col
          sm=12
          md=6
        >
          <a :href="'/project/' + key">
            <img
              :src="'/img' + page.featuredImage"
            />
          </a>
        </b-col>
        <b-col
          sm=12
          md=6
          class="dark"
        >
          <a :href="'/project/' + key">
            <h3>
              {{page.title}}
            </h3>
            <p>
              {{page.description}}
            </p>
          </a>
        </b-col>
      </b-row>


    </b-container>
  </div>
</template>

<style lang="scss">
img {
  width: 100%
}
.height-50 {
  min-height: 50vh;
  max-height: 80vh;
  background: black;
  color: white;
  a {
    color: white;
  }
}
.background-image {
  background-size: cover;
  background-position: center;
}
</style>


<script lang="ts">
import Vue from 'vue'
import HelloWorld from '@/components/HelloWorld.vue'
var json = require('@/static/content.json')
 // @ is an alias to /src

export default Vue.extend({
  name: 'home',
  components: {
    HelloWorld
  },
  data () {
    return {
      json: {}
    }
  },
  mounted () {
    this.json = json
    console.log(json)
  }
})
</script>
`