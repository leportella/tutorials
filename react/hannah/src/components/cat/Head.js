import React from 'react';

import Ear from './Ear';
import Eye from './Eye';
import Mouth from './Mouth';
import Nose from './Nose';
import './Head.css';

function Head(props) {

  return (
    <div>
      <div className='Ears'>
        <Ear color={props.color} ear='Left'/>
        <Ear color={props.color}/>
      </div>
      <div className={`Head ${props.color}`}>
        <div className='Eyes'>
          <Eye/><Nose/><Eye/>
        </div>
        <div className='Mouth'>
          <Mouth/>
        </div>
      </div>
    </div>
  );
}

export default Head;
