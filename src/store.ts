// store.js
import { reactive } from 'vue'
import axios from 'axios'

export const store = reactive({
  // Define pieces of state
  calc: Array(),
  number: 0,
  equals: false,
  loading: false,
  hist: Array(),
  answer: '',
  // Function to add a value to the calc array. Programmatically determines if input is a number or string (operator) and either appends the number to the number state or appends the number state to the calc array. If it detects an equals sign, it will send the axios request with the calc array as the payload

  // TODO: Parse decimals
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
  },
  // Function to clear the calc array and push the last item to a hist array (to keep all of the calculations)
  clearCalc() {
    this.hist.push(this.calc)
    this.calc = Array()
  },
  // Axios request that sends the calc array as a payload to Flask API at the /calc endpoint. I am logging the hist array to show that we could do something else with it. As the server will take the request array and iterate it down to a single answer value and return that array, we set the answer state to load the first item in the array
  request(req: Array<any>) {
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
