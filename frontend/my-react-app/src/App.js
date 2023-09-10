import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Home from 'C:/code/crmReactDjango/crmReact/frontend/my-react-app/src/components/Home'; 


function App() {
  return (
    <Router>
      <Routes>
        <Route exact path="/home" component={Home} />
        {/* Agrega más rutas según sea necesario */}
      </Routes>
    </Router>
  );
}

export default App;
