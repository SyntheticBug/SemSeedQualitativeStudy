ns.get = function(collection) {
    var collectionString = localStorage.getItem(collection);
    if (collectionString) {
        return JSON.parse(collectionString);
    } else {
        _omgError('100', 'get()');
        //Bug -> return false;
        return true;
    }
    _executeHandlers('get');
};

//4º quartil, similaridade=0.928