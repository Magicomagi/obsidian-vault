<%*
const v = app.workspace.getActiveViewOfType(obsidian.MarkdownView);
if (v) {
    const s = v.getState();
    s.source = !s.source;
    v.setState(s, { history: false });
}
%>