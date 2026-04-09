<%*
const view = app.workspace.getActiveViewOfType(obsidian.MarkdownView);
if (view) {
  const mode = view.getState().mode;
  const source = view.getState().source;

  // Se è in modalità editing, scambia tra Live Preview e Source
  if (mode === "source") {
    view.setState({ ...view.getState(), source: !source }, {});
  }
}
%>
