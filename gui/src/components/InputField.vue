<template>
  <p>
    <label v-bind:for="field.name"> {{field.label}} </label>
    <input 
      v-bind:id="field.name"
      v-bind:type="typeMappings[field.type]"
      v-bind:required="field.required"
      v-model="value"
      v-on:change="$emit('update', field.name, $event.target._value)"
    />
  </p>
</template>

<script>
export default {
  name: 'InputField',
  props: ['field'],
  data() {
    return {
      typeMappings : {
        "integer": "number",
        "string": "text",
        "url": "url",
        "image upload": "file",
        "datetime": "datetime-local"
      },
      value: ""
    }
  }
}
</script>