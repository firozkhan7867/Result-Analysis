import React, { Component } from 'react';
import Chart from '../../components/chart/Chart';
import FeaturedInfo from '../../components/featuredinfo/FeaturedInfo';
import "./home.css";
import {userData} from "../../dummyData";
import WidgetSm from '../../components/widgetSm/WidgetSm';
import WidgetLg from '../../components/widgetLg/WidgetLg';
import Combo from '../../components/chart/Combo';
class Home  extends Component{

    render() {
        
    
        return ( 
            <div className='home'>
                <FeaturedInfo  failCountData={this.props.failCount} passCountData={this.props.passCount} RegisteredData={this.props.Registered} />
                <Combo back_data={this.props.Backdata} cgpa_data={this.props.CGPA} />
                <Chart data={userData} title="User Analytics" grid datakey="Active User" />
                <div className="homeWidgets">
                    <WidgetSm />
                    <WidgetLg /> 
                </div>
            </div>
        );
    }
}

export default Home;

