var Menu = (function () {
	var r = {
		cleanGame: function () {
			$('#game').empty();
			Engine.destroy();
		},
		items: {
			home: {
				text: 'Home',
				title: 'Start here, read the news.',
				setup: function(ev) {
					console.log('Home selected');
					r.cleanGame();
					ev.preventDefault();

					API.getHome({}, function (data) {
						var game = $('#game'),
							news = $('<ul id="news"></ul>'),
							newsItem = [];

						console.log(data);

						if (data.news && data.news.length) {
							$.each(data.news, function (i, newsPiece) {
								newsItem = $('<li>');
								newsItem.html(newsPiece.html);
								news.append(newsItem);
							});

							game.append(news);
						}

						if (data.nicknameMissing) {
							game.append('<div class="options-block"><p>You don\'t have nickname set. Visit <a class="options" href="">Options</a> to remedy that.</p></div>');
						}
					});
				}
			},
			tutorial: {
				text: 'Tutorial',
				title: 'Learn to play here.',
				setup: function(ev) {
					console.log('Tutorial selected');
					r.cleanGame();
					ev.preventDefault();
				}
			},
			lobby: {
				text: 'Lobby',
				title: 'Meet here with your opponents.',
				setup: function(ev) {
					console.log('Lobby selected');
					r.cleanGame();
					ev.preventDefault();
				}
			},
			options: {
				text: 'Options',
				title: 'Manage your account, fill out the additional info.',
				setup: function(ev) {
					console.log('Options selected');
					r.cleanGame();
					ev.preventDefault();
				}
			},
			engineTest: {
				text: 'Engine Test',
				title: 'Test engine displaying.',
				setup: function(ev) {
					var navigation = $('#navigation'),
						game = $('#game');
					console.log('Engine Test selected');
					r.cleanGame();
					game.height(1000); // This will be actual map height; height will not scale if width is unchanged.
					game.width($(window).width() - navigation.outerWidth(true) - parseInt(navigation.css('left'), 10) - parseInt(game.css('paddingLeft'), 10));
					ev.preventDefault();
					Engine.initialize();
					Engine.animate();
				}
			}
		},
		buildMenu: function () {
			var list = $('<ul id="navigation"></ul>'),
				game = $('#game'),
				item = [],
				anchor = [];
			$.each(r.items, function (id, blob) {
				item = $('<li></li>');
				anchor = $('<a href="#" title="' + blob.title + '">' + blob.text + '</a>');
				anchor.on('click', blob.setup);

				item.append(anchor);
				list.append(item);

				game.on('click', '.' + id, blob.setup);
			});

			game.before(list);

			r.items.home.setup({preventDefault: function () {}});
		},
		hijackHeading: function () {
			$('#heading').on('click', r.items.home.setup);
		}
	}, u = {
		initialize: function () {
			r.hijackHeading();
			r.buildMenu();
		}
	};

	return u;
}());