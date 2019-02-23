<template>
  <div id="larp-form">
    <InputField
      v-for="field in writableFields"
      v-bind:field="field"
      v-on:update="onChildUpdate"
    />
    <button type="button" v-on:click="sendForm">Send</button> 
  Props: {{values}}
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
      fields: [],
      values: {}
    }
  },
  computed: {
    writableFields: function () {
      return Object.values(this.fields).filter(f => f.read_only === false);
      //TODO: change to dict, and identify by id not labels
    }

  },
  async mounted () {
    const response = await axios.options('http://localhost:8000/api/larps/')
      .catch(err => console.error(err))
    this.fields = response.data.actions.POST
  },
  methods: {
    onChildUpdate (child, newValue) {
      this.$set(this.values, child, newValue)
    },
    async sendForm () {
      const response = axios.post('http://localhost:8000/api/larps/', this.values)
        .catch(err => console.error(err))
      console.log(response)
    }
  }
}
</script>

<style>
</style>