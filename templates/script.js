<!DOCTYPE html>
<html>
<head>
  <title>Police data scraper</title>
</head>

<!-- BOOTSTRAP -->
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
<script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>

<!-- LEAFLET -->
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.6.0/dist/leaflet.css"
   integrity="sha512-xwE/Az9zrjBIphAcBb3F6JVqxf46+CDLwfLMHloNu6KEQCAWi6HcDUbeOfBIptF7tcCzusKFjFw2yuvEpDL9wQ=="
   crossorigin=""/>
<script src="https://unpkg.com/leaflet@1.6.0/dist/leaflet.js"
   integrity="sha512-gZwIG9x3wUXg2hdXF6+rVkLF/0Vi9U8D2Ntg4Ga5I5BZpVkVxlJWbSQtXPSiUTtC0TjtGOmxa1AJPuV0CPthew=="
   crossorigin=""></script>

<!-- AJAX -->
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>

<!-- Add icon library -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">


<!-- Google Charts -->
<script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
    


<body>
  
  <div class="row">
    <div class="col-3" id="main" style="margin-top: 30px; margin-left: 50px">
      

      <div id="lat">Latitude: &nbsp;&nbsp;&nbsp;55.905367</div>
      <div id="lng">Longitude: 12.362097</div>

      <br>
      <p><b>Search city</b></p>
      <input list="browsers" name="browser">
      <datalist id="browsers"></datalist>
      <button class="btn btn-info" id="showImg" onclick="updateImg()">Submit</button>
      <br>
      <br>


      <div class="row">
        
        <div class="col-6">
          <input onclick="categoryCircles('drugs')" type="checkbox" id="category1" name="category1">
          <label for="category1"> Drugs</label><br>
          <input onclick="categoryCircles('driving')" type="checkbox" id="category2" name="category2">
          <label for="category2"> Driving</label><br>
          <input onclick="categoryCircles('lethal')" type="checkbox" id="category3" name="category3">
          <label for="category3"> Lethal</label><br><br>
        </div>

        <div class="col-6">
          <input onclick="categoryCircles('violence')" type="checkbox" id="category4" name="category4">
          <label for="category4"> Violence</label><br>
          <input onclick="categoryCircles('stealing')" type="checkbox" id="category5" name="category5">
          <label for="category5"> Stealing</label><br>
          <input onclick="categoryCircles('other')" type="checkbox" id="category6" name="category5">
          <label for="category6"> Other</label><br><br>
        </div>

      </div> 

      <div>
        <input onclick="categoryCircles('all')" type="checkbox" id="category7" name="category7">
        <label for="category7"> Show All</label><br>
      </div>


      <div style="margin-top: 100%">
        <button type="button" class="btn btn-info" onclick="toggleMarker()">Toggle Markers</button>
        <button type="button" class="btn btn-warning" onclick="clearCircles()">Clear Circles</button>
      </div>


    </div>
    
    <div class="col-1" id="middle" style="visibility: hidden">
      <div id="chart_div" style="width: 700px; height: 500px;"></div>
    </div> 
    <div class="col" id="mapid" style="height: 1000px"></div>
    
  </div>

    
  
  

  <script>
    /*MAP OBJECT*/
    var mymap = L.map('mapid').setView([55.805367, 12.3620975], 10);
    mymap.setMaxBounds(mymap.getBounds());

    var OpenStreetMap_Mapnik = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      minZoom: 10,
      maxZoom: 13,
      attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(mymap);


    /*COORDINATES*/
    var lat, lng;

    mymap.addEventListener('mousemove', function(ev) {
       lat = ev.latlng.lat;
       lng = ev.latlng.lng;

       document.getElementById('lat').innerHTML = "Latitude: &nbsp;&nbsp;&nbsp;" + lat.toFixed(6);
       document.getElementById('lng').innerHTML = "Longitude: " + lng.toFixed(6);
    });


    /*GET CITY DATA*/
    var xhReq = new XMLHttpRequest();
    xhReq.open("GET", 'https://gist.githubusercontent.com/Marcrulo/9b287fde728d4271714103aa09f3cd2e/raw/a76de71dc85145b2463ed572a204d3413917a859/cities.json', false);
    xhReq.send(null);
    var jsonObject = JSON.parse(xhReq.responseText);


    /*TOGGLE MARKERS*/
    var layerGroupMarker = L.layerGroup().addTo(mymap);
    var toggleOn = false; 
    function toggleMarker(){
      if (!toggleOn){
        for (var key in jsonObject) {
          if (jsonObject.hasOwnProperty(key)){
            let cityLat = jsonObject[key][0];
            let cityLng = jsonObject[key][1];

            var marker = new L.Marker([cityLat, cityLng],{title:key.charAt(0).toUpperCase()+key.slice(1)});
            marker.addTo(layerGroupMarker);
          }
          toggleOn = true
        }
      }
      else{
        layerGroupMarker.clearLayers();
        toggleOn = false;
      }
    }

    /*SET CIRCLES BY CATEGORIES*/
    var layerGroupDrugs = L.layerGroup().addTo(mymap);
    var layerGroupDriving = L.layerGroup().addTo(mymap);
    var layerGroupLethal = L.layerGroup().addTo(mymap);
    var layerGroupViolence = L.layerGroup().addTo(mymap);
    var layerGroupStealing = L.layerGroup().addTo(mymap);
    var layerGroupOther = L.layerGroup().addTo(mymap);
    var layerGroupAll = L.layerGroup().addTo(mymap);

    var checked = {
      'drugs': true,
      'driving' : true,
      'lethal': true,
      'violence': true,
      'stealing': true,
      'other': true,
      'all': true,
    }
    var categoryColor = {
      'drugs': 'blue',
      'driving' : 'orange',
      'lethal': 'black',
      'violence': 'red',
      'stealing': 'white',
      'other': 'green',
      'all': 'purple'
    };
    var categoryLayerGroup = {
      'drugs': layerGroupDrugs,
      'driving' : layerGroupDriving,
      'lethal': layerGroupLethal,
      'violence': layerGroupViolence,
      'stealing': layerGroupStealing,
      'other': layerGroupOther,
      'all': layerGroupAll
    };

    /*DRAW CIRCLES*/
    function categoryCircles(category){
      /*CHECKBOXES*/
      if (category != 'all') {
        checked[category] = !checked[category];
        document.getElementById('category7').checked = false;
        layerGroupAll.clearLayers();
      }
      else{
        for(key in checked){
          checked[key] = true;
        }
        for(var i = 1; i <= 6; i++){
          let a = 'category' + i.toString();
          document.getElementById(a).checked = false;
        }
      }
      
      if (!checked[category]) {
        for(var key in jsonObject){
          let city = jsonObject[key];
          var circle = new L.circle([city[0], city[1]],{
            color: categoryColor[category],       
            fillOpacity: 0.06*city[4],   
            radius: 1000+(city[2]/20),       
          }).bindTooltip(
            "Severity: " + city[4].toFixed(2).toString()
          ).addTo(categoryLayerGroup[category]);
        }
        if (category == 'all') {
          layerGroupDrugs.clearLayers();
          layerGroupDriving.clearLayers();
          layerGroupLethal.clearLayers();
          layerGroupViolence.clearLayers();
          layerGroupStealing.clearLayers();
          layerGroupOther.clearLayers();
          for(var i = 1; i <= 6; i++){
            let a = 'category' + i.toString();
            document.getElementById(a).checked = false;
          }
          for(key in checked){
            checked[key] = true;
          }
          checked['all'] = false;
        }
        
      }
      else{
        categoryLayerGroup[category].clearLayers();
      }
  
    




    }

    /*CLEAR ALL CIRCLES*/
    function clearCircles(){
      for(var i = 1; i <= 7; i++){
        let a = 'category' + i.toString();
        document.getElementById(a).checked = false;
      }
      for(key in checked){
        checked[key] = true;
      }
      layerGroupDrugs.clearLayers();
      layerGroupDriving.clearLayers();
      layerGroupLethal.clearLayers();
      layerGroupViolence.clearLayers();
      layerGroupStealing.clearLayers();
      layerGroupOther.clearLayers();
      layerGroupAll.clearLayers();
    }

    function chooseCity(){

    }

    function resetCityView(){

    }

    function showCrime(){

    }





  </script>

</body>








</html>