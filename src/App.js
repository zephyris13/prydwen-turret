import Grid from '@material-ui/core/Grid';
import TurretView from './components/TurretView/turretview';
import TurretControls from './components/TurretControls/turretcontrols';
import AutoAim from './components/AutoAim/autoaim';
import React, { Component } from 'react';
import './App.css';

class App extends Component {

  render() {
    return (
      <div className="App App-background">
        <Grid container spacing={24}>

          <Grid item xs={1} />
          <Grid item xs={10}>
            <TurretView />
          </Grid>
          <Grid item xs={1} />

          <Grid item xs={1} />
          <Grid item xs={3}>
            <TurretControls />
          </Grid>
          <Grid item xs={7}>
            <AutoAim />
          </Grid>
          <Grid item xs={1} />

        </Grid>
      </div>
    );
  }
}

export default App;
