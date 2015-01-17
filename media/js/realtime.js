var Realtime = (function () {
	var r = {},
		u = {
			initialize: function () {
				var screen = $('#game'),
					urls = screen.data('realtimeurls') || [],
					port = screen.data('realtimeport') || 8888,
					host = window.location.host.split(':')[0];

				$.each(urls, function (name, url) {
					url = 'ws://' + host + ':' + port + url;

					r[name + 'WS'] = new WebSocket(url);

					r[name + 'WSonclose'] = [];
					r[name + 'WS'].onclose = function () {
						$.each(r[name + 'WSonclose'], function (i, fn) {
							fn();
						});
					};

					r[name + 'WSonerror'] = [];
					r[name + 'WS'].onerror = function (error) {
						$.each(r[name + 'WSonerror'], function (i, fn) {
							fn(error);
						});
					};

					r[name + 'WSonmessage'] = [];
					r[name + 'WS'].onmessage = function (message) {
						$.each(r[name + 'WSonmessage'], function (i, fn) {
							console.log('Calling function', fn);
							fn(message);
						});
					};

					r[name + 'WSonopen'] = [];
					r[name + 'WS'].onopen = function () {
						$.each(r[name + 'WSonopen'], function (i, fn) {
							fn();
						});
					};
				});

				return this;
			},
			send: function (name, data) {
//				console.log(r, r[name + 'WS'], name, name + 'WS');
				r[name + 'WS'].send(data);
			},
			close: function (name, code, reason) {
				r[name + 'WS'].close(code, reason);
			},
			attach: function (handlerEvent, cb) {
				var name = '', event = '';

				handlerEvent = handlerEvent.split(':');
				name = handlerEvent[0];
				event = handlerEvent[1];

				if (event.indexOf('on') === 0) {
					event = event.substring(2);
				}

				r[name + 'WSon' + event].unshift(cb);
			}
		};

	return u.initialize();
}());
