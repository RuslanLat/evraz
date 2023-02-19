import './Excauster.css';
import ExcausterTable from '../ExcausterTable/ExcausterTable';

const Excauster = () => {
    return(
        <div className="wrapper">
            <ExcausterTable name='9 ПС' t={220} top='362px' left='25px'/>
            <ExcausterTable name='8 ПС' t={220}  v={8} g={0} o={0} top='369px' left='25px'/>
            <ExcausterTable name='4 ПС' t={220} top='17px' left='431px'/>
            <ExcausterTable name='6 ПС' t={220} top='198px' left='431px'/>
            <ExcausterTable name='7 ПС' t={220} v={8} g={0} o={0} top='203px' left='431px'/>
            <ExcausterTable name='3 ПС' t={220} bottom='247px' left='576px'/>
            <ExcausterTable name='5 ПС' t={220} bottom='63px' left='576px'/>
            <ExcausterTable name='2 ПС' t={220}  v={8} g={0} o={0} bottom='129px' left='712px'/>
            <ExcausterTable name='1 ПС' t={220}  v={8} g={0} o={0} bottom='255px' left='1009px'/>
        </div>   
    )
}

export default Excauster;
