import React from 'react';
import { Link } from 'react-router-dom';

const Sidebar = () => {
	return (
		<ul id='mySidenav' className='sidenav'>
			<li>
				<Link to="/home">Tank Dashboard</Link>
			</li>
			<li>
				<Link to="/projects">Projects</Link>
			</li>
			<li>
				<Link to="/logout">Logout</Link>
			</li>
		</ul>
	);
};

export default Sidebar;