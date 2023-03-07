<script setup lang='ts'>
import { defineComponent } from 'vue'
import { store } from '../store'

defineComponent({
  data() {
    return {
      store
    }
  }
})

defineProps<{ filled: boolean }>()
</script>

<template>
  <div class="flex-1 px-2 py-2 justify-center flex items-center text-white text-2xl font-semibold cursor-pointer">
    <!-- Send value of button to the store -->
    <div @click='($event: Event) => store.addValue(($event.target as HTMLInputElement).outerText)' class='rounded-lg h-20 w-20 flex items-center justify-center shadow-lg border-2 border-teal-700 focus:outline-none' :class="filled ? 'hover:border-2 hover:border-gray-500 bg-teal-800' : 'bg-teal-900'">
      <slot></slot>
    </div>
  </div>
</template>

