import React from 'react';



const TankRoof = () => {
    
    return (
        <div>
            <h2>Tank Roof</h2>
            <select
                className="select-fields"
                id="impressCathodProtection"
            >
                <option 
                    value=""
                >Select Tank</option>
                <option 
                    value="floating-roof"
                >Floating Roof</option>
                <option 
                    value=""
                >Fixed Roof</option>
            </select>
        </div>
    );
};


export default TankRoof;