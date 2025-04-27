import "./student.css";
import logo_img from "./vjti-logo.webp";
import { useEffect, useRef, useState } from "react";

import Profile from "./sub-sections/profile";

//comment out this if block to to debug page without login
if (!sessionStorage.getItem("user") && window.location.pathname != "/login")
  window.location.href = "./login";

const uName = sessionStorage.getItem("user")
  ? JSON.parse(sessionStorage.getItem("user") || "").name
  : "User";
const uRoll = sessionStorage.getItem("user")
  ? JSON.parse(sessionStorage.getItem("user") || "").roll
  : "Roll No.";
//const uYear = sessionStorage.getItem("user") ? JSON.parse(sessionStorage.getItem("user") || "").year : "Year";
//const uBranch = sessionStorage.getItem("user") ? JSON.parse(sessionStorage.getItem("user") || "").branch : "Branch";
//const uCGPA = sessionStorage.getItem("user") ? JSON.parse(sessionStorage.getItem("user") || "").cgpa : "CGPA";
//const uDoB = sessionStorage.getItem("user") ? JSON.parse(sessionStorage.getItem("user") || "").dob : "DoB";

const [activeSection, setActiveSection] = useState("Home")

export default function Student() {
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
          gridRef.current.style.transform = `translate(${-moveX * 0.8}px, ${-moveY * 0.8}px)`;
      });
    };

    document.addEventListener("mousemove", handleMouseMove);

    return () => {
      document.removeEventListener("mousemove", handleMouseMove);
    };
  }, []);

  return (
    <div className="student-container">
        <title>VJTI Student Dashboard</title>
      <div id="student-parallax" ref={gridRef}></div>
      <header>
        <div id="student-main-head">
          <img src={logo_img} alt="VJTI" id="logo" />
          <div id="student-user-info">
            <div id="details">
              <p>{uName}</p>
              <p>{uRoll}</p>
            </div>
            <a
              id="logout"
              href="./login"
              onClick={(e) => {
                e.preventDefault();
                sessionStorage.clear();
                window.location.href = "./login";
              }}
            >
              LOG OUT
            </a>
          </div>
        </div>
        <nav id="navbar">
          <button className="nav-option" onClick = {() => setActiveSection("Home")}>
            Home
          </button>
          <button className="nav-option" onClick = {() => setActiveSection("Academic Reports")}>
            Academic Reports
          </button>
          <button className="nav-option" onClick = {() => setActiveSection("Downloads")}>
            Downloads
          </button>
          <button className="nav-option" onClick = {() => setActiveSection("Announcements")}>
            Announcements
          </button>
        </nav>
      </header>
      <div id = "student-main-body">
              {/*Display a div depending on the selected menu button here*/}
      </div>
    </div>
  );
}