const GET = async url => {
  (await fetch(url)).json();
};

export default {
  methods: {
    async openIndex(index) {
      return await GET(`/api/v1/index/${index}/open`);
    },

    async closeIndex(index) {
      return await GET(`/api/v1/index/${index}/close`);
    }
  }
};
