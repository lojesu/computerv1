use std::env;

mod parsing;
use parsing::parsing;

fn main() {
    let args: Vec<String> = env::args().collect();
    /*
        implement a leakser
    */
    parsing(args[1].clone());
}


/*
PARSING PART
available char => | 0..9 | + | - | * | / | ^ | . | = | X | x | space |
*/
