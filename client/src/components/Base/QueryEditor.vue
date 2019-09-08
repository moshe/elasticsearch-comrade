<template>
  <div v-on:keydown.enter="handleCmdEnter($event)" :style="cssProps" />
</template>

<script>
import JSONEditor from "jsoneditor";
import "jsoneditor/dist/jsoneditor.css";
import colors from "vuetify/lib/util/colors";
require("brace/theme/monokai");
require("brace/theme/clouds");
export default {
  props: {
    readOnly: {
      type: Boolean,
      default: false
    },
    init: {
      type: Object
    }
  },
  mounted() {
    const container = this.$el;
    if (!this.dark) {
      this.options.theme = "ace/theme/clouds";
    }
    this.editor = new JSONEditor(container, this.options);
    if (this.init) {
      this.setContent(this.init);
    }
    if (this.readOnly) {
      this.editor.aceEditor.setReadOnly(true);
    }
  },
  methods: {
    handleCmdEnter(e) {
      if (e.ctrlKey || e.metaKey || e.altKey) {
        this.$emit("execute");
      }
    },
    getQuery() {
      return this.editor.get();
    },
    setContent(content) {
      return this.editor.set(content);
    },
    refresh() {
      this.editor.set(this.editor.get());
    }
  },
  watch: {
    dark(isDark) {
      if (isDark) {
        console.log("dark!");
        this.options.theme = "ace/theme/monokai";
      } else {
        console.log("light!");
        this.options.theme = "ace/theme/clouds";
      }
      this.editor.destroy();
      this.editor = new JSONEditor(this.$el, this.options);
    }
  },
  data() {
    return {
      editor: null,
      options: {
        mode: "code",
        modes: ["code", "text"],
        search: false,
        statusBar: false,
        enableSort: false,
        enableTransform: false,
        mainMenuBar: true,
        theme: "ace/theme/monokai"
      }
    };
  },
  computed: {
    dark() {
      const { dark } = this.$vuetify.theme;
      return dark;
    },
    cssProps() {
      const { dark } = this;
      return {
        "--query-frame": dark ? colors.grey.darken3 : colors.grey.darken3,
        "--marker": dark ? colors.grey.darken2 : colors.grey.darken3
      };
    }
  }
};
</script>

<style>
div.jsoneditor,
div.jsoneditor-menu {
  border-color: var(--query-frame);
  background-color: var(--query-frame);
}
</style>
