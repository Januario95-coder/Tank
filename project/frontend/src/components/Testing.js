import React, { useState, useEffect } from 'react';


const Testing = () => {
	const [projectName, setProjectName] = useState('');
	const [prdFunction, setPrdFunction] = useState('');
    const [creationDate, setCreationDate] = useState('');
	
	const [valuesToSubmit, setValuesToSubmit] = useState({
        id: 1,
		PRD_identification_number: '',
		PRD_function: ''
	});
	
	
	const handleSubmit = (e) => {
        e.preventDefault();
        let data = {
            project_name: projectName,
            project_function: prdFunction,
            creation_date: creationDate
        }
        console.log(data);
		fetch('http://127.0.0.1:8000/api/create-project/', {
			method: 'post',
			headers: {
				'Content-Type': 'application/json'
			},
			credentials: 'include',
			body: JSON.stringify(data),
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
			})
			.catch(err => console.log(err));
	}
	
	useEffect(() => {
		//
	}, []);
	
	
	
	return (
		<div className="menu-session">
			<div className="create-prd">
				<form onSubmit={handleSubmit}>
					<div className="gen-form-row">
						<input 
							type="text"
							placeholder="Project Name"
							name="project_name"
							value={projectName}
                            required={true}
							onChange={e => setProjectName(e.target.value)}
						/>
						<input
							type="text"
							placeholder="PRD Function"
							name="PRD_function"
							value={prdFunction}
                            required={true}
							onChange={e => setPrdFunction(e.target.value)}
						/>
						<input
							type="date"
							placeholder="Creation Date"
							name="creation_date"
							value={creationDate}
                            required={true}
							onChange={e => setCreationDate(e.target.value)}
						/>
					</div>
					<button 
						className="btn-create-tanker"
					>Save Tank</button>
				</form>
			</div>
		</div>
	);
};

export default Testing;