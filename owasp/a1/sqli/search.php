<?php

$host = "localhost";
$db = "cyberblackhole";    // Database name
$user = "cyberblackhole"; // User
$pass = "password123"; // Password

$mysqli = new mysqli("$host", "$user", "$pass", "$db");
if ($mysqli->connect_errno) {
    echo "Failed to connect to MySQL: (" . $mysqli->connect_errno . ") " . $mysqli->connect_error;
    exit();

}else{
	$username="cyber";
	$password="changed";
	$sql="select * from login where user='$username' and password='$password'";

        $res=$mysqli->query($sql);

        while($row=$res->fetch_assoc()){
            echo 'id:  '.$row["id"];
	    print("\n");
            }       

}
?>
