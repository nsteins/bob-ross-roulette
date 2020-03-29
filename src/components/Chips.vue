<template>
    <v-row class="avatars">
        <v-avatar v-for="(value, name) in getBets" v-bind:key="name" :color="getChipColors[name]" size="36">
        <span class="white--text headline">{{value}}</span>
        </v-avatar>
    </v-row>
</template>

<script>
    import { mapState } from "vuex";

    export default {
        props: ['name', 'category'],
        computed: {
            ...mapState(['game', 'players']), 
            getBets() {
                var square = this.category + '_' + this.name
                if (square in this.game){
                    return this.game[square].bets;
                }
                else {
                    return [];
                }
            },
            getChipColors() {
                return Object.keys(this.players)
                        .reduce((obj, key) => {
                            obj[key] = this.players[key].color;
                            return obj;
                        }, {});
            } 
        }
    }
</script>

<style scoped>
    .avatars {
        position:absolute;
        bottom:0;
        margin-left:0;   
    }
</style>
