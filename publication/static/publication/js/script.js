window.onscroll = function showHeader() {
    var menu_1 = document.querySelector(".nav");
    var menu_2 = document.querySelector(".predmety");
    var log = document.querySelector(".link_log");
    if(window.pageYOffset > 200){
        menu_1.classList.add('menu_fixed');
        log.classList.add('new');
    } else{
        menu_1.classList.remove('menu_fixed');
        log.classList.remove('new');
    }
}