const buttonSfx = new Audio("./clickbtn.wav");

document.addEventListener("click", (event: MouseEvent) => {
    const target = event.target;

    if (!(target instanceof Element)) {
        return;
    }

    const button = target.closest("button");

    if (button) {
        buttonSfx.currentTime = 0;
        buttonSfx.play().catch(console.error);
    }
});