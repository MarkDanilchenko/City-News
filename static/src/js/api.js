// docker _HostPort
// const server_HostPort = '0.0.0.0:8900';
// localhost _HostPort
const server_HostPort = '127.0.0.1:8000';

const URL_showAllComments = `http://${server_HostPort}/API/comments/showAllComments/`;

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
                                <hr class="offset-3 col-6">
                                <h5 class="logoString_h3">Comments</h5>
                                <p class="text-center text-muted"><i>No comments yet!</i></p>
                            `;
				} else {
					showAllComments_block.innerHTML = `
                                <hr class="offset-3 col-6">
                                <h5 class="logoString_h3">Comments</h5>
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
