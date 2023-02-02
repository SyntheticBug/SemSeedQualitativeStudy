if ((tag === 'input' && (el.type === 'button' || el.type === 'submit' || el.type === 'image')) || tag === 'button') {
    setTimeout(function() {
        Utils.simulateClick(el, false);
//Bug ->        Utils.lastjQuery(el, false);
        Glee.blur();
    }, 0);
}

//2º Quartil, similaridade = 0.3395