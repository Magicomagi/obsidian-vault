<%*
const view = app.workspace.getActiveViewOfType(obsidian.MarkdownView);
if (view) {
    const state = view.getState();
    if (state.mode === "source") {
        state.source = !state.source;
        view.setState(state, { history: false });
    } else {
        new Notice("Attiva la modalità editing");
    }
}
%>
