var Engine = (function () {
	var r = {
		stopped: false,
		canvas: null,
		frameQueue: [
			{
				'x': 0,
				'y': 0,
				'img': (function () {
					var img = new Image();

					img.src = '/media/img/cms/terrain/grass.png';

					return img;
				}())
			}
		],
		initialized: false,
		resizeCanvas: function () {
			r.canvas.width = window.innerWidth;
			r.canvas.height = window.innerHeight;
		},
		initResize: function () {
			r.resizeCanvas();
			$(window).on('resize', r.resizeCanvas);
		},
		/*
		Draw single object
		 */
		draw: function (obj) {
			var context = r.canvas.getContext('2d');

			context.drawImage(obj.img, obj.x, obj.y);
		}
	}, u = {
		/*
		 Create a queue for the drawing of the frame. Elements will be painted in specified order.
		 With this one can achieve the z-index, which would otherwise be elusive

		 Use concat in case you have predefined list of objects (map, towers states, defenses states, lists
		 that don't need new calculations and that don't change through a game)
		 */
		queue: function (obj, concat) {
			if (concat) {
				r.frameQueue.concat(obj);
			} else {
				r.frameQueue.push(obj);
			}
		},
		animate: function () {
			var context = r.canvas.getContext('2d');

			if (r.stopped) {
				return;
			}

			// Clear everything
			context.clearRect(0, 0, r.canvas.width, r.canvas.height);
			// Draw the elements on queue
			$.each(r.frameQueue, function (i, obj) {
				r.draw(obj);
			});
			// Clear queue for the next frame
//			r.frameQueue = [];
			// Once doe with this frame, request next
			console.log('Frame, ', window.requestAnimationFrame(u.animate));
//			window.requestAnimationFrame(u.animate);
		},
		show: function () {
			$('#game-canvas').show();
			r.stopped = false;
		},
		hide: function () {
			$('#game-canvas').hide();
			r.stopped = true;
		},
		initialize: function (config) {
			var win = $(window);

			// Initialize once
			if (r.initialized) {
				return 'Already initialized';
			}

			config = config || {};

			$('#' + (config.canvasContainerId || 'game')).append('<canvas id="game-canvas"></canvas>');

			r.canvas = document.getElementById('game-canvas');

			// Init resizing
			r.initResize();

			// Initialized
			r.initialized = true;

			return this;
		}
	};

	return u.initialize();
}());