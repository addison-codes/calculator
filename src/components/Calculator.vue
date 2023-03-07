<script setup lang="ts">
import { defineComponent } from 'vue'
import { store } from '../store'
import CalcButton from './CalcButton.vue'
import CalcRow from './CalcRow.vue'

// Utilize app state via store
defineComponent({
  data() {
    return {
      store
    }
  },
})

</script>

<template>
  <!-- Define component layout with buttons -->
  <div class="mx-auto overflow-hidden max-w-sm mt-10 mb-2 bg-teal-900 shadow-lg border rounded-lg">
    <div class="pt-16 pb-16 mb-6 p-5 text-white text-right bg-teal-800 overflow-hidden">
      <!-- Show either current calculation in progress or the calculation that has been sent. -->
      <span class="text-sm">{{store.equals ? store.hist.slice(-1).toString().replaceAll(',', ' ') : store.calc.toString().replaceAll(',', ' ')}}</span>
      <br>
      <!-- Show either the user input, loading state, or the answer returned. -->
      <span class="text-3xl">{{store.loading ? 'Calculating...' : store.answer ? store.answer : store.number}}</span>
    </div>
      <CalcRow>
        <CalcButton :filled=false></CalcButton>  
        <CalcButton :filled=false></CalcButton>  
        <CalcButton :filled=false></CalcButton>  
        <CalcButton filled>÷</CalcButton>  
      </CalcRow>
      <CalcRow>
        <CalcButton filled>7</CalcButton>  
        <CalcButton filled>8</CalcButton>  
        <CalcButton filled>9</CalcButton>  
        <CalcButton filled>x</CalcButton>  
      </CalcRow>
      <CalcRow>
        <CalcButton filled>4</CalcButton>  
        <CalcButton filled>5</CalcButton>  
        <CalcButton filled>6</CalcButton>  
        <CalcButton filled>-</CalcButton>  
      </CalcRow>
      <CalcRow>
        <CalcButton filled>1</CalcButton>  
        <CalcButton filled>2</CalcButton>  
        <CalcButton filled>3</CalcButton>  
        <CalcButton filled>+</CalcButton>  
      </CalcRow>
      <CalcRow>
        <CalcButton :filled=false>AC</CalcButton>  
        <CalcButton filled>0</CalcButton>  
        <CalcButton filled>.</CalcButton>  
        <CalcButton filled>=</CalcButton>  
      </CalcRow>
      
  </div>

</template>
