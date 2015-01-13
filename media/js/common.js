/*
 *******************************************************
 *******************************************************
 *************** jQuery Extensions *********************
 *******************************************************
 *******************************************************
 */

/*
 Damn it Apple... who in their right mind would cache POST requests?!?!
 */
jQuery.ajaxSetup({
	headers: {
		"cache-control": "no-cache"
	}
});

// Jquery Django CSRF Token propagation
// Not stock - I've changed a bunch of things to follow JS best practices (single var, ===, ...)

jQuery(document).ajaxSend(function (event, xhr, settings) {
	function getCookie(name) {
		var cookieValue = null, cookies = [], i = 0, j = 0, cookie = {};
		if (document.cookie && document.cookie !== '') {
			cookies = document.cookie.split(';');
			for (j = cookies.length; i < j; i += 1) {
				cookie = jQuery.trim(cookies[i]);
				// Does this cookie string begin with the name we want?
				if (cookie.substring(0, name.length + 1) === (name + '=')) {
					cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
					break;
				}
			}
		}
		return cookieValue;
	}

	function sameOrigin(url) {
		// url could be relative or scheme relative or absolute
		var host = document.location.host, // host + port
			protocol = document.location.protocol,
			sr_origin = '//' + host,
			origin = protocol + sr_origin;
		// Allow absolute or scheme relative URLs to same origin
		return (url === origin || url.slice(0, origin.length + 1) === origin + '/') || (url === sr_origin || url.slice(0, sr_origin.length + 1) === sr_origin + '/') || // or any other URL that isn't scheme relative or absolute i.e relative.
			!(/^(\/\/|http:|https:).*/.test(url));
	}

	function safeMethod(method) {
		return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
	}

	if (!safeMethod(settings.type) && sameOrigin(settings.url)) {
		xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
	}
});

// Jquery Django CSRF Token propagation END!

var TowersOfCardsImageList = [];

// Use the following function to preload images to the client
(function () {
	var latestTimestamp = 0, currentTimestamp = 0, metaValue = '', i = 0, j = TowersOfCardsImageList.length, image = null;
	if ('localStorage' in window) {
		metaValue = $('meta[name=application-name]').prop('content');

		if (!metaValue) {
			return;
		}

		currentTimestamp = parseInt(metaValue.substring(metaValue.indexOf('(') + 1, metaValue.length - 1), 10);
		latestTimestamp = localStorage.latestTimestamp && parseInt(localStorage.latestTimestamp, 10) || 0;

		if (!latestTimestamp || currentTimestamp > latestTimestamp) {
			for (; i < j; i += 1) {
				image = new Image();
				image.src = TowersOfCardsImageList[i];
				if (!!console) {
					console.log('Loading image from ' + TowersOfCardsImageList[i]);
				}
			}

			localStorage.latestTimestamp = currentTimestamp;
		}
	}
}());