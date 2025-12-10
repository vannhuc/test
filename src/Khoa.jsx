import React, {Component} from "react";
import { variables } from "./Variables";    

export class Khoa extends Component
{
    constructor(props){
        super(props);
        this.state={
            khoas:[]
        }
    }   
    refreshList(){
        fetch(variables.API_URL+'khoa')
        .then(response=>response.json())
        .then(data=>{
            this.setState({khoas:data});
        });
    }
    componentDidMount(){
        this.refreshList();
    }   
    render(){
        const {khoas} = this.state;
        return (
        <div>
            <table className="table table-striped"> 
                <thead>
                    <tr>
                        <th>
                            Mã Khoa
                        </th>
                        <th>
                            Tên Khoa
                        </th>
                    </tr>
                </thead>
                <tbody>
                    {this.state.khoas.map(khoa=>
                        <tr key={khoa.ma_khoa}>
                            <td>{khoa.ma_khoa}</td>
                            <td>{khoa.ten_khoa}</td>
                        </tr>
                    )}
                </tbody>
            </table>
        </div>
    );
    }
    
}