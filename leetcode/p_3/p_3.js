let to_leng1 = function(x) {
    let p1 = 0
    let p2 = 1
    let list_of_true = []
    while(p1 < x.length){
        let temp = false
        if(p2 < x.length)
            temp = (x[p1]+1 == x[p2])
            if(temp){
                list_of_true.push(temp)
            }
        else if (p2 == x.length){
            temp = (x[p1-1]+1 == x[p1])
            if(temp){
                list_of_true.push(temp)
            }
        }
        p1+=1
        p2+=1
    }
    return list_of_true
}

let all_ints = function(x){
    all_nums = [];
    
    for(let i = 0; i < x.length; i ++){
        for(let j = 0; j < x[i].length; j++){
            all_nums.push(Number(x[i][j]))
        }
    }
    return all_nums

}

let lengthOfLongestSubstring = (s) =>{
    let record = [];
    let recorded_substring = [];
    let seen = [];
    let return_sub = '';
    let pos_1 = 0;
    let all_indexs = '';
    while(pos_1 < s.length-1){
        if((s[pos_1] != s[pos_1+1]) && (seen.includes(s[pos_1]) === false )){
            return_sub +=  s[pos_1];
            all_indexs += pos_1.toString();
            seen.push(s[pos_1]);
            record.push([all_indexs]);
        }
            
        pos_1+=1;
    }

    return record

}

let all_together = (s) => {
    let iter = lengthOfLongestSubstring(s)
    let only_numbers = []
    for(let i = 0; i < iter.length; i ++){
        only_numbers.push(all_ints(iter[i]))
    }
    let truth = []
    for(let j = 0; j < only_numbers.length; j++){
        truth.push(to_leng1(only_numbers[j]).length)
    }

    return Math.max(...truth)
}

let substring = "abcabcbb"
let substring1 = "pwwkew"
console.log(all_together(substring))