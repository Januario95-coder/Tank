import React from 'react';
// react router
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
// pages
import Home from './Home';
import About from './About';
import Newproject from './Newproject';


// navbar
import Navbar from './Navbar';

const ReactRouterSetup = () => {
    return (
        <Router>
            <Navbar />
            <Switch>
                <Route exact path='/'>
                    <Home />
                </Route>
                <Route path='/about'>
                    <About />
                </Route>
				<Route path='/project'>
                    <Newproject />
                </Route>
            </Switch>
        </Router>
    );
};

export default ReactRouterSetup;
