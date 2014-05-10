var mapboxTiles = L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
});


//heatmap


var map = L.map('map')
    .addLayer(mapboxTiles)
    .setView([33.7677129, -84.420604], 12);

var heatmap = new L.TileLayer.HeatCanvas({}, {
    'step': 0.5,
    'degree': HeatCanvas.LINEAR,
    'opacity': 0.5
});

var data = [
    [33.7677129, -84.420604, 10],
];

var markerLayers = new L.LayerGroup();
for (var i = 0, l = data.length; i < l; i++) {
    heatmap.pushData(data[i][0], data[i][1], data[i][2]);
    if (data[i][2] > 20) {
        var marker = new L.Marker(new L.LatLng(data[i][0], data[i][1]));
        marker.bindPopup(data[i].toString());
        markerLayers.addLayer(marker);
    }
}
map.addLayer(heatmap);
map.addLayer(markerLayers);