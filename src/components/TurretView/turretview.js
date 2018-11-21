import Grid from '@material-ui/core/Grid';
import Paper from '@material-ui/core/Paper';
import React, { Component } from 'react';
import Config from '../../config.json';
import '../../App.css';

class TurretView extends Component {
  constructor(props) {
    super(props);
    this.state = {cameraUrl: "http://" + Config["device_host"] + ":" + Config["camera_port"] + "/?action=stream"};
  }

  render() {
    return (
      <Grid container spacing={24}>
        <Grid item xs={1} />
        <Grid item xs={10}>
          <Paper className="Video">
            <p>Turret View</p>
            <img style={{ paddingBottom: "20px" }} src={this.state.cameraUrl} alt={this.state.cameraUrl} />
          </Paper>
        </Grid>
        <Grid item xs={1} />
      </Grid>
    );
  }
}

export default TurretView;