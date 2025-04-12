import './faculty.css';
import logo_img from './vjti-logo.webp';

if (!sessionStorage.getItem("user") && window.location.pathname != "/login")
    window.location.href = "./login";
  
const uName = sessionStorage.getItem("user") ? JSON.parse(sessionStorage.getItem("user") || "").name : "User";

export default function Faculty(){
    return(
    <div className = "faculty-container">
      <div id='parallax'></div>
    <header>
      <div id = "faculty-main-head">
        <img src= {logo_img} alt="VJTI" id="logo"/>
        <div id = "user-info">
            <p>{uName}</p>
          <a id = "logout" href = "./login" onClick={(e) => {
            e.preventDefault();
            sessionStorage.clear();
            window.location.href = "./login";
          }}>LOG OUT</a>
        </div>
      </div>
    </header>

    <div className="container">

    <div className="main-content">

      
    <div className='title'>Your Classes</div>
    <div className="class-container">
      <div className="classes">Maths</div>
      <div className="classes">Chemistry</div>
      
      
    </div>
    </div>
    </div>





    </div>
    )
  }

