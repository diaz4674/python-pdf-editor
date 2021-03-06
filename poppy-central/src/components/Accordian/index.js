import React, { useEffect, useMemo } from "react"
import { makeStyles } from "@material-ui/core/styles"
import Accordion from "@material-ui/core/Accordion"
import AccordionSummary from "@material-ui/core/AccordionSummary"
import Typography from "@material-ui/core/Typography"
import ExpandMoreIcon from "@material-ui/icons/ExpandMore"
import BusinesInputs from "../BusinessInputs"
import SignerInput from "../SignerInput"
import Button from "@material-ui/core/Button"
import checkmark from "../../assets/check.svg"
import error from "../../assets/close.svg"
import {
    generateDocs,
    loadingAnimation,
    saveProjectToStore,
    updateProjectToStore,
} from "../../actions"
import { connect } from "react-redux"
import { withRouter } from "react-router-dom"
import "./style.css"

const useStyles = makeStyles((theme) => ({
    root: {
        width: "100%",
    },
    heading: {
        fontSize: theme.typography.pxToRem(15),
        flexBasis: "33.33%",
        flexShrink: 0,
    },
    header1: {},
    secondaryHeading: {
        fontSize: theme.typography.pxToRem(15),
        color: theme.palette.text.secondary,
    },
}))

let totalSigners

const ControlledAccordions = (props) => {
    const classes = useStyles()
    const [expanded, setExpanded] = React.useState("panel1")
    const [loading, setLoading] = React.useState(false)
    const [allValue, setValues] = React.useState({
        numSigners: "",
        accountState: null,
        totalSigners,
    })

    useEffect(async () => {
        totalSigners = props.AccountInfo.numSigners
        if (props.savedProject === undefined) {
            await setValues({
                ...allValue,
                totalSigners,
                numSigners: totalSigners,
                TeamMembers: props.AccountInfo.TeamMembers,
                ProjectName: props.AccountInfo.ProjectName,
            })
        } else {
            let { savedProject } = props
            await setValues({
                ...allValue,
                totalSigners,
                numSigners: savedProject.totalSigners,
                TeamMembers: savedProject.TeamMembers,
                ProjectName: savedProject.ProjectName,
                savedProject,
            })
        }
    }, [])

    const handleChange = (panel) => (event, isExpanded) => {
        setExpanded(isExpanded ? panel : false)
    }

    const updateCardHandler = async () => {
        let payload = {
            AccountInfo: allValue.AccountInfo,
            totalSigners: allValue.totalSigners,
        }
        for (let i = 1; i < totalSigners + 1; i++) {
            if (allValue[`signer${+i}`] === undefined) {
                return alert("Sorry looks like your still missing some info")
            }
            payload[`signer${+i}`] = allValue[`signer${+i}`]
        }
        // Initializes loading animation
        props.loadingAnimation()
        await props.generateDocs(payload)
    }

    const saveProject = () => {
        // Check to see if this project is being edited or new
        if (allValue.savedProject === undefined) {
            // check to see if business info saved
            if (allValue.AccountInfo === undefined) {
                alert("Please save business information.")
            }
            // check to see if signer info has been saved
            for (let i = 1; i < totalSigners + 1; i++) {
                if (allValue[`signer${+i}`] === undefined) {
                    return alert("Please save signer data")
                }
            }
            props.saveProjectToStore(allValue)
            props.history.push("/")
        } else {
            props.updateProjectToStore(allValue)
            props.history.push("/")
        }

        console.log("success")
    }

    const updateSigners = async (e) => {
        // checks to see if this is being edited
        if (allValue.savedProject !== undefined) {
            // needed to change error to checkmark img
            await setValues((prevState) => ({
                ...prevState,
                [e.signerNumber]: e.person,
            }))
        }

        if (e.signerNumber !== undefined) {
            await setValues((prevState) => ({
                ...prevState,
                [e.signerNumber]: e.person,
            }))
        } else {
            await setValues((prevState) => ({
                ...prevState,
                AccountInfo: e[0],
            }))
        }
    }

    return (
        <div className={classes.root}>
            {allValue.numSigners === "" ? (
                <p>loading</p>
            ) : (
                    <>
                        <Accordion
                            expanded={expanded === "panel1"}
                            onChange={handleChange("panel1")}
                        >
                            <AccordionSummary
                                expandIcon={<ExpandMoreIcon />}
                                aria-controls="panel1bh-content"
                                id="panel1bh-header"
                            >
                                <Typography className={classes.header1}>
                                    Business Information
							</Typography>
                                {"AccountInfo" in allValue ? (
                                    <img
                                        src={checkmark}
                                        alt="checkmark"
                                        style={{ width: "25px", margin: "0 15px" }}
                                    />
                                ) : (
                                        <img
                                            src={error}
                                            alt="error"
                                            style={{ width: "25px", margin: "0 15px" }}
                                        />
                                    )}
                            </AccordionSummary>
                            <BusinesInputs
                                businessEdit={allValue.savedProject}
                                updateSignersFunc={updateSigners}
                                onChange={handleChange(`panel1bh-header`)}
                            />
                        </Accordion>
                        {Array.from(Array(totalSigners)).map((x, index) => (
                            <Accordion
                                key={index}
                                expanded={expanded === `panel${index + 2}`}
                                onChange={handleChange(`panel${index + 2}`)}
                            >
                                <AccordionSummary
                                    expandIcon={<ExpandMoreIcon />}
                                    aria-controls={`panel${index + 2}bh-content`}
                                    id={`panel${index + 2}bh-header`}
                                >
                                    <Typography>Signer {index + 1}</Typography>
                                    {"signer" + (index + 1) in allValue ? (
                                        <img
                                            src={checkmark}
                                            alt="checkmark"
                                            style={{ width: "25px", margin: "0 15px" }}
                                        />
                                    ) : (
                                            <img
                                                src={error}
                                                alt="error"
                                                style={{ width: "25px", margin: "0 15px" }}
                                            />
                                        )}
                                </AccordionSummary>

                                <SignerInput
                                    signerInfo={allValue.savedProject}
                                    updateSignersFunc={updateSigners}
                                    signerNumber={"signer" + (index + 1)}
                                    onChange={handleChange(`panel${index + 2}`)}
                                />
                            </Accordion>
                        ))}
                        <div className="buttonDiv">
                            <Button
                                variant="contained"
                                color="default"
                                onClick={saveProject}
                                className="submitButton"
                            >
                                {loading ? (
                                    <div class="load-3">
                                        <div class="line"></div>
                                        <div class="line"></div>
                                        <div class="line"></div>
                                    </div>
                                ) : (
                                        "Save Project"
                                    )}
                            </Button>
                            <Button
                                variant="contained"
                                color="default"
                                onClick={updateCardHandler}
                                className="submitButton"
                            >
                                {props.loading && (
                                    <div class="load-3">
                                        <div class="line"></div>
                                        <div class="line"></div>
                                        <div class="line"></div>
                                    </div>
                                )}
                                {!props.loading && "Download Documents"}
                            </Button>
                        </div>
                    </>
                )}
        </div>
    )
}

const mapStateToProps = (state) => {
    return { loading: state.isFetching }
}

export default withRouter(
    connect(mapStateToProps, {
        generateDocs,
        saveProjectToStore,
        loadingAnimation,
        updateProjectToStore,
    })(ControlledAccordions)
)
