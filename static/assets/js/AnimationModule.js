window.Bing = window.Bing || {};
window.Bing.Maps = window.Bing.Maps || {};
window.Bing.Maps.Animations = new function () {
    var _delay = 30,    //Time in ms between each frame of the animation
        EARTH_RADIUS_KM = 6378.1;

};

// Call the Module Loaded method
Microsoft.Maps.moduleLoaded('AnimationModule');


// drop the pushpin from a specified pixel height above the map to its location on the map
function simpleAnimation(renderFrameCallback, duration) {        
    var _timerId,
        _frame = 0;

    duration = (duration && duration > 0) ? duration : 150;

    _timerId = setInterval(function () {
        var progress = (_frame * _delay) / duration;

        if (progress > 1) {
            progress = 1;
        }

        renderFrameCallback(progress);

        if (progress == 1) {
            clearInterval(_timerId);
        }

        _frame++;
    }, _delay);
}
 

// animate the pushpins position results in a nice bounce effect
this.PushpinAnimations = {
    Drop:  function (pin, height, duration) {
        height = (height && height > 0) ? height : 150;
        duration = (duration && duration > 0) ? duration : 150;

        var anchor = pin.getAnchor();
        var from = anchor.y + height;

        pin.setOptions({ anchor: new Microsoft.Maps.Point(anchor.x, anchor.y + height) });

        simpleAnimation(
            function (progress) {
                var y = from - height * progress;
                pin.setOptions({ anchor: new Microsoft.Maps.Point(anchor.x, y) });
            },
            duration
        );
    },

    Bounce: function (pin, height, duration) {
        height = (height && height > 0) ? height : 150;
        duration = (duration && duration > 0) ? duration : 1000;

        var anchor = pin.getAnchor();
        var from = anchor.y + height;

        pin.setOptions({ anchor: new Microsoft.Maps.Point(anchor.x, anchor.y + height) });

        simpleAnimation(
            function (progress) {
                var delta = Math.abs(Math.cos(progress * 2.5 * Math.PI)) / Math.exp(3 * progress);
                var y = from - height * (1 - delta);
                pin.setOptions({ anchor: new Microsoft.Maps.Point(anchor.x, y) });
            },
            duration
        );
    }
};