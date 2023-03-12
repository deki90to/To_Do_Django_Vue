<template>
  <div v-for="task in tasks" v-bind:key="task.id">
    <table>
      <tr>
        <th>

          <div v-if="!task.editable">{{ task.task }}</div>
          <div v-else>
            <input type="text" v-model="task.task_edit">
            <button v-on:click="update_task(task)">Save</button>
          </div>

          <div style="float: right;">
            <button v-on:click="edit_task(task)"> ✎ </button>
            <button id="delete_task_btn" v-on:click="delete_task(task.id, task.task)"> 🗸 </button>
          </div>
        </th>
      </tr>
    </table>
  </div>
</template>
  

<script>
  import axios from 'axios'

  export default {
    data() {
      return {
        tasks: []
      }
    },
    mounted() {
      axios.get('http://localhost:8000/')
      .then(response => {
        this.tasks = response.data
        this.tasks.forEach(task => {
          task.editable = false
          task.task_edit = task.task
        })
      })
      .catch(error => {
        console.log(error.message)
      })
    },
    methods: {
      delete_task(id, taskName) {
        if (confirm("'" + taskName + "'" + " done?")) {
          axios.delete('http://localhost:8000/task_delete/' + id + '/')
          .then(
            window.location.reload()
            // console.log(response)
          )
          .catch(error => 
            console.log(error.message)
          )
        }
      },
      edit_task(task) {
        task.editable = true
      },
      update_task(task) {
        if (confirm("Edit '" + task.task + "'?")) {
          axios.put('http://localhost:8000/task_edit/' + task.id + '/', {
            task: task.task_edit
          })
          .then(response => {
              task.editable = false
              task.task = task.task_edit
              console.log(response)
            })
          .catch(error => {
            console.log(error.message)
          })
        }
      }
    },
  }
</script>

  
<style>
  table {
    font-family: arial, sans-serif;
    width: 100%;
  }
  td, th {
    border: 1px solid #eaeaea;
    text-align: left;
    padding: 10px 0px 0px 10px;
    border-radius: 10px;
    border: 0px;
    /* box-shadow: 1px 1px 5px 0px lightgoldenrodyellow; */
    background-color: lightcyan;
  }
  tr:nth-child(even) {
    background-color: #eaeaea;
  }
  #delete_task_btn {
    width: 30vw;
    margin-left: 5px;
    background-color: grey;
    color: white;
    border: 0px;
    border-radius: 5px;
    padding: 5px;
  }
</style>