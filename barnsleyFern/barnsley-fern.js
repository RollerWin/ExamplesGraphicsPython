const canvas = document.getElementById('barnsleyFern');
const ctx = canvas.getContext('2d');
const iterations = 100000; // Количество итераций

function clearCanvas() {
    ctx.fillStyle = 'black'; // Задний фон в черный цвет
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    ctx.fillStyle = 'green'; // Цвет точек - зеленый
}

function drawBarnsleyFern() {
    clearCanvas();
    let x = 0;
    let y = 0;

    for (let i = 0; i < iterations; i++) {
        const random = Math.random();
        let nextX, nextY;

            if (random < 0.01) {
                nextX = 0;
                nextY = 0.16 * y;
            } else if (random < 0.86) {
                nextX = 0.85 * x + 0.04 * y;
                nextY = -0.04 * x + 0.85 * y + 1.6;
            } else if (random < 0.93) {
                nextX = 0.2 * x - 0.26 * y;
                nextY = 0.23 * x + 0.22 * y + 1.6;
            } else {
                nextX = -0.15 * x + 0.28 * y;
                nextY = 0.26 * x + 0.24 * y + 0.44;
            }

        x = nextX;
        y = nextY;

        //---Пересчитываем координаты для отрисовки---//
        const screenX = canvas.width / 2 + x * 50 - 50;
        const screenY = canvas.height - y * 50 - 300;
        //--------------------------------------------//
        //---Рисуем точку-----------------------------//
        ctx.fillRect(screenX, screenY, 1, 1);
    }
}

drawBarnsleyFern();
