let addTwoNumbers = (l1, l2) => {
    let = joined_l1 = ''
    let = joined_l2 = ''
    for(i = 0; i < l1.length;i++){
        joined_l1 += l1[i].toString()
        joined_l2 += l2[i].toString()
    }
    temp = (Number(joined_l1)+Number(joined_l2)).toString()
    console.log(temp);
    let final_thing =[]
    for(let y = 0; y < l1.length; y++){
        final_thing.push(Number(temp[y]))
        
    }
    return final_thing.reverse();
}

let l1 = [2,4,3];
let l2 = [5,6,4];
console.log(addTwoNumbers(l1,l2));