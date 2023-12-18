usershadow@raspberrypi:/var/www/html $ cat station.php
<?php

$servername = "ipOfServer";
$username = "dbuser";
$password = "passw";
$dbname = "dbname";

try {
    // Create PDO connection
    $conn = new PDO("pgsql:host=$servername;dbname=$dbname", $username, $password);
    // Set the PDO error mode to exception
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    // Modify the SQL query to order by ID in ascending order
    $sql = "SELECT * FROM weatherlogs ORDER BY id ASC";
    $stmt = $conn->prepare($sql);
    $stmt->execute();

    $result = $stmt->fetchAll();

    // Start HTML output
    echo '<!DOCTYPE html><html><head><style>';
    echo 'table { border-collapse: collapse; width: 100%; }';
    echo 'th, td { border: 1px solid #ddd; padding: 8px; }';
    echo 'tr:nth-child(even){background-color: #f2f2f2;}';
    echo 'th { padding-top: 12px; padding-bottom: 12px; text-align: left; background-color: #4CAF50; color: white; }';
    echo '</style></head><body>';

    if (count($result) > 0) {
        echo "<table><tr><th>ID</th><th>Temperature</th><th>Humidity</th><th>Timestamp</th></tr>";
        // Output data of each row
        foreach($result as $row) {
            echo "<tr><td>".$row["id"]."</td><td>".$row["temperature"]." °C</td><td>".$row["humidity"]." %</td><td>".$row["timestamp"]."</td></tr>";
        }
        echo "</table>";
    } else {
        echo "0 results";
    }

    // End HTML output
    echo '</body></html>';

} catch(PDOException $e) {
    echo "Connection failed: " . $e->getMessage();
}

// Close connection
$conn = null;
?>
