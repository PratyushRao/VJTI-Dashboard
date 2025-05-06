import { Routes, Route, Navigate } from 'react-router-dom';
import { ToastContainer } from 'react-toastify';
import Login from './login/login.tsx';
import Student from './student-section/student.tsx';
import Faculty from './faculty-section/faculty.tsx';
import Subject from './faculty-section/subject.tsx';
import Edit from './edit-pass/edit.tsx';
import './index.css';

function App() {
  return (<>
    <ToastContainer
                position="top-right"
                autoClose={3000}
                hideProgressBar={false}
                newestOnTop={false}
                closeOnClick={false}
                rtl={false}
                pauseOnFocusLoss
                draggable
                pauseOnHover
                theme="dark"
            />
    
      <Routes>
        <Route path="*" element={<Navigate to="/login" replace />} />
        <Route path="/login" element={<Login />} />
        <Route path="/edit" element={<Edit />} />
        <Route path="/student" element={<Student />} />
        <Route path="/faculty" element={<Faculty />} />
        <Route path="/subject" element={<Subject />} />
        {/*add other routes here*/}
      </Routes>
      </>
  );
}

export default App;