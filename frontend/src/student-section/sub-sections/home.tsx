export default function Home() {
  const uName = sessionStorage.getItem("user")
    ? JSON.parse(sessionStorage.getItem("user") || "").name
    : "User";
  const uRoll = sessionStorage.getItem("user")
    ? JSON.parse(sessionStorage.getItem("user") || "").roll
    : "Roll No.";
  const uYear = sessionStorage.getItem("user")
    ? JSON.parse(sessionStorage.getItem("user") || "").year
    : "Year";
  const uBranch = (sessionStorage.getItem("user")
    ? JSON.parse(sessionStorage.getItem("user") || "").branch
    : "Branch").replace("EC", "Electronics").replace("ExTC", "Electronics & Telecommunication");
  const uCGPA = sessionStorage.getItem("user")
    ? JSON.parse(sessionStorage.getItem("user") || "").cgpa
    : "CGPA";
  const uDoB = (sessionStorage.getItem("user")
    ? JSON.parse(sessionStorage.getItem("user") || "").dob
    : "DoB").substring(0,10);
  const uEmail = sessionStorage.getItem("user")
    ? JSON.parse(sessionStorage.getItem("user") || "").email
    : "email";

  return (
    <div className="profile-container">
      <h1 className = "sub-section-title">👤 Student Profile</h1>
      <div className="profile-details">
        <div><div className="student-datatype">Name:</div> {uName}</div>
        <div><div className="student-datatype">Registration ID:</div> {uRoll}</div>
        <div><div className="student-datatype">Email Address:</div> {uEmail}</div>
        <div><div className="student-datatype">Current Year:</div> {uYear}</div>
        <div><div className="student-datatype">Current Semester:</div> {uYear*2}</div>
        <div><div className="student-datatype">Branch:</div> {uBranch}</div>
        <div><div className="student-datatype">Department:</div> Electrical</div>
        <div><div className="student-datatype">CGPA:</div> {uCGPA}</div>
        <div><div className="student-datatype">Date of Birth (YYYY-MM-DD):</div> {uDoB}</div>
        <div><div className="student-datatype">Blood Type:</div> B+</div>
      </div>
    </div>
  );
}
