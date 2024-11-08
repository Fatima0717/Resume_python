module.exports = {
  content: [
    "./templates/**/*.html",
    "./static/js/**/*.js"
  ],
  css: [
    "./static/css/**/*.css"
  ],
  output: "./static/css/optimized/",
  safelist: [
    "active",
    "show",
    "hide",
    /^swiper-/,
    /^fa-/
  ]
}
