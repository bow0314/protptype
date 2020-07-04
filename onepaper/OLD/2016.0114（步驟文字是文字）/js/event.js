$(function(){
    $("#BTN").on("click", OPENO);
    
    function OPENO(){
        $("#MENU").slideDown(300);
        $("#XX").on("click", CLOSEC);
    }
    
    function CLOSEC(){
        $("#MENU").slideUp(300);
        $("#XX").off("click");
    }
    
    $(window).on("resize",CLEARSTYLE);
    
    function CLEARSTYLE(){
        if($(window).innerWidth()>736){
            $("#MENU").attr("style","");
        }
    }
})