import { useEffect, useState } from 'react';
import { toast } from 'react-toastify';

declare namespace JSX {
  interface IntrinsicElements {
    'lord-icon': any;
  }
}


const sub = sessionStorage.getItem("sub") ? JSON.parse(sessionStorage.getItem("sub") || "") : "";
const subject = sessionStorage.getItem("subject") ? JSON.parse(sessionStorage.getItem("subject") || "") : "";

export default function Students() {
  const [students, setStudents] = useState<[]>([]);
  const [editId, setEditId] = useState<number | null>(null);
  const [selectedGrade, setSelectedGrade] = useState('AA');

  const handleChange = (event) => {
    setSelectedGrade(event.target.value);
  };

  useEffect(() => {
    const storedStudents = JSON.parse(sessionStorage.getItem("subject") || "[]");
    setStudents(storedStudents);
  }, []);

  const back = async () => {
    sessionStorage.getItem("sub") && sessionStorage.removeItem("sub");
    sessionStorage.getItem("subject") && sessionStorage.removeItem("subject");
    window.location.href = `/faculty`;

  }


  const addAtt = async (sub: string, reg: number, name: string) => {
    try {
      const response = await fetch("http://localhost:8000/addAttendance", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ sub, reg, name }),
      });

      const data = await response.json();
      const att = data.Attendance;

      const details = JSON.parse(sessionStorage.getItem("subject"));

      const updatedDetails = details?.map(student => {
        if (student.NAME === name && student.REG_NO === reg) {
          return { ...student, Attendance: att };
        }
        return student;
      });

      setStudents(updatedDetails);
      sessionStorage.setItem("subject", JSON.stringify(updatedDetails))


    } catch (error) {
      alert("Invalid");
      console.error("Error while editing data:", error);
    }
  };

  const subtractAtt = async (sub: string, reg: number, name: string) => {

    try {
      const response = await fetch("http://localhost:8000/subAttendance", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ sub, reg, name }),
      });

      const data = await response.json();
      const att = data.Attendance;

      const details = JSON.parse(sessionStorage.getItem("subject"));

      const updatedDetails = details?.map(student => {
        if (student.NAME === name && student.REG_NO === reg) {
          return { ...student, Attendance: att };
        }
        return student;
      });

      setStudents(updatedDetails);
      sessionStorage.setItem("subject", JSON.stringify(updatedDetails));
    } catch (error) {
      alert("Invalid");
      console.error("Error while editing data:", error);
    }
  }

  const saveGrade = async (sub: string, reg: number, name: string, grade) => {
    setEditId(null);

    try {
      const response = await fetch("http://localhost:8000/changeGrade", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ sub, reg, name, grade }),
      });

      const data = await response.json();
      const gr = data.GRADE;

      const details = JSON.parse(sessionStorage.getItem("subject"));

      const updatedDetails = details?.map(student => {
        if (student.NAME === name && student.REG_NO === reg) {
          return { ...student, GRADE: gr };
        }
        return student;
      });

      setStudents(updatedDetails);
      sessionStorage.setItem("subject", JSON.stringify(updatedDetails));
      toast.success('Grade Edited!', {
        position: "top-right",
        autoClose: 3000,
        hideProgressBar: false,
        closeOnClick: false,
        pauseOnHover: true,
        draggable: true,
        progress: undefined,
        theme: "dark",
    });

    } catch (error) {
      alert("Invalid");
      console.error("Error while editing data:", error);
    }

  }


  return <div className="subject-main-content">

    <div className="back" ><lord-icon onClick={(e) => { e.preventDefault(); back(); }}
      src="https://cdn.lordicon.com/vduvxizq.json"
      trigger="hover"
      colors="primary:#ae152d"
      style={{ width: '2.5rem', height: '2.5rem', "rotate": "180deg", "cursor": "pointer" }}>
    </lord-icon></div>
    <div className="subject-title" >{sub}</div>
    <div className="subject-details">
      <div className="branch">Branch: {subject[0].BRANCH}</div>
      <div className="sem">Sem: {subject[0].SEM}</div>
    </div>
    <table className='student-table'>
      <thead className='table-header'>
        <tr>
          <th className='th-elements'>Registration Number</th>
          <th className='th-elements'>Name</th>
          <th className='th-elements'>Grade</th>
          <th className='th-elements'>Attendance</th>

        </tr>
      </thead>
      <tbody>

        {students.map((item) => (
          editId !== item.REG_NO ? (
            <tr className='table-row' key={item.REG_NO}>
              <td className='td-elements'>{item.REG_NO}</td>
              <td className='td-elements'>{item.NAME}</td>
              <td className='td-elements'>
                {item.GRADE}

                <lord-icon
                  onClick={(e) => { e.preventDefault(); setEditId(item.REG_NO); }}
                  src="https://cdn.lordicon.com/iubtdgvu.json"
                  trigger="hover"
                  stroke="bold"
                  colors="primary:#1a1b25,secondary:#ae152d"
                  style={{ width: "25px", height: "25px", paddingTop: "6px" }}
                ></lord-icon>
              </td>
              <td className='td-elements'>
                <lord-icon
                  onClick={(e) => { e.preventDefault(); subtractAtt(sub, item.REG_NO, item.NAME); }}
                  src="https://cdn.lordicon.com/xcrmpfbb.json"
                  trigger="hover"
                  stroke="bold"
                  colors="primary:#1a1b25,secondary:#ae152d"
                  style={{ width: "25px", height: "25px", paddingTop: "6px" }}
                ></lord-icon>
                &nbsp;{item.Attendance}&nbsp;
                <lord-icon
                  onClick={(e) => { e.preventDefault(); addAtt(sub, item.REG_NO, item.NAME); }}
                  src="https://cdn.lordicon.com/mfdeeuho.json"
                  trigger="hover"
                  stroke="bold"
                  colors="primary:#1a1b25,secondary:#ae152d"
                  style={{ width: "25px", height: "25px", paddingTop: "6px" }}
                ></lord-icon>
              </td>
            </tr>
          ) : (
            <tr className='table-row' key={item.REG_NO}>
              <td className='td-elements'>{item.REG_NO}</td>
              <td className='td-elements'>{item.NAME}</td>
              <td className='td-elements'><p className='close' onClick={(e) => { e.preventDefault(); setEditId(null); }}>X</p>
                <select className='select' value={selectedGrade} onChange={handleChange}>
                  <option value="AA">AA</option>
                  <option value="AB">AB</option>
                  <option value="BB">BB</option>
                  <option value="BC">BC</option>
                  <option value="CC">CC</option>
                  <option value="CD">CD</option>
                  <option value="DD">DD</option>
                  <option value="FF">FF</option>
                </select>
                <lord-icon
                  onClick={(e) => { e.preventDefault(); saveGrade(sub, item.REG_NO, item.NAME, selectedGrade); }}
                  src="https://cdn.lordicon.com/ygymzvsj.json"
                  trigger="hover"
                  stroke="bold"
                  colors="primary:#1a1b25,secondary:#ae152d"
                  style={{ width: "25px", height: "25px", paddingTop: "6px" }}>
                </lord-icon>
              </td>
              <td className='td-elements'>
                <lord-icon
                  onClick={(e) => { e.preventDefault(); subtractAtt(sub, item.REG_NO, item.NAME); }}
                  src="https://cdn.lordicon.com/xcrmpfbb.json"
                  trigger="hover"
                  stroke="bold"
                  colors="primary:#1a1b25,secondary:#ae152d"
                  style={{ width: "25px", height: "25px", paddingTop: "6px" }}
                ></lord-icon> {item.Attendance} <lord-icon
                  onClick={(e) => { e.preventDefault(); addAtt(sub, item.REG_NO, item.NAME); }}
                  src="https://cdn.lordicon.com/mfdeeuho.json"
                  trigger="hover"
                  stroke="bold"
                  colors="primary:#1a1b25,secondary:#ae152d"
                  style={{ width: "25px", height: "25px", paddingTop: "6px", }}
                ></lord-icon>
              </td>
            </tr>
          )
        ))}


      </tbody>
    </table>
  </div>

}