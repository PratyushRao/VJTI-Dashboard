import './student.css';
import logo_img from './vjti-logo.webp'

if (!sessionStorage.getItem("user") && window.location.pathname != "/login")
  window.location.href = "./login";

const uName = sessionStorage.getItem("user") ? JSON.parse(sessionStorage.getItem("user") || "").name : "User";
const uRoll = sessionStorage.getItem("user") ? JSON.parse(sessionStorage.getItem("user") || "").roll : "Roll No.";
//const uYear = sessionStorage.getItem("user") ? JSON.parse(sessionStorage.getItem("user") || "").year : "Year";
//const uBranch = sessionStorage.getItem("user") ? JSON.parse(sessionStorage.getItem("user") || "").branch : "Branch";
//const uCGPA = sessionStorage.getItem("user") ? JSON.parse(sessionStorage.getItem("user") || "").cgpa : "CGPA";
//const uDoB = sessionStorage.getItem("user") ? JSON.parse(sessionStorage.getItem("user") || "").dob : "DoB";

export default function Student(){
  return(
  <header>
    <div id = "main-head">
      <img src= {logo_img} alt="VJTI" id="logo"/>
      <div id = "user-info">
        <div id = "details">
          <p>{uName}</p>
          <p>{uRoll}</p>
        </div>
        <a id = "logout" href = "./login" onClick={(e) => {
          e.preventDefault();
          sessionStorage.clear();
          window.location.href = "./login";
        }}>LOG OUT</a>
      </div>
    </div>
    <nav id = "navbar">
        <button className = "nav-option">Home</button>
        <button className = "nav-option">Profile</button>
        <button className = "nav-option">Academics</button>
        <button className = "nav-option">Downloads</button>
        <button className = "nav-option">Announcements</button>
    </nav>
  </header>
  )
}