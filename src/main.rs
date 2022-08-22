use std::env;


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
fn available_char(c: char) -> bool {
    match c {
        '+' => true,
        '-' => true,
        '*' => true,
        '/' => true,
        '^' => true,
        '.' => true,
        '=' => true,
        'X' => true,
        'x' => true,
        ' ' => true,
        _ => c.is_digit(10)
    }
}

fn basic_check(eq: String) -> bool {
    //check equal's number
    let mut equal_count = 0;
    eq.chars().for_each(|x| {
        if x == '=' {
            equal_count += 1;
        }
    });
    if equal_count != 1 {
        return false
    }

    true
}

//println!("NOP");
fn parsing(eq: String) {
    //check available character
    eq.chars().for_each(|x| {
        if available_char(x) == false {
            //error message
        }
    });
    if basic_check(eq.clone()) == false {
        //error message
    }
    let eq_vec: Vec<char> = eq.chars().collect();
    for (i, c) in eq_vec.iter().enumerate() {
        //check X format
        if *c == 'X' {
            match eq_vec.get(i + 1) {
                Some(x) => {
                    if *x != '^' {
                        //error message
                        println!("NOP");
                    } else {
                        match eq_vec.get(i + 2) {
                            Some(y) => {
                                if y.is_digit(10) == false {
                                    //error message
                                    println!("NOP");
                                }
                            },
                            _ => {//error message
                                println!("NOP");}
                        }
                    }
                },
                _ => {//error message
                        println!("NOP");}
            }
        }

        //check decimal number
        if *c == '.' {
            match eq_vec.get(i - 1) {
                Some(x) => {
                    if x.is_digit(10) == false {
                        //error message
                        println!("NOP");
                    }
                },
                _ => {//error message
                    println!("NOP");}
            }
            match eq_vec.get(i + 1) {
                Some(x) => {
                    if x.is_digit(10) == false {
                        //error message
                        println!("NOP");
                    }
                },
                _ => {//error message
                    println!("NOP");}
            }
        }

    //check

    }
}


/*
    FORMATTING PART
*/
