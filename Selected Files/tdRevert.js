function tdRevert() {
    var id = $(this).parents("tr").find(".id").text();
    $(this).parents("tr").find(".flag").html("publish");
    //Bug ->    updateURL.ajax({
    $.ajax({
        type: "POST",
        url: "/post_manager?action=revert",
        data: "id=" + id,
        success: function(msg) {
            alert(msg);
        }
    });
}

//3º Quartil, similaridade=0.3765