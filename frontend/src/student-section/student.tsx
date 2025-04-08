import './student.css';
import logo_img from './vjti-logo.webp'

//replace these with whatever the user logs in with
const uName = "Mudit Bengani";
const uRoll = "241090045";

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
        <a id = "logout" href = "./login">LOG OUT</a>
      </div>
    </div>
    <nav id = "navbar">
        <button className = "nav-option">Home</button>
        <button className = "nav-option">Profile</button>
        <button className = "nav-option">Semester Reports</button>
        <button className = "nav-option">Downloads</button>
        <button className = "nav-option">Announcements</button>
    </nav>
  </header>
  )
}