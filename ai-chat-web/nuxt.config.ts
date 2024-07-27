// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  modules: ["@nuxtjs/tailwindcss", "@vesp/nuxt-fontawesome", "@nuxtjs/mdc"],
  compatibilityDate: "2024-07-21",
  fontawesome: {
    icons: {
      solid: ["paper-plane"]
    }
  },
  css: ['@/assets/css/main.css']
})