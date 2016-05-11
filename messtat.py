# coding=utf-8
arrregions= {
	"Краснодарский край":{

    	"Краснодар": 4,
        "Кропоткин": 5
     },
     "Ставропольский край":{

     	"Пятигорск": 5,
        "Ставрополь": 6
     }
}
messstat = b'''
<!DOCTYPE html5> <!-- Объявление формата документа -->
<html>
<head> <!-- Техническая информация о документе -->
<meta charset="UTF-8"> <!-- Определяем кодировку символов документа -->
<title>...</title> <!-- Задаем заголовок документа -->

</head>
<body onload='showstat()'>
</body>

<style>
.regions{
  padding: 5px;
  font-weight:bold;
  cursor: pointer;
}
.regions:hover{
text-decoration:underline;
}
.cities{
  padding: 15px;

}
</style>
<script>
var mess=[];
var region = {
	"Краснодарский край":"99f89ef5-fad9-48da-ad4c-de9ec296c7c8",
    "Ставропольский край":"d33eaf26-d412-490b-8efd-7f870fe697aa"}


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


function showstat(){

var xmlhttp = getXmlHttp();
xmlhttp.open('POST', '/statistic', true);
xmlhttp.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded'); // Отправляем кодировку
xmlhttp.send('stat='+1); // Отправляем POST-запрос
xmlhttp.onreadystatechange = function() { // Ждём ответа от сервера
 	if (xmlhttp.readyState == 4) { // Ответ пришёл
 		if(xmlhttp.status == 200) { // Сервер вернул код 200 (что хорошо)
 			mess = JSON.parse(xmlhttp.responseText);
 			//alert(mess["Краснодарский край"]["Краснодар"]);
            for (var i in mess){
	            var summ=0;
                var div = document.createElement('div');
                document.body.appendChild(div);
                for (b in mess[i]){
                    summ=summ+mess[i][b];
                }
                div.innerHTML = "<div><span onclick='city("+'"'+i+'"'+")'>"+i+':'+ summ+"</span></div>";
                div.id=region[i];
                div.className = 'regions';
                //alert(i)
            }

 			//document.getElementById('fn3').innerHTML = xmlhttp.responseText;
        }
 	}
}

}

function city(reg){
//document.getElementById('region').parentNode.removeChild(document.getElementById('city'));
//document.getElementById('region').remove(document.getElementById('region'));
//alert(reg);
//location.reload();
if (document.getElementById('city')!=null){document.getElementById('city').remove()}
var citydiv='';
for (b in mess[reg]){
	citydiv = citydiv+"<div><span>"+b+':'+ mess[reg][b]+"</span></div>";
}
var div = document.createElement('div');
div.id='city';
div.className='cities';
div.innerHTML=citydiv;
document.body.insertBefore(div, document.getElementById(region[reg]).nextSibling);
}
</script>
</html>'''




