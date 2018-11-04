<?php
$conn= new mysqli("localhost","root","123456","phoenix");
$conn->autocommit(FALSE);
$select_result=$conn->query('select*from task_copy where status = 0 and tag_name="'.$_POST['tag_name'].'" limit 1 for update');
$row=$select_result->fetch_assoc();
echo json_encode(array('task_id' => $row['id'], 'src' => $row['copy_src'],'dest' => $row['copy_dest']));
$conn->query('update task_copy set status=1,host="'.$_POST['host'].'" where id='.$row['id']);
$conn->commit();
$conn->close();
?>
