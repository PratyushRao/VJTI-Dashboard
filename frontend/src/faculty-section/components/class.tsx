import back from './image.png';

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

export default function Students() {


  
  return <div className="subject-main-content">
    <div className="back" ><lord-icon
    src="https://cdn.lordicon.com/vduvxizq.json"
    trigger="hover"
    colors="primary:#ae152d"
    style={{width:'40px',height:'50px',"rotate":"180deg","cursor":"pointer"}}>
</lord-icon></div>
    <div className="subject-title" >CHEM</div>
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
        <tr className='table-row'>
          <td className='td-elements' >211090004 </td>
          <td className='td-elements' >Sanya Patel</td>
          <td className='td-elements' > BC<lord-icon
            src="https://cdn.lordicon.com/iubtdgvu.json"
            trigger="hover"
            stroke="bold"
            colors="primary:#1a1b25,secondary:#ae152d"
            style={{ width: "25px", height: "25px", "padding-top": "6px" }}>
          </lord-icon></td>
          <td className='td-elements' ><lord-icon
            src="https://cdn.lordicon.com/xcrmpfbb.json"
            trigger="hover"
            stroke="bold"
            colors="primary:#1a1b25,secondary:#ae152d"
            style={{ width: "25px", height: "25px", "padding-top": "6px" }}>
          </lord-icon> 16 <lord-icon
            src="https://cdn.lordicon.com/mfdeeuho.json"
            trigger="hover"
            stroke="bold"
            colors="primary:#1a1b25,secondary:#ae152d"
            style={{ width: "25px", height: "25px", "padding-top": "6px" }}>
            </lord-icon></td>
        </tr>
        <tr className='table-row'>
          <td className='td-elements' >211090004 </td>
          <td className='td-elements' >Sanya Patel</td>
          <td className='td-elements' > BC<lord-icon
            src="https://cdn.lordicon.com/iubtdgvu.json"
            trigger="hover"
            stroke="bold"
            colors="primary:#1a1b25,secondary:#ae152d"
            style={{ width: "25px", height: "25px", "padding-top": "6px" }}>
          </lord-icon> </td>
          <td className='td-elements' ><lord-icon
            src="https://cdn.lordicon.com/xcrmpfbb.json"
            trigger="hover"
            stroke="bold"
            colors="primary:#1a1b25,secondary:#ae152d"
            style={{ width: "25px", height: "25px", "padding-top": "6px" }}>
          </lord-icon> 25 <lord-icon
            src="https://cdn.lordicon.com/mfdeeuho.json"
            trigger="hover"
            stroke="bold"
            colors="primary:#1a1b25,secondary:#ae152d"
            style={{ width: "25px", height: "25px", "padding-top": "6px" }}>
            </lord-icon></td>
        </tr>
        <tr className='table-row'>
          <td className='td-elements' >211090004 </td>
          <td className='td-elements' >Sanya Patel</td>
          <td className='td-elements' > BC<lord-icon
            src="https://cdn.lordicon.com/iubtdgvu.json"
            trigger="hover"
            stroke="bold"
            colors="primary:#1a1b25,secondary:#ae152d"
            style={{ width: "25px", height: "25px", "padding-top": "6px" }}>
          </lord-icon> </td>
          <td className='td-elements' ><lord-icon
            src="https://cdn.lordicon.com/xcrmpfbb.json"
            trigger="hover"
            stroke="bold"
            colors="primary:#1a1b25,secondary:#ae152d"
            style={{ width: "25px", height: "25px", "padding-top": "6px" }}>
          </lord-icon> 22 <lord-icon
            src="https://cdn.lordicon.com/mfdeeuho.json"
            trigger="hover"
            stroke="bold"
            colors="primary:#1a1b25,secondary:#ae152d"
            style={{ width: "25px", height: "25px", "padding-top": "6px" }}>
            </lord-icon></td>
        </tr>
      </tbody>
    </table>
  </div>

}