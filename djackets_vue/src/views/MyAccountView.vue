<template>
    <div class="page-my-account">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">My account</h1>
            </div>

            <div class="column is-12">
                <button @click="logout()" class="button is-danger">Log out</button>
            </div>

            <hr>
        </div>
    </div>
</template>

<script>
import axios from 'axios'


export default {
    name: 'MyAccountView',
    components: {
        //OrderSummary
    },
    data() {
        return {
            orders: []
        }
    },
    mounted() {
        document.title = 'My account | Djackets'

        this.getMyOrders()
    },
    methods: {
        logout() {
            axios.defaults.headers.common["Authorization"] = ""

            localStorage.removeItem("token")
            localStorage.removeItem("username")
            localStorage.removeItem("userid")

            this.$store.commit('removeToken')

            this.$router.push('/')
        },
        async getMyOrders() {
            this.$store.commit('setIsLoading', true)

            await axios
                .get('/api/v1/orders/')
                .then(response => {
                    this.orders = response.data
                })
                .catch(error => {
                    console.log(error)
                })

            this.$store.commit('setIsLoading', false)
        }
    }
}
</script>