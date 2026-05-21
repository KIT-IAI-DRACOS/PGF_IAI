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
  <div id="map" class="leafmap" style="border: 1px solid #ccc"></div>
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

var basemap = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    'attribution': '&copy; <a href="https://osmlab.github.io/attribution-mark/copyright/?name={{ site.title }}">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Made with <a href="https://www.naturalearthdata.com/">Natural Earth</a>',
    'minZoom': 2,
    'maxZoom': 19
  });

var LeafIcon = L.Icon.extend({
    options: {
        iconUrl: 'assets/js/images/marker-icon.png',
        shadowUrl: 'assets/js/images/marker-shadow.png',
        iconSize:    [25, 41],
    		iconAnchor:  [12, 41],
    		popupAnchor: [1, -34],
    		tooltipAnchor: [16, -28],
    		shadowSize:  [41, 41]
    }
});

var blueIcon = new LeafIcon(),
    greenIcon = new LeafIcon({iconUrl: 'assets/js/images/marker-icon-green.png'}),
    purpleIcon = new LeafIcon({iconUrl: 'assets/js/images/marker-icon-purple.png'}),
    greenpurpleIcon = new LeafIcon({iconUrl: 'assets/js/images/marker-icon-green-purple.png'}),
    bluepurpleIcon = new LeafIcon({iconUrl: 'assets/js/images/marker-icon-blue-purple.png'}),
    greenblueIcon = new LeafIcon({iconUrl: 'assets/js/images/marker-icon-green-blue.png'}),
    yellowIcon = new LeafIcon({iconUrl: 'assets/js/images/marker-icon-yellow.png'});

var yellowTarget = L.icon({
    iconUrl: 'assets/js/images/marker-target-yellow.png',
    shadowUrl: 'assets/js/images/marker-target-shadow.png',
		iconSize:    [25, 25],
		iconAnchor:  [12, 12],
		popupAnchor: [1, -14],
		tooltipAnchor: [16, -28],
		shadowSize:  [27, 27]
});

const colIcons = {
    "Blue": blueIcon,
    "Green": greenIcon,
    "Purple": purpleIcon,
    "GreenPurple": greenpurpleIcon,
    "BluePurple": bluepurpleIcon,
    "GreenBlue": greenblueIcon,
    "Yellow": yellowIcon,
    "YellowTarget": yellowTarget
};

// Deploy  

var map = L.map('map', {
  'center': [35, -5],
  'zoom': 2,
  'layers': [basemap]
});

// GeoJSONs

L.geoJson(WesternInterconnectionGeo, {style: style, onEachFeature: mouseOverFeature}).addTo(map);
L.geoJson(TexasInterconnectionGeo, {style: style, onEachFeature: mouseOverFeature}).addTo(map);
L.geoJson(NordicGridGeo, {style: style, onEachFeature: mouseOverFeature}).addTo(map);
L.geoJson(RussianGeo, {style: style, onEachFeature: mouseOverFeature}).addTo(map);
L.geoJson(BalticGeo, {style: style, onEachFeature: mouseOverFeature}).addTo(map);
L.geoJson(NationalGridGeo, {style: style, onEachFeature: mouseOverFeature}).addTo(map);
L.geoJson(ContinentalEuropeGeo, {style: style, onEachFeature: mouseOverFeature}).addTo(map);
L.geoJson(IrishGeo, {style: style, onEachFeature: mouseOverFeature}).addTo(map);
L.geoJson(IcelandGeo, {style: style, onEachFeature: mouseOverFeature}).addTo(map);
L.geoJson(FaroeGeo, {style: style, onEachFeature: mouseOverFeature}).addTo(map);
L.geoJson(MallorcaGeo, {style: style, onEachFeature: mouseOverFeature}).addTo(map);
L.geoJson(GranCanariaGeo, {style: style, onEachFeature: mouseOverFeature}).addTo(map);
L.geoJson(SouthAfricaGeo, {style: style, onEachFeature: mouseOverFeature}).addTo(map);
L.geoJson(JapanGeo, {style: style, onEachFeature: mouseOverFeature}).addTo(map);

L.geoJSON(locations, {
    filter: function(feature) {
        return feature.properties.icon === "Green";
    },
    onEachFeature: iconBindPopup,
}).addTo(map);

function iconBindPopup(feature, layer) {
    if (feature.properties && feature.properties.location) {
        layer.bindPopup(feature.properties.logo + feature.properties.location);
    };
    if (feature.properties.icon) {
        layer.setIcon(colIcons[feature.properties.icon]);
    };
    if (feature.properties.icon === "Green") {
        layer.on('click', function() {
            window.location.href = BASE_URL + '/database/#standalone-measurements';
        });
    };
}


var SynchMeasurements = [[[49.0,  8.4],[53.1,  8.2]], [[49.0,  8.4],[38.7, -9.1]], [[49.0,  8.4],[41.0, 28.9]]];
var SemiSynchMeasurements = [[[49.0,  8.4],[46.6,  21.0]],[[49.0,  8.4],[47.6,  17.6]]];
var SemiSynchMeasurementsNG = [[[63.126178, 15.205319],[66.353562, 19.323426]], [[63.126178, 15.205319],[58.310608, 14.511484]]];
var SemiSynchMeasurementsNGSTRONG = [[[59.350029, 18.070009],[57.689769, 11.973701]], [[59.350029, 18.070009],[55.711850, 13.210120]], [[59.350029, 18.070009],[65.617792, 22.135986]], [[59.350029, 18.070009],[61.494200, 23.780750]], [[59.350029, 18.070009],[60.186463, 24.829515]], [[59.350029, 18.070009],[63.419443, 10.401995]]];



// Layers and layer control
// var LayerOfMap = { "<span style='color: black'><b>OpenStreetMap</b></span>": basemap};
// L.control.layers(LayerOfMap, years).addTo(map);

// PowerGrid Overlay
function style(feature) {
    return {
        fillColor: feature.colour,
        weight: 0,
        fillOpacity: 0.4
    };
}

var info = L.control();
info.onAdd = function (map) {
    this._div = L.DomUtil.create('div', 'info'); // create a div with a class "info"
    this.update();
    return this._div;
};
info.update = function (props) {
    this._div.innerHTML = '<h9>Synchronous Areas</h9><br />' +  (props ?
        '<b><h9>' + props.name + '</h9></b><br />'
        : '<h9>Hover over an area</h9>');
};

function mouseOverFeature(feature, layer) {
    layer.on({
        mouseover: function(e) {
        		var layer = e.target;
            info.update(layer.feature.properties);
        },
        mouseout: function(e) { info.update(); }
    });
}

var legend = L.control({position: 'bottomleft'});
legend.onAdd = function (map) {
    var div = L.DomUtil.create('div', 'info legend'),
        grades = [0, 10, 20, 50, 100, 200, 500, 1000],
        labels = [];
    div.innerHTML = '<img id="x" src="assets/js/images/marker-icon-green.png" width="30" height="30"/>' + '<h9>  Standalone Measurements</h9>';
    return div;
};

legend.addTo(map);
info.addTo(map);



</script>

<div style="margin-top:4em"></div>

{% include_relative details.md %}
