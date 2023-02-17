exports.factorial = function(x) {
  if (x <= 1) {
    return 1
  }
  return x * this.factorial(x-1);

};


exports.palindrome = function(string) {
  if (string.length <= 1) {
    return true
  }
  let new_word = string.toLowerCase().replace(/[^\w]*/g, '')
  if (new_word[0] != new_word[new_word.length - 1]) {
    return false
  }
  return this.palindrome(new_word.slice(1,new_word.length-1))

};

exports.bottles = function(num, original=null) {
  if (original === null) {
    original = num
  }
  if (num === 0){
    console.log(`No more bottles of beer on the wall, no more bottles of beer. Go to the store and buy some more, ${original} bottle${original>1 ? "s" : ""} of beer on the wall.`)
    return 1
  } else if (num ===1) {
    console.log(`1 bottle of beer on the wall, 1 bottle of beer. Take one down and pass it around, no more bottles of beer on the wall.`)
  } else {
    console.log(`${num} bottles of beer on the wall, ${num} bottles of beer. Take one down and pass it around, ${num -1} bottle${num-1>1 ? "s" : ""} of beer on the wall.`)
  }
  return this.bottles(num -1, original)
};

exports.romanNum = function(num) {
  const romanNumeralsMap = [
    [1000, "M"],
    [900, "CM"],
    [500, "D"],
    [400, "CD"],
    [100, "C"],
    [90, "XC"],
    [50, "L"],
    [40, "XL"],
    [10, "X"],
    [9, "IX"],
    [5, "V"],
    [4, "IV"],
    [1, "I"]
  ];

  for (let i=0; i<romanNumeralsMap.length; i++) {
    if (num === romanNumeralsMap[i][0]) {
      return romanNumeralsMap[i][1]
    } else if (num > romanNumeralsMap[i][0]) {
      return romanNumeralsMap[i][1] + this.romanNum(num - romanNumeralsMap[i][0])
    }
  }
};
