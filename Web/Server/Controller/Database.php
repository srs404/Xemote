<?php

class Database
{
    private $host = "localhost";
    private $db_name = "xemote";
    private $username = "root";
    private $password = "";

    private $conn;

    function __construct()
    {
        $this->connect();
    }

    public function connect()
    {
        if ($this->conn != null) {
            return $this->conn;
        }

        $this->conn = null;
        try {
            $this->conn = new PDO("mysql:host=" . $this->host . ";dbname=" . $this->db_name, $this->username, $this->password);
            $this->conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        } catch (PDOException $exception) {
            echo "Connection error: " . $exception->getMessage();
        }
        return $this->conn;
    }

    protected function get($uuid)
    {
        if ($this->conn == null) {
            $this->connect();
        }

        $sql = "SELECT * FROM command_center WHERE uuid = :id";
        $stmt = $this->connect()->prepare($sql);
        $stmt->bindParam(':id', $uuid);
        $stmt->execute();
        return $stmt->fetch(PDO::FETCH_ASSOC);
    }

    protected function put($uuid, $command)
    {
        if ($this->conn == null) {
            $this->connect();
        }
        $sql = "UPDATE command_center SET command = :command WHERE uuid = :id";
        $stmt = $this->connect()->prepare($sql);
        $stmt->bindParam(':command', $command);
        $stmt->bindParam(':id', $uuid);
        $stmt->execute();
    }

    public function redirect($url)
    {
        header("Location: $url");
    }

    function __destruct()
    {
        $this->conn = null;
    }
}
