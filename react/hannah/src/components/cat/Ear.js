import React from 'react';

import './Ear.css';

function Ear(props) {

  return (
    <div className={`Ear ${props.color} ${props.ear}`}></div>
  )

}

export default Ear;
