import Grid from '@material-ui/core/Grid';
import Paper from '@material-ui/core/Paper';
import Switch from '@material-ui/core/Switch';
import React, { Component } from 'react';
import './App.css';

class App extends Component {
  state = {
    autoaimChecked: false,
  };

  handleChange = name => event => {
    this.setState({ [name]: event.target.checked });
  };

  render() {
    return (
      <div className="App App-background">
        <Grid container spacing={24}>
          <Grid item xs={12}>
            <Paper className="Video">
              <p>Turret View</p>
            </Paper>
          </Grid>
          <Grid item xs={6}>
            <Paper className="Controls">
            <p>Controls</p>
            </Paper>
          </Grid>
          <Grid item xs={6}>
            <Paper className="AutoAim">
            <p>Auto Aim</p>
            <Switch
              checked={this.state.autoaimChecked}
              onChange={this.handleChange('autoaimChecked')}
              value=""
            />
            </Paper>
          </Grid>
        </Grid>
      </div>
    );
  }
}

export default App;
