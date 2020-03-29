<template>
  <v-row>
    <v-col cols=2>
      <Toolbar/>
    </v-col>
    <v-col>
      <Table />
    </v-col>
  </v-row>
</template>




<script>
import Table from "../components/Table";
import Toolbar from "../components/Toolbar";

import { mapState, mapMutations } from 'vuex';

export default {
  name: 'Game',
  components: {
    Table,
    Toolbar
  },
  computed: {
    ...mapState(['room', 'username', 'chip_color']),
    role() {
      return this.$route.name;
    },
  },
  mounted() {
    if (!this.username) this.set_username('#unknown');
    if (!this.room) this.set_room(this.$route.params.room);
    const params = {
      username: this.username,
      color: this.chip_color,
      room: this.room,
    };
    this.$socket.emit('join', params);
  },
  methods: {
    ...mapMutations(['set_room', 'set_username']),
  },
}
</script>

