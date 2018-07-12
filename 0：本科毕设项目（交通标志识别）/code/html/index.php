<html>
<head>
	<title>文件上传</title>
	<style type="text/css">  
		#preview, .img, img  
		{  
		 	width:640px;  
		 	height:480px;  
		 	margin:40px auto;
		}  
		#preview  
		{  
			border:1px solid #000;  
		}  
		.ui-header-positive, .ui-footer-positive {
			background-color: #f05557;
			color: #fff;
		}
		a {
			color: #f05557;
		}
		.login-button { /* 按钮美化 */  
    		width: 270px; /* 宽度 */  
    		height: 40px; /* 高度 */  
    		border-width: 0px; /* 边框宽度 */  
    		border-radius: 3px; /* 边框半径 */  
    		background: #1E90FF; /* 背景颜色 */  
    		cursor: pointer; /* 鼠标移入按钮范围时出现手势 */  
    		outline: none; /* 不显示轮廓线 */  
    		font-family: Microsoft YaHei; /* 设置字体 */  
    		color: white; /* 字体颜色 */  
    		font-size: 17px; /* 字体大小 */  
	}  
	.login-button:hover { /* 鼠标移入按钮范围时改变颜色 */  
   	 background: #5599FF;  
}  
	
	 </style>  
</head>
<body>
	<header class="ui-header ui-header-positive ui-border-b">
	<center><h1>交通标志检测</h1></center>
</header>
	<div id="preview"></div> 
	
	<form action="upload.php" method="post" enctype="multipart/form-data" name="formen" class="biaoge">
		
		<input type="hidden" name="MAX_FILE_SIZE" value="1000000">
		<input type="file"   name="myfile" style="visibility:hidden" onchange="preview(this)" id="picpath">

		<center>
		<input type="button" class="login-button" value="选择图片" onclick="document.formen.picpath.click()"/>
		</center>
		<br/>
		<center>
		<input type="submit" value="进行检测" class="login-button">
		</center>
	</form>
	
<script type="text/javascript">    
	 function preview(file)  
	 {  
		 var prevDiv = document.getElementById('preview');  
		 if (file.files && file.files[0])  
		 {  
			 var reader = new FileReader();  
			 reader.onload = function(evt){  
			 	prevDiv.innerHTML = '<img src="' + evt.target.result + '" />';  
			}    
		 	reader.readAsDataURL(file.files[0]);  
		}  
		else    
		{  
			prevDiv.innerHTML = '<div class="img" style="filter:progid:DXImageTransform.Microsoft.AlphaImageLoader(sizingMethod=scale,src=\'' + file.value + '\'"></div>';  
		}  
	 }  
 </script>  


	<?php	
	if(!empty($_GET['error'])){
		$error=$_GET['error'];
		if($error==1){
			echo "<script>alert('大小超出php配置文件大小')</script>";
		}
		else if($error == 2){
			echo "<script>alert('超出表单的约束值')</script>";
		}else if($error == 3){
			echo "<script>alert('不支持的格式，请传jpg格式')</script>";
		}else
		{
			echo "<script>alert('未知错误')</script>";
		}
	}?>

</body>
</html>
