<template>
  <div class="home">
    <v-form v-model="valid">
          <v-text-field
            v-model="name"
            :counter="10"
            label="Name"
            required
          ></v-text-field>
          <v-btn @click="createPlayer()">Create Player</v-btn>
        
    </v-form>
    <button v-on:click="getPlayers()">Get Players</button>
    <p>Players</p>
    <ul id='player-list'>
      <li v-for="player in players" :key="player.name">
        {{ player.name }}
      </li>
    </ul>

  </div>
</template>

<script>
// @ is an alias to /src


export default {
  name: 'Players',
  components: {
  },
  data () {
    return {
      players: [],
      name: ''
    }
  },

  methods: {
    getPlayers() {
      this.axios.get('/players')
      .then(
        response => {
          this.players = response.data.players
        }
      )
      .catch(
        error => {
          console.log(error)
        }
      )
    },

    createPlayer() {
      this.axios.post('/players', {'name':this.name})
      .then(
        response => {
          this.players = response.data.players
        }
      )
      .catch(
        error => {
          console.log(error)
        }
      )
    }


  }
}
</script>
