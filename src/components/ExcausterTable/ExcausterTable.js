import './ExcausterTable.css';
import classNames from 'classnames';
import { useState } from 'react';

const ExcausterTable = ({name, t, v = null, g = null, o = null, top = null, bottom = null, left = null, right = null}) => {

    const [temp, setTemp] = useState(t);
    const [vert, setVert] = useState(v);
    const [horizontal, setHorizontal] = useState(g);
    const [os, setOs] = useState(o);

    const tempStyle = classNames({
        'box_temp box_values': true,
        'warning': t >= 65 && t < 75,
        'danger' : t >= 75
    });

    const vertStyle = classNames({
        'box_values': true,
        'warning': v >= 4.5 && t < 7.1,
        'danger' : v >= 7.1
    });

    const horizontalStyle = classNames({
        'box_values': true,
        'warning': g >= 4.5 && t < 7.1,
        'danger' : g >= 7.1
    });

    const osStyle = classNames({
        'box_values': true,
        'warning': o >= 4.5 && t < 7.1,
        'danger' : o >= 7.1
    });


    return(
        <div className="box" style={{top: top, bottom: bottom, left:left, right:right}}>
        <div className="box_title">{name}</div>
       {temp!== null? <div className={tempStyle}>
          T, ℃ <span>{temp}</span>
        </div> : null}
        {vert!== null? <div className={vertStyle}>В,мм/с<span>8</span></div>: null}
        {horizontal!== null? <div className={horizontalStyle}>Г,мм/с<span>00</span></div>: null}
        {os!== null? <div className={osStyle}>О,мм/с<span>00</span></div>: null}
      </div>
    )
}

export default ExcausterTable;