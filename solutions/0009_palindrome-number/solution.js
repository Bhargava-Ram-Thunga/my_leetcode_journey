/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function (x) {
    let reverse = 0;
    var temp = x;
    while (temp > 0) {
        reverse = (reverse * 10) + (temp % 10);
        temp = Math.floor(temp / 10);
    }
    if (reverse == x) {
        return true;
    }
    return false;
};