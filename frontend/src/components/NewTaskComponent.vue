<template>
  <h3> Add new task </h3>
  <form @submit.prevent="task_create()">
    <input type="text" name="task" placeholder="Type new task here..." v-model="data.task"> 
    <button> Save </button> <br><br>
  </form>
</template>


<script>
  import axios from 'axios'

  export default {
    data() {
      return {
        data: {
          task: ''
        }
      }
    },
    methods: {
      task_create() {
        axios.post('http://localhost:8000/task_create/', this.data)
        .then(response => {
          this.task = response.data
        })
        .then(
          window.location.reload()
        )
        .catch(error =>{
          console.log(error.message)
        })
      }
    }
  }
</script>