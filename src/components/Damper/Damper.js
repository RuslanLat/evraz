import { useState } from 'react';
import './Damper.css';

const Damper = ({positionDumper}) => {

    const [position, setPosition] = useState(positionDumper);

    const dumpPosition = 297 + (+position * 0.71);

    return(
        <>
            <div className="dumper" style={{right:dumpPosition}}>
                <div className="line"></div>
                <div className="line_y"></div>
            </div>
            <div className="dumper_percent">
                {position}%
            </div>
        </>
    )
}

export default Damper;