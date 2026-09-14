const scriptUrl = document.currentScript?.src || document.baseURI;
const buttonSfx = new Audio(new URL("./assets/clickbtn.wav", scriptUrl));

buttonSfx.addEventListener(
  "error",
  () => {
    buttonSfx.src = new URL("./clickbtn.wav", scriptUrl);
  },
  { once: true },
);

document.addEventListener("click", (event) => {
  const button = event.target.closest("button");

  if (button) {
    buttonSfx.currentTime = 0;
    buttonSfx.play().catch(console.error);
  }
});
