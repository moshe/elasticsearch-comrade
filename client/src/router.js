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
      nodeName: "home",
      component: Home
    },
    {
      path: "/rest",
      nodeName: "rest",
      component: RESTView
    },
    {
      path: "/aliases",
      nodeName: "createAliases",
      component: AliasesView
    },
    {
      path: "/tasks",
      nodeName: "tasks",
      component: TasksView
    },
    {
      path: "/snapshots",
      nodeName: "snapshots",
      component: () =>
        import(/* webpackChunkName: "snapshots" */ "./views/SnapshotsView.vue")
    },
    {
      path: "/templates",
      nodeName: "templates",
      component: TemplatesView
    },
    {
      path: "/indexSettings/:indexName",
      nodeName: "indexSettings",
      component: IndexSettingsView,
      props: true
    },
    {
      path: "/node/:nodeId",
      nodeName: "NodeInfo",
      component: NodeInfoView,
      props: true
    }
  ]
});
