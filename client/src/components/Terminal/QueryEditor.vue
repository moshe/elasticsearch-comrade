<template>
  <div id="jsoneditor" style="height: 800px;"></div>
</template>

<script>
import JSONEditor from "jsoneditor";
import "jsoneditor/dist/jsoneditor.css";
export default {
  name: "QueryEditor",
  mounted() {
    const container = document.getElementById("jsoneditor");
    this.editor = new JSONEditor(container, this.options);
    // set json
    const json = {
      Array: [1, 2, 3],
      Boolean: true,
      Null: null,
      Number: 123,
      Object: { a: "b", c: "d" },
      String: "Hello World"
    };
    this.editor.set(json);
  },
  methods: {
    getQuery() {
      return this.editor.get();
    }
  },
  data() {
    return {
      editor: null,
      options: {
        mode: "code",
        modes: ["code", "text"],
        search: false
      }
    };
  }
};
</script>

<style>
/* dark styling of the editor */
div.jsoneditor,
div.jsoneditor-menu {
  border-color: #202020;
}
div.jsoneditor-menu {
  background-color: #202020;
}
div.jsoneditor-tree,
div.jsoneditor textarea.jsoneditor-text {
  background-color: #666666;
  color: #ffffff;
}
div.jsoneditor-field,
div.jsoneditor-value {
  color: #ffffff;
}
table.jsoneditor-search div.jsoneditor-frame {
  background: #808080;
}

tr.jsoneditor-highlight,
tr.jsoneditor-selected {
  background-color: #808080;
}

div.jsoneditor-field[contenteditable="true"]:focus,
div.jsoneditor-field[contenteditable="true"]:hover,
div.jsoneditor-value[contenteditable="true"]:focus,
div.jsoneditor-value[contenteditable="true"]:hover,
div.jsoneditor-field.jsoneditor-highlight,
div.jsoneditor-value.jsoneditor-highlight {
  background-color: #808080;
  border-color: #808080;
}

div.jsoneditor-field.highlight-active,
div.jsoneditor-field.highlight-active:focus,
div.jsoneditor-field.highlight-active:hover,
div.jsoneditor-value.highlight-active,
div.jsoneditor-value.highlight-active:focus,
div.jsoneditor-value.highlight-active:hover {
  background-color: #b1b1b1;
  border-color: #b1b1b1;
}

div.jsoneditor-tree button:focus {
  background-color: #868686;
}

/* coloring of JSON in tree mode */
div.jsoneditor-readonly {
  color: #acacac;
}
div.jsoneditor td.jsoneditor-separator {
  color: #acacac;
}
div.jsoneditor-value.jsoneditor-string {
  color: #00ff88;
}
div.jsoneditor-value.jsoneditor-object,
div.jsoneditor-value.jsoneditor-array {
  color: #bababa;
}
div.jsoneditor-value.jsoneditor-number {
  color: #ff4040;
}
div.jsoneditor-value.jsoneditor-boolean {
  color: #ff8048;
}
div.jsoneditor-value.jsoneditor-null {
  color: #49a7fc;
}
div.jsoneditor-value.jsoneditor-invalid {
  color: white;
}
div.ace_gutter {
  z-index: 1;
}
</style>
