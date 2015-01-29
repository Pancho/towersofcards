var Menu = (function () {
	var r = {
		cleanGame: function () {
			$('#game').empty().css({
				width: 'auto',
				height: 'auto'
			});
			Engine.destroy();
			Options.destroy();
			Lobby.destroy();
			Home.destroy();
		},
		items: {
			home: {
				text: 'Home',
				title: 'Start here, read the news.',
				setup: function(ev) {
					console.log('Home selected');
					r.cleanGame();
					if (ev) {
						ev.preventDefault();
					}
					Home.initialize();
					window.location.hash = 'home';
				}
			},
			tutorial: {
				text: 'Tutorial',
				title: 'Learn to play here.',
				setup: function(ev) {
					console.log('Tutorial selected');
					r.cleanGame();
					if (ev) {
						ev.preventDefault();
					}
					window.location.hash = 'tutorial';
				}
			},
			lobby: {
				text: 'Lobby',
				title: 'Meet here with your opponents.',
				setup: function(ev) {
					console.log('Lobby selected');
					r.cleanGame();
					if (ev) {
						ev.preventDefault();
					}
					Lobby.initialize();
					window.location.hash = 'lobby';
				}
			},
			options: {
				text: 'Options',
				title: 'Manage your account, fill out the additional info.',
				setup: function(ev) {
					console.log('Options selected');
					r.cleanGame();
					if (ev) {
						ev.preventDefault();
					}
					Options.initialize();
					window.location.hash = 'options';
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
					if (ev) {
						ev.preventDefault();
					}
					Engine.initialize();
					Engine.animate();

					window.location.hash = 'engineTest';
				}
			}
		},
		buildMenu: function () {
			var list = $('<ul id="navigation"></ul>'),
				game = $('#game'),
				item = [],
				anchor = [],
				hash = window.location.hash;

			hash = hash || '#home';
			hash = hash.replace('#', '');

			$.each(r.items, function (id, blob) {
				item = $('<li></li>');
				anchor = $('<a href="#" title="' + blob.title + '">' + blob.text + '</a>');
				anchor.on('click', blob.setup);

				item.append(anchor);
				list.append(item);

				game.on('click', '.' + id, blob.setup);
			});

			game.before(list);

			if (r.items[hash]) {
				r.items[hash].setup();
			} else {
				r.items.home.setup();
			}
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