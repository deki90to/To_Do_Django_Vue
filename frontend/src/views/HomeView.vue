<template>
  <div class="home">

    <NewTaskComponent />
    <TableComponent />
  
  </div>
</template>


<script>
  import TableComponent from '../components/TableComponent.vue';
  import NewTaskComponent from '../components/NewTaskComponent.vue';

  export default {
    components: {
      TableComponent,
      NewTaskComponent
    },
  }
</script>
