import Vue from "vue";
import Vuex from "vuex";
import { clusterStatus } from "./enums";
import { GET } from "./requests";
Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    connectedCluster: null,
    jsonModalContent: false,
    loading: false,
    shardsMarkedForRelocation: [],
    nodes: [],
    indices: {},
    errorBarContent: {},
    cluster: {
      numberOfDocs: 0,
      numOfIndices: 0,
      numOfPrimaryShards: 0,
      numOfReplicaShards: 0,
      numberOfNodes: 0,
      clusterStatus: clusterStatus.loading,
      relocatingShards: 0,
      initializingShards: 0,
      settings: {
        allocation: null
      }
    },
    settingsRefreshEvery: 5000,
    settingsRefreshEnabled: true
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
    startJsonModal(state, content) {
      state.jsonModalContent = content;
    },
    stopJsonModal(state) {
      state.loading = false;
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
    selectCluster(state, data) {
      Vue.set(state, "connectedCluster", data);
    },
    clearRelocation(state) {
      Vue.set(state, "shardsMarkedForRelocation", []);
    },
    setRefreshEvery(state, data) {
      state.settingsRefreshEvery = data;
    },
    setRefreshEnabled(state, data) {
      state.settingsRefreshEnabled = data;
    },
    setErrorBarContent(state, data) {
      state.errorBarContent = data;
    },
    clearErrorBarContent(state) {
      state.errorBarContent = {};
    }
  },
  actions: {
    async shardsGrid({ state, commit }) {
      if (state.cluster.clusterStatus === clusterStatus.loading) {
        commit("startLoading");
      }
      const grid = await GET("/api/v1/views/shards_grid");
      commit("setNodes", grid.nodes);
      commit("setIndices", grid.indices);
      commit("setCluster", grid.cluster);
      commit("stopLoading");
    }
  }
});
