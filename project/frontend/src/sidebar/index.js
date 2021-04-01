import React from 'react';
import {
	BrowserRouter as Router,
	Route,
	Switch
} from 'react-router-dom';
import Tanker from './Tanker';
import Projects from './Projects';
import Logout from './Logout';

import Sidebar from './Sidebar';


const ReactRouterSetup = () => {
	return (
		<Router>
            <Sidebar />
			<Switch>
				<Route path='/home'>
					<Tanker />
				</Route>
				<Route path='/projects'>
					<Projects loading={false} />
				</Route>
				<Route path='/logout'>
                    {/*<Logout />*/}
				</Route>
			</Switch>
        </Router>
	);
};

export default ReactRouterSetup;


// import bitly_api
// import os

// BITLY_ACCESS_TOKEN = os.getenv('BITLY_ACCESS_TOKEN')
// access = bitly_api.Connection(access_token=BITLY_ACCESS_TOKEN)
// full_link = 'https://janu-voting-system.netlify.app/'
// short_url = access.shorten(full_link)