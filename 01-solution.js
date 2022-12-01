const { readFile } = require('fs/promises')

async function solve () {

  const file = await readFile('./01-input.txt')
  const elves = file
    .toString()
    .trim()
    .split('\n\n')
    .map(elf => elf.split('\n'))
    .map(elf => arraySum(elf))
    .sort()

  console.log(elves.at(-1))
  console.log(arraySum(elves.slice(-3)))

}

const arraySum = arr => arr.reduce((s, x) => s + Number(x), 0)

solve()
