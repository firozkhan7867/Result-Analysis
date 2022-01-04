import React, { Component } from 'react'
import { CCard, CCardBody, CCardHeader} from '@coreui/react'
import { CChartPie } from '@coreui/react-chartjs'

class Charts extends Component {



  arr_key = () => {
    if (this.props.cgpa_data){
      const data = new Map(Object.entries(this.props.cgpa_data));
      return Array.from( data.keys() );
    }
    else{
      return [0,0,0,0,0];
    }
  }


  arry_val = () => {
    if (this.props.cgpa_data){
    const data = new Map(Object.entries(this.props.cgpa_data));
    return Array.from( data.values() );
  }
    
  else{
    return [0,0,0,0,0];
  }
  }

  render() {
    return (
    
      <CCard className="mb-1">
        <CCardHeader>Pie Chart</CCardHeader>
        <CCardBody>
          <CChartPie
            data={{
              labels: this.arr_key(),
              datasets: [
                {
                  data: this.arry_val(),
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
}

export default Charts