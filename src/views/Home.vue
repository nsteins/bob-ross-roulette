<template>
  <v-layout align-start justify-center text-xs-center row wrap>
    <v-flex lg4 md5 sm6 xs12>
      <v-avatar tile size="128">
      </v-avatar>
      <h1 class="cn-text">Bob Ross Roulette</h1>
      <v-alert
        :value="false"
        type="warning"
        outlined
      >
        If you experience issues, please try refreshing the page.
      </v-alert>
      
      <join-form></join-form>
      
    </v-flex>
  </v-layout>
</template>

<script>
import JoinForm from "../components/JoinForm";
export default {
  name: 'Home',
  components: {
    JoinForm
  },
}
</script>