// Show passwords when the page loads
showPasswords();

// Copy text to clipboard
function copyText(text) {
    navigator.clipboard.writeText(text)
        .then(() => {
            const alertBox = document.getElementById("alert");
            if (alertBox) {
                alertBox.style.display = "inline";
                setTimeout(() => {
                    alertBox.style.display = "none";
                }, 2000);
            } else {
                alert("Copied: " + text);
            }
        })
        .catch(() => {
            alert("Clipboard copying failed");
        });
}

// Display passwords
function showPasswords() {
    let passwords = JSON.parse(localStorage.getItem("passwords")) || [];

    let table = document.querySelector("table");

    table.innerHTML = `
        <tr>
            <th>Website</th>
            <th>Username</th>
            <th>Password</th>
            <th>Delete</th>
        </tr>
    `;

   passwords.forEach((element, index) => {
    table.innerHTML += `
        <tr>
            <td>
                ${element.website}
                <img
                    src="https://www.svgrepo.com/show/511165/copy.svg"
                    alt="Copy"
                    width="20"
                    style="cursor:pointer; vertical-align:middle; margin-left:8px;"
                    onclick="copyText('${element.website}')">
            </td>

            <td>
                ${element.username}
                <img
                    src="https://www.svgrepo.com/show/511165/copy.svg"
                    alt="Copy"
                    width="20"
                    style="cursor:pointer; vertical-align:middle; margin-left:8px;"
                    onclick="copyText('${element.username}')">
            </td>

            <td>
                ${element.password}
                <img
                    src="https://www.svgrepo.com/show/511165/copy.svg"
                    alt="Copy"
                    width="20"
                    style="cursor:pointer; vertical-align:middle; margin-left:8px;"
                    onclick="copyText('${element.password}')">
            </td>

            <td>
                <button onclick="deletePassword(${index})">
                    Delete
                </button>
            </td>
        </tr>
    `;
});
}

// Save password
document.getElementById("passwordForm").addEventListener("submit", function (e) {
    e.preventDefault();

    const website = document.getElementById("website").value;
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    let passwords = JSON.parse(localStorage.getItem("passwords")) || [];

    passwords.push({
        website,
        username,
        password
    });

    localStorage.setItem("passwords", JSON.stringify(passwords));

    alert("Password Saved Successfully!");

    document.getElementById("passwordForm").reset();

    showPasswords();
});

// Delete password
function deletePassword(index) {
    let passwords = JSON.parse(localStorage.getItem("passwords")) || [];

    passwords.splice(index, 1);

    localStorage.setItem("passwords", JSON.stringify(passwords));

    showPasswords();
}