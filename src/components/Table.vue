<template>
    
    <v-container class="green darken-4">
      
    <!-- First Row -->
    <v-row no-gutters>
      <Title name='Happy Trees'/>
      <Cell name='None' category='Trees' payout=10 img_src='none.png' />
      <Cell name='Deciduous' category='Trees' payout=2 img_src='deciduous.png' />
      <Cell name='Coniferous' category='Trees' payout=2 img_src='coniferous.png' />
      <Cell name='Both' category='Trees' payout=2 img_src='both.png' />
    </v-row>

    <!-- Second Row -->
    <v-row no-gutters>
      <Title name='Features'/>
      <v-col>
        <v-row no-gutters >
          <Cell name='Grass' category='Features' payout=2 img_src='grass.png' />
          <Cell name='River' category='Features' payout=3 img_src='river.png' />
          <Cell name='Lake' category='Features' payout=3 img_src='lake.png' />
          <Cell name='Boulders' category='Features' payout=3 img_src='boulder.png' />
        </v-row>
        <v-row no-gutters>
          <Cell name='Clouds' category='Features' payout=2 img_src='cloud.png' />
          <Cell name='Sun' category='Features' payout=3 img_src='sun.png' />
          <Cell name='Ocean' category='Features' payout=12 img_src='ocean.png' />
          <Cell name='Night' category='Features' payout=12 img_src='night.png' />
        </v-row>
      </v-col>
      <Title name='Mountains'/>
      <v-col>
        <v-row no-gutters >
          <Cell name='None' category='Mountains' payout=2 img_src='none.png' />
          <Cell name='Snow Capped' category='Mountains' payout=4 img_src='snow.png' />
        </v-row>
        <v-row no-gutters>
          <Cell name='1' category='Mountains' payout=4 img_src='one_mountain.png' />
          <Cell name='2+' category='Mountains' payout=4 img_src='two_mountains.png' />
        </v-row>
      </v-col>
    </v-row>

    <!-- Third Row -->
    <v-row no-gutters align="stretch">
      <v-col align-self-stretch>
        <v-row no-gutters>
          <Cell name='Any Manmade' category='Manmade' payout=4 />
        </v-row>
        <v-row no-gutters>
          <Cell name='Fence' category='Manmade' payout=12 img_src='fence.png' />
          <Cell name='Bridge' category='Manmade' payout=50 img_src='bridge.png' />
        </v-row>
        <v-row no-gutters>
          <Cell name='Human Figure' category='Manmade' payout=100 />
        </v-row>
      </v-col>

      <v-row no-gutters class="flex-column">
        <Cell name="Cabin" category='Manmade' payout=3 />
        <Title name="Windows"/>
        <v-row no-gutters class="d-flex child-flex">
          <Cell name="0" category='Windows' payout=2 />
          <Cell name="1" category='Windows' payout=2 />
          <Cell name="2" category='Windows' payout=2 />
        </v-row>
      </v-row>

      <Title name="All Bob Rossisms"/>

      <v-row no-gutters class="flex-column">
        <Cell name='Happy accidents' category='Isms' payout=2 />
        <Cell name="Let's get crazy" category='Isms' payout=2 />
        <Cell name="It's your world" category='Isms' payout=2 />
        <Cell name='Dark to show the light' category='Isms' payout=2 />
      </v-row>

    </v-row>

    <!-- Fourth Row -->
    <v-row no-gutters>
      <Title name="Beaten Devils"/>
      <Cell name="0" category='Devils' payout=2 />
      <Cell name="1" category='Devils' payout=2 />
      <Cell name="2+" category='Devils' payout=2 />
      <Cell name="Weird Frame" category='Weird Frame' payout=8 />
    </v-row>
  </v-container>
</template>

<script>
import Cell from "./Cell";
import Title from "./Title";


import { mapMutations } from 'vuex';

export default {
  name: 'Home',
  components: {
    Cell,
    Title,
  },
  methods: {
      ...mapMutations(['init_game'])
  }
}
</script>
