import React, {Component, PropTypes} from 'react';

import './TextBox.css';
import Button from './form/Button';

function TextBox({onChange, value}) {
    return (
      <input type="text"
             className="TextBox"
             value={value}
             onChange={({target}) => onChange(target.value)}
      />
    );
}

TextBox.defaultProps = {
  onChange: () => false
}

TextBox.propTypes = {
  onChange: PropTypes.func,
  value: PropTypes.string
}

export default TextBox;
