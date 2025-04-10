import { useState, useEffect, useRef } from 'react';
import './login.css';

function Login() {
  const [userType, setUserType] = useState<'student' | 'faculty'>('student');
  const [placeholderText, setPlaceholderText] = useState('Registration ID');
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const gridRef = useRef<HTMLDivElement>(null);
  const mainRef = useRef<HTMLDivElement>(null);
  const maxMovement = 16;

  // Toggle between student and faculty
  const toggleUserType = (type: 'student' | 'faculty') => {
    setUserType(type);
    setPlaceholderText(type === 'student' ? 'Registration ID' : 'Username');
  };

  // Parallax effect
  useEffect(() => {
    const handleMouseMove = (e: MouseEvent) => {
      const mouseX = e.clientX / window.innerWidth;
      const mouseY = e.clientY / window.innerHeight;
      const moveX = (mouseX - 0.5) * maxMovement;
      const moveY = (mouseY - 0.5) * maxMovement;

      requestAnimationFrame(() => {
        if (gridRef.current) {
          gridRef.current.style.transform = `translate(${-moveX}px, ${-moveY}px)`;
        }
        if (mainRef.current) {
          mainRef.current.style.transform = `translate(${8 + moveX * 0.4}px, ${8 + moveY * 0.4}px)`;
          mainRef.current.style.boxShadow = `var(--primary) ${12 - moveX * 0.4}px ${12 - moveY * 0.4}px`;
        }
      });
    };

    document.addEventListener('mousemove', handleMouseMove);

    return () => {
      document.removeEventListener('mousemove', handleMouseMove);
    };
  }, []);

  const submitData = async () => {
    try {
      sessionStorage.clear();
      const response = await fetch("http://localhost:8000/login", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({userType, username, password }),
      });

      const data = await response.json();
      if (!data.isValid) { 
        alert(data.message);
        return;
      }
      if (data.isValid) {
        sessionStorage.setItem("user", JSON.stringify(data.user));
        window.location.href = `/${userType}`;
      }


    } catch (error) {
      alert("Invalid");
      console.error("Login error:", error);
    }
  };

  return (
    <div className="login-container">
      <div id="bg-div"></div>
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
          <input type="text" id="user" placeholder={placeholderText} value={username.trim()} onChange={(e) => setUsername(e.target.value)}/>
          <input type="password" id="password" placeholder="Password" value={password.trim()} onChange={(e) => setPassword(e.target.value)}/>
          <button id="submit" onClick={(e) => { e.preventDefault(); submitData(); }}>CONTINUE</button>
        </div>
      </div>
    </div>
  );
}

export default Login;