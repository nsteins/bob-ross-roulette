<template>
  <v-fade-transition appear>
    <v-card>
      <v-card-text>
       
        <v-form v-model="userValid">
          <v-text-field label="Username" v-model="username" required></v-text-field>
          <color-picker v-on:colorUpdate='onColorUpdate'/>
          <v-btn block color="secondary" large 
                @click.stop="createGame" id="create-btn"
                :disabled="!userValid">Create Game</v-btn>
        </v-form>

        <div class="pa-4 ma-4"> <h2 class="text-center">or</h2> </div>

        <v-form v-model="roomValid">
          <v-text-field label="Enter Room ID" v-model="room_num" required solo light hide-details></v-text-field>
          <v-btn block color="secondary" large 
                @click.stop="joinGame"
                :disabled="(!userValid && !roomValid)">Join</v-btn>
          <v-alert type="error" :value="showInputError" transition="slide-y-reverse-transition">
            Room ID required to join.
          </v-alert>
        </v-form>

      </v-card-text>
    </v-card>
  </v-fade-transition>
</template>

<script>
import { mapState, mapMutations } from "vuex";
import ColorPicker from "./ColorPicker.vue"


export default {
  name: "create-form",
  components: {
    'color-picker': ColorPicker
  },
  data() {
    return {
      username: '',
      room_num: null,
      showInputError: false,
      rules: {
        required: value => !!value || "Required."
      },
      errors: [],
      userValid: false,
      roomValid: false,
      color: '#340876'
    };
  },
  computed: {
    ...mapState(['room']),
    room_id() {
      return this.room_num.toUpperCase();
    }
  },
  watch: {
    room() {
      this.set_room(this.room);
      this.$router.push({ name: 'Game', params: { room: this.room } });
    },
  },
  methods: {
    ...mapMutations(["set_player", "set_room"]),
    joinGame() {
      this.set_player({
        name: this.username,
        color: this.color
      });
      this.showInputError = false;
      if (this.room_num) {
        this.set_room(this.room_id);
        // This feels like it needs to be re-written
        this.$router.push({ name: "Game", params: { room: this.room_id } });
      } else {
        this.showInputError = true;
      }
    },
    createGame() {
      this.set_player({
        name: this.username,
        color: this.color
      });
      this.showInputError = false;
    //   Add username validation
      this.$socket.emit('create', {username: this.username, color: this.color});
    },
    onColorUpdate(value) {
      this.color = value;
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>