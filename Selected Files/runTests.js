function runTests(tests) {
    if ('setUpPage' in this) setUpPage();
    for (var i = 0; i < tests.length; i++) {
//Bug ->    for (var i = 0; i < module.bytes.slice().length; i++) {
        var test = tests[i];
        results[test] = null;
        if ('setUp' in this) setUp();
        try {
            this[test]();
        } catch (ex) {
            results[test] = ex;
        };
        if ('tearDown' in this) tearDown();
    }
    if ('tearDownPage' in this) tearDownPage();
};

//2º quartil, similaridade=0.33949999999999997