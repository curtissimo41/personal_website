$(document).ready(function() {
    $("#newWord").hide();
    
    var clicks = 0;
    var rand_word = "";
    makeNewWord();  // start off with new word right away
    
    function incrementClicks() {
        clicks++;
        $("#clickAmt").html(clicks);
    }
    
    function makeNewWord() {
        $.ajax({
            url: "http://0.0.0.0:8080/newWord",
            success: function(response) {
                console.log(response);
                rand_word = response;
            },
            error: function(error) {
                console.log(error);
            }
        });
    }
    
    $("#showButt").click(function() {
        $("#newWord").toggle();
        if ($("#newWord").is(":visible")) {
            makeNewWord();
            $("#newWord").html(rand_word);
            incrementClicks();
        }
    }); 
});
