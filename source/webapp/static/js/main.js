async function listQuote(event) {
    event.preventDefault();
    let response = await makeRequest(BASE_API_URL + 'quote/', 'GET');
    let data = await response.json();
    console.log(data);
    const container = document.getElementById('container')
    container.innerHTML = ''
    for (let i = 0; i < data.length; i++) {
        let div = document.createElement('div')
        div.classList.add('my-4', 'quote', 'p-3')
        container.append(div)
        div.innerHTML = `<h3 class="author">${data[i].author}</h3><p class="text">"${data[i].text}"</p><h6 class="rating">Рейтиг: ${data[i].rating}</h6><br/>
 <a href="${BASE_API_URL}quote/${data[i].id}" class="exact">Подробнее...</a>`
    }
    let exact = document.getElementsByClassName('exact')
    for (let i = 0; i < exact.length; i++) {
        exact[i].onclick = async function showQuote(event) {
            event.preventDefault();
            let response = await makeRequest(exact[i].href, 'GET')
            data = await response.json()
            console.log(data)
            const container = document.getElementById('container')
            container.innerHTML = ''
            let div = document.createElement('div')
            div.classList.add('my-4', 'quote', 'p-3')
            container.append(div)
            div.innerHTML = `<h3 class="author">${data.author}</h3><p class="email">${data.email} | ${data.status_display}</p><p class="text">"${data.text}"</p>
<h6 class="rating">Рейтиг: ${data.rating}</h6><br/><p class="date">${data.created_at}</p>`
        };
    }
}

async function createQuote(event) {
    event.preventDefault();
    let response = await makeRequest(BASE_API_URL + 'quote/', 'POST',  {
        'text': document.getElementById('text').value,
        'email': document.getElementById('email').value,
        'author': document.getElementById('author').value
    });
    let context = await response.json();
    console.log(context);
    const container = document.getElementById('container')
            container.innerHTML = ''
            let div = document.createElement('div')
            div.classList.add('my-4', 'quote', 'p-3')
            container.append(div)
            div.innerHTML = `<h3 class="author">${context.author}</h3><p class="email">${context.email} | ${context.status_display}</p><p class="text">"${context.text}"</p>
<h6 class="rating">Рейтиг: ${context.rating}</h6><br/><p class="date">${context.created_at}</p>`;

}

async function createForm(event) {
    event.preventDefault()
    const container = document.getElementById('container')
    container.innerHTML = ''
    let div = document.createElement('div')
    div.classList.add('my-4', 'p-3')
    container.append(div)
    div.innerHTML = '<form action="" method="post" id="main-form"><label for="text">Текст</label>' +
        '<br/><textarea rows="5" cols="45" id="text"></textarea><br/>' +
        '<label for="email">Email</label><br/><input type="text" id="email"><br/>' +
        '<label for="author">Автор</label><br/><input type="text" id="author"></form>'
    let submit = document.createElement('button')
    submit.innerText = 'Создать'
    submit.id = "submit"
    submit.classList.add('my-3', 'btn', 'btn-primary')
    div.append(submit)
    submit.onclick = createQuote;
}


window.addEventListener('load', function() {
    let list = document.getElementById('list');
    list.onclick = listQuote;
    let form = document.getElementById('create')
    form.onclick = createForm;
});