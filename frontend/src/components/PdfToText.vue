<template>
  <div>
    <input type="file" @change="onFile" accept="application/pdf" />
    <button @click="convert">Convert</button>
    <pre>{{ text }}</pre>
  </div>
</template>
<script setup>
import { ref } from "vue";
const file = ref();
const text = ref("");
const onFile = e => (file.value = e.target.files[0]);
const convert = async () => {
  text.value = "";
};
</script>