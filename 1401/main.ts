function checkOverlap(
  radius: number,
  xCenter: number,
  yCenter: number,
  x1: number,
  y1: number,
  x2: number,
  y2: number
): boolean {
  // x is smallest of xCenter and x2, and largest of x1 and result of that
  // this means we are getting the point in the rect that is closest to the center of the circle
  // ditto for y
  let nearestX = Math.max(x1, Math.min(xCenter, x2));
  let nearestY = Math.max(y1, Math.min(yCenter, y2));
  let distX = nearestX - xCenter;
  let distY = nearestY - yCenter;
  console.log(nearestX, nearestY, distX, distY);
  return Math.pow(distX, 2) + Math.pow(distY, 2) <= Math.pow(radius, 2);
}

// find closest point in rect and see if it's in the circle

console.log(checkOverlap(1, 0, 3, 7, 3, 10, 6));
