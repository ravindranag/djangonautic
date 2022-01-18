const titleInput = document.querySelector('input[name=title]')
const slugInput = document.querySelector('input[name=slug]')

const slugify = value => {
    return value.toString().toLowerCase().trim()
        .replace(/&/g, '-and-')
        .replace(/[\s\W-]+/g, '-')
}

titleInput.addEventListener('keyup', e => {
    slugInput.value = slugify(titleInput.value)
})