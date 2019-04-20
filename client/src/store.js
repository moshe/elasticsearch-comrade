import Vue from "vue";
import Vuex from "vuex";
import { clusterStatus } from "./enums";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    loading: true,
    shardsMarkedForRelocation: [],
    nodes: [],
    indices: {},
    cluster: {
      numberOfDocs: 0,
      numOfIndices: 0,
      numOfPrimaryShards: 0,
      numOfReplicaShards: 0,
      numberOfNodes: 0,
      clusterStatus: clusterStatus.loading,
      relocatingShards: 0,
      initializingShards: 0
    },
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
    stopLoading(state) {
      state.loading = false;
    },
    startLoading(state) {
      state.loading = true;
    },
    setNodes(state, data) {
      Vue.set(state, "nodes", data);
    },
    setIndices(state, data) {
      Vue.set(state, "indices", data);
    },
    setCluster(state, data) {
      Vue.set(state, "cluster", data);
    },
    clearRelocation(state) {
      Vue.set(state, "shardsMarkedForRelocation", []);
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
      commit("setCluster", a.cluster);
      commit("stopLoading");
    }
  }
});
