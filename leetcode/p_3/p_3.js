let to_leng1 = function(x) {
    let p1 = 0
    let p2 = 1
    let list_of_true = []
    while(p1 < x.length){
        let = false
        if(p2 < x.length)
            temp = (x[p1]+1 == x[p2])
            if(temp){
                list_of_true.push(temp)
            }
        else if (p2 == len(x)){
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
    for(let i = 0; i < x.length; i++){
        for(let nums = 0; nums < i.length; nums++){
            all_nums.push(Number(nums));
        }
    return all_nums;
}
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

    let all_numbers = record.forEach(all_ints)
    return record;

}

let substring = "abcabcbb"
let substring1 = "pwwkew"
console.log(lengthOfLongestSubstring(substring))