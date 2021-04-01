import React, { useState, useEffect } from 'react';
import {
    BrowserRouter as Router,
    Route,
    Switch,
    Link
} from 'react-router-dom';
import BottomPlates from './BottomPlates';
import ShellPlates from './ShellPlates';
import TankRoof from './TankRoof';
import RiskAssess from './RiskAssess';


const ProjectDetail = ({ id, loading }) => {
    const [isLoaded, setIsLoaded] = useState(loading);
    const [tankerName, setTankerName] = useState('');
    const [tankerDescription, setTankerDescription] = useState('');
    
    const fetchProject = () => {
        fetch(`http://127.0.0.1:8000/api/v1/projects/${id}/`)
            .then(res => res.json())
            .then(data => {
                console.log(data);
                setTankerName(data.name);
                setTankerDescription(data.description);
            })
            .catch(err => console.log(err));
    };
    
    useEffect(() => {
        fetchProject();
    }, []);
    
    
    return (
        <div>
            <span className="tanker-header">
                <i className="fab fa-servicestack"></i>
                <span>
                    <p className="tanker-title">{tankerName}</p>
                    <span className="tanker-title-summary">{tankerDescription}</span>
                </span>
            </span>
            <br />
            
            <Router>
                <div>
                    <ul className="plate-types">
                        <li>
                            <Link to="/bottom">Bottom Plate</Link>
                        </li>
                        <li>
                            <Link to="/shell">Shell Plates</Link>
                        </li>
                        <li>
                            <Link to="/roof">Tank Roof</Link>
                        </li>
                        <li>
                            <Link to="/risk">Risk Assessment Result & Inspection Planning</Link>
                        </li>
                    </ul>
                </div>
                <Switch>
                    <Route path="/bottom">
                        <BottomPlates 
                            id={id} 
                        />
                    </Route>
                    <Route path="/shell">
                        <ShellPlates />
                    </Route>
                    <Route path="/roof">
                        <TankRoof />
                    </Route>
                    <Route path="/risk">
                        <RiskAssess />
                    </Route>
                </Switch>
            </Router>
        </div>
    );
};


export default ProjectDetail;