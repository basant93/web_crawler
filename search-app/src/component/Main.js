import React, {Component} from 'react';
import axios from 'axios';
import Image from './Image';


class Main extends Component{

    constructor(props){

        super(props)
        this.state = {
            seed_url : "",
            depth : 1,
            //image_urls : ["https://homepages.cae.wisc.edu/~ece533/images/girl.png","https://homepages.cae.wisc.edu/~ece533/images/peppers.png"],
            //web_url : "https://www.lucidchart.com/"
            main_web_image_urls: [],
            //web_url: ""
        };

        // this.image_urls = ["https://homepages.cae.wisc.edu/~ece533/images/girl.png","https://homepages.cae.wisc.edu/~ece533/images/peppers.png"];

        // this.web_url = "https://www.lucidchart.com/";
    }

    changeImp(e){
        //this.setState({fName:e.target.value})

        // let tempObj = {};
        
        // tempObj[key] = e.target.value;
        // let self=this;
        // self.setState({key : e.target.value});
        // this.setState({
        //     key: e.target.value
        // });
        this.setState({seed_url: e.target.value}, function(){
            console.log('upd= ',this.state.seed_url);
            //this.takeAction();
        })
        
    }    


    changeDepth(e){
        //this.setState({fName:e.target.value})

        // let tempObj = {};
        
        // tempObj[key] = e.target.value;
        // let self=this;
        // self.setState({key : e.target.value});
        // this.setState({
        //     key: e.target.value
        // });
        this.setState({depth: e.target.value}, function(){
            console.log('upd= ',this.state.depth);
            //this.takeAction();
        })
        
    } 


    takeAction(){
        console.log('take action= ',this.state.seed_url);
        let data = {
	
            // "seed_url" : "https://www.linkedin.com/jobs/",
            // "depth" : 2
            "seed_url" : this.state.seed_url,
            "depth" : this.state.depth
        };
        var headers = {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*',
        };
        let self = this;
        axios.post('http://127.0.0.1:8000/crawl/webpage', data)
          .then(function (response) {
            
            console.log(response);
            
            // self.setState({web_url: response.data.image_urls.web_url}, function(){
            //    console.log('check reponse set= ',self.state.web_url);
            // })
            console.log('response.data= ',response.data);
            console.log('response length= ',typeof response.data.data.image_urls);
            self.setState({main_web_image_urls: response.data.data.image_urls}, function(){
                console.log('full response= ',response.data.data.image_urls.length);
                console.log('check reponse set= ',self.state.main_web_image_urls);
             })
          })
          .catch(function (error) {
            console.log(error);
            
          });
          console.log('outside: ',self.state.seed_url);
        
    }


    render(){
        axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';
        axios.defaults.headers.post['Access-Control-Allow-Origin'] = '*';
        //axios.defaults.headers.options['Access-Control-Allow-Origin'] = '*';
        return(
            <div>
        <ul >
            <li ><input type="text" placeholder="Seed Url" 
            // onChange={(e) =>{this.changeImp(e, 'seed_url')}}></input></li>
            onChange={this.changeImp.bind(this)}  height="150" width="350" ></input></li>
            <li><input type="text" placeholder="Depth" 
            // onChange={(e) =>{this.changeImp(e, 'depth')}}></input></li>
            onChange={this.changeDepth.bind(this)}
            ></input></li>
          
            <li><input type="submit" placeholder="Submit" onClick = {this.takeAction.bind(this)} /></li>
      </ul>
      
 {this.state.main_web_image_urls.toString()}

      {/* {this.state.main_web_image_urls.length >0 && this.state.main_web_image_urls.map((url, index) => {
          return <Image image_url= {this.url.web_image_urls}  web_url = {this.url.web_url}/>
      })} */}

       {this.state.main_web_image_urls.toString() && this.state.main_web_image_urls.map((url, index) => {
          return <Image key={index} image_url= {url.web_image_urls}  web_url = {url.web_url}/>
      })} 
    

            </div>
            
        );
    }
}


export default Main;