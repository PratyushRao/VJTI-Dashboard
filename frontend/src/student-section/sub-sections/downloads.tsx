const uYear = sessionStorage.getItem("user") ? JSON.parse(sessionStorage.getItem("user") || "").year : "Year";
const uBranch = sessionStorage.getItem("user") ? JSON.parse(sessionStorage.getItem("user") || "").branch : "Branch";

export default function Downloads() {
  const downloads: string[] = [
  `[AY 2024-25, B.Tech ${uBranch}] Semester ${uYear*2} ESE Hall Ticket`,
  `[AY 2024-25, B.Tech ${uBranch}] Semester ${uYear*2} ESE Time Table`,
  `[AY 2024-25, B.Tech ${uBranch}] Semester ${uYear*2} ESE Syllabus`,
  `[AY 2024-25, B.Tech ${uBranch}] Academic Calendar`,
  `[AY 2024-25, B.Tech ${uBranch}] Semester ${uYear*2} Class Schedule`,
  `[AY 2024-25, B.Tech ${uBranch}] Semester ${uYear*2 - 1} Report Card`,
  `[AY 2024-25] Placement Brochure`,
  `[AY 2024-25] Student Handbook`,
  `[AY 2024-25] Student Feedback Form`,
  `[AY 2024-25] Course Registration Form`,
  `Leave Application Form`,
  `Medical Certificate Form`,
  `Transfer Certificate Form`,
  ]

  return (
    <div className="downloads-container">
      <h1 className="sub-section-title">📥 Downloads</h1>
      <ul style = {{listStyleType: "square"}}>
        {downloads.map((download) => (
          <li className = "sub-list">{download}</li>
        ))}
      </ul>
    </div>
  );
}