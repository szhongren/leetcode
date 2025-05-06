function minPartitions(n: string): number {
  return Math.max(...n.split("").map((x) => parseInt(x)));
}
