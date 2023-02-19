import { useState } from 'react';
import './MainDrive.css'

const MainDrive = ({propAmperageA, propAmperageDrive, PropVoltageRoter, PropVoltageStarter}) => {

    const [amperageA, setAmperageA] = useState(propAmperageA);
    const [amperageDrive, setAmperageDrive] = useState(propAmperageDrive);
    const [voltageRoter, setVoltageRoter] = useState(PropVoltageRoter);
    const [voltageStarter, setVoltageStarter] = useState(PropVoltageStarter);

    return(
        <div className="MainDrive_wrapper">
            <div className="MainDrive_title">
                Главный привод
            </div>
            <div className="MainDrive_values">
                <div className="MainDrive_values_elem">
                    <div className="MainDrive_values_elem_title"><b>Ток,</b> А</div>
                </div>
                <div className="MainDrive_values_elem_value">
                    {amperageA}
                </div>
            </div>
                
            <div className="MainDrive_values">
                <div className="MainDrive_values_elem">
                    <div className="MainDrive_values_elem_title"><b>Ток двигателя,</b> А</div>
                </div>
                <div className="MainDrive_values_elem_value">
                    {amperageDrive}
                </div>
            </div>

            <div className="MainDrive_values">
                <div className="MainDrive_values_elem">
                    <div className="MainDrive_values_elem_title"><b>Напряжение ротора,</b> кВт</div>
                </div>
                <div className="MainDrive_values_elem_value">
                    {voltageRoter}
                </div>
            </div>

            <div className="MainDrive_values">
                <div className="MainDrive_values_elem">
                    <div className="MainDrive_values_elem_title"><b>Напряжение статера,</b> кВт</div>
                </div>
                <div className="MainDrive_values_elem_value">
                    {voltageStarter}
                </div>
            </div>

        </div>
    )
}
 export default MainDrive;