/*
 * funzione da eseguire quando si carica la pagina
 */
function caricata() {
    alert("documento caricato");
}

/*
 * funzione da eseguire quando si preme il pulsante
 */
function premuto() {
    document.getElementById("nota").innerHTML = "tasto premuto";
}

/*
 * funzione da eseguire quando si cambia il testo
 */
function cambiato() {
    alert("testo cambiato");
    document.getElementById("nota").innerHTML = "testo cambiato";
}