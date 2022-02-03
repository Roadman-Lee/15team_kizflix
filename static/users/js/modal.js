const modal = document.getElementById("modal_change_porfile");

const buttonAddFeed = document.getElementById("change_profile");
buttonAddFeed.addEventListener("click", e => {
    modal.style.display = "flex";
    document.body.style.overflowY = "hidden";
});

modal.addEventListener("click", e => {
    const evTarget = e.target
    if (evTarget.classList.contains("modal_overlay")) {
        modal.style.display = "none"
    }
})

window.addEventListener("keyup", e => {
    if (modal.style.display === "flex" && e.key === "Escape") {
        modal.style.display = "none"
    }
})