import { useState, useEffect, useRef } from 'react';
import './Login.css';

function Login() {
  const [userType, setUserType] = useState<'student' | 'faculty'>('student');
  const [placeholderText, setPlaceholderText] = useState('VJTI ID Number');
  const gridRef = useRef<HTMLDivElement>(null);
  const mainRef = useRef<HTMLDivElement>(null);
  const maxMovement = 16;

  //toggle between student and faculty
  const toggleUserType = (type: 'student' | 'faculty') => {
    setUserType(type);
    setPlaceholderText(type === 'student' ? 'VJTI ID Number' : 'VJTI Email Address');
  };

  //parallax effect
  useEffect(() => {
    const parallax = (e: MouseEvent) => {
      const mouseX = e.clientX / window.innerWidth;
      const mouseY = e.clientY / window.innerHeight;
      const moveX = (mouseX - 0.5) * maxMovement;
      const moveY = (mouseY - 0.5) * maxMovement;
      
      requestAnimationFrame(() => {
        if (!gridRef.current || !mainRef.current) return;
        gridRef.current.style.transform = `translate(${-moveX}px, ${-moveY}px)`;
        mainRef.current.style.transform = `translate(${8 + moveX * 0.4}px, ${8 + moveY * 0.4}px)`;
        mainRef.current.style.boxShadow = `var(--primary) ${12 - moveX * 0.4}px ${12 - moveY * 0.4}px`;
      });
    };

    document.addEventListener('mousemove', parallax);
  }, []);

  return (
    <div className="login-container">
      <div id="parallax-grid" ref={gridRef}></div>
      <div id="main" ref={mainRef}>
        <div id="toggle">
          <button 
            className={userType === 'student' ? 'active' : 'inactive'} 
            id="student"
            onClick={() => toggleUserType('student')}
          >
            STUDENT
          </button>
          <button 
            className={userType === 'faculty' ? 'active' : 'inactive'} 
            id="faculty"
            onClick={() => toggleUserType('faculty')}
          >
            FACULTY
          </button>
        </div>

        <h1>SIGN IN</h1>
        <div id="login">
          <input type="text" id="user" placeholder={placeholderText} />
          <input type="password" id="password" placeholder="Password" />
          <button id="submit">CONTINUE</button>
        </div>
      </div>
    </div>
  );
}

export default Login;