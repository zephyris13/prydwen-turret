import Grid from '@material-ui/core/Grid';
import Paper from '@material-ui/core/Paper';
import Button from '@material-ui/core/Button';
import Switch from '@material-ui/core/Switch';
import FormControlLabel from '@material-ui/core/FormControlLabel';
import ExpandLess from '@material-ui/icons/ExpandLess';
import ExpandMore from '@material-ui/icons/ExpandMore';
import ChevronLeft from '@material-ui/icons/ChevronLeft';
import ChevronRight from '@material-ui/icons/ChevronRight';
import MyLocation from '@material-ui/icons/MyLocation';
import React, { Component } from 'react';
import Config from '../../config.json';
import '../../App.css';

class TurretControls extends Component {
  constructor(props) {
    super(props);
    this.state = {
      cameraUrl: "http://" + Config["device_host"] + ":" + Config["camera_port"] + "/?action=stream",
      spoolupChecked: false,
    };
  }

  handleChange = name => event => {
    this.setState({ [name]: event.target.checked });
  };

  render() {
    return (
      <Paper className="Controls">
        <p>Controls</p>

        <Grid item xs={12}>
        
          <Grid item xs={12}>
            <Button color="default">
              <ExpandLess/>
            </Button>
          </Grid>

          <Grid item xs={12}>
            <Button color="default">
              <ChevronLeft/>
            </Button>

            <Button color="default">
              <MyLocation/>
            </Button>

            <Button color="default">
              <ChevronRight/>
            </Button>
          </Grid>

          <Grid item xs={12}>
            <Button color="default">
              <ExpandMore/>
            </Button>
          </Grid>

          <Grid item xs={12}>
            <FormControlLabel
              control={
                <Switch
                  color="secondary"
                  checked={this.state.spoolupChecked}
                  onChange={this.handleChange('spoolupChecked')}
                  value=""
                />
              }
              label="Spool Up"
            />
          </Grid>

        </Grid>
      </Paper>
    );
  }
}

export default TurretControls;