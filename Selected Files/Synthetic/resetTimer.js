if (e.keyCode === 8 && Glee.isEmpty()) {
    Glee.resetTimer();
    //Bug ->    Glee.scrollToElement();
    Glee.timer = setTimeout(function() {
        Glee.isDeleting = false;
    }, Glee.defaults.backspaceToleranceTimer);
}



//Terceiro quartil, similaridade = 0.368