/**
 * @param {number[]} piles
 * @return {number}
 */
var maxCoins = function(piles) {
    let res = 0;
    piles.sort((a,b)=>(a-b));
     for(let i=Math.floor(piles.length/3);i<piles.length;i+=2){
        res+=piles[i];
    }
    return res;
};