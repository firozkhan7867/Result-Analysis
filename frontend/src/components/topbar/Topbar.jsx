import React from 'react';
import "./topbar.css";
import { Language, NotificationsNone, Settings } from '@material-ui/icons';


const Topbar = () => {
    return (
        <div className="topbar">
            <div className="topbarWrapper">
                <div className="topLeft">
                    <span className="logo">
                       Result Analysis 
                    </span>
                </div>
                <div className="topRight">
                    <div className="topbarIconsContainer">
                         <NotificationsNone/>
                         <span className="topIconBadge">
                             2
                         </span>
                    </div>
                    <div className="topbarIconsContainer">
                         <Language/>
                         <span className="topIconBadge">
                             2
                         </span>
                    </div>
                    <div className="topbarIconsContainer">
                         <Settings/>
                         <span className="topIconBadge">
                             2
                         </span>
                    </div>
                    <img src="https://st3.depositphotos.com/15648834/17930/v/600/depositphotos_179308454-stock-illustration-unknown-person-silhouette-glasses-profile.jpg" 
                         alt="" className='topAvatar' />
                </div>
            </div>
        </div>
    );
}

export default Topbar;
