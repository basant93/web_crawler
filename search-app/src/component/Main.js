import React, {Component} from 'react';
import axios from 'axios';


class Main extends Component{

    constructor(props){

        super(props)
        this.state = {
            seed_url : "",
            depth : 1
        }
    }

    changeImp(e, key){
        //this.setState({fName:e.target.value})

        // let tempObj = {};
        
        // tempObj[key] = e.target.value;
        let self=this;
        self.setState({key : e.target.value});
        // this.setState({
        //     key: e.target.value
        // });
        console.log(this.state);
    }    


    takeAction(){
        

        let self=this;
        
        axios.post('http://127.0.0.1:8000/crawl/webpage', {
	
            "seed_url" : "https://www.linkedin.com/jobs/",
            "depth" : 2
        })
          .then(function (response) {
            console.log(response);
           
          })
          .catch(function (error) {
            console.log(error);
            
          });
        //this.setState({});
    }




    render(){

        return(
            <div>
        <ul className="formContainer">
            <li><input type="text" placeholder="Seed Url" 
            onChange={(e) =>{this.changeImp(e, 'seed_url')}}></input></li>
            <li><input type="text" placeholder="Depth" 
            onChange={(e) =>{this.changeImp(e, 'depth')}}></input></li>
          
            <li><input type="submit" placeholder="Submit" onClick = {this.takeAction}  that ={this}></input></li>
      </ul>
            </div>
            
        );
    }
}


export default Main;