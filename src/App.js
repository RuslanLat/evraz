import './App.css';
import ExcausterName from './components/ExcausterName/ExcausterName';
import Excauster from './components/Excauster/Excauster';
import TempGas from './components/TempGas/TempGas';
import OilTank from './components/OilTank/OilTank';
import OilCompression from './components/OilCompression/OilCompression';
import MainDrive from './components/MainDrive/MainDrive';
import TempCooler from './components/TempCooler/TempCooler';
import Damper from './components/Damper/Damper';

function App() {
  return (
    <div className="App">
      <ExcausterName name='X-172'/>
      <Excauster/>
      <TempGas PropTemp={45} PropVacuum={74.3} PropDustLevel={15}/>
      <OilTank OilLevel={19}/>
      <OilCompression compressionProp={5}/>
      <MainDrive propAmperageA={120} propAmperageDrive={10} PropVoltageRoter={50} PropVoltageStarter={80}/>
      <TempCooler PropTWaterBeforeCooler={45} PropTWaterAfterCooler={40} PropTOilBeforeCooler={100} PropTOilAfterCooler={80}/>
      <Damper positionDumper={30}/>
    </div>
  );
}

export default App;
