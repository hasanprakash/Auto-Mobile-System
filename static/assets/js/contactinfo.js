
      mapboxgl.accessToken = 'pk.eyJ1IjoiaGFzYW5wcmFrYXNoIiwiYSI6ImNrb3EyZzVjNTBxeXYyd2w0dWhhZ2FtcnoifQ.pRMaSQ5sYD4B9P3JEudspA';

      var geojson = {
        'type': 'FeatureCollection',
        'features': [
          {
            'type': 'Feature',
            'geometry': {
              'type': 'Point',
              'coordinates': [-77.032, 38.913]
            },
            'properties': {
              'title': 'Mapbox',
              'description': 'Washington, D.C.'
            }
          },
          {
            'type': 'Feature',
            'geometry': {
              'type': 'Point',
              'coordinates': [-122.414, 37.776]
            },
            'properties': {
              'title': 'Mapbox',
              'description': 'San Francisco, California'
            }
          }
        ]
      };

      var map = new mapboxgl.Map({
        container: 'map',
        style: 'mapbox://styles/mapbox/light-v10',
        center: [-96, 37.8],
        zoom: 3
      });

      // add markers to map
      geojson.features.forEach(function (marker) {
        // create a HTML element for each feature
        var el = document.createElement('div');
        el.className = 'marker';

        // make a marker for each feature and add it to the map
        new mapboxgl.Marker(el)
          .setLngLat(marker.geometry.coordinates)
          .setPopup(
            new mapboxgl.Popup({ offset: 25 }) // add popups
              .setHTML(
                '<h3>' +
                  marker.properties.title +
                  '</h3><p>' +
                  marker.properties.description +
                  '</p>'
              )
          )
          .addTo(map);
      });