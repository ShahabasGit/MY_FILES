let dropdown_click = document.querySelector('.dropdown-c')
let drodown = document.querySelector('.dropdown')
let body = document.querySelector('.c-back')

dropdown_click.addEventListener('click', function(){
    drodown.style.height = '80px'
    drodown.style.padding = '10px'
})

body.addEventListener('click', function(){
    drodown.style.height = '0'
    drodown.style.padding = '0'
})



