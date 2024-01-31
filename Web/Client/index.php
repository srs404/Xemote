<?php

require_once("../Server/Model/Commands.php");

$commands = new Commands();

// Get Command List
$commandList = $commands->getCommand(123456);

// Convert JSON
$commandList = json_decode($commandList['command'], true);

if (isset($_GET['blackout'])) {
    if ($_GET['blackout'] == "lock") {
        $commandList['blackout'] = 1;
        $commands->setCommand(123456, json_encode($commandList));
    } else if ($_GET['blackout'] == "unlock") {
        $commandList['blackout'] = 2;
        $commands->setCommand(123456, json_encode($commandList));
    }
    $commands->redirect($_SERVER['PHP_SELF']);
} else if (isset($_GET['webcam'])) {
    if ($_GET['webcam'] == "true") {
        $commandList['webcam'] = 1;
        $commands->setCommand(123456, json_encode($commandList));
    } else if ($_GET['webcam'] == "false") {
        $commandList['webcam'] = 0;
        $commands->setCommand(123456, json_encode($commandList));
    }
    $commands->redirect($_SERVER['PHP_SELF']);
} else if (isset($_GET['screenshot'])) {
    if ($_GET['screenshot'] == "false") {
        $commandList['screenshot'] = 0;
        $commands->setCommand(123456, json_encode($commandList));
    } else if ($_GET['screenshot'] == "true") {
        $commandList['screenshot'] = 1;
        $commands->setCommand(123456, json_encode($commandList));
    }
    $commands->redirect($_SERVER['PHP_SELF']);
} else if (isset($_GET['shutdown'])) {
    if ($_GET['shutdown'] == "false") {
        $commandList['shutdown'] = 0;
        $commands->setCommand(123456, json_encode($commandList));
    } else if ($_GET['shutdown'] == "true") {
        $commandList['shutdown'] = 1;
        $commands->setCommand(123456, json_encode($commandList));
    }
    $commands->redirect($_SERVER['PHP_SELF']);
} else if (isset($_GET['restart'])) {
    if ($_GET['restart'] == "false") {
        $commandList['shutdown'] = 0;
        $commands->setCommand(123456, json_encode($commandList));
    } else if ($_GET['restart'] == "true") {
        $commandList['shutdown'] = 2;
        $commands->setCommand(123456, json_encode($commandList));
    }
    $commands->redirect($_SERVER['PHP_SELF']);
} else if (isset($_GET['signout'])) {
    if ($_GET['signout'] == "false") {
        $commandList['shutdown'] = 0;
        $commands->setCommand(123456, json_encode($commandList));
    } else if ($_GET['signout'] == "true") {
        $commandList['shutdown'] = 3;
        $commands->setCommand(123456, json_encode($commandList));
    }
    $commands->redirect($_SERVER['PHP_SELF']);
}
?>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Panel | Xemote</title>
    <link rel="stylesheet" href="Assets/css/bootstrap/bootstrap.min.css">
    <link rel="stylesheet" href="Assets/css/main.css">
</head>

<body>

    <!-- Navbar -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <a class="navbar-brand" href="#">Navbar</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>

        <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav mr-auto">
                <li class="nav-item active">
                    <a class="nav-link" href="#">Home <span class="sr-only">(current)</span></a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="#">Link</a>
                </li>
                <li class="nav-item dropdown">
                    <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                        Dropdown
                    </a>
                    <div class="dropdown-menu" aria-labelledby="navbarDropdown">
                        <a class="dropdown-item" href="#">Action</a>
                        <a class="dropdown-item" href="#">Another action</a>
                        <div class="dropdown-divider"></div>
                        <a class="dropdown-item" href="#">Something else here</a>
                    </div>
                </li>
                <li class="nav-item">
                    <a class="nav-link disabled" href="#">Disabled</a>
                </li>
            </ul>
            <form class="form-inline my-2 my-lg-0">
                <input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search">
                <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
            </form>
        </div>
    </nav>

    <!-- Body Content -->
    <div class="container-fluid">
        <div class="row">
            <div class="col-md mainContent">
                <div class="card">
                    <div class="card-body" style="text-align: center;">
                        <h5 class="card-title">Shutdown Computer</h5>
                        <p class="card-text">Turn Off Your Device</p>
                        <button onclick="shutdown('shutdown')" class="btn btn-primary">Execute</button>
                    </div>
                </div>
            </div>
            <div class="col-md mainContent">
                <div class="card">
                    <div class="card-body" style="text-align: center;">
                        <h5 class="card-title">Restart Computer</h5>
                        <p class="card-text">Restart Your Device</p>
                        <button onclick="shutdown('restart')" class="btn btn-primary">Execute</button>
                    </div>
                </div>
            </div>
            <div class="col-md mainContent">
                <div class="card">
                    <div class="card-body" style="text-align: center;">
                        <h5 class="card-title">Sign Out</h5>
                        <p class="card-text">Sign Out From Your Device</p>
                        <button onclick="shutdown('signout')" class="btn btn-primary">Execute</button>
                    </div>
                </div>
            </div>
        </div>

        <div class="row">
            <div class="col-md mainContent">
                <div class="card">
                    <div class="card-body" style="text-align: center;">
                        <h5 class="card-title">Webcam</h5>
                        <p class="card-text">Capture Image Using Webcam</p>
                        <button onclick="webcam()" class="btn btn-primary">Execute</button>
                    </div>
                </div>
            </div>
            <div class="col-md mainContent">
                <div class="card">
                    <div class="card-body" style="text-align: center;">
                        <h5 class="card-title">Screenshot</h5>
                        <p class="card-text">Capture Screenshot of Current State</p>
                        <button onclick="screenshot()" class="btn btn-primary">Execute</button>
                    </div>
                </div>
            </div>
            <div class="col-md mainContent">
                <div class="card">
                    <div class="card-body" style="text-align: center;">
                        <h5 class="card-title">Blackout</h5>
                        <p class="card-text">Lock Access To Device</p>
                        <button onclick="blackout()" class="btn btn-primary">Execute</button>
                    </div>
                </div>
            </div>
        </div>
        <div class="row">
            <div class="col-md mainContent">
                <div class="card">
                    <div class="card-body" style="text-align: center;">
                        <h5 class="card-title">Showoff</h5>
                        <p class="card-text">Cool Device Effect To Show Off</p>
                        <button onclick="" class="btn btn-primary">Execute</button>
                    </div>
                </div>
            </div>
            <div class="col-md mainContent">
                <div class="card">
                    <div class="card-body" style="text-align: center;">
                        <h5 class="card-title">Shutdown Mayham</h5>
                        <p class="card-text">Keep Shutting Down Your Device</p>
                        <a href="#" class="btn btn-primary">Execute</a>
                    </div>
                </div>
            </div>
            <div class="col-md mainContent">
                <div class="card">
                    <div class="card-body" style="text-align: center;">
                        <h5 class="card-title">Upload Files</h5>
                        <p class="card-text">Upload Files To Your Device [Coming Soon]</p>
                        <a href="#" class="btn btn-primary">Execute</a>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <script src="Assets/js/bootstrap/jquery-3.2.1.slim.min.js"></script>
    <script src="Assets/js/bootstrap/popper.min.js"></script>
    <script src="Assets/js/bootstrap/bootstrap.min.js"></script>
    <script src="https://unpkg.com/sweetalert/dist/sweetalert.min.js"></script>
    <script>
        function blackout() {
            swal({
                title: "Are you sure?",
                text: "Once blacked out, you will not be able to turn on your device remotely",
                icon: "info",
                closeOnClickOutside: false,
                closeOnEsc: false,
                buttons: {
                    cancel: {
                        text: "Cancel",
                        value: "cancel",
                        visible: true,
                        closeModal: true,
                    },
                    unlock: {
                        text: "Unfreeze",
                        value: "unlock",
                        visible: true,
                    },
                    lock: {
                        text: "Initialize",
                        value: "blackout",
                    },
                },
            }).then((value) => {
                if (value == "blackout") {
                    swal("Initialized Blackout!", {
                        icon: "success",
                        timer: 1200,
                        button: false,
                    }).then(() => {
                        window.location.href = "<?php echo $_SERVER['PHP_SELF'] . "?blackout=lock" ?>";
                    });
                } else if (value == "unlock") {
                    swal("Unlocking Your Device!", {
                        icon: "success",
                        timer: 1000,
                        button: false,
                    }).then(() => {
                        window.location.href = "<?php echo $_SERVER['PHP_SELF'] . "?blackout=unlock" ?>";
                    });
                } else if (value == "cancel") {
                    swal(modalclose = true);
                }
            });
        }

        function webcam() {
            swal({
                title: "Are you sure?",
                text: "Once executed, you will be able to see the image captured from your device",
                icon: "info",
                closeOnClickOutside: false,
                closeOnEsc: false,
                buttons: {
                    cancel: {
                        text: "Remove Previous",
                        value: "cancel",
                        visible: true,
                    },
                    execute: {
                        text: "Execute",
                        value: "execute",
                    },
                },
            }).then((value) => {
                if (value == "execute") {
                    swal("Capturing Image!", {
                        icon: "success",
                        timer: 1200,
                        button: false,
                    }).then(() => {
                        window.location.href = "<?php echo $_SERVER['PHP_SELF'] . "?webcam=true" ?>";
                    });
                } else if (value == "cancel") {
                    swal("Cleared Command", {
                        icon: "success",
                        timer: 1000,
                        button: false,
                    }).then(() => {
                        window.location.href = "<?php echo $_SERVER['PHP_SELF'] . "?webcam=false" ?>";
                    });
                }
            });
        }

        function screenshot() {
            swal({
                title: "Are you sure?",
                text: "Once executed, you will be able to see the screenshot captured from your device",
                icon: "info",
                closeOnClickOutside: false,
                closeOnEsc: false,
                buttons: {
                    cancel: {
                        text: "Remove Previous",
                        value: "cancel",
                        visible: true,
                    },
                    execute: {
                        text: "Execute",
                        value: "execute",
                    },
                },
            }).then((value) => {
                if (value == "execute") {
                    swal("Capturing Screenshot!", {
                        icon: "success",
                        timer: 1200,
                        button: false,
                    }).then(() => {
                        window.location.href = "<?php echo $_SERVER['PHP_SELF'] . "?screenshot=true" ?>";
                    });
                } else if (value == "cancel") {
                    swal("Cleared Command!", {
                        icon: "success",
                        timer: 1000,
                        button: false,
                    }).then(() => {
                        window.location.href = "<?php echo $_SERVER['PHP_SELF'] . "?screenshot=false" ?>";
                    });
                }
            });
        }

        /**
         * Title: Shutdown
         * ~ Description: Shutdown, Restart, Signout
         * @param {string} option
         * @returns {void}
         */
        function shutdown(option) {
            if (option == "shutdown") {
                swal({
                        title: "Are you sure? [Shutdown]",
                        text: "Once shutdown, you will not be able to turn on your device remotely",
                        icon: "warning",
                        closeOnClickOutside: false,
                        closeOnEsc: false,
                        buttons: {
                            cancel: {
                                text: "Remove Previous",
                                value: "cancel",
                                visible: true,
                            },
                            execute: {
                                text: "Execute",
                                value: "execute",
                            },
                        },
                    })
                    .then((value) => {
                        if (value == "execute") {
                            window.location.href = "<?php echo $_SERVER['PHP_SELF'] . "?shutdown=true" ?>";
                        } else if (value == "cancel") {
                            swal("Cleared Command!", {
                                icon: "success",
                                timer: 1000,
                                button: false,
                            }).then(() => {
                                window.location.href = "<?php echo $_SERVER['PHP_SELF'] . "?shutdown=false" ?>";
                            });
                        }
                    });
            } else if (option == "restart") {
                swal({
                        title: "Are you sure? [Restart]",
                        text: "Once restarted, you will not be able to turn on your device remotely",
                        icon: "warning",
                        closeOnClickOutside: false,
                        closeOnEsc: false,
                        buttons: {
                            cancel: {
                                text: "Remove Previous",
                                value: "cancel",
                                visible: true,
                            },
                            execute: {
                                text: "Execute",
                                value: "execute",
                            },
                        },
                    })
                    .then((value) => {
                        if (value == "execute") {
                            window.location.href = "<?php echo $_SERVER['PHP_SELF'] . "?restart=true" ?>";
                        } else if (value == "cancel") {
                            swal("Cleared Command!", {
                                icon: "success",
                                timer: 1000,
                                button: false,
                            }).then(() => {
                                window.location.href = "<?php echo $_SERVER['PHP_SELF'] . "?restart=false" ?>";
                            });
                        }
                    });
            } else if (option == "signout") {
                swal({
                        title: "Are you sure? [Log Off]",
                        text: "Once signed out, you will not be able to turn on your device remotely",
                        icon: "warning",
                        closeOnClickOutside: false,
                        closeOnEsc: false,
                        buttons: {
                            cancel: {
                                text: "Remove Previous",
                                value: "cancel",
                                visible: true,
                            },
                            execute: {
                                text: "Execute",
                                value: "execute",
                            },
                        },
                    })
                    .then((value) => {
                        if (value) {
                            window.location.href = "<?php echo $_SERVER['PHP_SELF'] . "?signout=true" ?>";
                        } else if (value == "cancel") {
                            swal("Cleared Command!", {
                                icon: "success",
                                timer: 1000,
                                button: false,
                            }).then(() => {
                                window.location.href = "<?php echo $_SERVER['PHP_SELF'] . "?signout=false" ?>";
                            });
                        }
                    });
            }
        }
    </script>
</body>

</html>