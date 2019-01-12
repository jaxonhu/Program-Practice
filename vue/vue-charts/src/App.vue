<template>
  <div id="app">
    <Chart id="test"/>
    <img src="./assets/logo.png">
    <router-view/>
  </div>
</template>

<script>

import Chart from './components/charts'

export default {
  name: 'App',
  data () { null },
  components: {
    Chart
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
