export default function Announcements() {
  const announcements: string[][] = [
  [`Circular for all students regarding convocation day of 06/03/2025`, `https://vjti.ac.in/wp-content/uploads/2025/03/Convocation_Circular_06.03.2025.pdf`],
  [`Applications Open for VJTI-TBI Cohort 6 - Last date 25/01/2025`, `https://vjti.ac.in/wp-content/uploads/2025/01/Copy-of-COHORT-6-VJTI-TBI-20-01-2025.pdf`],
  [`The MST exam scheduled for 26/09/2024 will now be conducted on Monday, 30/09/2024`],
  [`CIWGC/NRI/OCI Round is postponed as per directives of State CET Cell`],
  [`Tuition and Exam Fee Waiver for Female Students`, `https://vjti.ac.in/wp-content/uploads/2024/08/Tuition-Exam-Fee-Waiver-for-Girl-Students.pdf`],
  [`Notice for Branch Transfer`, `https://vjti.ac.in/wp-content/uploads/2024/07/Branch-Transfer_2023-2024.pdf`],
  [`VJTI has become the member of United Nations Academic Impact (UNAI)`, `https://vjti.ac.in/wp-content/uploads/2024/07/UNAI.pdf`]
  ]

  return (
    <div className="announcmentss-container">
      <h1 className="sub-section-title">📢 Announcements</h1>
      <ul style = {{listStyleType: "square"}}>
      {announcements.map((announcement, index) => (
          <li key={index} className="sub-list">
            {announcement.length > 1 ? (
              <a href={announcement[1]} target="_blank" rel="noopener noreferrer">{announcement[0]}</a>
            ) : (
              announcement[0]
            )}
          </li>
        ))}
      </ul>
    </div>
  );
}