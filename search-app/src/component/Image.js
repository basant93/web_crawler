import React, {Component} from 'react'


class Image extends Component{

    constructor(props){
        super(props);
        this.state = {
            image_url : props.image_url
        }   
    }



    render(){

       
        return(
            <div align="left"> 


            {this.props.image_url.map((url, index) => { return  <img src={this.state.image_url}   border= "10px" alt="Smiley face" height="400" width="400"  /> })}
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