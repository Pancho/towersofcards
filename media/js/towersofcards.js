var TowersOfCards = (function () {
	var r = {
			staticFilesVersion: 1421091478
		}, u = {
		initialize: function () {
			$('#gt-screen').append('<canvas id="game"></canvas>');
		}
	};

	return u;
}());

$(function () {
	TowersOfCards.initialize();
});