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

    protected function get($id)
    {
        if ($this->conn == null) {
            $this->connect();
        }

        $sql = "SELECT * FROM command_center WHERE user_id = :id";
        $stmt = $this->getConnect()->prepare($sql);
        $stmt->bindParam(':id', $id);
        $stmt->execute();
        return $stmt->fetch(PDO::FETCH_ASSOC);
    }

    protected function put($id, $command)
    {
        if ($this->conn == null) {
            $this->connect();
        }
        $sql = "UPDATE command_center SET command = :command WHERE user_id = :id";
        $stmt = $this->getConnect()->prepare($sql);
        $stmt->bindParam(':command', $command);
        $stmt->bindParam(':id', $id);
        $stmt->execute();
    }

    protected function getConnect()
    {
        return $this->connect();
    }

    function __destruct()
    {
        $this->conn = null;
    }
}
