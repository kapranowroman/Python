 # coding: utf-8
import json
from db_magnit import selectregion

js2="'"+selectregion()+"'"
form = b'''
<html>
<head>
<meta charset="UTF-8">
<title>...</title> <!-- Задаем заголовок документа -->
</head>

<style>
:invalid {
  border: 2px solid red;

}

:required {
  border-color: #88a;
  -webkit-box-shadow: 0 0 5px rgba(0, 0, 255, .5);
  -moz-box-shadow: 0 0 5px rgba(0, 0, 255, .5);
  -o-box-shadow: 0 0 5px rgba(0, 0, 255, .5);
  -ms-box-shadow: 0 0 5px rgba(0, 0, 255, .5);
  box-shadow: 0 0 5px rgba(0, 0, 255, .5);
}

form {
  width:300px;
  margin: 20px auto;
}

input {
  padding-left: 5px;
    font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
    border: 1px solid #ccc;
    font-size: 16px;
    width: 300px;
    min-height: 20px;
    display: block;
    margin-bottom: 5px;
    margin-top: 5px;
    outline: none;
    background-color: white;

  -webkit-border-radius:5px;
  -moz-border-radius:5px;
  -o-border-radius:5px;
  -ms-border-radius:5px;
  border-radius:5px;


}

textarea {
    margin: 0px;
    width: 300px;
    height: 150px;
    border-radius: 5px;
    resize: none;
}

select {
	border-radius: 5px;
    font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
    border: 1px solid #ccc;
    font-size: 16px;
    width: 300px;
    min-height: 23px;
    display: block;
    margin-bottom: 15px;
    margin-top: 5px;
    outline: none;
	padding-left: 5px;

}
</style>

<body onload='region()'> <!-- Основная часть документа -->

<form>

	<label>Фамилия:</label>
	<input type='text' oninput='validator("LastName")' oblur='validator("LastName")'  id='LastName' name='LastName' placeholder='Иванов' required>
	<label>Имя:</label>
	<input type='text' oninput='validator("FirstName")' oblur='validator("FirstName")'  id='FirstName' name='FirstName' placeholder='Иван' required>
	<label>Отчество:</label>
	<input type='text' oninput='validator("Fathername")' oblur='validator("Fathername")' id='Fathername' name='Fathername' placeholder='Иванович' >
	<label>Регион:</label>
	<select onChange='city()' id='Region'></select>
	<label>Город:</label>
	<select id='City'></select>
	<label>Телефон:</label>
	<input type='text' oninput='vphone()' oblur='vphone()' id='Phone' name='Phone' title='+7(000)-000-00-00'>
	<label>E-mail:</label>
	<input type="email" id='Mail' oninput='validmail()' oblur='validmail()' name='Mail' >
	<label>Комментарий:</label>
	<textarea id="Message" oninput='validator("Message")' oblur='validator("Message")' name="Message" required></textarea>



	<input type="button" value="Отправить" onclick="sendMessage()" />
</form>

  <p>json местный: <span id="summ"></span></p>
  <p>json вернулся: <span id="summ2"></span></p>
   <p>JSON String: <span id="fn3"></span></p>
</div>


<script type="text/javascript">
var val={'LastName': 0, 'FirstName': 0, 'Fathername': 1, 'Phone': 1, 'Mail':1, "Message":0};
function validmail(){
if(document.getElementById('Mail').value!=''){
			var mail_pattern=/^[\w\.\d-_]+@[\w\.\d-_]+\.\w{2,4}$/i;
			if(mail_pattern.test(document.getElementById('Mail').value)==false){
				document.getElementById('Mail').style.border="3px solid red";
                val['Mail']=0;

			}
			else {
				document.getElementById('Mail').style.border="";
                val['Mail']=1;
			}
			}
            else {
            	document.getElementById('Mail').style.border="";
            	val['Mail']=1;}

}
function validator(idfield){
	if(document.getElementById(idfield).value!=''){
			var adr_pattern=/^[a-zA-Zа-яА-Я'][a-zA-Zа-яА-Я-' ]+[a-zA-Zа-яА-Я']?$/;
			if(adr_pattern.test(document.getElementById(idfield).value)==false){
				document.getElementById(idfield).style.border="3px solid red";
                val[idfield]=0;
			}
			else {
				document.getElementById(idfield).style.border="";
                val[idfield]=1;
			}
	}
    else {
        document.getElementById(idfield).style.border="";
        val[idfield]=1;
    }

}
function vphone(){

	var tel =document.getElementById('Phone').value;
	if(tel!=''){
        if(tel.length==1){
            tel="+7("+tel;
        }
        if(tel.length==6){
            tel=tel+")";
        }
        if(tel.length==10||tel.length==13){
            tel=tel+"-";
        }
       if(tel.length>16){
            tel=tel.substring(0, tel.length - 1);
       }
        document.getElementById('Phone').value=tel;
        if (/^\+\d\(\d{3}\)\d{3}-\d{2}-\d{2}$/.test(tel)==false){
            document.getElementById('Phone').style='border: 3px solid red';
        }
        else
            document.getElementById('Phone').style='border: 1px solid #ccc';
    }
    else {
        document.getElementById('Phone').style='border: 1px solid #ccc';
        val['Phone']=1;
    }

}

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

function sendMessage() {

    var summval=0;
    var strsum='';
    for (var i in val){summval=summval+val[i]; strsum=strsum+i+':'+val[i]};
    alert(strsum);
    alert(summval);
    if (summval==6){
        alert("все пучком!");
        var mess = new Object();
        mess.lastname = document.getElementById('LastName').value;
        mess.firstname = document.getElementById('FirstName').value;
        mess.fathername=document.getElementById('Fathername').value;
        mess.cityid=document.getElementById('City').value;
        mess.phonenumber=document.getElementById('Phone').value;
        mess.mail=document.getElementById('Mail').value;
        mess.coment=document.getElementById('Message').value;
        var jsonText = JSON.stringify(mess);
        var xmlhttp = getXmlHttp(); // Создаём объект XMLHTTP
            xmlhttp.open('POST', '/magnitsmg', true); // Открываем асинхронное соединение
            xmlhttp.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded'); // Отправляем кодировку
            xmlhttp.send('mess='+jsonText); // Отправляем POST-запрос
            xmlhttp.onreadystatechange = function() { // Ждём ответа от сервера
              if (xmlhttp.readyState == 4) { // Ответ пришёл
                if(xmlhttp.status == 200) { // Сервер вернул код 200 (что хорошо)
                  document.getElementById("summ2").innerHTML = xmlhttp.responseText; // Выводим ответ сервера

                }
              }
            }
            }
    else {alert("Проверьте корректность введенных данных")}
  //var idColor = document.getElementById('LastName').value;

  //var jstxt= JSON.
	document.getElementById('summ').innerHTML = jsonText;

}

function region() {

	var objSel = document.getElementById("Region");
	var regions = JSON.parse('''+js2+b''');
	//objSel.options[objSel.options.length] = new Option();
	//document.getElementById('fn3').innerHTML = regions[0][1];
	for (var i=0; i < regions.length; i++){
		objSel.options[objSel.options.length] = new Option(regions[i][1], regions[i][0]);
	}
	}
function city(){
	document.getElementById("City").options.length = 0;
	if ( document.getElementById("Region").selectedIndex != -1 && document.getElementById("Region").options[document.getElementById("Region").selectedIndex].value ){
		var region = JSON.stringify(document.getElementById("Region").value);
		var xmlhttp = getXmlHttp(); // Создаём объект XMLHTTP
		xmlhttp.open('POST', '/magnitcity', true); // Открываем асинхронное соединение
		xmlhttp.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded'); // Отправляем кодировку
		xmlhttp.send('region='+region); // Отправляем POST-запрос
		xmlhttp.onreadystatechange = function() { // Ждём ответа от сервера
			if (xmlhttp.readyState == 4) { // Ответ пришёл
				if(xmlhttp.status == 200) { // Сервер вернул код 200 (что хорошо)
					var cities=JSON.parse(xmlhttp.responseText);

					document.getElementById("City").options[document.getElementById("City").options.length] = new Option();
					document.getElementById('fn3').innerHTML = xmlhttp.responseText;
					for (var i=0; i < cities.length; i++){
						document.getElementById("City").options[document.getElementById("City").options.length] = new Option(cities[i][1], cities[i][0]);
					}
					//for (var i=0; i < cities.length; i++){
					//	opt="<option value='"+cities[i][0]+"'>"+cities[i][1]+"</option>";
					//	document.getElementById("City").innerHTML =opt;
					//}
				}
			}
		}

	}

}


</script>

</body>
</html>
'''