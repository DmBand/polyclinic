'use strict'

const myObs = new ResizeObserver(entries => {
    let polyclinicDiv;
    let titlelist = [];
    let addressList = [];
    let numbersLisr = [];

    entries.forEach(e => {
        polyclinicDiv = e.target.childNodes;
        polyclinicDiv.forEach(function (e) {
            if (e.tagName === 'DIV')  {
                for (let el of e.childNodes) {
                    switch (el.className) {
                        case 'p-title':
                            titlelist.push(el.clientHeight);
                            break;
                        case 'p-address':
                            addressList.push(el.clientHeight);
                            break;
                        case 'numbers':
                            numbersLisr.push(el.clientHeight);
                            break;
                    }
                }
            }
        })
        polyclinicDiv.forEach(function (e) {
            if (e.tagName === 'DIV')  {
                for (let el of e.childNodes) {
                    switch (el.className) {
                        case 'p-title':
                            el.style.minHeight = `${Math.max.apply(null, titlelist)}px`;
                            break;
                        case 'p-address':
                            el.style.minHeight = `${Math.max.apply(null, addressList)}px`;                            
                            break;
                        case 'numbers':
                            el.style.minHeight = `${Math.max.apply(null, numbersLisr)}px`;                            
                            break;
                    }
                }
            }
        })
    })
})

function changeHeight() {
    const div = document.querySelector('.polyclinics');
    myObs.observe(div);  
}

document.addEventListener('DOMContentLoaded', changeHeight);
