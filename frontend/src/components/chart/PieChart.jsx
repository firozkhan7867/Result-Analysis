import React from 'react'
import { CCard, CCardBody, CCardHeader} from '@coreui/react'
import { CChartPie } from '@coreui/react-chartjs'

const Charts = () => {
  return (
    
        <CCard className="mb-1">
          <CCardHeader>Pie Chart</CCardHeader>
          <CCardBody>
            <CChartPie
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
                  },
                ],
              }}
            />
          </CCardBody>
        </CCard>
  )
}

export default Charts