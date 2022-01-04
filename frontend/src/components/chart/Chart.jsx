import React from 'react'
import "./chart.css";
import { LineChart, Line, XAxis, CartesianGrid, Tooltip,  ResponsiveContainer } from 'recharts';


export default function Chart({title,data,datakey,grid}) {

    return (
        <div className='chart' >
            <h3 className="chartTitle">
                Semester Analytics
                {/* {title} */}
            </h3>
            <ResponsiveContainer width="100%" aspect={4/1} >
                <LineChart data={data} >
                    <XAxis dataKey="name"  stroke='#5550bd' />
                    <Line type="monotone" dataKey={datakey} stroke='#5550bd' />
                    <Tooltip />
                    {grid && <CartesianGrid stroke='#e0dfdf' />}
                </LineChart>
            </ResponsiveContainer>
        </div>
    )
}
