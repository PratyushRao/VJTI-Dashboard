import './faculty.css';
import logo_img from './vjti-logo.webp';
import { useEffect, useRef } from 'react';
import MainContent from './components/mainContent';
import Students from './components/class'; 

if (!sessionStorage.getItem("user") && window.location.pathname != "/login")
  window.location.href = "./login";

const uName = sessionStorage.getItem("user") ? JSON.parse(sessionStorage.getItem("user") || "").name : "User";

export default function Faculty() {
  const gridRef = useRef<HTMLDivElement>(null);
  const maxMovement = 16;

  // Parallax effect
  useEffect(() => {
    const handleMouseMove = (e: MouseEvent) => {
      const mouseX = e.clientX / window.innerWidth;
      const mouseY = e.clientY / window.innerHeight;
      const moveX = (mouseX - 0.5) * maxMovement;
      const moveY = (mouseY - 0.5) * maxMovement;

      requestAnimationFrame(() => {
        if (gridRef.current)
          gridRef.current.style.transform = `translate(${-moveX * 0.4}px, ${-moveY * 0.4}px)`;
      });
    };

    document.addEventListener('mousemove', handleMouseMove);

    return () => {
      document.removeEventListener('mousemove', handleMouseMove);
    };
  }, []);


  return (
    <div className="faculty-container">
      <div id="faculty-parallax" ref={gridRef}></div>
      <header>
        <div id="faculty-main-head">
          <img src={logo_img} alt="VJTI" id="logo" />
          <div id="faculty-user-info">
            <p>{uName}</p>
            <a id="logout" href="./login" onClick={(e) => {
              e.preventDefault();
              sessionStorage.clear();
              window.location.href = "./login";
            }}>LOG OUT</a>
          </div>
        </div>
      </header>

      <div className="container">
        {/* <MainContent /> */}
        <Students /> 
        </div>
    </div>
  )
}

