const newsArticlesTable = document.getElementById('newsArticlesTable');
if (newsArticlesTable) {
	const th = newsArticlesTable.querySelectorAll('th');
	let tbody = newsArticlesTable.querySelector('tbody');
	let rows = [...tbody.rows];

	th.forEach((element) => {
		element.addEventListener('click', () => {
			let columnIndex = element.cellIndex;
			if (columnIndex !== 0 && columnIndex !== 4) {
				let sortDirection = element.getAttribute('data-sort-direction') === 'asc' ? 'desc' : 'asc';
				element.setAttribute('data-sort-direction', sortDirection);
				rows.sort((a, b) => {
					let aText = a.cells[columnIndex].textContent;
					let bText = b.cells[columnIndex].textContent;
					if (sortDirection === 'asc') {
						return aText === bText ? 0 : aText > bText ? 1 : -1;
					} else {
						return aText === bText ? 0 : aText < bText ? 1 : -1;
					}
				});
				tbody.append(...rows);
			} else {
				return;
			}
		});
	});
}
