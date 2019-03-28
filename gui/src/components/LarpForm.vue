<template>
  <div id="larp-form">
    <InputField
      v-for="field in writableFields"
      v-bind:field="field"
      v-on:update="onChildUpdate"
    />
    <button type="button" v-on:click="sendForm">Send</button>
  {{status}}
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
      values: {},
      status: ""
    }
  },
  computed: {
    writableFields: function () {
      var writables = [];
      var keys = Object.keys(this.fields);
      keys.forEach(key => {
        if (this.fields[key].read_only === false){
          writables.push({...this.fields[key], name: key});
        }
      });
      return writables;
    }

  },
  async mounted () {
    const response = await axios.options('http://localhost:8000/api/larps/')
      .catch(err => console.error(err))
    this.fields = response.data.actions.POST;
  },
  methods: {
    onChildUpdate (child, newValue) {
      this.$set(this.values, child, newValue)
    },
    async sendForm () {
      const response = axios.post('http://localhost:8000/api/larps/', this.values)
        .catch(err => this.status = "Error")
      this.status = "Larp entry created"
    }
  }
}
</script>

<style>
</style>