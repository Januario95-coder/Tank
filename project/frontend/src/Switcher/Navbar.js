import React from 'react';
import { Link } from 'react-router-dom';


const Navbar = () => {
    return (
        <nav>
            <ul className="list-header">
                <li>
                    <Link to="">Homepage</Link>
                </li>
                <li>
                    <Link to="/project">New Project</Link>
                </li>
				<li>
                    <Link to="/about">Results</Link>
                </li>
            </ul>
        </nav>
    );
};

export default Navbar;
