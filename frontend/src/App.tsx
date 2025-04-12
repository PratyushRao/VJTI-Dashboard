import {Routes, Route, Navigate} from 'react-router-dom';
import Login from './login/login.tsx';
import Student from './student-section/student.tsx';
import Faculty from './faculty-section/faculty.tsx';
import './index.css';

function App() {
  return (
      <Routes>
        <Route path="*" element={<Navigate to="/login" replace />} />
        <Route path="/login" element={<Login />} />
        <Route path="/student" element={<Student />} />
        <Route path="/faculty" element={<Faculty />} />
        {/*add other routes here*/}
      </Routes>
  );
}

export default App;