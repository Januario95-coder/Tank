import React, { useState, useEffect } from 'react';
import ProjectDetail from './ProjectDetail';


let date1 = new Date(2019, 7, 10);
date1 = date1.toLocaleDateString()
let date2 = new Date(2020, 11, 23);
date2 = date2.toLocaleDateString();

const Projects = ({ loading=false }) => {
	const [tankerName, setTankerName] = useState('Tank 1');
	const [tankerDesc, setTankerDesc] = useState('Description of the Tank 1');
	const [startDate, setStartDate] = useState(date1);
	const [endDate, setEndDate] = useState(date2);
	const [user, setUser] = useState('default');
    const [admin, setAdmin] = useState('');
	const [error, setError] = useState('');
	const [tanker, setTanker] = useState({
		tanker_name: tankerName,
		tanker_descri: tankerDesc,
		start_date: startDate,
		end_date: endDate,
		user: user
	});
	const [tankers, setTankers] = useState([tanker]);
    const [allProjects, setAllProjects] = useState([]);
    const [projectIsLoaded, setProjectIsLoaded] = useState(false);
	
    const [createTankUpdate, setCreateTankUpdate] = useState('create')
    const [idToSubmit, setIdToSubmit] = useState(0);
    
    const [isDetailPage, setIsDetailPage] = useState(false);
	const [tankerId, setTankerId] = useState(null);
    const [isLoaded, setIsLoaded] = useState(false);
    
    
	const popupLoginToggle = () => {
		const popup = document.querySelector('.form-create-tank');
		popup.classList.toggle('active');
	}
	
    const getUser = () => {
        fetch('http://127.0.0.1:8000/api/v1/user/')
            .then(res => res.json())
            .then(data => {
                setAdmin(data.user);
            })
            .catch(err => console.log(err));
    }
    
	const handleSubmit = (e) => {
		e.preventDefault();
        console.log(createTankUpdate);
        
		if (user !== 'default') {
            let toSubmit = {
                'name': tankerName,
                'description': tankerDesc,
                'start_date': startDate,
                'end_date': endDate,
                //'default_values': null
            };
                
            if (createTankUpdate === 'create') {
                console.log(createTankUpdate);

                fetch('http://127.0.0.1:8000/api/v1/create-project/', {
                    method: 'POST',
                    headers: {
                            'Content-Type': 'application/json'
                    },
                    credentials: 'include',
                    body: JSON.stringify(toSubmit)
                })
                    .then(res => {
                        if (res.status >= 200 && res.status <= 299) {
                            return res.json();
                        } else {
                            throw Error(res.statusText);
                        }
                    })
                    .then(data => {
                        console.log(data);
                        fetchProjects();
                    })
                    .catch(err => console.log(err));
            } else if (createTankUpdate === 'update') {
                setCreateTankUpdate('create');
                toSubmit.id = idToSubmit;
                fetch('http://127.0.0.1:8000/api/v1/update-project/', {
                    method: 'POST',
                    headers: {
                            'Content-Type': 'application/json'
                    },
                    credentials: 'include',
                    body: JSON.stringify(toSubmit)
                })
                    .then(res => {
                        if (res.status >= 200 && res.status <= 299) {
                            return res.json();
                        } else {
                            throw Error(res.statusText);
                        }
                    })
                    .then(data => {
                        console.log(data);
                        fetchProjects();
                    })
                    .catch(err => console.log(err));
                
            }
                
			popupLoginToggle();
			setError('');
		} else {
			setError('User must be selected');
		}
	}
	
    
    const fetchProjects = () => {
        fetch('http://127.0.0.1:8000/api/v1/projects/')
            .then(res => res.json())
            .then(data => {
                // console.log(data);
                setAllProjects(data);
                setProjectIsLoaded(true);
            })
            .catch(err => console.log(err));
    }
    
    const handleDelete = (e) => {
        fetch(`http://127.0.0.1:8000/api/v1/projects/${e}/`, {
            method: 'DELETE',
            headers: { 
                'Content-Type': 'application/json'
            }
        });
            
        setTimeout(() => {
            fetchProjects();         
        }, 500);
	}
	
	const handleUser = (e) => {
		if (e.target.value !== 'default') {
			setError('');
		} else {
			setError('User must be selected');
		}
		setUser(e.target.value);
	}
    
    const handleDetails = (e) => {
        setTankerId(e);
        setIsDetailPage(true);
    }
    
    const modifyProject = (e) => {
        console.log(e);
        setIdToSubmit(e);
        setCreateTankUpdate('update');
        fetch(`http://127.0.0.1:8000/api/v1/projects/${e}/`)
            .then(res => res.json())
            .then(data => {
                //console.log(data);
                setTankerName(data.name);
                setTankerDesc(data.description);
                setStartDate(data.start_date);
                setEndDate(data.end_date);
            })
            .catch(err => console.log(err));
        
        popupLoginToggle();
    }
	
	useEffect(() => {
        fetchProjects();
        getUser();
	}, []);
			
			
	return (
		<div className="menu-session">
            {isDetailPage === false ? (
                <div>
                    <span className="tanker-header">
                        <i className="fab fa-servicestack"></i>
                        <span>
                            <p className="tanker-title">Create a Tank</p>
                            <span className="tanker-title-summary">Use the button below to create new tank</span>
                        </span>
                    </span>
                    
                    <div className="create-tank-button">
                        <button
                            onClick={popupLoginToggle}
                        >Create Tank</button>
                    </div>
                    
                    <div className="tankers-list">
                        {allProjects !== [] ? 
                            allProjects.map((tanker, index) => {
                                return (
                                    <div 
                                        key={index}
                                        className="tanker-detail"
                                    >
                                        <h3>{tanker.name}</h3>
                                        <p className="tanker-description">
                                            {tanker.description}
                                        </p>
                                        <span 
                                            className="display-dates"
                                        >
                                            <span className="display-date">Start: {tanker.start_date}</span>
                                            <span className="display-date">End: {tanker.end_date}</span>
                                        </span>
                                        <span className="tanker-pdf">
                                            <span>
                                                <i className="far fa-file-pdf"></i>
                                            </span>
                                            <span 
                                                className="modify-project" 
                                                id="modify-project"
                                                onClick={() => modifyProject(tanker.id)}
                                           >
                                                Update
                                            </span>
                                        </span>
                                        <span className="delete-assessment">
                                            <i 
                                                className="fas fa-trash-alt"
                                                onClick={() => handleDelete(tanker.id)}
                                            ></i>
                                            <span
                                                onClick={() => handleDetails(tanker.id)}
                                            >
                                                Assessment <i className="white-space">&nbsp;</i>
                                                <i className="fas fa-chevron-right"></i>
                                            </span>
                                        </span>
                                    </div>
                                );
                            }) : 
                            <div>
                                <p>No Tanker Yet</p>
                            </div>
                        }
                    </div>
                    
                    
                    <div className="create-tank">
                        <form 
                            className="form-create-tank"
                            onSubmit={handleSubmit}
                        >
                            <a className="close-form" onClick={popupLoginToggle}>
                                <img src="/close_red.png" />
                            </a>
                            <input
                                type="input"
                                className="tanker-name"
                                id="tanker-name"
                                value={tankerName}
                                onChange={e => setTankerName(e.target.value)}
                                placeholder="Tanker Name"
                                required={true}
                            />
                            <textarea
                                rows="5"
                                placeholder="Tanker Description"
                                value={tankerDesc}
                                onChange={e => setTankerDesc(e.target.value)}
                                required={true}
                            ></textarea>
                            <span className="dates">
                                <span>
                                    <label
                                        htmlFor="date1"
                                        className="date"
                                    >start date</label>
                                    <input 
                                        type="date" 
                                        id="date1"
                                        className="date1"
                                        value={startDate}
                                        name={startDate}
                                        onChange={e => setStartDate(e.target.value)}
                                        required={true}
                                    />
                                </span>
                                <span>
                                    <label
                                        htmlFor="date2"
                                        className="date"
                                    >end date</label>
                                    <input 
                                        type="date" 
                                        id="date2"
                                        className="date2"
                                        value={endDate}
                                        onChange={e => setEndDate(e.target.value)}
                                        required={true}
                                    />
                                </span>
                            </span>
                            <i style={{
                                color:"red",
                                fontSize:"12px"
                            }}>{error}</i>
                            <select 
                                className="select-user"
                                value={user}
                                onChange={handleUser}
                                required={true}
                            >
                                <option 
                                    value="default"
                                >Select Username</option>
                                <option
                                    value="user1"
                                >{admin}</option>
                            </select>
                            <button 
                                className="btn-create-tanker"
                            >Save Tank</button>
                        </form>
                    </div>
                </div>
            ) : <ProjectDetail 
                    id={tankerId} 
                    loading={loading}
                />
            }
		</div>
	);
};


const TankerList = ({tankers}) => {
	const handleDelete = (e) => {
		console.log(e);
	}
	
	return (
		<div className="tankers-list">
			{tankers.map((tanker, index) => {
				return (
					<div 
						key={index}
						className="tanker-detail"
					>
						<h3>{tanker.tanker_name}</h3>
						<p className="tanker-description">
							{tanker.tanker_descri}
						</p>
						<span>Start date: {tanker.start_date}</span>
						<br />
						<span>End date: {tanker.end_date}</span>
						<br />
						<span className="tanker-pdf">
							<span>
								<i className="far fa-clone"></i>
							</span>
							<span>
								<i className="far fa-file-pdf"></i>
							</span>
						</span>
						<span className="delete-assessment">
							<i 
								className="fas fa-trash-alt"
								onClick={handleDelete}
							></i>
							<span>
								Assessment <i className="white-space">&nbsp;</i>
								<i className="fas fa-chevron-right"></i>
							</span>
						</span>
					</div>
				);
			})}
		</div>
	);
}

export default Projects;