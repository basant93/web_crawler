import React, {Component} from 'react';
import axios from 'axios';
import Image from './Image';


class Main extends Component{

    constructor(props){

        super(props)
        this.state = {
            seed_url : "",
            depth : 1
        };

        this.image_urls = ["https://homepages.cae.wisc.edu/~ece533/images/girl.png","https://homepages.cae.wisc.edu/~ece533/images/peppers.png"];
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
        

        let data = {
	
            "seed_url" : "https://www.linkedin.com/jobs/",
            "depth" : 2
        };
        var headers = {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*',
        };

        axios.post('http://127.0.0.1:8000/crawl/webpage', data)
          .then(function (response) {
            console.log(response);
           
          })
          .catch(function (error) {
            console.log(error);
            
          });
        //this.setState({});
    }




    render(){
        axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';
        axios.defaults.headers.post['Access-Control-Allow-Origin'] = '*';
        //axios.defaults.headers.options['Access-Control-Allow-Origin'] = '*';
        return(
            <div>
        <ul className="formContainer">
            <li><input type="text" placeholder="Seed Url" 
            onChange={(e) =>{this.changeImp(e, 'seed_url')}}></input></li>
            <li><input type="text" placeholder="Depth" 
            onChange={(e) =>{this.changeImp(e, 'depth')}}></input></li>
          
            <li><input type="submit" placeholder="Submit" onClick = {this.takeAction}  that ={this}></input></li>
      </ul>

            <Image image_url= {this.image_urls}/>

            </div>
            
        );
    }
}


export default Main;