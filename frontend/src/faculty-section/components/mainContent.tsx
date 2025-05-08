const cData = sessionStorage.getItem("user") ? JSON.parse(sessionStorage.getItem("user") || "").classData : "CD";
const user = sessionStorage.getItem("user") ? JSON.parse(sessionStorage.getItem("user") || "").name : "User";


export default function MainContent() {

    const RequestData = async (sub: string) => {
        try {
            sessionStorage.getItem("subject") && sessionStorage.removeItem("subject");
            sessionStorage.getItem("sub") && sessionStorage.removeItem("sub");
            const response = await fetch("http://localhost:8000/faculty", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ user, sub }),
            });

            const data = await response.json();
            sessionStorage.setItem("subject", JSON.stringify(data.subjects));
            sessionStorage.setItem("sub", JSON.stringify(data.sub));
            window.location.href = `/subject`;


        } catch (error) {
            alert("Invalid");
            console.error("Error while collecting data:", error);
        }
    };

    return <div className="main-content">
        <h4 className='sub-section-title'>📚 Your Classes:</h4>
        <div className="class-container">
            {Object.entries(cData).map(([sub, [branch, sem]], idx: number) => (
                <div className="classes" key={idx} onClick={(e) => { e.preventDefault(); RequestData(sub); }}>
                    <div className="subject">{sub}</div>
                    <div className="branch-label"><div className = "faculty-label">Branch:</div> B.Tech [{branch}]</div>
                    <div className="semester"><div className="faculty-label">Semester:</div> {sem}</div>
                </div>
            ))}
        </div>
    </div>
}