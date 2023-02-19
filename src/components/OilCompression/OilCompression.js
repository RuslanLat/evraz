import { useState } from 'react';
import './OilCompression.css';
import classNames from 'classnames';

const OilCompression = ({compressionProp}) => {

    const [compression, setCompression] = useState(compressionProp);

    const OilCompressionStyle = classNames({
        'OilCompression_fill': true,
        'warning': compression  <= 0.5 && compression  > 0.2,
        'danger' : compression <= 0.2
    });

    return(
        <div className="OilCompression_wrapper">
        <div className={OilCompressionStyle} style={{width: `${compression*16.6}%`}}>
            {compression} <br />       
        </div>
        <span className='OilCompression_fill_text'>ДАВЛЕНИЕ МАСЛА, кг/см2 </span>
    </div>
    )
}
export default OilCompression;