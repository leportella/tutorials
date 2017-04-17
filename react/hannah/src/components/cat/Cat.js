import React from 'react';

import Head from './Head';
import Body from './Body';
import Leg from './Leg';
import Tail from './tail';

import './Cat.css';

function Cat(props) {
  return (
    <div className='Cat'>
      <Tail/>
      <div className='CatFront'>
        <div className='Upper'>
          <Body color={props.color}/>
          <Head color={props.color}/>
        </div>
        <div className='Lower'>
          <Leg leg='Left' color={props.color}/>
          <Leg leg='Right' color={props.color}/>
        </div>
      </div>
    </div>
  )

}

export default Cat;
