import { useState, useEffect, useRef } from 'react';

function Edit() {
  const [userType, setUserType] = useState<'student' | 'faculty'>('student');
  const [placeholderText, setPlaceholderText] = useState('Registration ID');
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [email, setEmail] = useState("");
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
      const response = await fetch("http://localhost:8000/edit", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ userType, username, email, password }),
      });

      const data = await response.json();
      if (!data.isValid) {
        alert(data.message);
        return;
      }
      if (data.isValid) {
        window.location.href = `/login`;
      }


    } catch (error) {
      alert("Invalid");
      console.error("Password error:", error);
    }
  };

  const handleKeyDown = (e) => {
    if (e.key === "Enter") {
      submitData();
    }
  };
  return (
    <div className="login-container">
      <title>VJTI Dashboard Login</title>
      <div id="parallax-grid" ref={gridRef}> </div>
      <div id="main-login" ref={mainRef}>

        <div id="toggle">
          <div className="back" style = {{
              width: "1.5rem",
              position: "absolute",
              left: "5%"}}><lord-icon onClick={(e) => { e.preventDefault(); window.location.href = `/login`; }}
            src="https://cdn.lordicon.com/vduvxizq.json"
            trigger="hover"
            colors="primary:#ae152d"
            style={{ width: '2.5rem', height: '2.5rem', "rotate": "180deg", "cursor": "pointer" }}>
          </lord-icon></div>
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

        <div id="login">
          <input type="text" id="user" placeholder={placeholderText} value={username.trim()} onChange={(e) => setUsername(e.target.value)} />
          <input type="text" id="password" placeholder="Email ID" value={email.trim()} onKeyDown={handleKeyDown} onChange={(e) => setEmail(e.target.value)} />
          <input type="password" id="password" placeholder="Enter New Password" value={password.trim()} onKeyDown={handleKeyDown} onChange={(e) => setPassword(e.target.value)} />
          <button id="submit" onClick={(e) => { e.preventDefault(); submitData(); }}>CONTINUE</button>

        </div>
      </div>
    </div>
  );
}

export default Edit;