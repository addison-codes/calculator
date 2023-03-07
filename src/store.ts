// store.js
import { reactive } from 'vue'
import axios from 'axios'

export const store = reactive({
  calc: Array(),
  number: 0,
  equals: false,
  loading: false,
  hist: Array(),
  answer: '',
  addValue(value) {
    if (isNaN(value)) {
      // value === '.' ? 
      this.calc.push(Number(this.number), value)
      this.number = 0
      value === '=' ? (this.loading = true, this.request(this.calc), this.clearCalc(), this.equals = true) : ''
    } else {
      this.answer = ''
      this.number === 0 ? value === '0' ? '' : (this.equals = false, this.number = value) : (this.equals = false, this.number += value)
      
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
    const path = 'http://localhost:5000/calc'
      axios.post(path, this.calc)
      .then( (res) => {
        console.log(res)
        this.loading = false
        this.answer = res.data.answer[0]
      })
      .catch((error) => {
        console.error(error)
      })
  }
})
