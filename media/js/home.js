var Home = (function () {
	var r = {
		initNews:function (newsList) {
			var game = $('#game'),
				news = $('<ul id="news"></ul>'),
				newsItem = [];

			$.each(newsList, function (i, newsPiece) {
				newsItem = $('<li>');
				newsItem.html(newsPiece.html);
				news.append(newsItem);
			});

			game.append(news);
		},
		initNicknameNotification: function () {
			var game = $('#game');

			game.append('<div class="options-block"><p>You don\'t have nickname set. Visit <a class="options" href="">Options</a> to remedy that.</p></div>');
		},
		getData: function () {
			API.getHome({}, function (data) {
				var game = $('#game'),
					news = $('<ul id="news"></ul>'),
					newsItem = [];

				console.log(data);

				if (data.news && data.news.length) {
					r.initNews(data.news);
				}

				if (data.nicknameMissing) {
					r.initNicknameNotification();
				}
			});
		}
	}, u = {
		initialize: function () {
			r.getData();
		},
		destroy: function () {

		}
	}

	return u;
}());