---
Title: Home

menus:
  main:
    weight: 1
    title: Home
layout: splash
classes: wide
---
<div class="wrapper">
  <div id="map" style="border: 1px solid #ccc;">
    <div class="map-info-box" id="map-info"><strong>Synchronous Areas</strong><br>Hover over an area</div>
    <div class="map-legend-box" id="map-legend"></div>
  </div>
  <div id="slider"></div>
</div>


<script type="text/javascript" src="assets/GeoJSON/WesternInterconnection.js"></script>
<script type="text/javascript" src="assets/GeoJSON/TexasInterconnection.js"></script>
<script type="text/javascript" src="assets/GeoJSON/NordicGrid.js"></script>
<script type="text/javascript" src="assets/GeoJSON/Russian.js"></script>
<script type="text/javascript" src="assets/GeoJSON/Baltic.js"></script>
<script type="text/javascript" src="assets/GeoJSON/NationalGrid.js"></script>
<script type="text/javascript" src="assets/GeoJSON/ContinentalEurope.js"></script>
<script type="text/javascript" src="assets/GeoJSON/Irish.js"></script>
<script type="text/javascript" src="assets/GeoJSON/Iceland.js"></script>
<script type="text/javascript" src="assets/GeoJSON/Faroe.js"></script>
<script type="text/javascript" src="assets/GeoJSON/Mallorca.js"></script>
<script type="text/javascript" src="assets/GeoJSON/GranCanaria.js"></script>
<script type="text/javascript" src="assets/GeoJSON/SouthAfrica.js"></script>
<script type="text/javascript" src="assets/GeoJSON/Japan.js"></script>

<script src="assets/locations/locations.js"></script>

<script>
const map = new maplibregl.Map({
  container: 'map',
  style: 'https://tiles.openfreemap.org/styles/liberty',
  center: [-5, 35],
  zoom: 2,
  minZoom: 2
});

const geoRegions = [
  ['western-interconnection', () => WesternInterconnectionGeo],
  ['texas-interconnection',   () => TexasInterconnectionGeo],
  ['nordic-grid',             () => NordicGridGeo],
  ['russian',                 () => RussianGeo],
  ['baltic',                  () => BalticGeo],
  ['national-grid',           () => NationalGridGeo],
  ['continental-europe',      () => ContinentalEuropeGeo],
  ['irish',                   () => IrishGeo],
  ['iceland',                 () => IcelandGeo],
  ['faroe',                   () => FaroeGeo],
  ['mallorca',                () => MallorcaGeo],
  ['gran-canaria',            () => GranCanariaGeo],
  ['south-africa',            () => SouthAfricaGeo],
  ['japan',                   () => JapanGeo],
];

function prepareGeo(data) {
  return {
    ...data,
    features: data.features.map(f => ({
      ...f,
      properties: { ...f.properties, colour: f.colour || '#3388ff' }
    }))
  };
}

const allMarkers = [];
const infoEl  = document.getElementById('map-info');
const legendEl = document.getElementById('map-legend');

map.on('load', function() {
  const fillLayers = [];

  geoRegions.forEach(([id, getData]) => {
    map.addSource(id, { type: 'geojson', data: prepareGeo(getData()) });
    map.addLayer({
      id: id + '-fill',
      type: 'fill',
      source: id,
      paint: {
        'fill-color': ['get', 'colour'],
        'fill-opacity': 0.4
      }
    });
    fillLayers.push(id + '-fill');
  });

  fillLayers.forEach(lid => {
    map.on('mousemove', lid, e => {
      map.getCanvas().style.cursor = 'pointer';
      infoEl.innerHTML = '<strong>Synchronous Areas</strong><br><b>' + e.features[0].properties.name + '</b>';
    });
    map.on('mouseleave', lid, () => {
      map.getCanvas().style.cursor = '';
      infoEl.innerHTML = '<strong>Synchronous Areas</strong><br>Hover over an area';
    });
  });


  legendEl.innerHTML = '<img src="' + BASE_URL + '/assets/js/images/marker-icon-green.png" width="18" height="30" style="vertical-align:middle"> Standalone Measurements';

  locations.features
    .filter(f => f.properties.icon === 'Green')
    .forEach(f => {
      const p = f.properties;
      const [lng, lat] = f.geometry.coordinates;

      const el = document.createElement('div');
      el.style.cssText = 'width:25px;height:41px;background:url(' + BASE_URL + '/assets/js/images/marker-icon-green.png) no-repeat center/contain;cursor:pointer;animation:fadein 1s;';

      const marker = new maplibregl.Marker({ element: el }).setLngLat([lng, lat]);

      el.addEventListener('click', function(e) {
        e.stopPropagation();
        window.location.href = BASE_URL + '/database/#standalone-measurements';
      });

      allMarkers.push({ marker, start_date: p.start_date, end_date: p.end_date });
    });

  var sliderEl = document.getElementById('slider');
  noUiSlider.create(sliderEl, {
    start: [2017, 2026],
    connect: true,
    step: 1,
    behaviour: 'tap-drag',
    range: { min: 2017, max: 2026 },
    pips: { mode: 'steps', density: 6 }
  });

  sliderEl.noUiSlider.on('update', function() {
    const t = sliderEl.noUiSlider.get(true);
    allMarkers.forEach(({ marker, start_date, end_date }) => {
      const visible = start_date <= t[1] && end_date >= t[0];
      if (visible && !marker._map) marker.addTo(map);
      else if (!visible && marker._map) marker.remove();
    });
  });
});
</script>

<div style="margin-top:4em"></div>

{% include_relative details.md %}
