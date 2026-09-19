export {};

const currentScript = document.currentScript;
const scriptUrl =
    currentScript instanceof HTMLScriptElement
        ? currentScript.src
        : document.baseURI;
const buttonSfx = new Audio(
    new URL("./assets/clickbtn.wav", scriptUrl).toString(),
);

buttonSfx.addEventListener(
    "error",
    () => {
        buttonSfx.src = new URL("./clickbtn.wav", scriptUrl).toString();
    },
    {once: true},
);

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
