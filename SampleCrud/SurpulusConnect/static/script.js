
// ==========================================
// OPEN ADD DONATION MODAL
// ==========================================

function openModal() {

    const form = document.getElementById("donationForm");

    form.reset();

    form.action = "/add-donation";

    document.getElementById("modalTitle").textContent =
        "Add New Donation";

    document.getElementById("submitBtn").textContent =
        "Save Donation";

    document.getElementById("donationModal").classList.add("show");
}


// ==========================================
// CLOSE MODAL
// ==========================================

function closeModal() {

    document.getElementById("donationModal")
        .classList.remove("show");
}


// ==========================================
// EDIT DONATION
// ==========================================

function editDonation(button) {

    const row = button.closest("tr");

    const form = document.getElementById("donationForm");

    // Set update URL
    form.action = "/update-donation/" + row.dataset.id;

    // Fill existing values
    document.getElementById("foodName").value =
        row.dataset.foodName;

    document.getElementById("quantity").value =
        row.dataset.quantity;

    document.getElementById("unit").value =
        row.dataset.unit;

    document.getElementById("location").value =
        row.dataset.location;

    document.getElementById("expiryTime").value =
        row.dataset.expiry;

    document.getElementById("description").value =
        row.dataset.description;

    // Update modal heading and button
    document.getElementById("modalTitle").textContent =
        "Edit Donation";

    document.getElementById("submitBtn").textContent =
        "Update Donation";

    document.getElementById("donationModal").classList.add("show");
}


// ==========================================
// SEARCH DONATIONS
// ==========================================

function searchDonations() {

    const search = document.getElementById("searchInput")
        .value.toLowerCase();

    const rows = document.querySelectorAll(
        "#donationTable tr"
    );

    rows.forEach(row => {

        const rowText = row.innerText.toLowerCase();

        row.style.display = rowText.includes(search)
            ? ""
            : "none";
    });
}
