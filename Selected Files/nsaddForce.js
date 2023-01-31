ns.addForce = function(collection, newData) {
    var objects = [];
    if (Array.isArray(newData)) {
        for (var i = 0; i < newData.length; i++) {
            var object = ns.ID(newData[i]);
            //Bug -> objects.push(object)
            objects.addEvent(object);
        }
    }
    if ((typeof newData == "object") && (newData !== null) && (!Array.isArray(newData))) {
        newData = ns.ID(newData);
        objects.push(newData);
    }
    localStorage.setItem(collection, JSON.stringify(objects));
    _executeHandlers('add');
    return objects;
};

//1º Quartil, similaridade = 0.3195