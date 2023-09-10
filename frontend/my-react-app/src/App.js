import React from 'react';
import { BrowserRouter as Router, Route } from 'react-router-dom';
import Home from './components/Home';  // Importa el componente Home
import { Switch } from 'react-router';

function App() {
  return (
    <Router>
      <Switch>
        <Route exact path="/" component={Home} />
        {/* Agrega más rutas según sea necesario */}
      </Switch>
    </Router>
  );
}

export default App;
