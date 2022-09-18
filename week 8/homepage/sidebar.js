document.addEventListener('DOMContentLoaded', function() {
    page_name = document.querySelector('div.header > h1').innerHTML.replace("Ari Gestetner<br>", "");
    document.querySelector('button.dropdown-toggle').innerHTML = page_name;
});