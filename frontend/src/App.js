import Topbar from "./components/topbar/Topbar";
import Sidebar from "./components/sidebar/Sidebar";
import Home from "./pages/home/Home";
import "./app.css";
import { Component } from "react";
class App extends Component {

  state = {
    data: [],
    fail_count: null,
    pass_count:null,
    total_resgistered:null,
    cgpa_data: {},
    back_data: {},
  }


  setdataintoDAta = data => {
    this.setState({fail_count: data["Fail_count"], pass_count: data["Pass_count"], total_resgistered: data["Total_Registered"],
  
                      cgpa_data: data["CGPA"], back_data: data["Back_data"], data: data});
    console.log(this.state.data)

  }


  componentDidMount(){
    fetch( `http://127.0.0.1:8000/subj/1`,{
            method: "GET",
        }).then(resp => resp.json())
        // .then(resp => console.log(resp))
        .then(res => this.setdataintoDAta(res["Semester PerFormance"]))
        .catch(error => console.log(error))
  }


  display = () => {
    console.log(this.state.data);
  }



  render() {
    return (
      <div className="App">
        <Topbar/>
  
        <div className="container">
          <Sidebar/>
          <Home  failCount={this.state.fail_count} passCount={this.state.pass_count} Registered={this.state.total_resgistered}
          Backdata={this.state.back_data} CGPA={this.state.cgpa_data} />
        </div>
      </div>
    );
  }
}

export default App;
