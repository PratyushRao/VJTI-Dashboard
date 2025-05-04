export default async function Reports() {
  const uRoll = sessionStorage.getItem("user")
  ? JSON.parse(sessionStorage.getItem("user") || "").roll
  : "Roll No.";
  const uYear = sessionStorage.getItem("user")
  ? JSON.parse(sessionStorage.getItem("user") || "").year
  : "Year";
  const uBranch = (sessionStorage.getItem("user")
  ? JSON.parse(sessionStorage.getItem("user") || "").branch
  : "Branch").replace("EC", "Electronics").replace("ExTC", "Electronics & Telecommunication");

  try {
    const response = await fetch(`http://localhost:8000/reports?roll=${uRoll}&year=${uYear}&branch=${encodeURIComponent(uBranch)}`, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      }
    });
    const data = await response.json();
  } catch (error) {
    console.error("Error fetching reports:", error);
  }


  return (
    <div className="reports-container">
      <h1 className="sub-section-title">📊 Academic Reports</h1>
    </div>
  )
}