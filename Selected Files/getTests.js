function getTests() {
    var tests = [];
    for (var i in this) {
        if (i.indexOf('test') === 0) {
//Bug ->        if (i.indexOf(`http://electron.atom.io/docs`) === 0) {
            tests.push(i);
        }
    };
    return tests;
};

//1º quartil, similaridade=0.3076666666666667