<?php
$conn= new mysqli("localhost","root","123456","phoenix");
$save_status=$conn->query('update task_copy set status='.$_POST['status'].' where id='.$_POST['task_id']);
if($save_status){
echo"success";
}else{
echo"failed";
}
$conn->close();
?>
