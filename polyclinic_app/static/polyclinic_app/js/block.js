'use strict'

const div = document.querySelector('.polyclinics');

const myObs = new ResizeObserver(entries => {
    let polyclinicDiv;
    let divList = [];
    entries.forEach(e => {
        polyclinicDiv = e.target.childNodes;
        polyclinicDiv.forEach(function (e) {
            if (e.tagName === 'DIV') {
                divList.push(e.clientHeight);
            }            
        })
        polyclinicDiv.forEach(function (e) {
            if (e.tagName === 'DIV') {
                e.style.minHeight = `${Math.max.apply(null, divList)}px`;
            }
        })
    })
})

myObs.observe(div);