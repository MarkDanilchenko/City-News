// docker _HostPort or localhost _HostPort
const server_HostPort = process.env.server_HostPort || '127.0.0.1:8000';
// URLS
// URLS
// URLS
const URL_showAllComments = `http://${server_HostPort}/API/comments/showAllComments/`;
const URL_addComment = `http://${server_HostPort}/API/comments/addComment/`;

// showAllComments
// showAllComments
// showAllComments
const showAllComments_form = document.getElementById('showAllComments');
const showAllComments_block = document.getElementById('blockComments');
if (showAllComments_form) {
	showAllComments_form.addEventListener('click', (e) => {
		e.preventDefault();
		const formData = new FormData(showAllComments_form);
		fetch(URL_showAllComments, {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json',
				'X-CSRFToken': document.getElementsByName('csrfmiddlewaretoken')[0].value,
			},
			mode: 'cors',
			body: JSON.stringify(Object.fromEntries(formData)),
		})
			.then((response) => {
				return response.json();
			})
			.then((data) => {
				if (data.length == 0) {
					showAllComments_block.innerHTML = `
                                <p class="text-center text-muted"><i>No comments yet!</i></p>
                            `;
				} else {
					showAllComments_block.innerHTML = `
                                ${data.reduce(
									(acc, comment) => `
                                    ${acc}<div class="card mb-3">
                                                <div class="card-header d-flex justify-content-between text-small text-muted">
                                                    <span>User: <i>${comment.author}</i></span>
                                                    <span>Date: <i>${comment.publish_date}</i></span>
                                                </div>
                                                <div class="card-body">
                                                    <p class="card-text">${comment.text}</p>
                                                </div>
                                            </div>
                                            `,
									''
								)}
                                            `;
				}
			})
			.catch((error) => {
				console.error('Error:', error);
			});
	});
}

// addComment
// addComment
// addComment
const addComment_form = document.getElementById('addComments');
if (addComment_form) {
	addComment_form.addEventListener('submit', (e) => {
		e.preventDefault();
		const formData = new FormData(addComment_form);
		if (formData.get('text') == '') {
			return;
		}
		fetch(URL_addComment, {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json',
				'X-CSRFToken': document.getElementsByName('csrfmiddlewaretoken')[0].value,
			},
			mode: 'cors',
			body: JSON.stringify(Object.fromEntries(formData)),
		})
			.then((response) => {
				return response.json();
			})
			.then((data) => {
				if (data.message) {
					$('#exampleModal').modal('show');
				} else {
					if (data.length == 0) {
						showAllComments_block.innerHTML = `
                                    <p class="text-center text-muted"><i>No comments yet!</i></p>
                                `;
					} else {
						showAllComments_block.innerHTML = `
                                    ${data.reduce(
										(acc, comment) => `
                                        ${acc}<div class="card mb-3">
                                                    <div class="card-header d-flex justify-content-between text-small text-muted">
                                                        <span>User: <i>${comment.author}</i></span>
                                                        <span>Date: <i>${comment.publish_date}</i></span>
                                                    </div>
                                                    <div class="card-body">
                                                        <p class="card-text">${comment.text}</p>
                                                    </div>
                                                </div>
                                                `,
										''
									)}
                                                `;
					}
					$('#floatingTextarea2').val('');
				}
			})
			.catch((error) => {
				console.error('Error:', error);
			});
	});
}
