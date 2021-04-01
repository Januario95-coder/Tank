import React, { useState, useEffect } from 'react';



class FetchSelectData {
    constructor() {
        this.data = [];
    }
    

    fetching(url) {
        let data = [];
        fetch(url)
            .then(res => res.json())
            .then(result => {
                //console.log(result);
                data = result;
                //console.log(this.data);
                
            })
            .catch(err => console.log(err));
            
        //console.log(this.data);
        return data;
    }
}

const BottomPlates = ({ id, loading }) => {
    const [impressCathodProtection, setImpressCathodProtection] = useState([]);
    const [impressCathodProtectionValue, setImpressCathodProtectionValue] = useState(undefined);
    
    const [sacriCathProte, setSacriCathProte] = useState([]);
    const [sacriCathProteValue, setSacriCathProteValue] = useState('');
    
    const [bottomPlatesInternalCoating, setBottomPlatesInternalCoating] = useState([]);
    const [bottomPlatesInternalCoatingValue, setBottomPlatesInternalCoatingValue] = useState([]);
    
    const [bottomPlatesExternalCoating, setBottomPlatesExternalCoating] = useState([]);
    const [bottomPlatesExternalCoatingValue, setBottomPlatesExternalCoatingValue] = useState([]);
    
    const [storageCondition, setStorageCondition] = useState([]);
    const [storageConditionValue, setStorageConditionValue] = useState([]);
    
    const [typeOfBotton, setTypeOfBotton] = useState([]);
    const [typeOfBottonValue, setTypeOfBottonValue] = useState([]);
    
    const [heatingCoilsInTank, setHeatingCoilsInTank] = useState([]);
    const [heatingCoilsInTankValue, setHeatingCoilsInTankValue] = useState([]);
    
    const [productCorrosivity, setProductCorrosivity] = useState([]);
    const [productCorrosivityValue, setProductCorrosivityValue] = useState([]);
    
    const [foundationType, setFoundationType] = useState([]);
    const [foundationTypeValue, setFoundationTypeValue] = useState([]);
    
    const [heightOfFoundation, setHeightOfFoundation] = useState([]);
    const [heightOfFoundationValue, setHeightOfFoundationValue] = useState([]);
    
    const [effectiveDrainage, setEffectiveDrainage] = useState([]);
    const [effectiveDrainageValue, setEffectiveDrainageValue] = useState([]);
    
    const [scoreFive, setScoreFive] = useState([]);
    
    const [timeToRepair, setTimeToRepair] = useState([]);
    const [timeToRepairValue, setTimeToRepairValue] = useState([]);
    
    const [costOfRepair, setCostOfRepair] = useState([]);
    const [costOfRepairValue, setCostOfRepairValue] = useState([]);
    
    const [drainageMagnitude, setDrainageMagnitude] = useState([]);
    const [drainageMagnitudeValue, setDrainageMagnitudeValue] = useState([]);
    
    
    const [likelihoodOfInjury, setLikelihoodOfInjury] = useState([]);
    const [productFlamability, setProductFlamability] = useState([]);
    const [productToxicity, setProductToxicity] = useState([]);
    const [locationOfTank, setLocationOfTank] = useState([]);
    const [environHazard, setEnvironHazard] = useState([]);
    const [vapourEmission, setVapourEmission] = useState([]);
    
    const [lastInspection, setLastInspection] = useState('');
    const [minThicknessMeasuredPrevInsp, setMinThicknessMeasuredPrevInsp] = useState([]);
    const [minThicknessMeasuredPresentInsp, setMinThicknessMeasuredPresentInsp] = useState('');
    const [periodOfServiceBetweenPrevAndPresentInspe, setPeriodOfServiceBetweenPrevAndPresentInspe] = useState('');
    const [minAllowBottomPlaceThickness, setMinAllowBottomPlaceThickness] = useState('');
    const [ndtMethodUsed, setNdtMethodUsed] = useState([]);
    const [freqOfInternalInsp, setFreqOfInternalInsp] = useState([]);
    const [typeOfInternecting, setTypeOfInternecting] = useState([]);
    
    const [probabilityFactor, setProbabilityFactor] = useState('');
    const [probabilityRating, setProbabilityRating] = useState('');
    const [economicAspectsConsequenceFactor, setEconomicAspectsConsequenceFactor] = useState('');
    const [economicAspectsConseqRating, setEconomicAspectsConseqRating] = useState('');
    const [healthSafetyAspectsconseqFactor, setHealthSafetyAspectsconseqFactor] = useState('');
    const [healthSafetyAspectsConseqRating, setHealthSafetyAspectsConseqRating] = useState('');
    const [environAspectsConsequenceFactor, setEnvironAspectsConsequenceFactor] = useState('');
    const [environAspectsConsequenceRating, setEnvironAspectsConsequenceRating] = useState('');
    const [overallConsequenceFactor, setOverallConsequenceFactor] = useState('');
    const [overallConsequenceRating, setOverallConsequenceRating] = useState('');
    const [riskRating, setRiskRating] = useState('');
    
    const [corrosionRate, setCorrosionRate] = useState('');
    const [accelerationFactorForPitting, setAccelerationFactorForPitting] = useState('');
    const [adjustedCorrosionRate, setAdjustedCorrosionRate] = useState('');
    const [remainingLife, setRemainingLife] = useState('');
    const [confidenceFactor, setConfidenceFactor] = useState('');
    const [confidenceFactorAdjustement, setConfidenceFactorAdjustement] = useState('');
    const [ajustedConfidenceFactor, setAjustedConfidenceFactor] = useState('');
    const [intervalBeforeNextRequiredInspection, setIntervalBeforeNextRequiredInspection] = useState('');
    const [nextInspection, setNextInspection] = useState('');
    
    const [isLoaded, setIsLoaded] = useState(loading);
    const [toggleProbaFactorData, setToggleProbaFactorData] = useState(false);
    const [toggleConseFactorData, setToggleConseFactorData] = useState(false);
    const [toggleInspeData, setToggleInspeData] = useState(false);
    const [toggleResults, setToggleResults] = useState(false);
    const [toggleRiskAssess, setToggleRiskAssess] = useState(false);
    const fetcher = new FetchSelectData();
    
    const fetchProject = () => {
        fetch(`http://127.0.0.1:8000/api/v1/projects/${id}/`)
            .then(res => res.json())
            .then(data => {
                setImpressCathodProtectionValue(
                    data.default_values.probability_factor_data.impresses_cathodic_protect
                );
                setSacriCathProteValue(
                    data.default_values.probability_factor_data.sacrificial_cathodic_propect
                );
                setBottomPlatesInternalCoatingValue(
                    data.default_values.probability_factor_data.bottom_plates_internal_coating_or_linin
                );
                setBottomPlatesExternalCoatingValue(
                    data.default_values.probability_factor_data.bottom_plates_external_coatin
                );
                setStorageConditionValue(
                    data.default_values.probability_factor_data.storage_condition
                );
                setTypeOfBottonValue(
                    data.default_values.probability_factor_data.types_of_bottom
                );
                setHeatingCoilsInTankValue(
                    data.default_values.probability_factor_data.heating_coils_in_tanks
                );
                setProductCorrosivityValue(
                    data.default_values.probability_factor_data.products_corrosivity
                );
                setFoundationTypeValue(
                    data.default_values.probability_factor_data.foundation_types
                );
                setHeightOfFoundationValue(
                    data.default_values.probability_factor_data.heights_of_foundation
                );
                setEffectiveDrainageValue(
                    data.default_values.probability_factor_data.effectiveness_of_drainages
                );
                setTimeToRepairValue(
                    data.default_values.probability_factor_data.time_to_repair
                );
                setCostOfRepairValue(
                    data.default_values.probability_factor_data.cost_of_repair
                );
                setDrainageMagnitudeValue(
                    data.default_values.probability_factor_data.probable_magnitude_of_product_loss
                );
            })
            .catch(err => console.log(err));
    }
    
    const fetchImpressCathodic = () => {
        fetch('http://127.0.0.1:8000/api/v1/selectfields/impress-cathodic/')
            .then(res => res.json())
            .then(data => {
                setImpressCathodProtection(data);
                // console.log(impressCathodProtection);
                setIsLoaded(true);
            })
            .catch(err => console.log(err));
    }
    
    
    const fetchsacriCathProte = () => {
        fetch("http://127.0.0.1:8000/api/v1/selectfields/sacrificial-cathodic/")
            .then(res => res.json())
            .then(data => {
                setSacriCathProte(data);
                //console.log(sacriCathProte);
                setIsLoaded(true);
            })
            .catch(err => console.log(err));
    }
    
    const fetchbottomPlatesInternalCoating = () => {
        fetch("http://127.0.0.1:8000/api/v1/selectfields/internal-coating/")
            .then(res => res.json())
            .then(data => {
                setBottomPlatesInternalCoating(data);
                //console.log(bottomPlatesInternalCoating);
                setIsLoaded(true);
            })
            .catch(err => console.log(err));
    }
    
    const fetchbottomPlatesExternalCoating = () => {
        fetch("http://127.0.0.1:8000/api/v1/selectfields/external-coating/")
            .then(res => res.json())
            .then(data => {
                setBottomPlatesExternalCoating(data);
                //console.log(bottomPlatesExternalCoating);
                setIsLoaded(true);
            })
            .catch(err => console.log(err));
    }
    
    const fetchstorageCondition = () => {
        fetch("http://127.0.0.1:8000/api/v1/selectfields/storage-conditions/")
            .then(res => res.json())
            .then(data => {
                setStorageCondition(data);
                //console.log(storageCondition);
                setIsLoaded(true);
            })
            .catch(err => console.log(err));
    }
    
    const fetchtypeOfBotton = () => {
        fetch("http://127.0.0.1:8000/api/v1/selectfields/type-of-bottom/")
            .then(res => res.json())
            .then(data => {
                setTypeOfBotton(data);
                //console.log(typeOfBotton);
                setIsLoaded(true);
            })
            .catch(err => console.log(err));
    }
    
    const fetchheatingCoilsInTank = () => {
        fetch("http://127.0.0.1:8000/api/v1/selectfields/heating-coils/")
            .then(res => res.json())
            .then(data => {
                setHeatingCoilsInTank(data);
                //console.log(heatingCoilsInTank);
                setIsLoaded(true);
            })
            .catch(err => console.log(err));
    }
    
    const fetchproductCorrosivity = () => {
        fetch("http://127.0.0.1:8000/api/v1/selectfields/product-corrosivity/")
            .then(res => res.json())
            .then(data => {
                setProductCorrosivity(data);
                //console.log(productCorrosivity);
                setIsLoaded(true);
            })
            .catch(err => console.log(err));
    }
    
    const fetchfoundationType = () => {
        fetch("http://127.0.0.1:8000/api/v1/selectfields/foundation-type/")
            .then(res => res.json())
            .then(data => {
                setFoundationType(data);
                //console.log(foundationType);
                setIsLoaded(true);
            })
            .catch(err => console.log(err));
    }
    
    const fetchheightOfFoundation = () => {
        fetch("http://127.0.0.1:8000/api/v1/selectfields/height-of-foundation/")
            .then(res => res.json())
            .then(data => {
                setHeightOfFoundation(data);
                //console.log(heightOfFoundation);
                setIsLoaded(true);
            })
            .catch(err => console.log(err));
    }
    
    
    const fetcheffectiveDrainage = () => {
        fetch("http://127.0.0.1:8000/api/v1/selectfields/effectivenessOf-drainage/")
            .then(res => res.json())
            .then(data => {
                setEffectiveDrainage(data);
                //console.log(effectiveDrainage);
                setIsLoaded(true);
            })
            .catch(err => console.log(err));
    }
    
    const fetchtimeToRepair = () => {
        fetch("http://127.0.0.1:8000/api/v1/selectfields/time-to-repair/")
            .then(res => res.json())
            .then(data => {
                setTimeToRepair(data);
                // console.log(timeToRepair);
                setIsLoaded(true);
            })
            .catch(err => console.log(err));
    }
    
    const fetchcostOfRepair = () => {
        fetch("http://127.0.0.1:8000/api/v1/selectfields/cost-of-repair/")
            .then(res => res.json())
            .then(data => {
                setCostOfRepair(data);
                //console.log(costOfRepair);
                setIsLoaded(true);
            })
            .catch(err => console.log(err));
    }
    
    const fetchdrainageMagnitude = () => {
        fetch("http://127.0.0.1:8000/api/v1/selectfields/drainage-magnitude/")
            .then(res => res.json())
            .then(data => {
                setDrainageMagnitude(data);
                //console.log(drainageMagnitude);
                setIsLoaded(true);
            })
            .catch(err => console.log(err));
    }
    
    const fetchlikelihoodOfInjury = () => {
        fetch("http://127.0.0.1:8000/api/v1/selectfields/likelihood-of-injury/")
            .then(res => res.json())
            .then(data => {
                setLikelihoodOfInjury(data);
                //console.log(likelihoodOfInjury);
                setIsLoaded(true);
            })
            .catch(err => console.log(err));
    }
    
    const fetchproductFlamability = () => {
        fetch("http://127.0.0.1:8000/api/v1/selectfields/likelihood-of-injury/")
            .then(res => res.json())
            .then(data => {
                setProductFlamability(data);
                //console.log(productFlamability);
                setIsLoaded(true);
            })
            .catch(err => console.log(err));
    }
    
    const fetchproductToxicity = () => {
        fetch("http://127.0.0.1:8000/api/v1/selectfields/likelihood-of-injury/")
            .then(res => res.json())
            .then(data => {
                setProductToxicity(data);
                //console.log(productToxicity);
                setIsLoaded(true);
            })
            .catch(err => console.log(err));
    }
    
    const fetchlocationOfTank = () => {
        fetch("http://127.0.0.1:8000/api/v1/selectfields/likelihood-of-injury/")
            .then(res => res.json())
            .then(data => {
                setLocationOfTank(data);
                //console.log(locationOfTank);
                setIsLoaded(true);
            })
            .catch(err => console.log(err));
    }
    
    const fetchenvironHazard = () => {
        fetch("http://127.0.0.1:8000/api/v1/selectfields/environmental-hazard/")
            .then(res => res.json())
            .then(data => {
                setEnvironHazard(data);
                //console.log(environHazard);
                setIsLoaded(true);
            })
            .catch(err => console.log(err));
    }
    
    const fetchvapourEmission = () => {
        fetch("http://127.0.0.1:8000/api/v1/selectfields/vapour-emission/")
            .then(res => res.json())
            .then(data => {
                setVapourEmission(data);
                //console.log(vapourEmission);
                setIsLoaded(true);
            })
            .catch(err => console.log(err));
    }
    
    const fetchndtMethodUsed = () => {
        fetch("http://127.0.0.1:8000/api/v1/selectfields/ndt-method-used/")
            .then(res => res.json())
            .then(data => {
                setNdtMethodUsed(data);
                //console.log(vapourEmission);
                setIsLoaded(true);
            })
            .catch(err => console.log(err));
    }
    
    
    const fetchFreqOfInternalInsp = () => {
        fetch("http://127.0.0.1:8000/api/v1/selectfields/freq-of-internal-insp/")
            .then(res => res.json())
            .then(data => {
                setFreqOfInternalInsp(data);
                //console.log(vapourEmission);
                setIsLoaded(true);
            })
            .catch(err => console.log(err));
    }
    
    const fetchTypeOfInternecting = () => {
        fetch("http://127.0.0.1:8000/api/v1/selectfields/type-of-internecting/")
            .then(res => res.json())
            .then(data => {
                setTypeOfInternecting(data);
                //console.log(data);
                setIsLoaded(true);
            })
            .catch(err => console.log(err));
    }
    

    
    useEffect(() => {
        fetchProject();
        
        fetchImpressCathodic();
        fetchsacriCathProte();
        fetchbottomPlatesInternalCoating();
        fetchbottomPlatesExternalCoating();
        fetchstorageCondition();
        fetchtypeOfBotton();
        fetchheatingCoilsInTank();
        fetchproductCorrosivity();
        fetchfoundationType();
        fetchheightOfFoundation();
        fetcheffectiveDrainage();
        fetchtimeToRepair();
        fetchcostOfRepair();
        fetchdrainageMagnitude();
        fetchlikelihoodOfInjury();
        fetchproductFlamability();
        fetchproductToxicity();
        fetchlocationOfTank();
        fetchenvironHazard();
        fetchvapourEmission();
        fetchndtMethodUsed();
        fetchFreqOfInternalInsp();
        fetchTypeOfInternecting();
    }, []);
    
    
    const handleSubmit = (e) => {
        e.preventDefault();
        console.log('Submitted');
        fetch('http://127.0.0.1:8000/api/v1/update-project-details/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            credentials: 'include',
            body: JSON.stringify({
                id: id,
                impressCathodProtectionValue: impressCathodProtectionValue,
                sacriCathProteValue: sacriCathProteValue,
                bottomPlatesInternalCoatingValue: bottomPlatesInternalCoatingValue,
                bottomPlatesExternalCoatingValue: bottomPlatesExternalCoatingValue,
                storageConditionValue: storageConditionValue,
                typeOfBottonValue: typeOfBottonValue,
                heatingCoilsInTankValue: heatingCoilsInTankValue,
                productCorrosivityValue: productCorrosivityValue,
                foundationTypeValue: foundationTypeValue,
                heightOfFoundationValue: heightOfFoundationValue,
                effectiveDrainageValue: effectiveDrainageValue,
                timeToRepairValue: timeToRepairValue,
                costOfRepairValue: costOfRepairValue,
                drainageMagnitudeValue: drainageMagnitudeValue
            })
        })
            .then(res => res.json())
            .then(data => {
                console.log(data);
            })
            .catch(err => console.log(err));
    }
    
    const impressCathodProtectionHandler = (e) => {
        console.log(e.target.value);
        setImpressCathodProtectionValue(e.target.value);
    }
    
    const sacriCathProteHandler = (e) => {
        console.log(e.target.value);
        setSacriCathProteValue(e.target.value);
    }
    
    const bottomPlatesInternalCoatingHandler = (e) => {
        console.log(e.target.value);
        setBottomPlatesInternalCoatingValue(e.target.value);
    }
    
    const bottomPlatesExternalCoatingHandler = (e) => {
        console.log(e.target.value);
        setBottomPlatesExternalCoatingValue(e.target.value);
    }
    
    const storageConditionValueHandler = (e) => {
        console.log(e.target.value);
        setStorageConditionValue(e.target.value);
    }
    
    const typeOfBottonValueHandler = (e) => {
        console.log(e.target.value);
        setTypeOfBottonValue(e.target.value);
    }
    
    const heatingCoilsInTankValueHandler = (e) => {
        console.log(e.target.value);
        setHeatingCoilsInTankValue(e.target.value);
    }
    
    const productCorrosivityValueHandler = (e) => {
        console.log(e.target.value);
        setProductCorrosivityValue(e.target.value);
    }
    
    const foundationTypeValueHandler = (e) => {
        console.log(e.target.value);
        setFoundationTypeValue(e.target.value);
    }
    
    const heightOfFoundationHandler = (e) => {
        console.log(e.target.value);
        setHeightOfFoundationValue(e.target.value);
    }
    
    const effectiveDrainageValueHandler = (e) => {
        console.log(e.target.value);
        setEffectiveDrainageValue(e.target.value);
    }
    
    const timeToRepairValueHandler = (e) => {
        console.log(e.target.value);
        setTimeToRepairValue(e.target.value);
    }
    
    const costOfRepairValueHandler = (e) => {
        console.log(e.target.value);
        setCostOfRepairValue(e.target.value);
    }
    
    const drainageMagnitudeValueHandler = (e) => {
        console.log(e.target.value);
        setDrainageMagnitudeValue(e.target.value);
    }
    

    

    return (
        <div>
            <h2>Bottom Plates</h2>
            <br />
            <form>
                {isLoaded === true ? (
                    <div>
                        <div>
                            <h4
                                className="data-module"
                                id="proba-factor"
                                onClick={() => setToggleProbaFactorData(!toggleProbaFactorData)}
                            >
                                <span>
                                    Probability Factor Data
                                </span>
                                <span className="toggle-sign">
                                    {toggleProbaFactorData === true ? (
                                        <span>&#9650;</span>
                                    ) : <span>&#9660;</span>}
                                </span>
                            </h4>
                            {toggleProbaFactorData === true ? (
                                <div>
                                    <div className="data-section">
                                        <h6 className="data-title"><b>Above Ground Flat Bottommed Storage Tanks</b></h6>
                                        <div className="select-fields-div">
                                            <SelectField 
                                                fields={impressCathodProtection}
                                                value={impressCathodProtectionValue}
                                                labelValue="Impress Cathodic Protection"
                                                valueHandler={impressCathodProtectionHandler}
                                            />
                                            <SelectField 
                                                fields={sacriCathProte}
                                                value={sacriCathProteValue}
                                                labelValue="Sacrificial Cathodic Protection"
                                                valueHandler={sacriCathProteHandler}
                                            />
                                            <SelectField 
                                                fields={bottomPlatesInternalCoating} 
                                                value={bottomPlatesInternalCoatingValue}
                                                labelValue="Bottom Plates Internal Coating"
                                                valueHandler={bottomPlatesInternalCoatingHandler}
                                            />
                                            <SelectField 
                                                fields={bottomPlatesExternalCoating} 
                                                value={bottomPlatesExternalCoatingValue}
                                                labelValue="Bottom Plates External Coating"
                                                valueHandler={bottomPlatesExternalCoatingHandler}
                                            />
                                        </div>
                                        
                                        <br /> <br />
                                        <h6 className="data-title"><b>Atmospheric Storage Tanks</b></h6>
                                        <div>
                                            <div className="select-fields-div">
                                                <SelectField 
                                                    fields={storageCondition} 
                                                    value={storageConditionValue}
                                                    labelValue="Storage Conditions"
                                                    valueHandler={storageConditionValueHandler}
                                                />
                                                <SelectField
                                                    fields={typeOfBotton}
                                                    value={typeOfBottonValue}
                                                    labelValue="Type Of Botton"
                                                    valueHandler={typeOfBottonValueHandler}
                                                />
                                                <SelectField
                                                    fields={heatingCoilsInTank}
                                                    value={heatingCoilsInTankValue}
                                                    labelValue="Heating Coils In Tank"
                                                    valueHandler={heatingCoilsInTankValueHandler}
                                                />
                                                <SelectField
                                                    fields={productCorrosivity}
                                                    value={productCorrosivityValue}
                                                    labelValue="Product Corrosivity"
                                                    valueHandler={productCorrosivityValueHandler}
                                                />
                                            </div>
                                        </div>
                                        
                                        <br /> <br />
                                        <h6 className="data-title"><b>RBI for Athmospheric Storage Tanks</b></h6>
                                        <div>
                                            <div className="select-fields-div">
                                                <SelectField 
                                                    fields={foundationType}
                                                    value={foundationTypeValue}
                                                    labelValue="Foundation Type"
                                                    valueHandler={foundationTypeValueHandler}
                                                />
                                                <SelectField 
                                                    fields={heightOfFoundation}
                                                    value={heightOfFoundationValue}
                                                    labelValue="Height Of Foundation"
                                                    valueHandler={heightOfFoundationHandler}
                                                />
                                                <SelectField 
                                                    fields={effectiveDrainage}
                                                    value={effectiveDrainageValue}
                                                    labelValue="Effective Drainage"
                                                    valueHandler={effectiveDrainageValueHandler}
                                                />
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            ) : "" }
                            
                            <span />
                            <h4
                                className="data-module"
                                id="conseq-factor"
                                onClick={() => setToggleConseFactorData(!toggleConseFactorData)}
                            >
                                <span>Consequence Factor Data</span>
                                <span className="toggle-sign">
                                    {toggleConseFactorData === true ? (
                                        <span>&#9650;</span>
                                    ) : <span>&#9660;</span>}
                                </span>
                            </h4>
                            {toggleConseFactorData === true ? (
                                <div>
                                    <div className="data-section">
                                        <h6 className="data-title"><b>Economic Aspects</b></h6>
                                        <div className="select-fields-div">
                                            <SelectField
                                                fields={timeToRepair}
                                                value={timeToRepairValue}
                                                labelValue="Time To Repair"
                                                valueHandler={timeToRepairValueHandler}
                                            />
                                            <SelectField
                                                fields={costOfRepair}
                                                value={costOfRepairValue}
                                                labelValue="Cost Of Repair"
                                                valueHandler={costOfRepairValueHandler}
                                            />
                                            <SelectField
                                                fields={drainageMagnitude}
                                                value={drainageMagnitudeValue}
                                                labelValue="Probable Magnitude of Product Loss"
                                                valueHandler={drainageMagnitudeValueHandler}
                                            />
                                        </div>
                                        
                                        <br/>
                                        <h6 className="data-title"><b>Health and Safety Concerns</b></h6>
                                        <div className="select-fields-div">
                                            <SelectField
                                                fields={likelihoodOfInjury}
                                                labelValue="Likelihood Of Injury to Personnel"
                                            />
                                            <SelectField
                                                fields={productFlamability}
                                                labelValue="Product Flamability as per MCSP"
                                            />
                                            <SelectField
                                                fields={productToxicity}
                                                labelValue="Product Toxicity"
                                            />
                                            <SelectField
                                                fields={locationOfTank}
                                                labelValue="Location Of Tank Farm"
                                            />
                                        </div>
                                        
                                        <br/>
                                        <h6 className="data-title"><b>Environmental Aspects</b></h6>
                                        <div className="select-fields-div">
                                            <SelectField
                                                fields={environHazard}
                                                labelValue="Environmetal Hazard to Soil and Water as the Potential to Cause"
                                            />
                                            <SelectField
                                                fields={vapourEmission}
                                                labelValue="Vapour Emission"
                                            />
                                        </div>
                                    </div>
                                </div>
                            ) : "" }
                            
                            <span/>
                            <h4
                                className="data-module"
                                id="inspe-data"
                                onClick={() => setToggleInspeData(!toggleInspeData)}
                            >
                                <span>Inspection Data</span>
                                <span className="toggle-sign">
                                    {toggleInspeData === true ? (
                                        <span>&#9650;</span>
                                    ) : <span>&#9660;</span>}
                                </span>
                            </h4>
                            {toggleInspeData === true ? (
                                <div>
                                    <div className="data-section">
                                        <h6 className="data-title"><b>Economic Aspects</b></h6>
                                        <div className="select-fields-div">
                                            <div className="select-fields-one">
                                                <label htmlFor="last_inspection">Last Inspection</label>
                                                <br />
                                                <input
                                                    type="date"
                                                    id="last_inspection"
                                                    className="select-fields input"
                                                    name="Installation_of_PRD"
                                                    value={lastInspection}
                                                    onChange={(e) => setLastInspection(e.target.value)}
                                                />
                                            </div>
                                            <div className="select-fields-one">
                                                <label htmlFor="">Minimum Thickness Measured During Previous Inspection</label>
                                                <br/>
                                                <input
                                                    type="text"
                                                    className="select-fields input"
                                                    name="Installation_of_PRD"
                                                    value={minThicknessMeasuredPrevInsp}
                                                    onChange={(e) => setMinThicknessMeasuredPrevInsp(e.target.value)}
                                                />
                                            </div>
                                            <div className="select-fields-one">
                                                <label htmlFor="">Period of Service Between Previous Inspection and Present Inspection</label>
                                                <br/>
                                                <input
                                                    type="text"
                                                    className="select-fields input"
                                                    name="Installation_of_PRD"
                                                    value={periodOfServiceBetweenPrevAndPresentInspe}
                                                    onChange={(e) => setPeriodOfServiceBetweenPrevAndPresentInspe(e.target.value)}
                                                />
                                            </div>
                                            <div className="select-fields-one">
                                                <label htmlFor="">Minimum Thickness Measured During Present Inspection</label>
                                                <br/>
                                                <input
                                                    type="text"
                                                    className="select-fields input"
                                                    name="Installation_of_PRD"
                                                    value={minThicknessMeasuredPresentInsp}
                                                    onChange={(e) => setMinThicknessMeasuredPresentInsp(e.target.value)}
                                                />
                                            </div>
                                            <div className="select-fields-one">
                                                <label htmlFor="">Minimum Allowable Bottom Place Thickness</label>
                                                <br/>
                                                <input
                                                    type="text"
                                                    className="select-fields input"
                                                    name="Installation_of_PRD"
                                                    value={minAllowBottomPlaceThickness}
                                                    onChange={(e) => setMinAllowBottomPlaceThickness(e.target.value)}
                                                />
                                            </div>
                                            <SelectField
                                                fields={ndtMethodUsed}
                                                labelValue="Frequency Of Internal Inspection"
                                            />
                                            <SelectField
                                                fields={freqOfInternalInsp}
                                                labelValue="NDT Method Used"
                                            />
                                            <SelectField
                                                fields={typeOfInternecting}
                                                labelValue="NDT Method Used"
                                            />
                                        </div>
                                    </div>
                                </div>
                            ) : ""}
                            <button
                                className="btn-submit"
                                onClick={handleSubmit}
                            >Submit</button>
                            
                            <br/><br/>
                            <h4
                                className="data-module"
                                onClick={() => setToggleRiskAssess(!toggleRiskAssess)}
                            >
                                <span>Results</span>
                                <span className="toggle-sign">
                                    {toggleRiskAssess === true ? (
                                        <span>&#9650;</span>
                                    ) : <span>&#9660;</span>}
                                </span>
                            </h4>
                            {toggleRiskAssess === true ? (
                                <div>
                                    <div className="data-section">
                                        <h6 className="data-title"><b>Risk Assessment</b></h6>
                                        <div className="select-fields-div-results">
                                            <div className="select-fields-one">
                                                <label htmlFor="">Probability Factor</label>
                                                
                                                <input
                                                    type="text"
                                                    className="select-fields input probability-factor"
                                                    name="probability_factor"
                                                    value={probabilityFactor}
                                                    onChange={(e) => setProbabilityFactor(e.target.value)}
                                                    disabled={true}
                                                    style={{
                                                        backgroundColor: "white"
                                                    }}
                                                />
                                            </div>
                                            <div className="select-fields-one">
                                                <label htmlFor="">Probability Rating</label>
                                                
                                                <input
                                                    type="text"
                                                    className="select-fields input probability-rating"
                                                    name="probability_rating"
                                                    value={probabilityRating}
                                                    onChange={(e) => setProbabilityRating(e.target.value)}
                                                    disabled={true}
                                                    style={{
                                                        backgroundColor: "white"
                                                    }}
                                                />
                                            </div>
                                            <div className="select-fields-one">
                                                <label htmlFor="">Economic Aspects Consequence Factor</label>
                                                
                                                <input
                                                    type="text"
                                                    className="select-fields input economic-factor"
                                                    name="economic_aspects_consequence_factor"
                                                    value={economicAspectsConsequenceFactor}
                                                    onChange={(e) => setEconomicAspectsConsequenceFactor(e.target.value)}
                                                    disabled={true}
                                                    style={{
                                                        backgroundColor: "white"
                                                    }}
                                                />
                                            </div>
                                            <div className="select-fields-one">
                                                <label htmlFor="">Economic Aspects Consequence Rating</label>
                                                
                                                <input
                                                    type="text"
                                                    className="select-fields input economic-rating"
                                                    name="economic_aspects_consequence_rating"
                                                    value={economicAspectsConseqRating}
                                                    onChange={(e) => setEconomicAspectsConseqRating(e.target.value)}
                                                    disabled={true}
                                                    style={{
                                                        backgroundColor: "white"
                                                    }}
                                                />
                                            </div>
                                            <div className="select-fields-one">
                                                <label htmlFor="">Health and Safety Aspects Consequence Factor</label>
                                                
                                                <input
                                                    type="text"
                                                    className="select-fields input health-factor"
                                                    name="health_and_safety_aspects_consequence_factor"
                                                    value={healthSafetyAspectsconseqFactor}
                                                    onChange={(e) => setHealthSafetyAspectsconseqFactor(e.target.value)}
                                                    disabled={true}
                                                    style={{
                                                        backgroundColor: "white"
                                                    }}
                                                />
                                            </div>
                                            <div className="select-fields-one">
                                                <label htmlFor="">Health and Safety Aspects Consequence Rating</label>
                                                
                                                <input
                                                    type="text"
                                                    className="select-fields input health-rating"
                                                    name="health_and_safety_aspects_consequence_rating"
                                                    value={healthSafetyAspectsConseqRating}
                                                    onChange={(e) => setHealthSafetyAspectsConseqRating(e.target.value)}
                                                    disabled={true}
                                                    style={{
                                                        backgroundColor: "white"
                                                    }}
                                                />
                                            </div>
                                            <div className="select-fields-one">
                                                <label htmlFor="">Environmental Aspects Consequence Factor</label>
                                                
                                                <input
                                                    type="text"
                                                    className="select-fields input environmental-factor"
                                                    name="environmental_aspects_consequence_factor"
                                                    value={environAspectsConsequenceFactor}
                                                    onChange={(e) => setEnvironAspectsConsequenceFactor(e.target.value)}
                                                    disabled={true}
                                                    style={{
                                                        backgroundColor: "white"
                                                    }}
                                                />
                                            </div>
                                            <div className="select-fields-one">
                                                <label htmlFor="">Environmental Aspects Consequence Rating</label>
                                                
                                                <input
                                                    type="text"
                                                    className="select-fields input environmental-rating"
                                                    name="environmental_aspects_consequence_rating"
                                                    value={environAspectsConsequenceRating}
                                                    onChange={(e) => setEnvironAspectsConsequenceRating(e.target.value)}
                                                    disabled={true}
                                                    style={{
                                                        backgroundColor: "white"
                                                    }}
                                                />
                                            </div>
                                            <div className="select-fields-one">
                                                <label htmlFor="">Overall Consequence Factor</label>
                                                
                                                <input
                                                    type="text"
                                                    className="select-fields input overall-factor"
                                                    name="overall_consequence_factor"
                                                    value={overallConsequenceFactor}
                                                    onChange={(e) => setOverallConsequenceFactor(e.target.value)}
                                                    disabled={true}
                                                    style={{
                                                        backgroundColor: "white"
                                                    }}
                                                />
                                            </div>
                                            <div className="select-fields-one">
                                                <label htmlFor="">Overall Consequence Rating</label>
                                                
                                                <input
                                                    type="text"
                                                    className="select-fields input overall-rating"
                                                    name="overall_consequence_rating"
                                                    value={overallConsequenceRating}
                                                    onChange={(e) => setOverallConsequenceRating(e.target.value)}
                                                    disabled={true}
                                                    style={{
                                                        backgroundColor: "white"
                                                    }}
                                                />
                                            </div>
                                            <div className="select-fields-one">
                                                <label htmlFor="">Risk Rating</label>
                                                
                                                <input
                                                    type="text"
                                                    className="select-fields input risk-rating"
                                                    name="risk_rating"
                                                    value={riskRating}
                                                    onChange={(e) => setRiskRating(e.target.value)}
                                                    disabled={true}
                                                    style={{
                                                        backgroundColor: "white"
                                                    }}
                                                />
                                            </div>
                                        </div>
                                        
                                        <br />
                                        <h6 className="data-title"><b>Remaining Life And Inspection Interval Assessment</b></h6>
                                        <div className="select-fields-div-results">
                                            <div className="select-fields-one">
                                                <label htmlFor="">Corrosion Rate</label>
                                                
                                                <input
                                                    type="text"
                                                    className="select-fields input corrosion-rate"
                                                    name="corrosion_rate"
                                                    value={corrosionRate}
                                                    onChange={(e) => setCorrosionRate(e.target.value)}
                                                    disabled={true}
                                                    style={{
                                                        backgroundColor: "white"
                                                    }}
                                                />
                                            </div>
                                            <div className="select-fields-one">
                                                <label htmlFor="">Acceleration Factor for Pitting</label>
                                                
                                                <input
                                                    type="text"
                                                    className="select-fields input acceleration-factor-pitting"
                                                    name="acceleration_factor_for_pitting"
                                                    value={accelerationFactorForPitting}
                                                    onChange={(e) => setAccelerationFactorForPitting(e.target.value)}
                                                    disabled={true}
                                                    style={{
                                                        backgroundColor: "white"
                                                    }}
                                                />
                                            </div>
                                            <div className="select-fields-one">
                                                <label htmlFor="">Adjusted Corrosion Rate</label>
                                                <input
                                                    type="text"
                                                    className="select-fields input adjusted-corrosion-rate"
                                                    name="adjusted_corrosion_rate"
                                                    value={adjustedCorrosionRate}
                                                    onChange={(e) => setAdjustedCorrosionRate(e.target.value)}
                                                    disabled={true}
                                                    style={{
                                                        backgroundColor: "white"
                                                    }}
                                                />
                                            </div>
                                            <div className="select-fields-one">
                                                <label htmlFor="">Remaining Life</label>
                                                <input
                                                    type="text"
                                                    className="select-fields input remaining-life"
                                                    name="remaining_life"
                                                    value={remainingLife}
                                                    onChange={(e) => setRemainingLife(e.target.value)}
                                                    disabled={true}
                                                    style={{
                                                        backgroundColor: "white"
                                                    }}
                                                />
                                            </div>
                                            <div className="select-fields-one">
                                                <label htmlFor="">Confidence Factor</label>
                                                <input
                                                    type="text"
                                                    className="select-fields input confidence-factor"
                                                    name="confidence_factor"
                                                    value={confidenceFactor}
                                                    onChange={(e) => setConfidenceFactor(e.target.value)}
                                                    disabled={true}
                                                    style={{
                                                        backgroundColor: "white"
                                                    }}
                                                />
                                            </div>
                                            <div className="select-fields-one">
                                                <label htmlFor="">Confidence Factor Adjustement</label>
                                                <input
                                                    type="text"
                                                    className="select-fields input confidence-factor-adjustement"
                                                    name="confidence_factor_adjustement"
                                                    value={confidenceFactorAdjustement}
                                                    onChange={(e) => setConfidenceFactorAdjustement(e.target.value)}
                                                    disabled={true}
                                                    style={{
                                                        backgroundColor: "white"
                                                    }}
                                                />
                                            </div>
                                            <div className="select-fields-one">
                                                <label htmlFor="">Ajusted Confidence Factor</label>
                                                <input
                                                    type="text"
                                                    className="select-fields input ajusted-confidence-factor"
                                                    name="ajusted_confidence_factor"
                                                    value={ajustedConfidenceFactor}
                                                    onChange={(e) => setAjustedConfidenceFactor(e.target.value)}
                                                    disabled={true}
                                                    style={{
                                                        backgroundColor: "white"
                                                    }}
                                                />
                                            </div>
                                            <div className="select-fields-one">
                                                <label htmlFor="">Interval Before Next Required Inspection</label>
                                                <input
                                                    type="text"
                                                    className="select-fields input before-next-inspection"
                                                    name="interval_before_next_required_inspection"
                                                    value={intervalBeforeNextRequiredInspection}
                                                    onChange={(e) => setIntervalBeforeNextRequiredInspection(e.target.value)}
                                                    disabled={true}
                                                    style={{
                                                        backgroundColor: "white"
                                                    }}
                                                />
                                            </div>
                                            <div className="select-fields-one">
                                                <label htmlFor="">Next Inspection</label>
                                                <input
                                                    type="text"
                                                    className="select-fields input next-inspection"
                                                    name="next_inspection"
                                                    value={nextInspection}
                                                    onChange={(e) => setNextInspection(e.target.value)}
                                                    disabled={true}
                                                    style={{
                                                        backgroundColor: "white"
                                                    }}
                                                />
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            ) : ""}
                        </div>
                    </div>
                ) : ""}
            </form>
        </div>
    );
};


const SelectField = ({ fields, value, labelValue, valueHandler }) => {
    
    if (value !== undefined) {
        fields = fields.filter((field) => {
            return field.id !== value.id
        })
    }
    
    return (
        <div className="select-fields-one">
            <label htmlFor="impressCathodProtection">{labelValue}</label>
            <br />
            <select
                className="select-fields"
                id="impressCathodProtection"
                value={value}
                onChange={valueHandler}
            >
                {value !== undefined ? (
                    <option
                        value={value.name}
                    >{value.name}</option>
                    ) : ""
                }
                {fields.map((value, index) => {
                    return (
                        <option 
                            key={index}
                            value={value.name}
                        >
                            {value.name}
                        </option>
                    );
                })}
            </select>
        </div>
    );
}

export default BottomPlates;
