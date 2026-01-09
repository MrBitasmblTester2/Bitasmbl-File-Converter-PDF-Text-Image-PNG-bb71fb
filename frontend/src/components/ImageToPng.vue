<template>
  <div>
    <input type="file" @change="onFile" accept="image/*" />
    <button @click="convert">Convert</button>
    <a v-if="url" :href="url">Download PNG</a>
  </div>
</template>
<script setup>
import { ref } from "vue";
const file = ref();
const url = ref("");
const onFile = e => (file.value = e.target.files[0]);
const convert = async () => {
  url.value = "";
};
</script>