import logo from "./logo-mobile.svg";
import "./SignerChanges.css";
import PropTypes from "prop-types";
import { withStyles } from "@material-ui/styles";
import React, { Component } from "react";
import axios from "axios";
import { makeStyles } from "@material-ui/core/styles";
import TextField from "@material-ui/core/TextField";
import CloudUploadIcon from "@material-ui/icons/CloudUpload";
import Button from "@material-ui/core/Button";
import download from "downloadjs";
import Checkbox from '@material-ui/core/Checkbox';
import FormControlLabel from '@material-ui/core/FormControlLabel';
import FormControl from '@material-ui/core/FormControl';
import FormLabel from '@material-ui/core/FormLabel';
import FormGroup from '@material-ui/core/FormGroup';
import Select from '@material-ui/core/Select';
import MenuItem from '@material-ui/core/MenuItem';
import List from '@material-ui/core/List';
import ListItem from '@material-ui/core/ListItem';
import Divider from '@material-ui/core/Divider';
import ListItemText from '@material-ui/core/ListItemText';
import Avatar from '@material-ui/core/Avatar';
import AvatarGroup from '@material-ui/lab/AvatarGroup';
import checkmark from "./check.svg"
import ListItemAvatar from '@material-ui/core/ListItemAvatar';
import contract from "./contract.svg"
import ImageIcon from '@material-ui/icons/Image';
import HeaderAccountInfo from "./HeaderAccountInfo"

const useStyles = makeStyles((theme) => ({
    root: {
        "& > *": {
            margin: theme.spacing(1),
            width: "25ch",
        },
        button: {
            margin: theme.spacing(1),
        },
    },
}));

class SignerChanges extends Component {
    render() {
        return (
            <div className="container">
                <div className="InputBox">
                    <div style={{ display: 'flex', flexDirection: "column", alignContent: "center", justifyContent: "center", width: "100%", margin: "0 0 30px" }}>
                        <div style={{
                            width: "100%", display: 'flex',
                            justifyContent: "center"
                        }}>
                            <img src={logo} className="logo" />
                        </div>
                        <h1 style={{ fontFamily: 'Roboto sans-serif', color: "#595a59" }}>Information</h1>
                        <HeaderAccountInfo />
                    </div>
                </div>
            </div>
        );
    }
}

SignerChanges.propTypes = {
    classes: PropTypes.object.isRequired,
};

export default withStyles(useStyles)(SignerChanges);