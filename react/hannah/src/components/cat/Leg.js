import React from 'react';

import './Leg.css'

function Leg(props) {
  return (
    <div className={`Leg ${props.leg} ${props.color}`}></div>
  )
}

export default Leg;
