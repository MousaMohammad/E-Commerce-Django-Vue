<template>
<div class="page-category">
  <div class="columns is-multiline">
    <div class="column is-12">
      <h2 class="is-size-2 has-text-centered" v-if="category && category.name">{{ category.name }}</h2>
    </div>

    <div v-if="category && category.products.length > 0 ">
      <ProductBox
        v-for="product in category.products"
        v-bind:key="product.id"
        v-bind:product="product" />
    </div>
  </div>
</div>
</template>
function getPost(state){
 return function(authorID){

}
}
<script>
import axios from "axios";
import ProductBox from "@/components/ProductBox.vue";
import {toast} from "bulma-toast";

export default {
  name: 'CategoryView',
  components: {
    ProductBox
  },
  date () {
    return {
      category: {
        products: []
      }
    }
  },
  mounted() {
    this.getCategory()
  },
  watch: {
    $route(to, from) {
      if (to.name === 'category') {
        this.getCategory()
      }
    }
  },
  methods: {
    async getCategory() {
      const categorySlug = this.$route.params.category_slug

      this.$store.commit('setIsLoading', true)

      axios
          .get(`/api/v1/products/${categorySlug}/`)
          .then(response => {
            this.category = response.data
            console.log(this.category)
            document.title = this.category.name + ' | Djackets'
          })
          .catch(error => {
            console.log(error)

            toast({
              message: 'Something went wrong. Please try again.',
              type: 'is-danger',
              dismissible: true,
              pauseOnHover: true,
              duration: 2000,
              position: 'bottom-right',
            })
          })

      this.$store.commit('setIsLoading', false)
    }
  }
}
</script>