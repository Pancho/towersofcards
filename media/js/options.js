var Options = (function () {
	var r = {
		initNicknameForm: function () {
			var game = $('#game'),
				form = $('<form id="toc-nickname" method="get" action=""></forms>');

			game.append(form);

			form.on('submit', function (ev) {
				ev.preventDefault();
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