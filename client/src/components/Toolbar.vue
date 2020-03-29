<template>

      <v-list
          dense
          nav
          class="py-0"
        >
        <v-list-item class='pt-4 pb-2'>
          <h3> Room ID: {{room}}</h3>
        </v-list-item>

        <div class='pt-2 pb-4 px-2'>
          <v-btn v-if="(!isStarted && isAdmin)" color="primary" @click="startRound()">Start Round</v-btn>
          <v-btn v-else-if="(isStarted && isAdmin)" color="secondary" @click="endRound()">End Round</v-btn>
        </div>
        <v-divider></v-divider>

        <v-list-item two-line class='px-0'>
          <v-list-item-avatar :color="chip_color" size="48">
            <v-icon v-if="isAdmin">mdi-crown</v-icon>
          </v-list-item-avatar>

          <v-list-item-content>
            <v-list-item-title>{{username}}</v-list-item-title>
            <v-list-item-subtitle>Chips: {{getChips}}</v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>


        <v-list-item v-for="player in otherPlayers" v-bind:key="player.name" two-line class='px-0'>
            <v-list-item-avatar :color="player.color" size="48">
              <v-icon v-if="player.admin">mdi-crown</v-icon>
            </v-list-item-avatar>
              
            <v-list-item-content>
              <v-list-item-title>{{player.name}}</v-list-item-title>
              <v-list-item-subtitle>Chips: {{player.chips}}</v-list-item-subtitle>
            </v-list-item-content>
          </v-list-item>
      </v-list>
</template>

<script>
import { mapState, mapGetters} from "vuex";

export default {
    name: "Toolbar",
    computed:{
        ...mapState(['room', 'username', 'chip_color', 'players', 'admin', 'isStarted']),
        ...mapGetters(['getChips','isAdmin']),
        otherPlayers (){
          return Object.keys(this.players)
            .filter(key => key !== this.username)
            .reduce((obj, key) => {
              let p = this.players[key];
              p['admin'] = (p.name === this.admin);
              obj[key] = p;
              return obj;
            }, {});
        }
    },
    methods: {
      startRound() {
        this.$socket.emit('start_round', {room: this.room});
      },
      endRound() {
        this.$socket.emit('end_round', {room: this.room});
      }
    }
}
</script>