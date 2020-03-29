<template>
    <v-row justify="center" align="center">
            <v-col cols=4>
              <label>Chip color</label>
            </v-col>
			<v-col style="min-width: 220px;">
				<!-- <v-text-field v-model="dummy" hide-details class="ma-0 pa-0" solo> -->
					<!-- <template v-slot:append> -->
						<v-menu v-model="menu" top nudge-bottom="105" nudge-left="16" :close-on-content-click="false">
							<template v-slot:activator="{ on }">
								<div :style="swatchStyle" v-on="on" />
							</template>
							<v-card>
								<v-card-text class="pa-0">
									<v-color-picker v-model="color" flat hide-inputs show-swatches/>
								</v-card-text>
							</v-card>
						</v-menu>
					<!-- </template> -->
				<!-- </v-text-field> -->
			</v-col>
		</v-row>
</template>

<script>

export default {
    name: "ColorPicker",
    data: () => ({
        menu: false,
        color: '#340876',
    }),
    computed: {
        swatchStyle() {
            const { color, menu } = this;
            this.$emit('colorUpdate', color);
            return {
                backgroundColor: color,
                cursor: 'pointer',
                height: '30px',
                width: '80%',
                float: 'right',
                borderRadius: menu ? '50%' : '4px',
                transition: 'border-radius 200ms ease-in-out'
            }
        }
    }
}
</script>