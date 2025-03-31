import {Routes, Route, Navigate} from 'react-router-dom';
import Login from './login/login.tsx';
import './index.css';

function App() {
  return (
      <Routes>
        <Route path="*" element={<Navigate to="/login" replace />} />
        <Route path="/login" element={<Login />} />
        {/*add other routes here*/}
      </Routes>
  );
}

export default App;