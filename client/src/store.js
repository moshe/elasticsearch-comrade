import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    shardsMarkedForRelocation: [],
    nodes: [],
    settingsRefreshEvery: 5000
  },
  mutations: {
    toggleShardForRelocation(state, { index, id, nodeName }) {
      for (let i = 0; i < state.shardsMarkedForRelocation.length; i++) {
        const mark = state.shardsMarkedForRelocation[i];
        if (
          mark.index === index &&
          mark.nodeName === nodeName &&
          mark.id === id
        ) {
          state.shardsMarkedForRelocation.splice(i, 1);
          return;
        }
      }
      state.shardsMarkedForRelocation.push({ index, id, nodeName });
    },
    setNodes(state, data) {
      Vue.set(state, "nodes", data);
    },
    setIndices(state, data) {
      Vue.set(state, "indices", data);
    },
    setRefreshEvery(state, data) {
      state.settingsRefreshEvery = data;
    }
  },
  actions: {
    async shardsGrid({ commit }) {
      const a = await (await fetch("/api/v1/shards_grid")).json();
      commit("setNodes", a.nodes);
      commit("setIndices", a.indices);
    }
  }
});
