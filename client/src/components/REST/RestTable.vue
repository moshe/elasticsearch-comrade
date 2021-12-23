<template>
  <v-card>
    <v-card-title>
      overview
      <v-spacer></v-spacer>
      <v-text-field
        v-model="search"
        append-icon="mdi-magnify"
        label="Search"
        single-line
        hide-details
      ></v-text-field>
    </v-card-title>
    <v-data-table
      :headers="headers"
      :items="this.resultData"
      :search="search"
    ></v-data-table>
  </v-card>
</template>
<script>
import { mapState } from "vuex";

export default ({
    name: "RestTable",
    data(){
        return {
            search: "",
            headers: [],
        }
    },
    props: {
        resultData:{
            type: Array,
            default:()=> []
        }
    },
    created(){
       this.refreshTable(true)
    },
    destroyed() {
        clearTimeout(this.timeout);
    },
    computed: {
        ...mapState(["settingsRefreshEvery", "settingsRefreshEnabled"]),
    },
    methods:{
        getHeaders(){
           return Object.keys(this.resultData[0]).map(item=>({"text":item,"value":item}))
        },
        async refreshTable(force) {
            if (this.settingsRefreshEnabled || force) {
                this.headers = await this.getHeaders();
            }
            this.timeout = setTimeout(this.refreshTable, 400);
        }
        
    },
})
</script>
