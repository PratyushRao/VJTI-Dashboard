declare namespace JSX {
  interface IntrinsicElements {
    'lord-icon': React.DetailedHTMLProps<React.HTMLAttributes<HTMLElement>, HTMLElement> & {
      src?: string;
      trigger?: string;
      colors?: string;
      state?: string;
      style?: React.CSSProperties;
      [key: string]: any;
    };
  }
}

type Student = {
  REG_NO: number;
  NAME: string;
  GRADE: string;
  FACULTY: string;
  BRANCH: string;
  SEM: number;
  Attendance: string;
};

const students= sessionStorage.getItem("subject") ? JSON.parse(sessionStorage.getItem("subject") || "") : [];
const sub = sessionStorage.getItem("sub") ? JSON.parse(sessionStorage.getItem("sub") || "") : "";


export default function Students() {

  const addAtt = async (sub: string, reg:number, name:string) =>{}
  

  const subtractAtt = async (sub: string, reg:number, name:string) =>{}
  
  return <div className="subject-main-content">
    <div className="back" ><lord-icon
    src="https://cdn.lordicon.com/vduvxizq.json"
    trigger="hover"
    colors="primary:#ae152d"
    style={{width:'2.5rem',height:'2.5rem',"rotate":"180deg","cursor":"pointer"}}>
</lord-icon></div>
    <div className="subject-title" >{sub}</div>
    <div className="subject-details">
      <div className="branch">Branch: ExTC</div>
      <div className="sem">Sem: 2</div>
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

      {students.map((item)=>
        <tr className='table-row' key={item.REG_NO}>
          <td className='td-elements' >{item.REG_NO} </td>
          <td className='td-elements' >{item.NAME}</td>
          <td className='td-elements' > {item.GRADE}<lord-icon
            src="https://cdn.lordicon.com/iubtdgvu.json"
            trigger="hover"
            stroke="bold"
            colors="primary:#1a1b25,secondary:#ae152d"
            style={{ width: "25px", height: "25px", "padding-top": "6px" }}>
          </lord-icon></td>
          <td className='td-elements' ><lord-icon onClick={(e) => { e.preventDefault(); subtractAtt(sub,item.REG_NO,item.NAME); }}
            src="https://cdn.lordicon.com/xcrmpfbb.json"
            trigger="hover"
            stroke="bold"
            colors="primary:#1a1b25,secondary:#ae152d"
            style={{ width: "25px", height: "25px", "padding-top": "6px" }}>
          </lord-icon> {item.Attendance} <lord-icon onClick={(e) => { e.preventDefault(); addAtt(sub,item.REG_NO,item.NAME); }}
            src="https://cdn.lordicon.com/mfdeeuho.json"
            trigger="hover"
            stroke="bold"
            colors="primary:#1a1b25,secondary:#ae152d"
            style={{ width: "25px", height: "25px", "padding-top": "6px" }}>
            </lord-icon></td>
        </tr>

)
}

        
      </tbody>
    </table>
  </div>

}