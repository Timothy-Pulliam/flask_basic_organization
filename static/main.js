var app = new Vue({
  el: '#app',
  delimiters: ['[[', ']]'],
  data: {
    product: 'Socks',
    description: "100% Cotton Men's socks. Breathable for odor resistence.",
    altText: "A pair of socks",
    link: "https://bombas.com/collections/mens-socks",
    image: "/static/assets/vmSocks-green.jpg",
    inventory: 8,
    onSale: true,
    details: ["80% cotton", "20% polyester", "Gender-neutral"],
    variants: [
      {
        viariantId: 2234,
        variantColor: "green",
        variantImage: "/static/assets/vmSocks-green.jpg",
      },
      {
        viariantId: 2235,
        variantColor: "blue",
        variantImage: "/static/assets/vmSocks-blue.jpg",
      }
    ],
    sizes: ['small', 'medium', 'large',],
    cart: 0,
  },
  methods: {
    addToCart() {
      this.cart += 1
    },
    removeFromCart() {
      if (this.cart > 0) {
        this.cart -= 1;
      }
    },
    updateProduct(variantImage) {
      this.image = variantImage
    },
  }
})
