function inRange(num, ref) {
  return num >= 0 && num < ref;
}

function shortestTime(n, m, mapInfo) {
  let q = [];
  let [idx, maxDistance] = [0, 0];
  const direct = [
    [-1, 0],
    [0, -1],
    [1, 0],
    [0, 1],
  ];

  mapInfo.forEach((row, i) => {
    row.split("").forEach((position, j) => {
      if (position === "L") {
        const visited = Array.from({ length: n }, () => Array(m));
        q.push([i, j, 0]);
        visited[i][j] = true;

        while (q.length > idx) {
          const [y, x, distance] = q[idx];
          if (distance > maxDistance) {
            maxDistance = distance;
          }
          idx += 1;
          const newDistance = distance + 1;

          direct.forEach(([dy, dx]) => {
            const [ny, nx] = [y + dy, x + dx];
            if (inRange(ny, n) && inRange(nx, m)) {
              if (mapInfo[ny][nx] === "L" && !visited[ny][nx]) {
                visited[ny][nx] = true;
                q.push([ny, nx, newDistance]);
              }
            }
          });
        }
        q = [];
        idx = 0;
      }
    });
  });

  return maxDistance;
}

const input = require("fs").readFileSync("/dev/stdin").toString().split("\n");
const [n, m] = input[0].split(" ").map(Number);

console.log(shortestTime(n, m, input.slice(1, n + 1)));
