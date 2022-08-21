<?php

   $dbhost = $_ENV["DB_HOST"];
   $dbuser = $_ENV["DB_USER"];
   $dbpass = $_ENV["DB_PASSWD"];

   try {
      $dsn = "mysql:host=$dbhost;dbname=tp2";
      $dbh = new PDO($dsn, $dbuser, $dbpass);
   } catch (PDOException $e){
      echo $e->getMessage();
   }

   $sql = 'SELECT texto FROM mensajes;';

  // FETCH_OBJ
  $stmt = $dbh->prepare($sql);
  // Ejecutamos
  $stmt->execute();
  // Ahora vamos a indicar el fetch mode cuando llamamos a fetch:
  while($row = $stmt->fetch(PDO::FETCH_OBJ)){
      echo '<h3>'.$row->texto.'</h3>';
   }

?>

