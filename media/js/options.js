var Options = (function () {
	var r = {
		initNicknameForm: function () {
			var game = $('#game'),
				form = $('<form id="toc-nickname" method="get" action="">' +
					'<fieldset>' +
						'<legend>Change your nick name</legend>' +
						'<ol>' +
							'<li><label>Nick name:</label><input type="text" name="nick" id="toc-nick"></input></li>' +
						'</ol>' +
					'<div class="toc-control">' +
						'<input type="submit"/>' +
					'</div>' +
				'</fieldset>' +
			'</form>');

			game.append(form);

			form.on('submit', function (ev) {
				ev.preventDefault();
				alert('boom! ' + $('input#toc-nick').val());
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
