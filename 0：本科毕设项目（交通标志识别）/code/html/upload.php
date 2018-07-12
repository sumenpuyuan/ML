<?php
	ini_set('display_errors', true);
        error_reporting(E_ALL);
	echo '12132';

	$allowtype=array("jpg");
	$size=1000000;
	//判断文件是否可以成功上传到服务器$_FILE['myfile'['error']]为0代表上传成功
	if($_FILES['myfile']['error']){
		//header("Location:index.php?error=1");
	}
	//echo $_FILES['myfile']['name'];
	//判断上传的文件是否为允许的文件类型 通过文件后缀名
	$test=explode(".",$_FILES['myfile']['name']);
	$hz=array_pop($test);
	//通过判断文件后准 判断是否允许上传、
	if(!in_array($hz, $allowtype)){
		//header("Location:index.php?error=3");
	}
	if($_FILES['myfile']['size'] > $size){
		//header("Location:index.php?error=2");
	}
	//上传文件
	
	//$_FILES['myfile']['name']="/var/www/html/SSD-Tensorflow-master/demo/".$_FILES['myfile']['name'];
	$_FILES['myfile']['name']="/var/www/html/SSD-Tensorflow-master/demo/lvxuejie.jpg";
	echo $_FILES['myfile']['name'];
	move_uploaded_file($_FILES['myfile']['tmp_name'], $_FILES['myfile']['name']);
	//echo 'ok';
	//$filename=$_FILES['myfile']['name'];
	//var_dump($arr);
	//echo $arr[0];
	//$filename是头像图片名字
	//这是缩放的操作
	echo "hhhhh";

	//开始调用shell文件
	//$a='python /var/www/html/SSD-Tensorflow-master/notebooks/test2.py';
	//echo system($a);
	//echo "123";
	//passthru('ls -l',$returnvalue);
	//system('cat /var/www/html/SSD-Tensorflow-master/test.py',$returnvalue);
	//system('echo `su - root`',$returnvalue);
	//system('python /var/www/html/SSD-Tensorflow-master/test.py',$returnvalue);
	system('python /var/www/html/SSD-Tensorflow-master/test.py',$returnvalue);
	//echo $returnvalue;
	if ($returnvalue != 0){
	//we have a problem!
	echo "wrong";
	//add error code here
	}else{
	//we are okay
	echo "ok";
	//redirect to some other page
	header("Location: result.php");   
	//确保重定向后，后续代码不会被执行   
	exit;  
}
		
?>
