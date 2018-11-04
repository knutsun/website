function initMap() {
  //location of Gateway by coordinates
  var gatewayCoordinates = {lat: 30.865456, lng: -83.383767};

  var map = new google.maps.Map(
    document.getElementById('map'), {zoom: 12, center: gatewayCoordinates});

  var marker = new google.maps.Marker({position: gatewayCoordinates, map: map});

}
