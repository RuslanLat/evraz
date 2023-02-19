import { useState } from 'react';
import classNames from 'classnames';
import './OilTank.css';

const OilTank = ({OilLevel}) => {

    const [level, setLevel] = useState(OilLevel);

    const OilTankStyle = classNames({
        'OilTank_fill': true,
        'warning': OilLevel  <= 20 && OilLevel > 10,
        'danger' : OilLevel <= 10 
    });

    return(
        <div className="OilTank_wrapper">
        <div className={OilTankStyle} style={{width: `${level}%`}}>
            {level} <br />            
        </div>
        <span className='OilTank_fill_text'>УРОВЕНЬ МАСЛА, %</span>
    </div>
    )
}

export default OilTank;