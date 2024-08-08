$.get("https://swapi-api.alx-tools.com/api/films/?format=json", function() {
    $("DIV#list_movies").append("<ul></ul>")
});
