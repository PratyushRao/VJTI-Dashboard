import { useState } from "react";

export default function Reports() {
  const semReports = sessionStorage.getItem("user")
    ? JSON.parse(sessionStorage.getItem("user") || "{}").semReports
    : "No Reports Available";

  const [activeSem, setActiveSem] = useState(semReports.length - 1);

  let grades = {
    AA: 10,
    AB: 9,
    BB: 8,
    BC: 7,
    CC: 6,
    CD: 5,
    DD: 4,
    FF: 0,
  };

  const renderSemReports = () => {
    return (
      <div className="sem-reports">
        {semReports[activeSem].map((subject: any, index: number) => {
          return (
            <div className="report-card" key={index}>
              <div className="report-title">{subject.SUBJECT}</div>
              <div className="report-details">
                Grade: <span className="subject-data">{subject.GRADE}</span>
              </div>
              <div className="report-details">
                Attendance:{" "}
                <span className="subject-data">{subject.Attendance}</span>
              </div>
              <div className="report-details">
                Faculty: <span className="subject-data">{subject.FACULTY}</span>
              </div>
              <div className="report-details">
                Credits:{" "}
                <span className="subject-data">
                  {subject.CREDIT.toFixed(1)}
                </span>
              </div>
            </div>
            
          );
        })}
      </div>
    );
  };

  const calculateSGPA = () => {
    let totalCredits = 0;
    let totalPoints = 0;

    semReports[activeSem].forEach(
      (subject: { GRADE: keyof typeof grades; CREDIT: number }) => {
        const grade = subject.GRADE;
        const credits = subject.CREDIT;
        totalCredits += credits;
        totalPoints += grades[grade] * credits;
      }
    );

    return (totalPoints / totalCredits).toFixed(2);
  };

  return (
    <div className="reports-container">
      <div>
        <h1 className="sub-section-title">📊 Academic Reports</h1>
        {renderSemReports()}
      </div>

      <footer id="reports-footer">
        <div className="sem-selector-container">
          <h4>SEMESTER:</h4>
          <div className="sem-selector">
            {semReports.map((_: any, index: number) => {
              return (
                <button
                  onClick={() => setActiveSem(index)}
                  id={activeSem === index ? "active-sem" : ""}
                >
                  {index + 1}
                </button>
              );
            })}
          </div>
        </div>

        <div className="sgpa-container">
          <p className="sgpa-title">SGPA: </p>
          <div className="sgpa">{calculateSGPA()}</div>
        </div>
      </footer>
    </div>
  );
}
