# coding: utf-8
import json
messlist = b'''
 <!DOCTYPE html5>
 <html>
 <head>
 <meta charset="UTF-8">
 <title>...</title>

 </head>

 <body onload='showmess()'>
 </body>

 <script>


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

     function showmess(){
        var xmlhttp = getXmlHttp();
        xmlhttp.open('POST', '/mess', true);
        xmlhttp.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
        xmlhttp.send('mess='+1);
        xmlhttp.onreadystatechange = function() {
            if (xmlhttp.readyState == 4) {
                if(xmlhttp.status == 200) {
                    var mess = JSON.parse(xmlhttp.responseText)
                    for (var i=0; i < mess.length; i++){
                        var div = document.createElement('div');
                            div.className = "message";
                            div.id=mess[i][0];
                            div.innerHTML = "<div><span>"+ mess[i][1]+"</span></div>" + "<div><button onclick='deletemess("+'"'+mess[i][0]+'"'+")'>del</button></div>";
                        document.body.appendChild(div);
                    }
                }
            }
        }
     }

     function deletemess(id) {
        var idpers=JSON.stringify(id);
        var xmlhttp = getXmlHttp();
        xmlhttp.open('POST', '/delmess', true);
        xmlhttp.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
        xmlhttp.send('messdel='+idpers);
        xmlhttp.onreadystatechange = function() {
            if (xmlhttp.readyState == 4) {
                if(xmlhttp.status == 200) {
                    document.getElementById(id).remove();
                }
            }
        }
     }
 </script>

 <style>
 .message {
   padding: 15px;
   border: 1px solid #C0C5E6;
   border-radius: 4px;
   color: black;
   background-color: #FFFFFF;
 }

 </style>


 </html>'''




