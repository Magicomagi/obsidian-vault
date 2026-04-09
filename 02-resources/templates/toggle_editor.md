<%*
const view = app.workspace.getActiveViewOfType(obsidian.MarkdownView);

if (view) {
    const state = view.getState();
    if (state.mode === "source") {
        // Inverte lo stato tra Live Preview (false) e Source Mode (true)
        state.source = !state.source;
        view.setState(state, { history: false });
        
        // Feedback visivo immediato su iPad
        const modo = state.source ? "Sorgente" : "Live Preview";
        new Notice("Modalità: " + modo);
    } else {
        new Notice("Passa alla modalità Editing per usare lo script");
    }
}
%>
