import React, {PropTypes} from 'react';

import './Home.css';

function Home(props) {
  return (
    <div className="home">
      {props.children}
    </div>
  );
}

Home.propTypes =  {
  children: PropTypes.node.isRequired
}

export default Home;
