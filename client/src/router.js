import Router from "vue-router";
import AliasesView from "./views/AliasesView.vue";
import Home from "./views/Home.vue";
import IndexSettingsView from "./views/IndexSettingsView.vue";
import NodeInfoView from "./views/NodeInfoView.vue";
import RESTView from "./views/RESTView.vue";
import TasksView from "./views/TasksView.vue";
import TemplatesView from "./views/TemplatesView.vue";

export default new Router({
  mode: "history",
  routes: [
    {
      path: "/",
      name: "home",
      component: Home
    },
    {
      path: "/rest",
      name: "rest",
      component: RESTView,
      props: route => ({ ...route.params })
    },
    {
      path: "/aliases",
      name: "createAliases",
      component: AliasesView
    },
    {
      path: "/tasks",
      name: "tasks",
      component: TasksView
    },
    {
      path: "/snapshots",
      name: "snapshots",
      component: () =>
        import(/* webpackChunkName: "snapshots" */ "./views/SnapshotsView.vue")
    },
    {
      path: "/templates",
      name: "templates",
      component: TemplatesView
    },
    {
      path: "/indexSettings/:indexName",
      name: "indexSettings",
      component: IndexSettingsView,
      props: true
    },
    {
      path: "/node/:nodeId",
      name: "NodeInfo",
      component: NodeInfoView,
      props: true
    }
  ]
});
