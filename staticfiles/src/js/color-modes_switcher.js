try {
	const colorMode_switcher = localStorage.getItem('colorMode_switcher');
	if (colorMode_switcher === null) {
		throw new Error('The color theme switched to light-mode as default');
	} else {
		$('html').attr('data-bs-theme', `${colorMode_switcher}`);
		if (colorMode_switcher == 'dark') {
			$('header').css('background-color', '#212529');
		} else {
			$('header').css('background-color', '#fff');
		}
	}
} catch (e) {
	$('html').attr('data-bs-theme', `${'light'}`);
	$('header').css('background-color', '#fff');
	localStorage.setItem('colorMode_switcher', 'light');
}

// color theme switcher button
if (document.getElementById('colorMode_switcher')) {
	document.getElementById('colorMode_switcher').addEventListener('click', () => {
		const switcher = $('html').attr('data-bs-theme');
		if (switcher == 'dark') {
			$('html').attr('data-bs-theme', 'light');
			$('header').css('background-color', '#fff');
			localStorage.setItem('colorMode_switcher', 'light');
		} else if (switcher == 'light') {
			$('html').attr('data-bs-theme', 'dark');
			$('header').css('background-color', '#212529');
			localStorage.setItem('colorMode_switcher', 'dark');
		}
	});
}
