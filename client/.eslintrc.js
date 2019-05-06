module.exports = {
  root: true,

  env: {
    node: true
  },

  extends: ["plugin:vue/essential", "@vue/prettier"],
  plugins: ["import"],

  rules: {
    "no-console": process.env.NODE_ENV === "production" ? "error" : "off",
    "no-debugger": process.env.NODE_ENV === "production" ? "error" : "off",
    "import/extensions": [
      "error",
      "always",
      {
        js: "never"
      }
    ]
  },

  parserOptions: {
    parser: "babel-eslint"
  }
};
