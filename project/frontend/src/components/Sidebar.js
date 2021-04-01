import {
	BrowserRouter as Router,
	Route, 
	Switch
} from 'react-router-dom';

const Sidebar = () => {
	const openNav = () => {
		document.getElementById('mySidenav').style.width = '250px';
	}


	const closeNav = () => {
		document.getElementById('mySidenav').style.width = '0';
	}
	
	return (
		<Router>
			<div id='mySidenav' className='sidenav'>
				<Switch>
					<Route path='/'>
						<a href='/'>Tanker</a>
					</Route>
					<Route path='/'>
						<a href='/'>Create Tanker</a>
					</Route>
					<Route path='/'>
						<a href='/'>Projects</a>
					</Route>
					<Route path='/'>
						<a href='/'>Logout</a>
					</Route>
				</Switch>
			</div>
		</Router>
	);
}


export default Sidebar;