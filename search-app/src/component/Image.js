import React, {Component} from 'react'


class Image extends Component{

    constructor(props){
        super(props);
        this.state = {
            image_url : props.image_url,
            web_url : props.web_url
        }   
    }

    render(){
       
        return(
            <div align="left"> 
<img src="https://homepages.cae.wisc.edu/~ece533/images/girl.png"  border= "10px" alt="Smiley face" height="200" width="200"  /> 
            <h1>   <b>Web Page Url : {this.state.web_url}  </b> </h1>
            {this.props.image_url.map((url, index) => { return  <img key={ index } src={url.image_url}   border= "10px" alt="Smiley face" height="450" width="450"  /> })}
                {/* {this.state.image_url}
                {this.state.image_url} */}

{/*                  
                 <img src={this.state.image_url}  border= "10px"  alt="Smiley face" height="200" width="200"  /> 
                 <img src={this.state.image_url}  border= "10px"  alt="Smiley face" height="200" width="200"  /> 
                 <img src={this.state.image_url}  border= "10px"  alt="Smiley face" height="200" width="200"  /> 
                 <img src={this.state.image_url}  border= "10px" alt="Smiley face" height="200" width="200"  /> 
                 <img src={this.state.image_url}  border= "10px" alt="Smiley face" height="200" width="200"  /> 
                 <img src={this.state.image_url}  border= "10px" alt="Smiley face" height="200" width="200"  /> 
                 <img src={this.state.image_url} border= "10px"  alt="Smiley face" height="200" width="200"  /> 
                 <img src={this.state.image_url} border= "10px"  alt="Smiley face" height="200" width="200"  /> 
                 <img src={this.state.image_url}  border= "10px" alt="Smiley face" height="200" width="200"  /> 
                 <img src={this.state.image_url}  border= "10px" alt="Smiley face" height="200" width="200"  /> 

            <img src={this.state.image_url}  border= "10px" alt="Smiley face" height="200" width="200"  /> 
            */}
           
            </div>
        );

    }
}

export default Image;