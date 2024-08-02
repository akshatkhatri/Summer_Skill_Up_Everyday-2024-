let civilians = [
    {
        name: "Alice",
        age: 30,
        profession: "Engineer"
    },
    {
        name: "Bob",
        age: 25,
        profession: "Designer"
    },
    {
        name: "Charlie",
        age: 35,
        profession: "Teacher"
    },
    {
        name: "Diana",
        age: 28,
        profession: "Doctor"
    },
    {
        name: "Eve",
        age: 40,
        profession: "Architect"
    },
    {
        name: "Frank",
        age: 32,
        profession: "Chef"
    },
    {
        name: "Grace",
        age: 29,
        profession: "Lawyer"
    },
    {
        name: "Hank",
        age: 33,
        profession: "Artist"
    },
    {
        name: "Ivy",
        age: 27,
        profession: "Scientist"
    },
    {
        name: "Jack",
        age: 38,
        profession: "Writer"
    }
];

let elder_civi = civilians.filter((s)=> s.age >=30);

let elder_civilians = elder_civi.map((s) => {
    let newObj = {
        name: `${s.name} The Elder`,
        age: s.age,
        profession: s.profession
    };
    return newObj;
});

console.log(elder_civilians)