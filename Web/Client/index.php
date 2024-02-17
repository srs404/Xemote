<?php 

session_start();

if(isset($_SESSION['user']['LOGIN_STATUS']) && $_SESSION['user']['LOGIN_STATUS'] == true){
    include_once("../Server/View/panel.php");
} else {
    include_once("../Server/View/login.php");
}
