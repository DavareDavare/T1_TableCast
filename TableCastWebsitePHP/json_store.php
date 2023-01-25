<?php

if(isset($_REQUEST['submit']))
{


    $data = '';
    $filename = "data.json";
    if(is_file($filename))
    {
        $data = file_get_contents($filename);
    }
    
    
    $json_arr = json_decode($data, true);

    $json_arr[] = array('Helligkeit' => $_REQUEST['Helligkeit'], 'Geschwindigkeit' => $_REQUEST['Geschwindigkeit'], 'Text' => $_REQUEST['Text']);
    file_put_contents($filename, json_encode($json_arr));
    header("Location: http://localhost:3000/index.html");
}
?>
