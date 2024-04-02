/*!
* Start Bootstrap - Agency v7.0.12 (https://startbootstrap.com/theme/agency)
* Copyright 2013-2023 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-agency/blob/master/LICENSE)
*/
//
// Scripts
// 

window.addEventListener('DOMContentLoaded', event => {

    // Navbar shrink function
    var navbarShrink = function () {
        const navbarCollapsible = document.body.querySelector('#mainNav');
        if (!navbarCollapsible) {
            return;
        }
        if (window.scrollY === 0) {
            navbarCollapsible.classList.remove('navbar-shrink')
        } else {
            navbarCollapsible.classList.add('navbar-shrink')
        }

    };

    // Shrink the navbar 
    navbarShrink();

    // Shrink the navbar when page is scrolled
    document.addEventListener('scroll', navbarShrink);

    //  Activate Bootstrap scrollspy on the main nav element
    const mainNav = document.body.querySelector('#mainNav');
    if (mainNav) {
        new bootstrap.ScrollSpy(document.body, {
            target: '#mainNav',
            rootMargin: '0px 0px -40%',
        });
    };

    // Collapse responsive navbar when toggler is visible
    const navbarToggler = document.body.querySelector('.navbar-toggler');
    const responsiveNavItems = [].slice.call(
        document.querySelectorAll('#navbarResponsive .nav-link')
    );
    responsiveNavItems.map(function (responsiveNavItem) {
        responsiveNavItem.addEventListener('click', () => {
            if (window.getComputedStyle(navbarToggler).display !== 'none') {
                navbarToggler.click();
            }
        });
    });

});


function preparePlayer(songId, audioUrl, title, artist, imageUrl) {
    // Configura la información de la canción en el reproductor fijo
    document.getElementById('songTitle').innerText = title;
    document.getElementById('songArtist').innerText = artist;
    document.getElementById('albumImage').src = imageUrl;

    // Configura el audio source
    var audioPlayer = document.getElementById('fixedAudioPlayer');
    audioPlayer.src = audioUrl;
    
    // Opcional: Si quieres reproducir automáticamente la canción al cargarla
    // audioPlayer.play();
}


//Regula la opacitat del navbar
window.addEventListener('scroll', function() {
    const navbar = document.querySelector('.navbar'); // Cambia a tu selector de navbar específico
    const maxOpacity = 0.6;
    const scrollRange = 500; // Ajusta este valor según la altura a partir de la cual la opacidad debe llegar a 0.3
    let scrollY = window.scrollY || window.pageYOffset;
    let opacity = scrollY / scrollRange * maxOpacity;
    opacity = Math.min(maxOpacity, opacity); // Asegura que la opacidad no exceda de 0.3
  
    navbar.style.backgroundColor = `rgba(0, 0, 0, ${opacity})`;
  });



//PAGINA DEL EVENTO -- EVENTOS RELACIONATS (PERMET ARRASTRAR I SCROLLEJAR DES DE QUALSEVOL PUNT DE)
// Selector del contenedor que quieres que sea desplazable
document.addEventListener('DOMContentLoaded', function() {
    const slider = document.querySelector('.row-scrollable');
    let isDown = false;
    let startX;
    let scrollLeft;
  
    slider.addEventListener('mousedown', (e) => {
      isDown = true;
      slider.classList.add('grabbing');
      startX = e.pageX - slider.offsetLeft;
      scrollLeft = slider.scrollLeft;
    });
  
    slider.addEventListener('mouseleave', () => {
      isDown = false;
      slider.classList.remove('grabbing');
    });
  
    slider.addEventListener('mouseup', () => {
      isDown = false;
      slider.classList.remove('grabbing');
    });
  
    slider.addEventListener('mousemove', (e) => {
      if (!isDown) return;
      e.preventDefault();
      const x = e.pageX - slider.offsetLeft;
      const walk = (x - startX); // Controla la velocidad del arrastre
      slider.scrollLeft = scrollLeft - walk;
    });
  });