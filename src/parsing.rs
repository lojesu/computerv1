//println!("NOP");
pub fn parsing(eq: String) {
    //check available character
    eq.chars().for_each(|x| {
        if available_char(x) == false {
            //error message
        }
    });
    if basic_check(eq.clone()) == false {
        //error message
    }
    //specefic check in a loop
    let eq_vec: Vec<char> = eq.chars().collect();
    for (i, c) in eq_vec.iter().enumerate() {
        check_x_format(eq_vec.clone(), *c, i);
        check_decimal_format(eq_vec.clone(), *c, i);
    }
}


fn check_x_format(eq_vec: Vec<char>, c: char, i: usize) {
    if c == 'X' {
        if i > 0 {
            match eq_vec.get(i - 1) {
                Some(x) => {
                    if *x == '^' {
                        //error message
                        println!("NOP");
                    }
                }
                _ => {
                    //error message
                    println!("NOP");
                }
            }
        } else {}
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
                        _ => {
                            //error message
                            println!("NOP");}
                    }
                }
            },
            _ => {
                //error message
                println!("NOP");}
        }
    }
}

fn check_decimal_format(eq_vec: Vec<char>, c: char, i: usize) {
    if c == '.' {
        if i > 0 {
            match eq_vec.get(i - 1) {
                Some(x) => {
                    if x.is_digit(10) == false {
                        //error message
                        println!("NOP");
                    }
                },
                _ => {
                    //error message
                    println!("NOP");}
            }
        } else {
            //error message
            println!("NOP");
        }
        match eq_vec.get(i + 1) {
            Some(x) => {
                if x.is_digit(10) == false {
                    //error message
                    println!("NOP");
                }
            },
            _ => {
                //error message
                println!("NOP");}
        }
    }
}

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

