let contador = 0;
let tiempo = 10;
let intervalo = null;
let jugando = false;

const botonClick = document.getElementById("botonClick");
const botonEmpezar = document.getElementById("botonEmpezar");
const botonReiniciar = document.getElementById("botonReiniciar");

const contadorSpan = document.getElementById("contador");
const tiempoSpan = document.getElementById("tiempo");
const mensaje = document.getElementById("mensaje");

function empezarJuego() {
  if (intervalo !== null) return;
  jugando = true;
  mensaje.textContent = "";
  intervalo = setInterval(() => {
    tiempo--;
    tiempoSpan.textContent = tiempo;
    if (tiempo <= 0) {
      clearInterval(intervalo);
      intervalo = null;
      jugando = false;
      mensaje.textContent = "Fin del juego. Puntaje final: " + contador;
    }
  }, 1000);
}

function reiniciarJuego() {
  clearInterval(intervalo);
  intervalo = null;
  contador = 0;
  tiempo = 10;
  jugando = false;
  contadorSpan.textContent = contador;
  tiempoSpan.textContent = tiempo;
  mensaje.textContent = "";
}

botonClick.addEventListener("click", () => {
  if (jugando === true) {
    contador++;
    contadorSpan.textContent = contador;
  }});
botonEmpezar.addEventListener("click", empezarJuego);
botonReiniciar.addEventListener("click", reiniciarJuego);