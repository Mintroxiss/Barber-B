console.log('men js here')

let men = () => {
    url = '/men_api/'
    fetch(url)
    .then(resp => resp.json())
    .then(data => {
        console.log('DATA: ', data)

        for(service of data) {
            let card = 
            `<div class="card">
                <img src="${service.image}" alt="men_haircut">
                <div class="flex jc-sb">
                    <p>${service.service_type}</p>
                    <h3>${service.price}р</h3>
                </div>
            </div>`

            document.querySelector('#men_services').innerHTML += card
        }
    })
}


men()



