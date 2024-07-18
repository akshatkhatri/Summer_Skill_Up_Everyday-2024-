synonyms = ["Array","Collection of items","Grouped elements"];
console.log(synonyms[1]);
console.log(synonyms.indexOf("Array"));
console.log();
synonyms[1] = "collection"

let last_ele = synonyms.pop()
console.log(synonyms);
synonyms.push(last_ele)
console.log(synonyms);

let sorted_arr = ["c","b","a","d","f","e"].sort()
console.log(sorted_arr);

let joined_arr = ["Bear","Cow","things"].join(" & ")
console.log(joined_arr);

let concat_arr = [1,2,3].concat([4,5,6])
console.log(concat_arr);