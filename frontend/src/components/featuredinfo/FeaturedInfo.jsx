 import React, {Component} from 'react';
 import "./featuredinfo.css"
 class FeaturedInfo extends Component {
     render(){
        return (
            <div className='featured'>
                <div className="featuredItem total">
                    <span className="featuredTitle">Total Applications</span>
                    <div className="featuredMoneyContainer">
                        <span className="featuredMoney">{this.props.RegisteredData}</span>
                        {/* <span className="featuredMoneyRate"> -11.4   */}
                        {/* <ArrowDownward className='featuredIcon'/> */}
                        {/* </span> */}
                    </div>
                    <span className="featuredSb">
                       Students Registered
                    </span>
                </div>
                <div className="featuredItem pass">
                    <span className="featuredTitle">No of Students Passed</span>
                    <div className="featuredMoneyContainer">
                        <span className="featuredMoney">{this.props.passCountData}</span>
                        {/* <span className="featuredMoneyRate"> -1.4  
                        <ArrowDownward className='featuredIcon negative'/>
                        </span> */}
                    </div>
                    <span className="featuredSb">
                        Students passed
                    </span>
                </div>
                <div className="featuredItem fail">
                    <span className="featuredTitle">No of Students Failed</span>
                    <div className="featuredMoneyContainer">
                        <span className="featuredMoney">{this.props.failCountData}</span>
                        {/* <span className="featuredMoneyRate"> +2.4  
                        <ArrowUpward className='featuredIcon'/></span> */}
                    </div>
                    <span className="featuredSb">
                        Students Failed
                    </span>
                </div>
            </div>
        )
     }
 }


export default FeaturedInfo;
 