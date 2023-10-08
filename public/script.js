document.addEventListener('DOMContentLoaded', () => {
    const tiltContainer = document.querySelector('.tilt-container');
    const tiltImage = document.querySelector('.tilt-image');

    if (!tiltContainer || !tiltImage) {
        console.error("Tilt container or tilt image not found.");
        return;
    }

    tiltContainer.addEventListener('mousemove', (e) => {
        const xAxis = (window.innerWidth / 2 - e.pageX) / 80; // Adjust the division factor as needed
        const yAxis = (window.innerHeight / 2 - e.pageY) / 80; // Adjust the division factor as needed

        tiltImage.style.transform = `rotateY(${xAxis}deg) rotateX(${yAxis}deg)`;
    });

    tiltContainer.addEventListener('mouseenter', () => {
        tiltImage.style.transition = 'none';
    });

    tiltContainer.addEventListener('mouseleave', () => {
        tiltImage.style.transform = 'rotateY(0deg) rotateX(0deg)';
        tiltImage.style.transition = 'transform 0.5s ease';
    });
});


t=document.getElementById("textarea");

t.addEventListener("keydown", function(event) {
    if (event.keyCode === 13) {
      console.log(window.location.href+'search');
      var url = new URL(window.location.href+'search');
      url.searchParams.append('query', event.target.value);
      window.location.href = url.href
    }
});