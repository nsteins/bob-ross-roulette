<template>
    <v-dialog
        v-model="dialog"
        width="500"
        >
    <template v-slot:activator="{ on }">
        <v-col>
            <v-card
                :class="'mx-auto cell ' + 'green darken-4'"
                outlined
                tile
                height="100%"
                v-on="on"
                > 
                <div v-if="isPaidOut && !(category == 'Devils')" class="bob">
                    <img class="bob_img" src='@/assets/bob_ross.png'/>
                </div>

                <v-card-title class="justify-center">{{name}}</v-card-title> 
                
                <div class="odds" v-if="!['Isms','Windows','Devils'].includes(category)">{{odds}}:1</div>
                
                <v-img 
                    v-if="img_src !== undefined"
                    :src="require(`@/assets/cell_pics/${img_src}`)" 
                    max-height="100px" max-width="100px"
                ></v-img>

                <div v-if="(category == 'Devils') && isPaidOut" class='wizard'><img src="@/assets/wizard.png" width='100px' /></div>    

                <Chips :name=name :category=category />

            </v-card>
        </v-col>
    </template>

    <v-card
        >
        <v-card-title
          class="headline light-green darken-4"
          primary-title
        >
          {{name}} [{{category}}] -- Place Bet
        </v-card-title>

        <v-container>
            <v-row justify="space-between">
                <v-col cols=8>
                    <v-card-title class='ps-2'>Payout is {{odds}}:1</v-card-title>
                    <v-form v-model="betValid">
                        <v-text-field
                            v-model="betValue"
                            label="Bet"
                            type="number"
                            class="ps-2"
                            :rules="[v => v>0 || 'Bet must be positive!',
                                    v => v<=getChips || 'Not enough chips for this bet']"
                        />
                    </v-form>
                </v-col>
                <v-col>
                    <v-img 
                        v-if="img_src !== undefined"
                        :src="require(`@/assets/cell_pics/${img_src}`)" 
                        max-height="100px" max-width="100px"
                        ></v-img>
                </v-col>
            </v-row>
            <v-row v-if='category === "Windows"'>
                <v-card-text>Betting on windows is only allowed after a cabin has been marked</v-card-text>
            </v-row>
        </v-container>

        <v-divider></v-divider>

        <v-card-actions>
        <v-btn
            v-if="(isAdmin && !isPaidOut && isStarted)"
            color="yellow lighten-1"
            text
            @click="markPayout(true); dialog = false"
            >
            Mark Payout
        </v-btn>
        <v-btn
            v-if="(isAdmin && isPaidOut && isStarted)"
            color="yellow lighten-1"
            text
            @click="markPayout(false); dialog = false"
            >
            Clear Payout
        </v-btn>
        <v-spacer></v-spacer>
        <v-btn
            color="red darken-4"
            v-if='hasBets'
            text
            :disabled="disableBetting"
            @click="submitBet(0); dialog = false"
        >
            Clear Bets
        </v-btn>
        <v-btn
            color="red darken-4"
            v-else
            text
            @click="dialog = false"
        >
            Cancel
        </v-btn>
        
        <v-btn
            color="primary"
            text
            :disabled="disableBetting"
            @click="submitBet(betValue); dialog = false"
        >
            Place Bet
        </v-btn>

        </v-card-actions>
      </v-card>
    </v-dialog>

</template>

<script>
import Chips from './Chips';

import { mapActions, mapState, mapGetters } from 'vuex';

export default {
    props: ['name', 'img_src', 'category'],
    components: {
        Chips
    },

    data () {
      return {
        dialog: false,
        betValue: 1,
        betValid: false
      }
    },
    computed:{
        ...mapState(['username','room','game', 'isStarted']),
        ...mapGetters(['getChips', 'isAdmin']),
        isPaidOut(){
            var key = this.category + '_' + this.name;
            if (key in this.game){
                return this.game[key].payout;
            } else {
                return false;
            }
        },
        hasBets(){
            var key = this.category + '_' + this.name;
            if (key in this.game){
                return this.username in this.game[key].bets;
            } else {
                return false;
            }
            
        },
        cellColor(){
            return (this.isPaidOut) ?  "red darken-4" : "green darken-4"
        },
        odds(){
            var key = this.category + '_' + this.name;
            if (key in this.game){
                return this.game[key].odds;
            } else {
                return 1;
            }
        },
        disableBetting(){
            // returns true when betting should be **disabled**
            var notAllowed
            if (this.category === 'Isms'){
                notAllowed = false;
            }
            else if (this.category === 'Windows'){
                // Betting on windows is only enabled once a cabin is marked
                notAllowed = !this.game['Manmade_Cabin'].payout;
            }
            else {
                notAllowed = this.isStarted;
            }
            return (!this.betValid || this.isPaidOut || notAllowed)
        }
    },
    methods: {
        ...mapActions(['placeBet']),
        submitBet (amount) {
            this.$socket.emit('bet',{ 
                room: this.room,
                square: this.category + '_' + this.name,
                username: this.username, 
                amount: parseInt(amount)
            });
        },
        markPayout (value) {
            this.$socket.emit('mark_payout',{ 
                room: this.room,
                square: this.category + '_' + this.name,
                payout: value
            });
        }
    }

}
</script>

<style scoped>
    .cell {
        outline: 3px solid #ffffff;
    }
    .v-image{
        margin: auto;
    }
    .odds {
        text-align: center;
        font-size: 1em;
        color: #f3ff47;
    }
    .v-card__title {
        line-height: 0em;
        /* color: #ffffff; */
        word-break: keep-all;
    }
    .dialog {
        background-color: #252525;
        color: #ffffff
    }
    .bob {
        position: absolute;
        z-index: 2;
        margin: auto;
        height: 100%;
    }
    .bob_img {
        display: block;
        margin-left: auto;
        margin-right: auto;
        height: 90%;
        width: 'auto';
        object-fit: contain;
    }
    .wizard {
        position: absolute;
        bottom: 0;
    }
    
</style>