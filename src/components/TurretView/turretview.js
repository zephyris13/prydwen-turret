import Grid from '@material-ui/core/Grid';
import Paper from '@material-ui/core/Paper';
import React, { Component } from 'react';
import '../../App.css';

class TurretView extends Component {
  render() {
    return (
      <Grid container spacing={24}>
        <Grid item xs={1} />
        <Grid item xs={10}>
          <Paper className="Video">
            <p>Turret View</p>
            <img style={{ paddingBottom: "20px" }} src="http://192.168.0.58:8080/?action=stream" alt="http://192.168.0.58:8080/?action=stream" />
          </Paper>
        </Grid>
        <Grid item xs={1} />
      </Grid>
    );
  }
}

export default TurretView;