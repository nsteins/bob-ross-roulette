<template>
    <v-row>
        <v-col>
            <v-btn @click="init_game()">Reset State</v-btn>
        </v-col>
        <v-col>
            {{username}}: {{getChips}}
        </v-col>
        <v-col>
            Room: {{room}}
        </v-col>

    </v-row>
</template>

<script>
import { mapState, mapGetters } from "vuex";

export default {
    computed:{
        ...mapState(['room', 'username']),
        ...mapGetters(['getChips'])
    }
}
</script>
