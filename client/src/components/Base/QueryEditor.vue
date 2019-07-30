<template>
  <div v-on:keydown.enter="handleCmdEnter($event)" :style="cssProps" />
</template>

<script>
import JSONEditor from "jsoneditor";
import "jsoneditor/dist/jsoneditor.css";
import colors from "vuetify/lib/util/colors";
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
        mainMenuBar: true
      }
    };
  },
  computed: {
    cssProps() {
      const { dark } = this.$vuetify.theme;
      return {
        "--query-frame": dark ? colors.grey.darken3 : colors.grey.darken1,
        "--marker": dark ? colors.grey.darken2 : colors.grey.darken2
      };
    }
  }
};
</script>

<style>
/* dark styling of the editor */
div.jsoneditor,
div.jsoneditor-menu {
  border-color: var(--query-frame);
  background-color: var(--query-frame);
}

div.ace_gutter {
  z-index: 1;
  background: #4e6e44;
}

.ace-jsoneditor .ace_gutter {
  background: var(--query-frame) !important;
  color: white !important;
}

div.ace_folding-enabled > .ace_gutter-cell {
  padding: 0 15px 0 5px;
  text-align: left;
}

div.ace_content {
  background-color: #f5f5f5;
}

.ace-jsoneditor .ace_marker-layer .ace_active-line {
  background: #e3f2fd !important;
}
.ace-jsoneditor .ace_gutter-active-line {
  background-color: var(--marker) !important;
}
</style>
