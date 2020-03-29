import Vue from 'vue';
import Vuex from 'vuex';
import VuexPersist from 'vuex-persist';

const vuexLocalStorage = new VuexPersist({
  key: 'vuex', // The key to store the state on in the storage provider.
  storage: window.localStorage, // or window.sessionStorage or localForage
  // Function that passes the state and returns the state with only the objects you want to store.
  reducer: state => ({
    'room': state.room,
    'username': state.username,
    'chip_color': state.chip_color
  })
  // Function that passes a mutation and lets you decide if it should update the state in localStorage.
  // filter: mutation => (true)
})

Vue.use(Vuex);


var board_squares =  ['Trees_None','Trees_Both','Trees_Deciduous','Trees_Coniferous',
        'Features_Grass','Features_River','Features_Lake','Features_Boulders',
    'Features_Clouds','Features_Sun','Features_Ocean','Features_Night',
    'Mountains_None','Mountains_Snow Capped','Mountains_1','Mountains_2',
    'Manmade_Any','Manmade_Fence','Manmade_Bridge','Manmade_Human','Manmade_Cabin',
    'Windows_0','Windows_1','Windows_2',
    'Isms_Happy accidents',"Isms_Let's get crazy","Isms_It's your world",
    "Isms_Dark to show the light","Devils_0","Devils_1",'Devils_2+','Weird Frame_Weird Frame'];

export default new Vuex.Store({
  state: {
    game: {},
    username: '',
    chip_color: 'indigo',
    players: {},
    connected: false,
    room: '',
    error: null,
    admin: '',
    isStarted: false
  },
  getters: {
    getChips(state) {
      if (state.username in state.players){
        return state.players[state.username].chips;
      }
      else {
        return 0;
      }
    },
    isAdmin(state) {
      return state.username === state.admin;
    }

  },
  mutations: {
    init_game(state){
        let game_dict = {};
        board_squares.forEach(element => {
            game_dict[element] = {
                bets: [],
                payout: false
            }
        });
        state.game = game_dict;
    },
    set_player(state, player_data){
      state.username = player_data.name;
      state.chip_color = player_data.color;
    },
    set_room(state, room_id){
      state.room = room_id;
    },
    socket_connect(state) {
      state.connected = true;
    },
    socket_disconnect(state) {
      state.connected = false;
    },
    socket_message(state, message) {
      state.game = message.game_state;
      state.room = message.game_id;
      state.players = message.players;
      state.admin = message.admin;
      state.isStarted = message.is_started;
      state.error = null;
    },
    socket_join_room(state, message) {
      state.error = null;
      state.room = message.room;
    },
    socket_error(state, message) {
      state.error = message.error;
    },
  },
  actions: {
    reset_counter(context) {
      context.commit('set_counter', 0)
    },
    placeBet(context, bet) {
        context.commit('addBet', bet)
    },
  },
  plugins: [vuexLocalStorage.plugin]
});