var API = (function () {
	var r = {},
		u = {
			initialize: function () {
				var screen = $('#game'),
					urls = screen.data('apiurls') || [];

				$.each(urls, function (name, url) {
					u['get' + Utils.capitalize(name)] = function (data, success, error) {
						$.ajax({
							url: url,
							method: 'get',
							data: data,
							success: success || function () {},
							error: error || function () {}
						});
					};
					u['post' + Utils.capitalize(name)] = function (data, success, error) {
						$.ajax({
							url: url,
							method: 'post',
							data: data,
							success: success || function () {},
							error: error || function () {}
						});
					};
				});
				return this;
			}
		};

	return u.initialize();
}());