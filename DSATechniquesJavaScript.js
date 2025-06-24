// Input: arr = [2, 7, 11, 15], target = 9  
// Output: [0, 1]  // because arr[0] + arr[1] = 2 + 7 = 9


// let arr = [1, 7, 2, 15]
// let target = 9
// for(let i = 0; i < arr.length; i++){
//     // console.log(`${i} value of i`)
//     for(let j = i+1; j < arr.length; j++){
//         // console.log(`${arr[j]} value of j`)
//         if (arr[i] + arr[j] == target) {
//             console.log(`${arr[i]} and ${arr[j]} is matach`)
//         }
        
//     }
    
// }


// # Find the longest palindromic substring in a given string using brute force.


function palindrome(plain){
    
    return plain == plain.split('').reverse().join('');

}

function longestPalindrome(s) {
    let max_len = 0;
    let longest = "";

    for(let i = 0; i < s.length; i++) {
        for(let j = i; j < s.length; j++) {
            let substring = s.substring(i, j + 1);
            if(palindrome(substring) && substring.length > max_len) {
                max_len = substring.length;
                longest = substring;
            }
        }
    }
    return longest;
}

console.log(longestPalindrome("babad")); // Output: "bab" or "aba"
console.log(longestPalindrome("cbbd"));  // Output: "bb"