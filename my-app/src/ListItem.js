import React, {Component} from 'react'
import './ListItem.css';

const ListItem = (props) =>{
    const item = props.item;
    if(item.done){
        return (
            <div>
                <p className="done-item">{item.content}</p> 
            </div>
        )
    }else{
        return <p className="item">{item.content}</p>
    }
} 

export default ListItem;