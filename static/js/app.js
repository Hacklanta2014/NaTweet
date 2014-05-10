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

var markerLayers = new L.LayerGroup();
map.addLayer(heatmap);
map.addLayer(markerLayers);

$(function() {
    $( "#datepicker" ).datepicker();
  });
  
  $(function() {
    $( "#slider-range" ).slider({
      range: true,
      min: 0,
      max: 24,
      values: [ 0, 24],
      slide: function( event, ui ) {
        $( "#amount" ).val( "from " + ui.values[ 0 ] + " till " + ui.values[ 1 ] );
		window.startingHour = ui.values[ 0 ];
		window.endingHour = ui.values[ 1 ];
		//console.log(window.startingHour);
		//console.log(window.endingHour);
      }
    });
  });
  
  //$.get('api/languages').done(function(langs){
  var langs = ['English','Russian','Arabic'];
  $.each(langs, function(index, value){
	$('#langSelector').append('<option>'+value+'</options>');
  });
  //});
  
  $('#langSelector').on('click', function(){
	window.languageSelected = $('#langSelector').val();
	//console.log(window.languageSelected);
  });
  $('#go').on('click', function(){
	$.ajax({
		url: 'api/data',
		data: {
			lang: window.languageSelected,
			date: $( "#datepicker" ).datepicker( "getDate" ),
			startHour: window.startingHour,
			endingHour: window.endingHour
		}
	}).done(function(data){
	var data = [
		[33.7677129, -84.420604, 10],
	];
	for (var i = 0, l = data.length; i < l; i++) {
    heatmap.pushData(data[i][0], data[i][1], data[i][2]);
    if (data[i][2] > 20) {
        var marker = new L.Marker(new L.LatLng(data[i][0], data[i][1]));
        marker.bindPopup(data[i].toString());
        markerLayers.addLayer(marker);
    }
}
	});
  });
  