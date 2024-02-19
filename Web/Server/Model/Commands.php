<?php

require_once("../Server/Controller/Database.php");

class Commands extends Database
{
    function __construct()
    {
        parent::__construct();
    }

    public function setCommand($id, $command)
    {
        $this->put($id, $command);
    }

    public function getCommand($uuid)
    {
        return $this->get($uuid);
    }

    function __destruct()
    {
        parent::__destruct();
    }
}
