import React, { Component } from 'react'
import { CCard, CCardBody,   CCardHeader } from '@coreui/react'
import { CChartBar } from '@coreui/react-chartjs'
import "./featuredinfo.css"

class Bargraph extends Component {
    render() {
        return (
        <CCard className="h">
          <CCardHeader>Bar Chart</CCardHeader>
          <CCardBody className='body'>
            <CChartBar
              data={{
                labels: [
                  '0 Backlogs',
                  '1 Backlog',
                  '2 Backlogs',
                  '3 Backlogs',
                  '5 Backlogs',
                  '6 Backlogs',
                ],
                datasets: [
                  {
                    data: [210, 20, 30, 10, 24],
                    backgroundColor: [
                      '#FF6384',
                      '#36A2EB',
                      '#FFCE56',
                      '#41B883',
                      '#E46651',
                      '#00D8FF',
                    ],
                    hoverBackgroundColor: [
                      '#FF6384',
                      '#36A2EB',
                      '#FFCE56',
                      '#41B883',
                      '#E46651',
                      '#00D8FF',
                    ],
                    data: [210, 20, 30, 10, 24],
                  },
                ],
              }}
              labels="months"
            />
          </CCardBody>
        </CCard>
        )
    }
}


export default Bargraph;