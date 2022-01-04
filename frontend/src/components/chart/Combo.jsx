import React, {Component} from 'react';
import PieChart from "./PieChart";
import Bargraph from "./Bargraph"
import "./featuredinfo.css"
class Combo extends Component {
    render(){
       return (
           <div className='featured'>
               <div className="featuredItem ">
                   <PieChart />
               </div>
               <div className="featuredItem ">
                   <Bargraph />
                   <Bargraph />
               </div>
               
           </div>
       )
    }
}


export default Combo;
