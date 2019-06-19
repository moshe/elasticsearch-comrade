module.exports = {
  lintOnSave: false,
  devServer: {
    proxy: {
      "^/api": {
        target: "http://127.0.0.1:8000/"
      }
    }
  }
};
