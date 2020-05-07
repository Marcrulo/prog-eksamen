    google.charts.load('current', {'packages':['corechart']});
      google.charts.setOnLoadCallback(drawChart);

      function drawChart() {
        var data = google.visualization.arrayToDataTable([
          ['Month', 'Severity'],
          [ 'Jan',      12],
          [ 'Feb',      5.5],
          [ 'Mar',     14],
          [ 'Apr',      5],
          [ 'May',      3.5],
          [ 'Jun',    7],
          [ 'Jul',    7],
          [ 'Aug',    7],
          [ 'Sep',    7],
          [ 'Oct',    7],
          [ 'Nov',    7],
          [ 'Dec',    7],
        ]);

        var options = {
          title: cityLink,
          hAxis: {title: 'Age', minValue: 0, maxValue: 15},
          vAxis: {title: 'Weight', minValue: 0, maxValue: 15},
          legend: 'none'
        };

        var chart = new google.visualization.ScatterChart(document.getElementById('chart_div'));

        chart.draw(data, options);
      }
      
    var cityLat;
    var cityLng;
    var citySize;
    var citySev;
    var strCitySev;
    var cityLink;

    /////////////////////////////////////////////////////////////////
    var mymap = L.map('mapid').setView([55.805367, 12.3620975], 10);
    mymap.setMaxBounds(mymap.getBounds());
    
    var OpenStreetMap_Mapnik = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      // Set interval   minZoom < maxZoom
      minZoom: 10,
      maxZoom: 13,
      attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(mymap);


    var lat, lng;

    mymap.addEventListener('mousemove', function(ev) {
       lat = ev.latlng.lat;
       lng = ev.latlng.lng;

       document.getElementById('lat').innerHTML = "Latitude: &nbsp;&nbsp;&nbsp;" + lat.toFixed(6);
       document.getElementById('lng').innerHTML = "Longitude: " + lng.toFixed(6);
    });
    /////////////////////////////////////////////////////////////////
    var cities = []; 
    var submitCity;


    $.getJSON('https://gist.githubusercontent.com/Marcrulo/9b287fde728d4271714103aa09f3cd2e/raw/73637abeb4e15b34800f6b12fc48794e04ec4bf6/gistfile1.txt',function(data){
        for (var key in data){
          cities.push(key.charAt(0).toUpperCase()+key.slice(1));
          if (data.hasOwnProperty(key)){
            let cityLat = data[key][0];
            let cityLng = data[key][1];

            var marker = new L.Marker([cityLat, cityLng],{title:key.charAt(0).toUpperCase()+key.slice(1)});
            marker.addTo(mymap);
          }
        }  
        $.each(cities, function(i, item) {
          $("#browsers").append($("<option>").attr('value', item));
        });
        
        console.log(document.getElementById('browsers')); 
      });

    
    ///////////////////////////////////////////////////////////////////
    function updateImg(){
      //document.getElementById('CityData').src = cityLink;
    }

    ///////////////////////////////////////////////////////////////////
    var minimized = false;
    function changeMapSize(){
      if (!minimized) {
        document.getElementById("middle").className = "col-4";
        document.getElementById("middle").style.visibility = "visible";
        minimized = true;
      }
      else{
        document.getElementById("middle").className = "col-1";
        document.getElementById("middle").style.visibility = "hidden";
        minimized = false;
      }
    }

    ///////////////////////////////////////////////////////////////////
    function addNibba(crimeKey){
      /*
      var remove = false; // Dont delete background
      mymap.eachLayer(function (layer) {
        if(remove){
          mymap.removeLayer(layer);
        }
        remove = true;
      });
      */
      let category = {
        'drugs': 'blue',
        'driving' : 'orange',
        'lethal': 'black',
        'violence': 'red',
        'stealing': 'white',
        'other': 'green',
        'all': 'purple'
      };

      

      $.getJSON('https://gist.githubusercontent.com/Marcrulo/9b287fde728d4271714103aa09f3cd2e/raw/bd40a2ae264e114edd940e23af5d3851b5e86466/cities.json',function(data){
        for (var key in data){
          if (data.hasOwnProperty(key)){
            cityLat = data[key][0];
            cityLng = data[key][1];
            citySize = data[key][2];
            citySev = data[key][3];
            strCitySev = "Severity: " + citySev.toFixed(2).toString();
            cityLink = data[key][4];


            L.circle([cityLat, cityLng],{
              color: category[crimeKey],       // Kategori
              fillOpacity: 0.06*citySev,   // Styrke/severity
              radius: 1000+(citySize/20),       // Størrelse/mængde

            }).bindTooltip(strCitySev).addTo(mymap);
          }
        }  

      });
    }
    ////////////////////////////////////////////////////////////////////
    function clearCircles(){
      var remove = false; 
      mymap.eachLayer(function (layer) {
        if(remove){
          mymap.removeLayer(layer);
        }
        remove = true;
      });

      $.getJSON('https://gist.githubusercontent.com/Marcrulo/9b287fde728d4271714103aa09f3cd2e/raw/bd40a2ae264e114edd940e23af5d3851b5e86466/cities.json',function(data){
        for (var key in data){
          if (data.hasOwnProperty(key)){
            let cityLat = data[key][0];
            let cityLng = data[key][1];

            var marker = new L.Marker([cityLat, cityLng],{title:key.charAt(0).toUpperCase()+key.slice(1)});
            marker.addTo(mymap);
          }
        }   

      });
           
    }

    //////////////////////////////////////////////////////////////////////////
    function chosenCity(){
      submitCity = document.getElementById('myInput').value;
      document.getElementById('cityShow').innerHTML = submitCity;
      console.log(submitCity);
    }


    /////////////////////////////////////////////////////////////////////////
    