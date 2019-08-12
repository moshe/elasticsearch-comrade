module.exports = {
  publicPath: process.env.NODE_ENV === 'production' ? '/static/' : '/',
  lintOnSave: false,
  devServer: {
    proxy: {
      "^/api": {
        target: "http://127.0.0.1:8000/"
      }
    }
  }
};
