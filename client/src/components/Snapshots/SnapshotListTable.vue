<template>
  <v-data-table
    :headers="headers"
    :items="snapshots"
    class="elevation-1 snapshots-list-table"
    item-key="id"
    :rows-per-page-items="[30, 100, 200]"
  >
    <template v-slot:items="props">
      <tr>
        <td>{{ props.item.snapshot }}</td>
        <td>{{ props.item.state }}</td>
        <td>{{ props.item.start_time.split(":")[0] }}</td>
        <td>{{ parseInt(props.item.duration_in_millis / 1000) }}</td>
        <td>
          <v-btn flat icon small @click="$emit('restore', props.item)">
            <v-icon small>arrow_downward</v-icon>
          </v-btn>
        </td>
      </tr>
    </template>
  </v-data-table>
</template>

<script>
export default {
  props: {
    snapshots: {
      type: Array,
      required: true
    }
  },
  data() {
    return {
      headers: [
        { text: "Id", value: "snapshot" },
        { text: "State", value: "state" },
        { text: "Time", value: "start_time" },
        { text: "Took", value: "duration_in_millis" },
        { text: "Actions", value: "duration_in_millis" }
      ]
    };
  }
};
</script>

<style>
.snapshots-list-table table.v-table tbody td {
  padding: 0 !important;
  padding-left: 5px !important;
}
.snapshots-list-table table.v-table thead th {
  padding: 0 !important;
  padding-left: 5px !important;
}
.snapshots-list-table table.v-table tbody td {
  height: 24px;
  line-height: 24px;
  text-align: left;
}

.snapshots-list-table table.v-table thead th {
  height: 50px;
  line-height: 50px;
  font-size: 14px;
  text-align: center;
}
</style>
