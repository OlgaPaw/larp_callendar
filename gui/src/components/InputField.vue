<template>
  <p>
    <label v-bind:for="field.label"> {{field.label}} </label>
    <input v-bind:id="field.label" v-bind:type="field.type" v-bind:required="field.required"/>
  </p>
</template>

<script>
export default {
  name: 'InputField',
  props: ['field'],
}
</script>