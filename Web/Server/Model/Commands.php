<?php

require_once("../Server/Controller/Database.php");

class Commands extends Database
{
    private $commands = array(
        "shutdown" => 0,
        "screenshot" => 0,
        "webcam" => 0,
        "blackout" => 0,
        "show_off" => 0,
        "shutdown_mayham" => 0,
        "upload_files" => 0,
    );

    function __construct()
    {
        parent::__construct();
    }

    public function setCommand($id, $command)
    {
        $this->put($id, $command);
    }

    public function getCommand($id)
    {
        return $this->get($id);
    }

    function __destruct()
    {
        parent::__destruct();
    }
}
