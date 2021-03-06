var Options = (function () {
	var r = {
		initNicknameForm: function () {
			var game = $('#game'),
				form = $('<form id="toc-nickname" method="get" action="">' +
					'<fieldset>' +
						'<legend>Change your nick name</legend>' +
						'<ol>' +
							'<li><label for="toc-nick">Nick name:</label>' +
							'<input type="text" name="toc-nick" id="toc-nick" required="required"></input></li>' +
						'</ol>' +
						'<div class="toc-control">' +
							'<input type="submit"/>' +
						'</div>' +
					'</fieldset>' +
				'</form>');

			game.append(form);

			API.getNick({}, function (data) {
				form.find('#toc-nick').val(data.nickname);
			});

			form.on('submit', function (ev) {
				ev.preventDefault();
				API.postNick({"nickname": $('#toc-nick').val()}, function (data) {

				});
			});
		}
	}, u = {
		initialize: function () {
			r.initNicknameForm();
		},
		destroy: function () {

		}
	};

	return u;
}());
