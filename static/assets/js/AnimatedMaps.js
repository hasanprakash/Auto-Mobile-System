var map, currentAnimation;

var path = [
    new Microsoft.Maps.Location(42.8, 12.49),   //Italy
    new Microsoft.Maps.Location(51.5, 0),       //London
    new Microsoft.Maps.Location(40.8, -73.8),   //New York
    new Microsoft.Maps.Location(47.6, -122.3)   //Seattle
];

function GetMap() {
    map = new Microsoft.Maps.Map(document.getElementById("myMap"), {
        credentials: "YOUR_BING_MAPS_KEY"
    });

    //Load the Animation Module
    Microsoft.Maps.loadModule("AnimationModule");
}

function ClearMap() {
    map.entities.clear();

    if (currentAnimation != null) {
        currentAnimation.stop();
        currentAnimation = null;
    }
}

function ScalingPin() {
    ClearMap();

    var pin = new Microsoft.Maps.Pushpin(map.getCenter(), { typeName: 'scaleStyle' });
    map.entities.push(pin);
}

function DropPin() {
    ClearMap();

    var pin = new Microsoft.Maps.Pushpin(map.getCenter());
    map.entities.push(pin);

    Bing.Maps.Animations.PushpinAnimations.Drop(pin);
}

function BouncePin() {
    ClearMap();

    var pin = new Microsoft.Maps.Pushpin(map.getCenter());
    map.entities.push(pin);

    Bing.Maps.Animations.PushpinAnimations.Bounce(pin);
}

function Bounce4Pins() {
    ClearMap();

    var idx = 0;

    for (var i = 0; i < path.length; i++) {
        setTimeout(function () {
            var pin = new Microsoft.Maps.Pushpin(path[idx]);
            map.entities.push(pin);

            Bing.Maps.Animations.PushpinAnimations.Bounce(pin);
            idx++;
        }, i * 500);
    }
}

function MovePinOnPath(isGeodesic) {
}

function MoveMapOnPath(isGeodesic) {
}

function DrawPath(isGeodesic) {
}

//Initialization logic for loading the map control
(function () {
    function initialize() {
        Microsoft.Maps.loadModule('Microsoft.Maps.Map', { callback: GetMap });
    }

    document.addEventListener("DOMContentLoaded", initialize, false);
})();



