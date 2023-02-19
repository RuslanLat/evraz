import { useState } from 'react'
import './TempGas.css'

const TempGas = ({PropTemp, PropVacuum, PropDustLevel}) => {
    const [temp, setTemp] = useState(PropTemp);
    const [vakuum, setVacuum] = useState(PropVacuum);
    const [dustLevel, setDustLevel] = useState(PropDustLevel);

    return(
    <div className="TempGasWrapper_main">
        <div className="TempGasWrapper">
            <div className="wrapper2">
                <div className="TempGasFill" style={{width: `${temp}%`}}>
                    {temp} <br />            
                </div>
                <span className='TempGasFill_text'>ТЕМПЕРАТУРА ГАЗА, °C</span>
            </div>
        </div>
        <div className="tempGas_values">
                    <div className="tempGas_elem_title">Разряжение, мм.в.ст</div>
                <div className="tempGas_elem_value">
                    {vakuum}
                </div>
        </div>

        <div className="tempGas_values">
                    <div className="tempGas_elem_title">Уровень пыли, мг/м3</div>
                <div className="tempGas_elem_value">
                    {dustLevel}
                </div>
        </div>
    </div>
    )
}

export default TempGas;