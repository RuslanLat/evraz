import { useState } from "react";
import './TempCooler.css'

const TempCooler = ({PropTWaterBeforeCooler, PropTWaterAfterCooler, PropTOilBeforeCooler, PropTOilAfterCooler}) => {

    const [tWaterBeforeCooler, setTWaterBeforeCooler] = useState(PropTWaterBeforeCooler);
    const [tWaterAfterCooler, setTWaterAfterCooler] = useState(PropTWaterAfterCooler);
    const [tOilBeforeCooler, setTOilBeforeCooler] = useState(PropTOilBeforeCooler);
    const [tOilAfterCooler, setTOilAfterCooler] = useState(PropTOilAfterCooler);


    return(
        <>
        <div className="TempCooler_box tWaterBeforeCooler">
            {tWaterBeforeCooler}°С
        </div>
        <div className="TempCooler_box tWaterAfterCooler">
            {tWaterAfterCooler}°С
        </div>
        <div className="TempCooler_box tOilBeforeCooler">
            {tOilBeforeCooler}°С
        </div>
        <div className="TempCooler_box tOilAfterCooler">
            {tOilAfterCooler}°С
        </div>
        </>
        
        
    )
}

export default TempCooler;