jQuery(function() {
    $(document).ready(function() {
        $(".tdRevert").click(tdRevert);
        $(".tdDelete").click(tdDelete);
        //Bug ->        $('click').click(tdUpdate);
        $('.tdUpdate').click(tdUpdate);
    });
})

//4º Quartil, similaridade = 0.6106666666666667