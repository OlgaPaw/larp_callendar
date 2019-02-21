<template>
  <div id="larp-form">
   <InputField v-for="field in writableFields" v-bind:field="field"/>
  </div>
</template>

<script>
import axios from 'axios'
import InputField from './InputField.vue'

export default {
  name: 'LarpForm',
  components: {
    InputField,
  },
  data() {
    return {
      fields: []
    }
  },
  computed: {
     writableFields: function () {
      return Object.values(this.fields).filter(f => f.read_only === false);
    }
  },
  async mounted () {
    const response = await axios.options('http://localhost:8000/api/larps/')
      .catch(err => console.error(err))
    this.fields = response.data.actions.POST
  },
  methods: {
  },
}
</script>

<style>
</style>