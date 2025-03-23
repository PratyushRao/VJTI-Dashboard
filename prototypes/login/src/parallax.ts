const grid = document.getElementById('parallax-grid');
const main = document.getElementById('main');
const maxMovement = 16;

document.addEventListener('mousemove', (e) => {
  const mouseX = e.clientX / window.innerWidth;
  const mouseY = e.clientY / window.innerHeight;
  const moveX = (mouseX - 0.5) * maxMovement;
  const moveY = (mouseY - 0.5) * maxMovement;
  requestAnimationFrame(() => {
    if(grid) grid.style.transform = `translate(${-moveX}px, ${-moveY}px)`;
    if(main){
        main.style.transform = `translate(${8 + moveX * 0.4}px, ${8 + moveY * 0.4}px)`;
        main.style.boxShadow = `var(--primary) ${12 - moveX * 0.4}px ${12 - moveY * 0.4}px`;
    }
  });
});