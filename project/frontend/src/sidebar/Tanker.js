import React from 'react';


const Tanker = () => {
	return (
		<div className="Tank-dashboard menu-session">
			<p>Tank Dashboard</p>
			<span className="Tank-header">
				<i className="fab fa-servicestack"></i>
				<span>
					<p className="Tank-title">Tank Dashboard</p>
					<span className="Tank-title-summary">Tank Summary Dashboard</span>
				</span>
			</span>
			
			<div className="image-session">
				<img src="/circle.JPG" alt="image-session" />
			</div>
			
			<div className="Tank-summary">
				<span>Project List</span>
				<br />
				<select className="select-Tank">
					<option value="default">Select Tank</option>
					<option value="Tank1">Tank 1</option>
				</select>
				
				<div>
					<table className="Tank-table">
						<thead>
							<tr className="Tank-table-header">
								<th>S No</th>
								<th className="rest-cell">Tank Name</th>
								<th className="rest-cell">Primary Function</th>
								<th className="rest-cell">Tank Manned Status</th>
								<th className="rest-cell">Tank Risk Ranking</th>
								<th>Exposure Category</th>
								<th className="cell-fixed-width">Selected Next Inspection Intervals (years)</th>
								<th className="cell-fixe-date">Last Inspection Date</th>
								<th className="cell-fixe-date">Next Inspection Date</th>
							</tr>
						</thead>
						<tbody>
							<tr>
								<td>1</td>
								<td>Production</td>
								<td>Yes</td>
								<td>VL</td>
								<td>L-3</td>
								<td>2</td>
								<td>6</td>
								<td></td>
								<td></td>
							</tr>
						</tbody>
					</table>
				</div>
			</div>
		</div>
	);
};

export default Tanker;