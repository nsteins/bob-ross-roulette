<template>
    <v-col
     :cols = "name === 'Windows' ? false : 1">
        <v-card
        class="pa-2 title-card"
        outlined
        tile
        height="100%"
        > 
        <v-card-title class="justify-center" v-if="name === 'Windows'">{{name}}</v-card-title>
        <div class="title" v-else>{{name}}</div> 
        </v-card>
      </v-col>
</template>

<script>
export default {
    props: ['name']
}
</script>

<style scoped> 
    .title-card {
        background-color: #083f0b;
        color: #ffffff;
        outline: 3px solid #ffffff;
    }
    .title {
        writing-mode: vertical-lr;
        
    }
    .v-card__title {
        line-height: 0em;
        word-break: keep-all;
    }

</style>