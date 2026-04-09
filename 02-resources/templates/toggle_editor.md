<%*
const view = app.workspace.getActiveViewOfType(obsidian.MarkdownView);

if (view) {
    const state = view.getState();
    if (state.mode === "source") {
        // Inverte lo stato
        state.source = !state.source;
        // Applica lo stato
        await view.setState(state, { history: false });
        
        // Forza il focus per evitare che la tastiera fisica si scolleghi dalla nota
        setTimeout(() => {
            view.editor.focus();
        }, 100);
        
        new Notice(state.source ? "Sorgente" : "Live Preview");
    }
} else {
    new Notice("Apri una nota per cambiare modalità");
}
%>
