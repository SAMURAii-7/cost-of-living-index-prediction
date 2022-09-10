function onClickedEstimatePrice() {
    // console.log("Estimate price button clicked");
    var rent = document.getElementById("rentIndex");
    var groceries = document.getElementById("groceriesIndex");
    var restaurant = document.getElementById("restaurantIndex");
    var local_purchasing = document.getElementById("localIndex");
    var estPrice = document.getElementById("uiEstimatedPrice");

    var url = "http://127.0.0.1:5000/predict";

    const options = {
        method: "POST",
        headers: { "Content-Type": "application/x-www-form-urlencoded" },
        body: new URLSearchParams({
            rent_ind: rent.value,
            groceries_ind: groceries.value,
            rp_ind: restaurant.value,
            ppi_ind: local_purchasing.value,
        }),
    };

    fetch(url, options)
        .then((response) => response.json())
        .then(
            (response) =>
                (estPrice.innerHTML =
                    "<h2>" + response.estimated_coi.toString() + "</h2>")
        )
        .catch((err) => console.error(err));

    const form = document.getElementById("frm");
    form.reset();
}

function formReset() {
    const form = document.getElementById("frm");
    const estPrice = document.getElementById("uiEstimatedPrice");

    form.reset();
    estPrice.reset();
}

window.onload = formReset;
