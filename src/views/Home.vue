<template>
  <v-layout align-start justify-center text-xs-center row wrap>
    <v-flex lg4 md5 sm6 xs12>
      <div class="container">
        <img class="image" src="@/assets/bob_ross.png" alt="">
        <h1 class="centered">Bob Ross Roulette</h1>
      </div>

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

<style scoped>
.container {
  position: relative;
  text-align: center;
  color: white;
}
.centered {
  position: absolute;
  top: 50%;
  left: 50%;
  width: 200px;
  transform: translate(-50%, -50%);
}
.image {
    /* position: absolute; */
    /* left: 50%; */
    width: 250px;
    /* margin:-60px 0 0 -60px; */
    -webkit-animation:spin 4s linear infinite;
    -moz-animation:spin 4s linear infinite;
    animation:spin 4s linear infinite;
}
@-moz-keyframes spin { 100% { -moz-transform: rotate(360deg); } }
@-webkit-keyframes spin { 100% { -webkit-transform: rotate(360deg); } }
@keyframes spin { 100% { -webkit-transform: rotate(360deg); transform:rotate(360deg); } }
</style>