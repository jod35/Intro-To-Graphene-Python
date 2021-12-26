from collections import namedtuple

Person=namedtuple("Person",['email','first_name','last_name','age'])

data={
    1:Person("johndoe@gmail.com","John","Doe",23),
    2:Person("jerryblue@gmail.com","Jerry","Blue",24),
    3:Person("jasonross@gmail.com","Jason","Ross",25),
    4:Person("brucewayne@gmail.com","Bruce","Wayne",28),
}