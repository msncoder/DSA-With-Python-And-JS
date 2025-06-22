// Input: arr = [2, 7, 11, 15], target = 9  
// Output: [0, 1]  // because arr[0] + arr[1] = 2 + 7 = 9


let arr = [1, 7, 2, 15]
let target = 9
for(let i = 0; i < arr.length; i++){
    // console.log(`${i} value of i`)
    for(let j = i+1; j < arr.length; j++){
        // console.log(`${arr[j]} value of j`)
        if (arr[i] + arr[j] == target) {
            console.log(`${arr[i]} and ${arr[j]} is matach`)
        }
        
    }
    
}


