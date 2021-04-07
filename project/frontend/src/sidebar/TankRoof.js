import React, { useState, useEffect } from 'react';
import {
    BrowserRouter as Router,
    Route,
    Switch,
    Link
} from 'react-router-dom';
import FixedRoof from './FixedRoof';
import FloatingRoof from './FloatingRoof';



const TankRoof = ({ id, loading }) => {
    const [isLoaded, setIsLoaded] = useState(loading);
    const [selectRoof, setSelectRook] = useState('');
    const [tankerName, setTankerName] = useState('');
    const [tankerDescription, setTankerDescription] = useState('');
    
    const [showFloatingRoof, setShowFloatingRoof] = useState(false);
    const [showFixedRoof, setShowFixedRoof] = useState(false);
    
    const fetchProject = () => {
        fetch(`http://127.0.0.1:8000/api/v1/projects/${id}/`)
            .then(res => res.json())
            .then(data => {
                console.log(data);
            })
            .catch(err => console.log(err));
    };
    
    const selectRoofHandler = (e) => {
        let roof = e.target.value;
        if (roof == 'fixed-roof') {
            setShowFloatingRoof(false);
            setShowFixedRoof(true);
        } else if (roof == 'floating-roof') {
            setShowFixedRoof(false);
            setShowFloatingRoof(true);
        }
        setSelectRook(roof);
    }
    
    useEffect(() => {
        fetchProject();
    }, []);
    
    
    return (
        <div>
            <h2>Tank Roofs</h2>
            <div>
                <select
                    className="select-fields"
                    value={selectRoof}
                    onChange={selectRoofHandler}
                >
                    <option value="">Select Roof</option>
                    <option value="fixed-roof">Fixed Roof</option>
                    <option value="floating-roof">Floating Roof</option>
                </select>
            </div>
            
            {showFixedRoof === true ? (
                <FixedRoof />
            ) : ""}
            {showFloatingRoof === true ? (
                <FloatingRoof />
            ) : ""}
            
            
            {/*
            <Router>
                <div>
                    <select
                        className="select-fields"
                        value={selectRoof}
                        onChange={selectRoofHandler}
                    >
                        <option value="">Select Roof</option>
                        <option value="fixed-roof">Fixed Roof</option>
                        <option value="floating-roof">Floating Roof</option>
                    </select>
                </div>
                <Switch>
                    <Route path="/shell/floating-roof">
                        
                    </Route>
                    <Route path="/shell/fixed-roof">
                        
                    </Route>
                </Switch>
            </Router>
            */}
        </div>
    );
};


export default TankRoof;