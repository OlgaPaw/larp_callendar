<template>
  <div id="app">
    <Calendar></Calendar>
    <LarpForm></LarpForm>
  </div>
</template>

<script>
import Calendar from './components/Calendar.vue'
import LarpForm from './components/LarpForm.vue'

export default {
  name: 'app',
  components: {
    Calendar,
    LarpForm
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
  height: 90vh;
}
</style>
