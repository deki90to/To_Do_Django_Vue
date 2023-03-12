<template>
  <form @submit.prevent="task_create()">
    <input type="text" id="new_task_field" name="task" placeholder="Type new task here..." v-model="data.task"> 
    <button id="new_task_save_btn"> Save </button> <br><br>
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

<style>
  #new_task_field {
    padding: 10px;
    border: 0px solid grey;
    border-radius: 10px;
    width: 50vw;
    box-shadow: 2px 2px 5px 0px grey;
  }
  #new_task_save_btn {
    margin-left: 10px;
    padding: 10px;
    border: 0;
    border-radius: 5px;
    box-shadow: 2px 2px 5px 0px grey;
  }
</style>