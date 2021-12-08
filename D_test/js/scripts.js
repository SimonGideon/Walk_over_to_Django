//
// Scripts
// 
$(document).ready(function(){
    $nav=$('.nav');
    $togleCollapse = $('.toggle-collapse');
    // Click event
    $togleCollapse.click(function(){
        $nav.toggleClass('collapse');
    })
    // owl carousel
    $('.owl-carouse').owlCarousel();
})
window.addEventListener('DOMContentLoaded', event => {

    // Activate Bootstrap scrollspy on the main nav element
    const mynavmenu = document.body.querySelector('#mynavmenu');
    if (mynavmenu) {
        new bootstrap.ScrollSpy(document.body, {
            target: '#mynavmenu',
            offset: 74,
        });
    };

    // Collapse responsive navbar when toggler is visible
    const navbarToggler = document.body.querySelector('.navbar-toggler');
    const responsiveNavItems = [].slice.call(
        document.querySelectorAll('#navmenu .nav-link')
    );
    responsiveNavItems.map(function (responsiveNavItem) {
        responsiveNavItem.addEventListener('click', () => {
            if (window.getComputedStyle(navbarToggler).display !== 'none') {
                navbarToggler.click();
            }
        });
    });

