document.addEventListener("DOMContentLoaded", () => {

    const search = document.querySelector("#search");
    const status = document.querySelector(".toolbar__filter");
    const priority = document.querySelector(".toolbar__priority");
    const titleInput = document.querySelector("#form__title");

    if (search) {
        search.focus();
        const len = search.value.length;
        search.setSelectionRange(len, len);
    }

    if (titleInput) {
         titleInput.focus();
    }

     async function filter() {

        const response = await fetch("/search/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                search: search.value,
                status: status.value,
                priority: priority.value
            })
        });

        const data = await response.json();
        window.location.href = data.redirect;
    }

    search.addEventListener("input", filter);
    status.addEventListener("change", filter);
    priority.addEventListener("change", filter);
});