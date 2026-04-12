<%*
const view = app.workspace.getActiveViewOfType(obsidian.MarkdownView);
if (view) {
    const state = view.getState();
    state.source = !state.source;
    view.setState(state, { history: false });
}
%>