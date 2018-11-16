import Grid from '@material-ui/core/Grid';
import Paper from '@material-ui/core/Paper';
import Switch from '@material-ui/core/Switch';
import Button from '@material-ui/core/Button';
import ExpandLess from '@material-ui/icons/ExpandLess';
import ExpandMore from '@material-ui/icons/ExpandMore';
import ChevronLeft from '@material-ui/icons/ChevronLeft';
import ChevronRight from '@material-ui/icons/ChevronRight';
import MyLocation from '@material-ui/icons/MyLocation';
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
          <Grid item xs={1}/>
          <Grid item xs={10}>
            <Paper className="Video">
              <p>Turret View</p>
            </Paper>
          </Grid>
          <Grid item xs={1}/>

          <Grid item xs={1}/>
          <Grid item xs={3}>
            <Paper className="Controls">
              <p>Controls</p>

              <Grid item xs={12}>

                <Grid item xs={12}>
                  <Button color="secondary">
                    <ExpandLess/>
                  </Button>
                </Grid>

                <Grid item xs={12}>
                  <Button color="secondary">
                    <ChevronLeft/>
                  </Button>

                  <Button color="secondary">
                    <MyLocation/>
                  </Button>

                  <Button color="secondary">
                    <ChevronRight/>
                  </Button>
                </Grid>

                <Grid item xs={12}>
                  <Button color="secondary">
                    <ExpandMore/>
                  </Button>
                </Grid>

              </Grid>
            </Paper>
          </Grid>

          <Grid item xs={7}>
            <Paper className="AutoAim">
            <p>Auto Aim</p>
            <Switch
              checked={this.state.autoaimChecked}
              onChange={this.handleChange('autoaimChecked')}
              value=""
            />
            </Paper>
          </Grid>
          <Grid item xs={1}/>
        </Grid>
      </div>
    );
  }
}

export default App;
