<%*
const view = app.workspace.getActiveViewOfType(obsidian.MarkdownView);

if (view) {
    const state = view.getState();
    // Verifica che siamo in modalità editing (source), non in lettura (preview)
    if (state.mode === "source") {
        // Inverte il valore di source: 
        // true = Source Mode (codice puro)
        // false = Live Preview (editing dinamico)
        state.source = !state.source;
        view.setState(state, { history: false });
    } else {
        new Notice("Devi essere in modalità Editing per cambiare la visualizzazione.");
    }
} else {
    new Notice("Nessuna nota attiva trovata.");
}
%>
