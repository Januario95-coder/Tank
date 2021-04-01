import { Link } from 'react-router-dom';
import Header from './components/Header';
//import Sidebar from './components/Sidebar';
import Switcher from './Switcher';
import Sidebar from './sidebar';


const App = () => {
	return (
		<div className="main">
			<>
				<Sidebar />
			</>
			{/*<div>
				<Switcher />
			</div>
			*/}
		</div>
	);
}

export default App;
