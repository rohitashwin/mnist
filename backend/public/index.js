let drag = false; // set to true to enable dragging
const cellArray = Array(28)
  .fill(0)
  .map((_) => new Array(28).fill(0));

function main() {
  const root = document.getElementById("root");
  const grid = document.querySelector(".grid");
  for (let i = 0; i < 28; ++i) {
    for (let j = 0; j < 28; ++j) {
      const newElement = document.createElement("div");
      newElement.className = "cell";
      newElement.setAttribute("cellx", i);
      newElement.setAttribute("celly", j);
      grid.append(newElement);
    }
  }
}

function initCells() {
  const cells = document.getElementsByClassName("cell");
  for (let i = 0; i < cells.length; i++) {
    const cell = cells[i];
    cell.setAttribute("class", "cell");
    cell.addEventListener("mousedown", cellMouseDown);
    cell.addEventListener("mousemove", cellMouseMove);
    window.addEventListener("mouseup", cellMouseUp);
  }
}

function initButtons() {
  const clearButton = document.querySelector(".clear-button");
  console.log(clearButton);
  const recognizeButton = document.querySelector(".recognize-button");
  clearButton.addEventListener("click", clear);
  recognizeButton.addEventListener("click", recogonize);
}

function clear() {
  const cells = document.getElementsByClassName("cell");
  // set all the cell to inactive and set the cellArray to 0
  for (let i = 0; i < cells.length; i++) {
    const cell = cells[i];
    cell.setAttribute("class", "cell");
  }
  for (let i = 0; i < 28; ++i) {
    for (let j = 0; j < 28; ++j) {
      cellArray[i][j] = 0;
    }
  }
}

function draw(location, target) {
  const { cellX, cellY } = location;
  target.setAttribute("class", "cell active");
  // set the surrounding cells 8 cells to active in a loop
  for (let i = -1; i <= 1; ++i) {
    for (let j = -1; j <= 1; ++j) {
      const x = cellX + i;
      const y = cellY + j;
      if (x >= 0 && x < 28 && y >= 0 && y < 28) {
        const cell = document.querySelector(`[cellx="${x}"][celly="${y}"]`);
        cell.setAttribute("class", "cell active");
        // set to some random value between 0.5 and 1
        cellArray[x][y] = Math.random() * 0.5 + 0.5;
      }
    }
  }
}

function getLocation(cell) {
  const location = {
    cellX: 0,
    cellY: 0,
  };
  location.cellX = Number(cell.getAttribute("cellx"));
  location.cellY = Number(cell.getAttribute("celly"));
  return location;
}

function cellMouseDown(event) {
  const cell = event.target;
  const location = getLocation(cell);
  // if the location is already active, then enable delete mode
  console.log(cellArray[location.cellX][location.cellY]);
  draw(location, cell);
  drag = true;
}

function cellMouseMove(event) {
  if (drag) {
    const cell = event.target;
    const location = getLocation(cell);
    draw(location, cell);
  }
}

function cellMouseUp(event) {
  drag = false;
}

function recogonize(event) {
  // send the cellArray to the backend
  // disable the button to prevent multiple requests
  const button = event.target;
  button.disabled = true;
  const data = {
    image: cellArray,
  };
  const options = {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  };
  console.log("sending data");
  fetch("/predict", options)
    .then((response) => response.json())
    .then((data) => {
      console.log(data);
      const result = document.querySelector(".result");
      result.innerHTML = `Result: ${data}`;
      button.disabled = false;
    }).catch((error) => {
		const result = document.querySelector(".result");
		result.innerHTML = `There was a problem connecting to the server, please try again later`;
	  button.disabled = true;
	});		
}

main();
initCells();
initButtons();
