import React from 'react';
import "./sidebar.css"; 
import {LineStyle, Timeline, TrendingUp,
    Storefront,
    AttachMoney,
    BarChart,
    MailOutline,
    DynamicFeed,
    ChatBubbleOutline,
    WorkOutline,
    Report,
    PermIdentity} from "@material-ui/icons";


const Sidebar = () => {
    return (
        <div className='sidebar'> 
            <div className="sidebarWrapper">
                <div className="sidebarMenu">
                        <h3 className="sidebarTitle"></h3>
                        <ul className="sidebarList">
                        </ul> 
                </div>
                <div className="sidebarMenu">
                        <h3 className="sidebarTitle"></h3>
                        <ul className="sidebarList">
                        </ul> 
                </div>
                <div className="sidebarMenu">
                        <h3 className="sidebarTitle"></h3>
                        <ul className="sidebarList">
                        </ul> 
                </div>
                <div className="sidebarMenu">
                    <h3 className="sidebarTitle">Dashboard</h3>
                    <ul className="sidebarList">
                        <li className="sidebarListItem active">
                            <LineStyle className="sidebarIcon" />
                            Home
                        </li>
                        
                    </ul> 
                </div>
            </div>
        </div>
    );
}

export default Sidebar;
