<template>
  <section class="space-y-6">
    <PdfToText />
    <ImageToPng />
  </section>
</template>
<script setup>
import PdfToText from "../components/PdfToText.vue";
import ImageToPng from "../components/ImageToPng.vue";
</script>