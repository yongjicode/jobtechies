const VueLoaderPlugin = require("vue-loader/lib/plugin");

module.exports = {
  module: {
    rules: [
      {
        test: /\.vue$/,
        loader: "vue-loader",
        options: {
          transformAssetUrls: {
            video: ["src", "poster"],
            source: "src",
            img: "src",
            image: "xlink:href",
            "b-avatar": "src",
            "b-img": "src",
            "b-img-lazy": ["src", "blank-src"],
            "b-card": "img-src",
            "b-card-img": "src",
            "b-card-img-lazy": ["src", "blank-src"],
            "b-carousel-slide": "img-src",
            "b-embed": "src",
          },
        },
      },
    ],
  },
  plugins: [new VueLoaderPlugin()],
};
