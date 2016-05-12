# coding=utf-8

messstat = b'''
<!DOCTYPE html5>
<html>
<head>
<meta charset="UTF-8">
<title>...</title>

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
    function getXmlHttp() {
         var xmlhttp;
         try {
           xmlhttp = new ActiveXObject("Msxml2.XMLHTTP");
         } catch (e) {
         try {
           xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
         } catch (e) {
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
        xmlhttp.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
        xmlhttp.onreadystatechange = function() {
            if (xmlhttp.readyState == 4) {
                if(xmlhttp.status == 200) {
                    mess = JSON.parse(xmlhttp.responseText);
                    for (var i=0; i < mess.length; i++){
                        var div = document.createElement('div');
                        document.body.appendChild(div);
                        div.innerHTML = "<div><span onclick='city("+'"'+mess[i][0]+'"'+")'>"+mess[i][1]+':'+ mess[i][2]+"</span></div>";
                        div.id=mess[i][0];
                        div.className = 'regions';
                    }
                }
            }
        }
        xmlhttp.send('stat='+1);
    }

    function city(reg){
        var citydiv='';
        if (document.getElementById('city')!=null){document.getElementById('city').remove()}
        var xmlhttp = getXmlHttp();
        xmlhttp.open('POST', '/statcity', true);
        xmlhttp.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
        reg2=JSON.stringify(reg)
        xmlhttp.onreadystatechange = function() {
            if (xmlhttp.readyState == 4) {
                if(xmlhttp.status == 200) {
                    mess = JSON.parse(xmlhttp.responseText);
                    for (var i=0; i < mess.length; i++){
                        var div = document.createElement('div');
                        citydiv = citydiv+"<div><span>"+mess[i][1]+':'+ mess[i][2]+"</span></div>";
                    }
                    var div = document.createElement('div');
                    div.id='city';
                    div.className='cities';
                    div.innerHTML=citydiv;
                    document.body.insertBefore(div, document.getElementById(reg).nextSibling);

                }
            }
        }
        xmlhttp.send('statcity='+reg2);
    }
</script>
</html>'''




