const numbers = [10, 5, 8, 20, 15]

let largest = -Infinity
let secondLargest = -Infinity

for (const number of numbers) {
	if (number > largest) {
		secondLargest = largest
		largest = number
	} else if (number > secondLargest && number < largest) {
		secondLargest = number
	}
}

// console.log(secondLargest)

// const numbers = [10, 5, 8, 20, 15]

// const hasDuplicates = new Set(numbers).size !== numbers.length

// console.log(hasDuplicates)