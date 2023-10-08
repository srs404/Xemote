<?php

class Database
{
    private $credentials = [
        'server'   => 'localhost',
        'username' => 'root',
        'password' => '',
        'dbname'   => 'xemote'
    ];

    private function connection()
    {
        try {
            $conn = new PDO("mysql:host=" . $this->credentials['server'] . ";dbname=" . $this->credentials['dbname'], $this->credentials['username'], $this->credentials['password']);
            // set the PDO error mode to exception
            $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
            echo "Connected successfully";
        } catch (PDOException $e) {
            echo "Connection failed: " . $e->getMessage();
        }
    }
    public function connect()
    {
        $this->connection();
    }
}
