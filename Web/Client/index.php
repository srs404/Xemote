<?php

require_once("../Server/Model/Commands.php");

$commands = new Commands();

// Get Command List
$commandList = $commands->getCommand(123456);

// Convert JSON
$commandList = json_decode($commandList['command'], true);

if (isset($_GET['blackout']) && $_GET['blackout'] == "true") {
    if ($commandList['blackout'] == 0)
        $commandList['blackout'] = 1;
    else
        $commandList['blackout'] = 0;
    $commands->setCommand(123456, json_encode($commandList));
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
                        <a href="#" class="btn btn-primary">Execute</a>
                    </div>
                </div>
            </div>
            <div class="col-md mainContent">
                <div class="card">
                    <div class="card-body" style="text-align: center;">
                        <h5 class="card-title">Restart Computer</h5>
                        <p class="card-text">Restart Your Device</p>
                        <a href="#" class="btn btn-primary">Execute</a>
                    </div>
                </div>
            </div>
            <div class="col-md mainContent">
                <div class="card">
                    <div class="card-body" style="text-align: center;">
                        <h5 class="card-title">Sign Out</h5>
                        <p class="card-text">Sign Out From Your Device</p>
                        <a href="#" class="btn btn-primary">Execute</a>
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
                        <a href="#" class="btn btn-primary">Execute</a>
                    </div>
                </div>
            </div>
            <div class="col-md mainContent">
                <div class="card">
                    <div class="card-body" style="text-align: center;">
                        <h5 class="card-title">Screenshot</h5>
                        <p class="card-text">Capture Screenshot of Current State</p>
                        <a href="#" class="btn btn-primary">Execute</a>
                    </div>
                </div>
            </div>
            <div class="col-md mainContent">
                <div class="card">
                    <div class="card-body" style="text-align: center;">
                        <h5 class="card-title">Blackout</h5>
                        <p class="card-text">Lock Access To Device</p>
                        <a href="<?php echo $_SERVER['PHP_SELF'] . "?blackout=true" ?>" class="btn btn-primary">Execute</a>
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
                        <a href="#" class="btn btn-primary">Execute</a>
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
</body>

</html>