
const cData = sessionStorage.getItem("user") ? JSON.parse(sessionStorage.getItem("user") || "").classData : "CD";
export default function MainContent(){
    return <div className="main-content">
        <div className='title'>Your Classes:</div>
        <div className="class-container">
            {Object.entries(cData).map(([sub, [branch, sem]], idx: number) => (
                <div className="classes" key={idx}>
                    <div className="subject">{sub}</div>
                    <div className="year">{`Branch: BTech ${branch}, Semester: ${sem}`}</div>
                </div>
            ))}
        </div>
    </div>
}