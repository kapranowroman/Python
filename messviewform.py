 # coding: utf-8
import json
from db_magnit import messread

js2="'"+messread()+"'"
messlist = b'''
<!DOCTYPE html5>
<html>
<head> <!-- Техническая информация о документе -->
<meta charset="UTF-8"> <!-- Определяем кодировку символов документа -->
<title>...</title> <!-- Задаем заголовок документа -->

</head>

<body onload='showmess(messages)'> 
</body>

<script>


function getXmlHttp() {
    var xmlhttp;
    try {
      xmlhttp = new ActiveXObject("Msxml2.XMLHTTP");
    } catch (e) {
    try {
      xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
    } catch (E) {
      xmlhttp = false;
    }
    }
    if (!xmlhttp && typeof XMLHttpRequest!='undefined') {
      xmlhttp = new XMLHttpRequest();
    }
    return xmlhttp;
}

function showmess(mess){
	var xmlhttp = getXmlHttp();
	xmlhttp.open('POST', '/mess', true);
	xmlhttp.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded'); // Отправляем кодировку
	xmlhttp.send('mess='1); // Отправляем POST-запрос
	xmlhttp.onreadystatechange = function() { // Ждём ответа от сервера
		if (xmlhttp.readyState == 4) { // Ответ пришёл
			if(xmlhttp.status == 200) { // Сервер вернул код 200 (что хорошо)
			  	var messages = JSON.parse(xmlhttp.responseText)
		}
	}

	
	for (var i=0; i < mess.length; i++){
		var div = document.createElement('div');
			div.className = "message";
			div.id=mess[i][0]; 
			div.innerHTML = "<div>"+ mess[i][1]+"</div>" + "<div><button onclick='deletemess("+'"'+mess[i][0]+'"'+")'>del</button></div>";
	 	document.body.appendChild(div);
	}
}
function deletemess(id) {
	var idpers=JSON.stringify(id);
	var xmlhttp = getXmlHttp();
	xmlhttp.open('POST', '/delmess', true);
	xmlhttp.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded'); // Отправляем кодировку
	xmlhttp.send('messdel='+idpers); // Отправляем POST-запрос
	xmlhttp.onreadystatechange = function() { // Ждём ответа от сервера
		if (xmlhttp.readyState == 4) { // Ответ пришёл
			document.getElementById(id).remove();
		}
	}
}
</script>

<style>
.message {
  padding: 15px;
  border: 1px solid #d6e9c6;
  border-radius: 4px;
  color: #3c763d;
  background-color: #dff0d8;
}

</style>


</html>'''




