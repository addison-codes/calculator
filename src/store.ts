// store.js
import { reactive } from 'vue'

export const store = reactive({
  calc: Array(),
  number: 0,
  hist: Array(),
  addValue(value) {
    if (isNaN(value)) {
      this.calc.push(Number(this.number), value)
      this.number = 0
      value === '=' ? (this.request(this.calc), this.clearCalc()) : ''
    } else {
      this.number === 0 ? value === '0' ? '' : this.number = value : this.number += value
      
    }
    console.log(this.calc)
  },
  clearCalc() {
    this.hist.push(this.calc)
    this.calc = Array()
  },
  request(req: Array<any>) {
    console.log('request', req)
    console.log('hist', this.hist)
  }
})
