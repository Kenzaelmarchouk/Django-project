
/*QUnit.module('magicTricks', {
    beforeEach: function() {
        var $ = django.jQuery;
        $('#qunit-fixture').append('<button class="button"></button>');
    }
});

QUnit.test('removeOnClick removes button on click', function(assert) {
    var $ = django.jQuery;
    removeOnClick('.button');
    assert.equal($('.button').length, 1);
    $('.button').click();
    assert.equal($('.button').length, 0);
});

QUnit.test('copyOnClick adds button on click', function(assert) {
    var $ = django.jQuery;
    copyOnClick('.button');
    assert.equal($('.button').length, 1);
    $('.button').click();
    assert.equal($('.button').length, 2);
});*/

let myImage = document.querySelector('img');

myImage.addEventListener('click', function() {
    let mySrc = myImage.getAttribute('src');
    if (mySrc === 'images/firefox-icon.png') {
      myImage.setAttribute('src', 'ok.png');
    } else {
      myImage.setAttribute('src', 'go.png');
    }
});