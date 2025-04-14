export default function Students(){
    return <div className="subject-main-content">
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
        <td className='td-elements' > BC </td>
        <td className='td-elements' > 78.60</td>
      </tr>
      <tr className='table-row'>
        <td className='td-elements' >211090004 </td>
        <td className='td-elements' >Sanya Patel</td>
        <td className='td-elements' > BC </td>
        <td className='td-elements' > 78.60</td>
      </tr>
      <tr className='table-row'>
        <td className='td-elements' >211090004 </td>
        <td className='td-elements' >Sanya Patel</td>
        <td className='td-elements' > BC </td>
        <td className='td-elements' > 78.60</td>
      </tr>
  </tbody>
</table>
  </div>

}