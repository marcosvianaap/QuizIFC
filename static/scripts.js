document.addEventListener("DOMContentLoaded", function() {
    const items = document.querySelectorAll(".content .opcoes li");
    items.forEach((item, index) => {
        item.style.animationDelay = `${0.2 * index}s`;
        item.classList.add("animated");
    });
});


$(document).ready(function() {
    $('.opcoes li').each(function(index) {
        $(this).css('--order', index + 1);
    });
});