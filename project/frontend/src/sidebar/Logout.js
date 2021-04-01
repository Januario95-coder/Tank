import React, { useState, useEffect } from 'react';


const Logout = () => {
	const [typeOfPRD, setTypeOfPRD] = useState([]);
	const [serviceSeverity, setServiceSeverity] = useState([]);
	const [prdDischarge, setPrdDischarge] = useState([]);
	const [environFactor, setEnvironFactor] = useState([]);
	
	const [idNumber, setIdNumber] = useState('');
	const [prdFunction, setPrdFunction] = useState('');
	const [installDate, setInstallDate] = useState('');
	const [assesDate, setAssesDate] = useState('');
	const [typeOfPrdVal, setTypeOfPrdVal] = useState('');
	const [softSeats, setSoftSeats] = useState('');
	const [prdSet, setPrdSet] = useState('');
	const [serviceSeverityVal, setServiceSeverityVal] = useState('');
	const [dischargeVal, setDischargeVal] = useState('');
	const [environFactorVal, setEnvironFactorVal] = useState('');
	const [ruptureDisk, setRuptureDisk] = useState('');
	
	const [valuesToSubmit, setValuesToSubmit] = useState({
        id: 1,
		PRD_identification_number: '',
		PRD_function: '',
		Installation_of_PRD: '',
		RBI_assessment_date: '',
		Type_of_PRD: '',
		PRD_Containing_Soft_Seats: '',
		PRD_set: '',
		Service_severity: '',
		PRD_Discharge_Location: '',
		Environment_Factor_Modifier: '',
		Rupture_disk_is_installed_upstream_of_PRD: '',
		extraField: ''
	});
	
	
	const submitData = () => {
		fetch('http://127.0.0.1:8000/api/submit/', {
			method: 'post',
			headers: {
				'Content-Type': 'application/json'
			},
			credentials: 'include',
			body: JSON.stringify(valuesToSubmit),
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
	
	
	const handleSubmit = (e) => {
		e.preventDefault();
		
		setValuesToSubmit({
            id: 1,
			PRD_identification_number: idNumber,
			PRD_function: prdFunction,
			Installation_of_PRD: installDate,
			RBI_assessment_date: assesDate,
			Type_of_PRD: typeOfPrdVal,
			PRD_Containing_Soft_Seats: softSeats,
			PRD_set: prdSet,
			Service_severity: serviceSeverityVal,
			PRD_Discharge_Location: dischargeVal,
			Environment_Factor_Modifier: environFactorVal,
			Rupture_disk_is_installed_upstream_of_PRD: ruptureDisk,
			extraField: 'extraField'
		});
		console.log(valuesToSubmit);
		setTimeout(() => {
			submitData();
		}, 1000);
	}
	
	
	
	const fetchData = () => {
		fetch('http://127.0.0.1:8000/api/type-of-prd/')
			.then(res => res.json())
			.then(data => {
				setTypeOfPRD(data);
			})
			.catch(err => console.log(err));
			
		fetch('http://127.0.0.1:8000/api/service-severity/')
			.then(res => res.json())
			.then(data => {
				setServiceSeverity(data);
			})
			.catch(err => console.log(err));
			
		fetch('http://127.0.0.1:8000/api/prd-discharge/')
			.then(res => res.json())
			.then(data => {
				setPrdDischarge(data);
			})
			
		fetch('http://127.0.0.1:8000/api/environ-factor/')
			.then(res => res.json())
			.then(data => {
				setEnvironFactor(data);
			})
			.catch(err => console.log(err));
	}
	
	useEffect(() => {
		fetchData();
	}, []);
	
	
	
	return (
		<div className="menu-session">
			<div className="create-prd">
				<form onSubmit={handleSubmit}>
					<div className="gen-form-row">
						<input 
							type="text"
							placeholder="ID Number"
							name="PRD_identification_number"
							value={idNumber}
							onChange={e => setIdNumber(e.target.value)}
						/>
						<input
							type="text"
							placeholder="PRD Function"
							name="PRD_function"
							value={prdFunction}
							onChange={e => setPrdFunction(e.target.value)}
						/>
						<input
							type="datetime-local"
							name="Installation_of_PRD"
							value={installDate}
							onChange={e => setInstallDate(e.target.value)}
						/>
					</div>
					<br />
					<div className="gen-form-row">
						<input 
							type="datetime-local"
							name="RBI_assessment_date"
							value={assesDate}
							onChange={e => setAssesDate(e.target.value)}
						/>
						<select
							name="Type_of_PRD"
							onChange={e => setTypeOfPrdVal(e.target.value)}
						> 
							{typeOfPRD.map((prd, index) => {
								return (
									<option 
										key={index}
										value={prd.name}
									>
										{prd.name}
									</option>
								);
							})}
						</select>
						<select 
							name="PRD_Containing_Soft_Seats"
							onChange={e => setSoftSeats(e.target.value)}
						>
							<option value="Yes">Yes</option>
							<option value="No">No</option>
						</select>
					</div>
					<div className="gen-form-row">
						<input 
							type="text"
							name="PRD_set"
							value={prdSet}
							onChange={e => setPrdSet(e.target.value)}
						/>
						<select
							name="Service_severity"
							onChange={e => setServiceSeverityVal(e.target.value)}
						>
							{serviceSeverity.map((prd, index) => {
								return (
									<option 
										key={index}
										value={prd.name}
									>
										{prd.name}
									</option>
								);
							})}
						</select>
						<select
							name="PRD_Discharge_Location"
							onChange={e => setDischargeVal(e.target.value)}
						>
							{prdDischarge.map((prd, index) => {
								return (
									<option 
										key={index}
										value={prd.name}
									>
										{prd.name}
									</option>
								);
							})}
						</select>
					</div>
					<div className="gen-form-row">
						<select
							name="Environment_Factor_Modifier"
							onChange={e => setEnvironFactorVal(e.target.value)}
						>
							{environFactor.map((prd, index) => {
								return (
									<option 
										key={index}
										value={prd.name}
									>
										{prd.name}
									</option>
								);
							})}
						</select>
						<select
							name="Rupture_disk_is_installed_upstream_of_PRD"
							onChange={e => setRuptureDisk(e.target.value)}
						>
							<option value="Yes">Yes</option>
							<option value="No">No</option>
						</select>
					</div>
					<button 
						className="btn-create-tanker"
					>Save Tank</button>
				</form>
			</div>
		</div>
	);
};

export default Logout;