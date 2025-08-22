// 250822
// 24044 KB / 244 ms
function minDif() {
  const input = require("fs")
    .readFileSync("/dev/stdin")
    .toString()
    .trim()
    .split("\n");
  const [n, m] = input[0].split(" ");
  const numbers = input.slice(1, n + 1).map(Number);
  numbers.sort((a, b) => a - b);
  let answer = numbers.at(-1) - numbers[0];
  let [i, j] = [0, 0];

  while (i < n) {
    const dif = numbers[j] - numbers[i];
    if (dif >= m) {
      if (answer > dif) {
        answer = dif;
      }
      i += 1;
    } else if (j < n - 1) {
      j += 1;
    } else {
      i += 1;
    }
  }
  return answer;
}

console.log(minDif());

// 23816 KB / 240 ms
function minDif() {
  const input = require("fs")
    .readFileSync("/dev/stdin")
    .toString()
    .trim()
    .split("\n");
  const [n, m] = input[0].split(" ");
  const numbers = input.slice(1, n + 1).map(Number);
  numbers.sort((a, b) => a - b);
  let answer = Number(2e9);
  let [i, j] = [0, 0];

  while (i < n) {
    const dif = numbers[j] - numbers[i];
    if (dif >= m) {
      if (answer > dif) {
        answer = dif;
      }
      i += 1;
    } else if (j < n - 1) {
      j += 1;
    } else {
      i += 1;
    }
  }
  return answer;
}

console.log(minDif());
