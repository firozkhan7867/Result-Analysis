import React, {Component} from 'react';
import PieChart from "./PieChart";
import Bargraph from "./Bargraph"
import "./featuredinfo.css"
class Combo extends Component {

    
    render(){
       return (
           <div className='featured'>
               <div className="featuredItem ">
                   <h2>Grade Analysis</h2>
                   <br /><br /><br />
                   <PieChart cgpa_data={this.props.cgpa_data} />
                   
               </div>
               <div className="featuredItem ">
                   <h1>BackLog Details and Count</h1>
                   <br />
                   <br /><br /><br /><br /><br />
                   <Bargraph back_data={this.props.back_data} />
                   {/* <Bargraph  /> */}
               </div>
           </div>
       )
    }
}


export default Combo;
