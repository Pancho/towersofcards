var Lobby = (function () {
	var r = {
		initChat: function () {
			var container = $('#toc-lobby-control'),
				chatHolder = $('<div id="lobby-chat"></div>'),
				chatLog = $('<dl></dl>'),
				chatPost = $('<form><fieldset><input type="text" name="toc-chat-text" id="toc-chat-text" /></fieldset></form>');


			chatPost.on('submit', function (ev) {
				var text = $('#toc-chat-text').val();

				ev.preventDefault();

				if ($.trim(text) !== '') {
					Realtime.send('lobbychat', text);
				}
			});

			Realtime.attach('lobbychat:message', function (msg) {
				try {
					msg = JSON.parse(msg.data);
					chatLog.append('<dd>' + msg.who + '</dd><dt>' + msg.what + '</dt>');
				} catch (e) {
					console.log(e);
				}
			});


			chatHolder.append(chatLog);
			chatHolder.append(chatPost);
			container.append(chatHolder);
		},
		initStartCustomGame: function () {

		},
		initJoinGame: function () {

		},
		showPlayerData: function () {

		}
	}, u = {
		initialize: function () {
			var game = $('#game');

			game.append('<div id="toc-play"></div><div id="toc-lobby-control"></div>');

			r.initJoinGame();
			r.initStartCustomGame();
			r.initChat();
			r.showPlayerData();
		},
		destroy: function () {

		}
	}

	return u;
}());