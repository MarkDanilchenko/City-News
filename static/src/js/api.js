// docker _HostPort
const server_HostPort = '0.0.0.0:8900';
// localhost _HostPort
// const server_HostPort = '127.0.0.1:8000';

// button for window reload
if (document.getElementById('resetPage')) {
  document.getElementById('resetPage').addEventListener('click', () => {
    window.location.reload();
  });
}

// // task 1 url (Fortune Cookies)
// // task 1 url (Fortune Cookies)
// // task 1 url (Fortune Cookies)
const url = `http://${server_HostPort}/api/fortune_cookies/random`;
// // button
const getFortuneCookies = document.getElementById('getFortuneCookies');
// // render block
const fortuneCookiesResult = document.getElementById('fortuneCookiesResult');
if (getFortuneCookies) {
  getFortuneCookies.addEventListener('click', () => {
    getFortuneCookies.disabled = true;
    $(fortuneCookiesResult).css({
      'animation-name': 'FortuneCookies',
      'animation-duration': '3s',
      'animation-timing-function': 'linear',
      'animation-iteration-count': '1',
    });
    fetch(url, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
      },
      mode: 'cors',
    })
      .then((response) => response.json())
      .then((data) => {
        fortuneCookiesResult.innerHTML = `<span>${data.result}</span>`;
      })
      .catch((error) => {
        console.log(error);
      });
    // FortuneCookies cooldown for 3 seconds
    setTimeout(() => {
      getFortuneCookies.disabled = false;
      $(fortuneCookiesResult).css({
        'animation-name': 'none',
      });
    }, 3000);
  });
}

// // task 2 url (Random Numbers)
// // task 2 url (Random Numbers)
// // task 2 url (Random Numbers)
// 2.1
const url2_1 = `http://${server_HostPort}/api/random_numbers/randomInt/`;

// // button
const getRandomInt = document.getElementById('randomInt');
// // render block
const randomIntResult = document.getElementById('randomIntResult');
if (getRandomInt) {
  getRandomInt.addEventListener('click', () => {
    fetch(url2_1, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
      },
      mode: 'cors',
    })
      .then((response) => response.json())
      .then((data) => {
        randomIntResult.innerHTML = `<span>${data.result}</span>`;
      })
      .then(() => {
        $('#randomIntResult span').fadeOut(3000);
      })
      .catch((error) => {
        console.log(error);
      });
  });
}

// 2.2
const url2_2 = `http://${server_HostPort}/api/random_numbers/randomIntInRange/`;
// // form POST
const randomIntInRange = document.getElementById('randomIntInRange');
// // render block
const randomIntInRangeResult = document.getElementById('randomIntInRangeResult');
if (randomIntInRange) {
  randomIntInRange.addEventListener('submit', (event) => {
    event.preventDefault();
    const formData = new FormData(event.target);
    fetch(url2_2, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': document.getElementsByName('csrfmiddlewaretoken')[0].value,
      },
      body: JSON.stringify(Object.fromEntries(formData)),
      mode: 'cors',
    })
      .then((response) => response.json())
      .then((data) => {
        randomIntInRangeResult.innerHTML = `<span>${data.result}</span>`;
      })
      .then(() => {
        $('#randomIntInRangeResult span').fadeOut(3000);
      })
      .catch((error) => {
        console.log(error);
      });
  });
}

// 2.3
const url2_3 = `http://${server_HostPort}/api/random_numbers/randomList/`;
// // button
const getRandomList = document.getElementById('randomList');
// // render block
const randomListResult = document.getElementById('randomListResult');
if (getRandomList) {
  getRandomList.addEventListener('click', () => {
    fetch(url2_3, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
      },
      mode: 'cors',
    })
      .then((response) => response.json())
      .then((data) => {
        randomListResult.innerHTML = `<span>${data.result}</span>`;
      })
      .then(() => {
        $('#randomListResult span').fadeOut(3000);
      })
      .catch((error) => {
        console.log(error);
      });
  });
}

// // task 3 url (Poems)
// // task 3 url (Poems)
// // task 3 url (Poems)
// 3.1
const url3_1 = `http://${server_HostPort}/api/poems/randomPoem/`;
// // button
const getRandomPoem = document.getElementById('randomPoem');
// // render block
const randomPoemResult = document.getElementById('randomPoemResult');
if (getRandomPoem) {
  getRandomPoem.addEventListener('click', () => {
    getRandomPoem.disabled = true;
    fetch(url3_1, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
      },
      mode: 'cors',
    })
      .then((response) => response.json())
      .then((data) => {
        randomPoemResult.innerHTML = `
        <div id="list" class="">
          <p class="text-center mb-3">${data.result.title}</p>
          <p class="px-3">${data.result.text}</p>
          <p class="text-end">"<i>${data.result.author}</i>"</p>
        </div>
        `;
      })
      .catch((error) => {
        console.log(error);
      });
    // randomPoem cooldown for 1 second
    setTimeout(() => {
      getRandomPoem.disabled = false;
    }, 1000);
  });
}

// 3.2
const url3_2 = `http://${server_HostPort}/api/poems/randomPoemByTheme/`;
// // form POST
const randomPoemByTheme = document.getElementById('randomPoemByTheme');
// // render block
const randomPoemByThemeResult = document.getElementById('randomPoemByThemeResult');
if (randomPoemByTheme) {
  randomPoemByTheme.addEventListener('submit', (event) => {
    event.preventDefault();
    const formData = new FormData(event.target);
    fetch(url3_2, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': document.getElementsByName('csrfmiddlewaretoken')[0].value,
      },
      mode: 'cors',
      body: JSON.stringify(Object.fromEntries(formData)),
    })
      .then((response) => response.json())
      .then((data) => {
        randomPoemByThemeResult.innerHTML = `
        <div id="list" class="">
          <p class="text-center mb-3">${data.result.title}</p>
          <p class="px-3">${data.result.text}</p>
          <p class="text-end">"<i>${data.result.author}</i>"</p>
        </div>
      `;
      })
      .catch((error) => {
        console.log(error);
      });
  });
}

// 3.3
const url3_3 = `http://${server_HostPort}/api/poems/randomPoemByAuthor/`;
// // form POST
const randomPoemByAuthor = document.getElementById('randomPoemByAuthor');
// // render block
const randomPoemByAuthorResult = document.getElementById('randomPoemByAuthorResult');
if (randomPoemByAuthor) {
  randomPoemByAuthor.addEventListener('submit', (event) => {
    event.preventDefault();
    const formData = new FormData(event.target);
    fetch(url3_3, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': document.getElementsByName('csrfmiddlewaretoken')[0].value,
      },
      mode: 'cors',
      body: JSON.stringify(Object.fromEntries(formData)),
    })
      .then((response) => response.json())
      .then((data) => {
        randomPoemByAuthorResult.innerHTML = `
        <div id="list" class="">
          <p class="text-center mb-3">${data.result.title}</p>
          <p class="px-3">${data.result.text}</p>
          <p class="text-end">"<i>${data.result.author}</i>"</p>
        </div>`;
      })
      .catch((error) => {
        console.log(error);
      });
  });
}

// 4.1
const url4_1 = `http://${server_HostPort}/api/poems/getAuthorsList/`;
// // button
const getAuthorsList = document.getElementById('getAuthorsList');
// // render block
const getAuthorsListResult = document.getElementById('getAuthorsListResult');
if (getAuthorsList) {
  getAuthorsList.addEventListener('click', () => {
    fetch(url4_1, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
      },
      mode: 'cors',
    })
      .then((response) => response.json())
      .then((data) => {
        getAuthorsListResult.innerHTML = `
        <div id="list" class="">
          <p class="text-center"><b>Full Authors' list</b></p>
          <ol>
          ${data.result.reduce((acc, elem) => `${acc}<li>${elem}</li>`, '')}
          </ol>
        </div>`;
      })
      .catch((error) => {
        console.log(error);
      });
  });
}

// 4.2
const url4_2 = `http://${server_HostPort}/api/poems/getThemesList/`;
// // button
const getThemesList = document.getElementById('getThemesList');
// // render block
const getThemesListResult = document.getElementById('getThemesListResult');
if (getThemesList) {
  getThemesList.addEventListener('click', () => {
    fetch(url4_2, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
      },
      mode: 'cors',
    })
      .then((response) => response.json())
      .then((data) => {
        getThemesListResult.innerHTML = `
        <div id="list" class="">
          <p class="text-center"><b>Full Themes' list</b></p>
          <ol>
          ${data.result.reduce((acc, elem) => `${acc}<li>${elem}</li>`, '')}
          </ol>
        </div>`;
      })
      .catch((error) => {
        console.log(error);
      });
  });
}

// 4.3
const url4_3 = `http://${server_HostPort}/api/poems/getPoemsListByAuthor/`;
// // form POST
const getPoemsListByAuthor = document.getElementById('getPoemsListByAuthor');
// // render block
const getPoemsListByAuthorResult = document.getElementById('getPoemsListByAuthorResult');
if (getPoemsListByAuthor) {
  getPoemsListByAuthor.addEventListener('submit', (event) => {
    event.preventDefault();
    const formData = new FormData(event.target);
    fetch(url4_3, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': document.getElementsByName('csrfmiddlewaretoken')[0].value,
      },
      mode: 'cors',
      body: JSON.stringify(Object.fromEntries(formData)),
    })
      .then((response) => response.json())
      .then((data) => {
        getPoemsListByAuthorResult.innerHTML = `
        <div id="list" class="">
        <p class="text-center"><b>${data.author}'s <br><span class="text-small">poems list</span></br></p>
        <ol>
        ${data.result.reduce((acc, elem) => `${acc}<li>${elem}</li>`, '')}
        </ol>
        </div>`;
      })
      .catch((error) => {
        console.log(error);
      });
  });
}

// 4.4
const url4_4 = `http://${server_HostPort}/api/poems/getPoemsListByTheme/`;
// // form POST
const getPoemsListByTheme = document.getElementById('getPoemsListByTheme');
// // render block
const getPoemsListByThemeResult = document.getElementById('getPoemsListByThemeResult');
if (getPoemsListByTheme) {
  getPoemsListByTheme.addEventListener('submit', (event) => {
    event.preventDefault();
    const formData = new FormData(event.target);
    fetch(url4_4, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': document.getElementsByName('csrfmiddlewaretoken')[0].value,
      },
      mode: 'cors',
      body: JSON.stringify(Object.fromEntries(formData)),
    })
      .then((response) => response.json())
      .then((data) => {
        getPoemsListByThemeResult.innerHTML = `
        <div id="list" class="">
        <p class="text-center"><b>${data.theme}</b></p>
        <ol>
        ${data.result.reduce((acc, elem) => `${acc}<li>${elem}</li>`, '')}
        </ol>
        </div>`;
      })
      .catch((error) => {
        console.log(error);
      });
  });
}
